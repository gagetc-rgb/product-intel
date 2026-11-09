"""Meta Ad Library US, active ads per cohort brand domain (exact phrase = domain). Frozen 2026-11-07.
Per domain: active total, started >=90 days ago, >=180 days ago (Meta counts), plus a sample of up to ~150
loaded ads: start date, page, landing domain (to check the phrase hits the brand's own ads).
Limits: US library shows ACTIVE ads only; phrase match can include resellers/affiliates mentioning the domain.
Run: python meta_brands.py [--names] -> meta_brands.json (--names: query = brand name from brand_names.json, key name:<domain>;
own_domain_share then tells how many sampled ads land on the brand site)
"""
import json, re, sys, pathlib, urllib.parse, datetime as dt
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).parent
TODAY = dt.date(2026, 11, 7)
OUT = HERE / "meta_brands.json"
res = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
sites = json.loads((HERE / "sites.json").read_text(encoding="utf-8"))
NAMES = json.loads((HERE / "brand_names.json").read_text(encoding="utf-8")) if "--names" in sys.argv else None
DOMS = sorted({v for k, v in sites.items() if v and not k.startswith("_") and "." in v and " " not in v})
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"
CARDS = r"""() => { const out=[]; for (const s of document.querySelectorAll('span')) {
  const m=s.textContent.trim().match(/^Library ID: (\d+)$/); if (!m) continue; let el=s; for(let i=0;i<8;i++) el=el.parentElement;
  out.push([m[1], el.innerText.slice(0,2500)]); } return out; }"""
DOM = re.compile(r"^(?:[A-Z0-9-]+\.)+[A-Z]{2,6}$")
def url(q, maxdate=None):
    u = ("https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US"
         f"&q={urllib.parse.quote(chr(34)+q+chr(34))}&search_type=keyword_exact_phrase&media_type=all")
    return u + (f"&start_date[max]={maxdate}" if maxdate else "")
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
    dom = next((x for x in L[i+1:] if DOM.match(x)), "") if i >= 0 else ""
    return {"id": lid, "page": L[i-1] if i > 0 else "", "start": start, "domain": dom.lower()}
with sync_playwright() as pw:
    br = pw.chromium.launch(headless=True)
    pg = br.new_page(user_agent=UA, viewport={"width": 1280, "height": 900}, locale="en-US")
    for d in DOMS:
        if NAMES and d not in NAMES: continue
        key, q = ("name:" + d, NAMES[d]) if NAMES else (d, d)
        if key in res and res[key].get("active") is not None: continue
        try:
            r = {"query": q, "active": count(pg, url(q))}
            r["aged90"] = count(pg, url(q, (TODAY - dt.timedelta(days=90)).isoformat())) if r["active"] else 0
            r["aged180"] = count(pg, url(q, (TODAY - dt.timedelta(days=180)).isoformat())) if r["active"] else 0
            ads = []
            if r["active"]:
                pg.goto(url(q), wait_until="domcontentloaded", timeout=60000); pg.wait_for_timeout(5000)
                seen = stall = 0
                for _ in range(10):
                    pg.mouse.wheel(0, 30000); pg.wait_for_timeout(2000)
                    n = pg.evaluate("document.body.innerText.split('Library ID:').length - 1")
                    stall = stall + 1 if n == seen else 0; seen = n
                    if stall >= 2 or n >= 150: break
                ads = [parse(l, t) for l, t in pg.evaluate(CARDS)]
            starts = sorted(a["start"] for a in ads if a["start"])
            r.update(sample=len(ads), own_domain_share=round(sum(a["domain"] == d for a in ads) / len(ads), 2) if ads else None,
                     oldest=starts[0] if starts else None, pages=sorted({a["page"] for a in ads})[:8], ads=ads)
        except Exception as e:
            r = {"active": None, "err": str(e)[:200]}
        res[key] = r
        OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        print(key, r.get("active"), r.get("aged90"), r.get("aged180"), r.get("oldest"), r.get("own_domain_share"), flush=True)
