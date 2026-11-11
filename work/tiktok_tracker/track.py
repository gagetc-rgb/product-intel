"""TikTok Shop US sold-counter tracker (started 2026-11-10).

The public 'sold' counter is lifetime, so the difference between two snapshots = units sold in between.
Source: Apify actor lurkapi/tiktok-shop-scraper (logged-off, US storefront, pay per product ~$2/1K; no login, no CAPTCHA solving on keyword/product inputs).
Direct access from this PC fails (puzzle captcha; product pages say "not available in your region").

  python work/tiktok_tracker/track.py discover        # weekly: keyword search per category, refresh watchlist
  python work/tiktok_tracker/track.py daily           # daily (or every 2 days): snapshot watched products by id
  python work/tiktok_tracker/track.py report          # write REPORT.md
  python work/tiktok_tracker/track.py import FILE.json <category|daily> [YYYY-MM-DD]   # load a saved dataset (tests, manual runs)

NOT STARTED: the category list below is provisional; the owner confirms it before the first paid run.

Token: APIFY_TOKEN in .env at the repo root (never in chat or git).
Title filters are the Amazon ones (work/blind/amz_filter.py) so the categories match BLIND_PASS.
"""
import json, os, re, sqlite3, sys, time, datetime as dt
from pathlib import Path
import requests

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "work" / "blind"))
from amz_filter import MUST, NOT  # noqa: E402

DB = Path(os.environ.get("TT_DB", HERE / "tt.db"))
RAW = HERE / "raw"
ACTOR = "lurkapi~tiktok-shop-scraper"
MAX_USD_PER_RUN = 1.0   # Apify stops the run once it has charged this much

# category id (as in work/blind) -> TikTok search phrase. Top 5 + reserve of v2.2, the 3 one-time products, CarPlay.
CATEGORIES = {
    "dog_fountain": "pet water fountain",
    "color_foundation": "color changing foundation",
    "lash_serum": "eyelash growth serum",
    "tallow_balm": "beef tallow balm",
    "shower_filter": "filtered shower head",
    "hair_serum": "hair growth serum",
    "body_oil": "body oil",
    "persimmon_soap": "persimmon soap",
    "vacuum_bags": "travel vacuum bags",
    "duffel": "garment duffel bag",
    "steam_cleaner": "handheld steam cleaner",
    "carplay": "wireless carplay adapter",
}
PER_KEYWORD = 20   # products read per category in discover
TOP_N = 8          # watched: best sellers per category
YOUNG_N = 4        # watched: plus the best-selling products first seen within YOUNG_DAYS
YOUNG_DAYS = 365
ENTRANT_DAYS = (90, 730)   # B1 window: first seen 3-24 months ago
WINNER_PER_MONTH = 1000    # same bar as Amazon B1


def on_target(cat, title):
    t = title or ""
    return bool(re.search(MUST[cat], t, re.I)) and not (cat in NOT and re.search(NOT[cat], t, re.I))


def db():
    con = sqlite3.connect(DB)
    con.executescript("""
    create table if not exists products(product_id text primary key, category text, title text, seller text,
        url text, first_seen text, watch integer default 0, added text);
    create table if not exists snaps(day text, product_id text, sold integer, price real, rating real,
        reviews integer, source text, primary key(day, product_id));
    """)
    return con


def token():
    if os.environ.get("APIFY_TOKEN"):
        return os.environ["APIFY_TOKEN"]
    env = ROOT / ".env"
    for line in env.read_text(encoding="utf-8").splitlines() if env.exists() else []:
        k, _, v = line.partition("=")
        if k.strip() == "APIFY_TOKEN":
            return v.strip().strip('"')
    sys.exit("APIFY_TOKEN missing: add a line APIFY_TOKEN=... to .env in the repo root")


