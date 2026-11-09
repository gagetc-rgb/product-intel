"""Meta Ad Library (US, active ads, exact phrase): how many ads run and how long they live. Frozen 2026-11-07.

Per category phrase (same phrases as the earlier meta scans, from products.py):
  counts (counted by Meta, tier 1): active ads total; of them started >= 90 days ago; >= 180 days ago
  sample (first ~150-250 ads Meta shows): page name, start date, landing domain, 'N ads use this creative'
Limits: the US library shows ACTIVE ads only, so stopped ads (the failures) are invisible here;
the sample order is Meta's, not random.
Usage: python meta_ages.py pid="phrase" [...]   -> meta_ages/<pid>.json
"""
import json, re, sys, time, pathlib, urllib.parse, datetime as dt
from playwright.sync_api import sync_playwright
TODAY = dt.date.today()  # was fixed 2026-11-07 for the first 9 categories; each file stores its own date
D = pathlib.Path(__file__).with_name("meta_ages"); D.mkdir(exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"
JOBS = [a.split("=", 1) for a in sys.argv[1:] if not a.startswith("--")]
CARDS = r"""() => { const out=[]; for (const s of document.querySelectorAll('span')) {
  const m=s.textContent.trim().match(/^Library ID: (\d+)$/); if (!m) continue; let el=s; for(let i=0;i<8;i++) el=el.parentElement;
  out.push([m[1], el.innerText.slice(0,2500)]); } return out; }"""
DOM = re.compile(r"^(?:[A-Z0-9-]+\.)+(?:COM|CO|SHOP|STORE|US|NET|ORG|IO|BEAUTY|SKIN|CARE|LIFE|CO\.UK)$")

def url(phrase, maxdate=None, mindate=None):
    u = ("https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US"
         f"&q={urllib.parse.quote(chr(34) + phrase + chr(34))}&search_type=keyword_exact_phrase&media_type=all")
    return u + (f"&start_date[min]={mindate}" if mindate else "") + (f"&start_date[max]={maxdate}" if maxdate else "")
# logged-out Meta shows only ~30 ads per query, so the sample is stratified by ad age (30 per window)
def ago(d): return (TODAY - dt.timedelta(days=d)).isoformat()
WINDOWS = [("180+", None, ago(180)), ("90-180", ago(180), ago(90)), ("30-90", ago(90), ago(30)), ("0-30", ago(30), None)]

def count(pg, u):
    pg.goto(u, wait_until="domcontentloaded", timeout=60000); pg.wait_for_timeout(5000)
    t = pg.evaluate("document.body.innerText")
    m = re.search(r"~?([\d,]+) results?", t)
    return int(m.group(1).replace(",", "")) if m else (0 if re.search(r"No ads match|no results", t, re.I) else None)

def parse(lid, t):
    L = [x.strip() for x in t.split("\n") if x.strip() and x.strip() != "​"]
    i = L.index("Sponsored") if "Sponsored" in L else -1
    m = re.search(r"Started running on (\d{1,2} \w{3} \d{4})", t)
    start = dt.datetime.strptime(m.group(1), "%d %b %Y").date().isoformat() if m else ""
    n = re.search(r"(\d+) ads use this creative", t)
    dom = next((x for x in L[i + 1:] if DOM.match(x)), "") if i >= 0 else ""
    return {"id": lid, "page": L[i - 1] if i > 0 else "", "start": start, "n": int(n.group(1)) if n else 1, "domain": dom.lower()}

if __name__ == "__main__":
    with sync_playwright() as pw:
        br = pw.chromium.launch(headless=True)
        pg = br.new_page(user_agent=UA, viewport={"width": 1280, "height": 900}, locale="en-US")
        for pid, phrase in JOBS:
            f = D / f"{pid}.json"
            if f.exists() and "--force" not in sys.argv:
                res = json.loads(f.read_text(encoding="utf-8"))
                if "aged30" not in res:  # B2 (2026-11-08): add the 30-day count to older files
                    res["aged30"] = count(pg, url(res["phrase"], ago(30))); res["aged30_date"] = TODAY.isoformat()
                    f.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
                print(pid, "done; aged30", res["aged30"], flush=True); pg.wait_for_timeout(4000); continue
            res = {"phrase": phrase, "date": TODAY.isoformat()}
            res["active"] = count(pg, url(phrase))
            res["aged30"] = count(pg, url(phrase, ago(30)))
            res["aged90"] = count(pg, url(phrase, (TODAY - dt.timedelta(days=90)).isoformat()))
            res["aged180"] = count(pg, url(phrase, (TODAY - dt.timedelta(days=180)).isoformat()))
            res["ads"], ids = [], set()
            for w, lo, hi in WINDOWS:
                pg.goto(url(phrase, hi, lo), wait_until="domcontentloaded", timeout=60000); pg.wait_for_timeout(5000)
                pg.evaluate("window.scrollTo(0, document.body.scrollHeight)"); pg.wait_for_timeout(2500)
                for lid, t in pg.evaluate(CARDS):
                    if lid in ids: continue
                    ids.add(lid); a = parse(lid, t); a["window"] = w; res["ads"].append(a)
            f.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"{pid}: active {res['active']} aged30 {res['aged30']} aged90 {res['aged90']} aged180 {res['aged180']} sample {len(res['ads'])}", flush=True)
            pg.wait_for_timeout(5000)
        br.close()
