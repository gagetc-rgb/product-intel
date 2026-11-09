"""Blind popularity scoring (rules fixed before the data was read in full; same rules for every product).

Channels (independent):
  AMZ  Amazon US search, top-20 organic: sum of 'bought in past month' badges (units/month, Amazon's own lower bound)
  TT   TikTok Shop US keyword page: highest lifetime 'sold' of an on-target product (thousands)
  META Meta Ad Library US, exact category phrase: active ads started 180+ days ago (all advertisers)
Each channel -> 0..5 on a log scale.
v2 after a data check: Meta exact-phrase search proved noisy (it matches services and unrelated ads), so
POP = mean of the SALES channels only (AMZ, TT); Meta enters only CONF, and not at all for META_NOISY phrases.
CONF = number of channels scoring >= 3 (max 3).
Clone signals (shown, not scored): Amazon listings selling 1K+/month, distinct advertisers with 180+ day ads.
Nothing about earlier verdicts, the owner's picks or the YouTuber's claims enters the score.
Run: python score.py -> blind_rank.md, blind_rank.csv
"""
import json, csv, pathlib, re
from products import P
from amz_filter import MUST, NOT
from tiktok import TT, NOTES

H = pathlib.Path(__file__).parent
meta = {}
for f in ("meta.json", "meta_rev.json", "meta_mid.json"):
    if (H / f).exists():
        for k, v in json.loads((H / f).read_text(encoding="utf-8")).items():
            if v.get("all") is not None or k not in meta:
                meta[k] = v
amz = json.loads((H / "amazon.json").read_text(encoding="utf-8"))


def bucket(x, cuts):
    if x is None:
        return None
    return sum(x >= c for c in cuts)


# Checked after the scan: the top 180+ day advertisers for these phrases are mostly off-target
# (med-spas, nail salons, clinics, car dealers, unrelated products), so their Meta count is not evidence.
META_NOISY = {"seat_cushion", "s_men_metabolism", "leakproof_boxers", "eye_mask", "s_cinnamon", "tightening_wand",
              "collagen_mask", "chin_wrap", "body_oil", "carplay", "s_oregano", "puppy_pad", "pendant"}
A_CUTS = (500, 3000, 10000, 30000, 100000)      # units / month
T_CUTS = (0.3, 2, 10, 50, 200)                  # thousand sold, lifetime
M_CUTS = (1, 5, 15, 50, 150)                    # ads aged 180+ days

rows = []
for pid, block, name, mph, aq, flag in P:
    a = amz.get(pid, {})
    m = meta.get(pid, {})
    ab = None
    if a.get("items") is not None:  # keep on-target titles only, drop duplicate listings
        seen, keep = set(), []
        for i in a["items"]:
            key = (i["title"][:60], i["rev"])
            if key in seen or not re.search(MUST[pid], i["title"], re.I) or (pid in NOT and re.search(NOT[pid], i["title"], re.I)):
                continue
            seen.add(key)
            keep.append(i)
        ab = sum(i["b"] for i in keep)
        a = dict(a, n_1k=sum(i["b"] >= 1000 for i in keep), max_rev=max([i["r"] for i in keep] or [0]))
    t = TT.get(pid)
    mo = m.get("aged180")
    sa, st, sm = bucket(ab, A_CUTS), bucket(t, T_CUTS), bucket(mo, M_CUTS)
    if pid in META_NOISY:
        sm = None  # phrase hits salons/clinics/dealers or unrelated products: not usable
    sc = [s for s in (sa, st) if s is not None]  # sales channels only
    pop = round(sum(sc) / len(sc), 2) if sc else 0
    conf = sum(s >= 3 for s in sc) + (1 if (sm or 0) >= 3 else 0)
    rows.append(dict(id=pid, block=block, name=name, flag=flag,
                     amz_bought=ab, amz_1k=a.get("n_1k"), amz_maxrev=a.get("max_rev"),
                     tt_k=t, meta_all=m.get("all"), meta_180=mo, adv_180=len(m.get("advertisers180", []) or []),
                     sA=sa, sT=st, sM=sm, POP=pop, CONF=conf, note=NOTES.get(pid, "")))

rows.sort(key=lambda r: (-r["CONF"], -r["POP"]))
with open(H / "blind_rank.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)


def fmt(x):
    if x is None:
        return "n/a"
    if isinstance(x, float):
        return f"{x:g}"
    return f"{x:,}"


out = ["# Blind popularity ranking (2026-11-07)", "",
       "Rules in `score.py` docstring. AMZ = Amazon units/month (top-20 organic, 'bought in past month'); "
       "TT = TikTok Shop top on-target product, thousand sold lifetime; META180 = Meta US ads live 180+ days for the category phrase. "
       "Scores 0-5 per channel; POP = mean; CONF = channels scoring 3+. n/a = no data (not zero).", ""]
for block, title in (("MAIN", "Main block (non-ingestible)"), ("SUPP", "Supplements block")):
    out += [f"## {title}", "",
            "| # | Product | Flag | AMZ units/mo | AMZ 1K+ listings | TT k sold | META all / 180+ | advertisers 180+ | sA sT sM | POP | CONF | Note |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate([r for r in rows if r["block"] == block], 1):
        out.append(f"| {i} | {r['name']} | {r['flag']} | {fmt(r['amz_bought'])} | {fmt(r['amz_1k'])} | {fmt(r['tt_k'])} | "
                   f"{fmt(r['meta_all'])} / {fmt(r['meta_180'])} | {r['adv_180']} | {fmt(r['sA'])} {fmt(r['sT'])} {fmt(r['sM'])} | "
                   f"{r['POP']} | {r['CONF']} | {r['note']} |")
    out.append("")
(H / "blind_rank.md").write_text("\n".join(out), encoding="utf-8")
print("rows", len(rows))