def run_actor(inp):
    h = {"Authorization": f"Bearer {token()}"}
    r = requests.post(f"https://api.apify.com/v2/acts/{ACTOR}/runs", json=inp, headers=h,
                      params={"maxTotalChargeUsd": MAX_USD_PER_RUN}, timeout=60)
    r.raise_for_status()
    run = r.json()["data"]
    while run["status"] in ("READY", "RUNNING"):
        time.sleep(15)
        run = requests.get(f"https://api.apify.com/v2/actor-runs/{run['id']}", headers=h, timeout=60).json()["data"]
    print("run", run["id"], run["status"])
    items = requests.get(f"https://api.apify.com/v2/datasets/{run['defaultDatasetId']}/items",
                         headers=h, params={"clean": "true", "format": "json"}, timeout=120).json()
    return items


def save_raw(items, mode, day):
    RAW.mkdir(exist_ok=True)
    p = RAW / f"{day}_{mode}.json"
    p.write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
    return p


def load(items, mode, day, cat=None):
    """Store rows. discover: `cat` is the category searched (one actor run per keyword); daily: product already known."""
    con = db()
    n = 0
    for it in items:
        if it.get("status") not in (None, "Success") or it.get("soldCount") is None:
            continue
        pid = str(it["productId"])
        if mode == "discover":
            if not on_target(cat, it.get("title")):
                continue
            con.execute("""insert into products(product_id, category, title, seller, url, first_seen, added)
                values(?,?,?,?,?,?,?) on conflict(product_id) do update set title=excluded.title,
                first_seen=coalesce(excluded.first_seen, products.first_seen)""",
                        (pid, cat, it.get("title"), it.get("sellerName"), it.get("productUrl"),
                         (it.get("firstSeen") or "")[:10] or None, day))
        elif not con.execute("select 1 from products where product_id=?", (pid,)).fetchone():
            continue
        con.execute("insert or replace into snaps values(?,?,?,?,?,?,?)",
                    (day, pid, int(it["soldCount"]), it.get("currentPrice"), it.get("rating"),
                     it.get("reviewCount"), mode))
        n += 1
    if mode == "discover":
        pick_watchlist(con, day)
    con.commit()
    print(f"{mode} {day}: stored {n} snapshots")


def pick_watchlist(con, day):
    con.execute("update products set watch=0")
    cutoff = (dt.date.fromisoformat(day) - dt.timedelta(days=YOUNG_DAYS)).isoformat()
    for cat in CATEGORIES:
        rows = con.execute("""select p.product_id, s.sold, p.first_seen from products p join snaps s
            on s.product_id=p.product_id and s.day=(select max(day) from snaps where product_id=p.product_id)
            where p.category=? order by s.sold desc""", (cat,)).fetchall()
        keep = [r[0] for r in rows[:TOP_N]]
        keep += [r[0] for r in rows if r[2] and r[2] >= cutoff and r[0] not in keep][:YOUNG_N]
        con.executemany("update products set watch=1 where product_id=?", [(k,) for k in keep])


def discover(day):
    # one run per keyword: the output rows do not say which keyword found them, and title filters overlap (oil, serum)
    for cat, kw in CATEGORIES.items():
        items = run_actor({"country": "US", "keywords": [kw], "keywordSortBy": "default",
                           "maxProductsPerSource": PER_KEYWORD, "includeFirstSeen": True})
        save_raw(items, f"discover_{cat}", day)
        load(items, "discover", day, cat)


def daily(day):
    ids = [r[0] for r in db().execute("select product_id from products where watch=1")]
    if not ids:
        sys.exit("watchlist empty: run discover first")
    items = run_actor({"country": "US", "productIds": ids, "maxProductsPerSource": 1})
    save_raw(items, "daily", day)
    load(items, "daily", day)


def rate(con, pid, start, end):
    """Units/day between the snapshot nearest after `start` and the last one up to `end`."""
    a = con.execute("select day, sold from snaps where product_id=? and day>=? and day<=? order by day limit 1",
                    (pid, start, end)).fetchone()
    b = con.execute("select day, sold from snaps where product_id=? and day>=? and day<=? order by day desc limit 1",
                    (pid, start, end)).fetchone()
    if not a or not b or a[0] == b[0]:
        return None
    days = (dt.date.fromisoformat(b[0]) - dt.date.fromisoformat(a[0])).days
    return max(b[1] - a[1], 0) / days


def report(today):
    con = db()
    d = dt.date.fromisoformat(today)
    w1, w0 = (d - dt.timedelta(days=7)).isoformat(), (d - dt.timedelta(days=14)).isoformat()
    out = [f"# TikTok Shop US tracker: report {today}", "",
           "Units/day = growth of the public lifetime 'sold' counter between snapshots (◆ counter, ◈ our difference).",
           "Big counters are rounded (e.g. 371.5K, step 100): read their weekly change, not daily.", "",
           "## Categories (watched listings)", "",
           "| Category | Watched | Units/day, last 7 d | Units/day, 7 d before | Change | Top seller now |",
           "|---|---|---|---|---|---|"]
    for cat in CATEGORIES:
        ids = [r[0] for r in con.execute("select product_id from products where category=? and watch=1", (cat,))]
        now = [rate(con, i, w1, today) for i in ids]
        before = [rate(con, i, w0, w1) for i in ids]
        s_now = sum(x for x in now if x is not None) if any(x is not None for x in now) else None
        s_bef = sum(x for x in before if x is not None) if any(x is not None for x in before) else None
        ch = f"{(s_now / s_bef - 1) * 100:+.0f}%" if s_now is not None and s_bef else "n/a"
        top = con.execute("""select p.title, s.sold from products p join snaps s on s.product_id=p.product_id
            where p.category=? and s.day=(select max(day) from snaps) order by s.sold desc limit 1""", (cat,)).fetchone()
        fmt = lambda x: "n/a" if x is None else f"{x:,.0f}"
        out.append(f"| {cat} | {len(ids)} | {fmt(s_now)} | {fmt(s_bef)} | {ch} | "
                   f"{(top[0] or '')[:45] + f' ({top[1]:,})' if top else 'n/a'} |")
    # B1 on TikTok: entrants first seen 3-24 months ago, lifetime average pace (works from the first discover)
    out += ["", "## Newcomers (TikTok version of B1)", "",
            f"Entrants = on-target products first seen {ENTRANT_DAYS[0]}-{ENTRANT_DAYS[1]} days ago among the top {PER_KEYWORD} per keyword "
            f"(upper bound: products that left the top are invisible). Winner = lifetime average ≥ {WINNER_PER_MONTH:,}/month. "
            "'First seen' is the actor's estimate ◈.", "",
            "| Category | Entrants | Winners | Share | Best entrant (sold, months live) |", "|---|---|---|---|---|"]
    for cat in CATEGORIES:
        rows = con.execute("""select p.title, p.first_seen, max(s.sold) from products p join snaps s on s.product_id=p.product_id
            where p.category=? and p.first_seen is not null group by p.product_id""", (cat,)).fetchall()
        ent = []
        for title, fs, sold in rows:
            age = (d - dt.date.fromisoformat(fs)).days
            if ENTRANT_DAYS[0] <= age <= ENTRANT_DAYS[1]:
                ent.append((sold / (age / 30.4), title, sold, age / 30.4))
        win = [e for e in ent if e[0] >= WINNER_PER_MONTH]
        best = max(ent, default=None)
        out.append(f"| {cat} | {len(ent)} | {len(win)} | {f'{len(win) / len(ent):.0%}' if ent else 'n/a'} | "
                   f"{(best[1] or '')[:40] + f' ({best[2]:,}, {best[3]:.0f} mo)' if best else 'n/a'} |")
    days = [r[0] for r in con.execute("select distinct day from snaps order by day")]
    out += ["", f"Snapshot days: {len(days)} ({days[0] if days else '-'} … {days[-1] if days else '-'})."]
    (HERE / "REPORT.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    cmd = sys.argv[1] if len(sys.argv) > 1 else "report"
    today = dt.date.today().isoformat()
    if cmd == "discover":
        discover(today)
    elif cmd == "daily":
        daily(today)
    elif cmd == "report":
        report(today)
    elif cmd == "import":
        items = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
        mode = sys.argv[3] if len(sys.argv) > 3 else "daily"
        load(items, "discover" if mode in CATEGORIES else mode, sys.argv[4] if len(sys.argv) > 4 else today,
             mode if mode in CATEGORIES else None)
    else:
        sys.exit(__doc__)
