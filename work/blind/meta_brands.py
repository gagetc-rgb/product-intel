"""Brand-level Meta ad longevity (US, active, exact phrase = brand name). 2026-11-07, method v2.0.
Per brand: active ads, of them started >= 90 / >= 180 days ago (Meta counts), and which pages run them
(first ~30 ads) so we can see the phrase really hits the brand's own ads.
Usage: python meta_brands.py "category|Brand phrase" ...   -> meta_brands.json
"""
import json, sys, pathlib, collections, datetime as dt
from playwright.sync_api import sync_playwright
import meta_ages as M  # url(), count(), parse(), CARDS (module code runs only its function defs when no JOBS)
OUT = pathlib.Path(__file__).with_name("meta_brands.json")
res = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
with sync_playwright() as pw:
    br = pw.chromium.launch(headless=True)
    pg = br.new_page(user_agent=M.UA, viewport={"width": 1280, "height": 900}, locale="en-US")
    for job in [a for a in sys.argv[1:] if "|" in a]:
        cat, phrase = job.split("|", 1)
        if phrase in res: print(phrase, "done"); continue
        r = {"cat": cat, "active": M.count(pg, M.url(phrase)), "aged90": M.count(pg, M.url(phrase, M.ago(90))),
             "aged180": M.count(pg, M.url(phrase, M.ago(180)))}
        pg.goto(M.url(phrase), wait_until="domcontentloaded", timeout=60000); pg.wait_for_timeout(5000)
        ads = [M.parse(l, t) for l, t in pg.evaluate(M.CARDS)]
        r["pages"] = collections.Counter(a["page"] for a in ads).most_common(4)
        r["domains"] = collections.Counter(a["domain"] for a in ads if a["domain"]).most_common(3)
        res[phrase] = r
        OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{cat:16} {phrase:22} active {r['active']} 90d+ {r['aged90']} 180d+ {r['aged180']} pages {r['pages'][:2]} dom {r['domains'][:2]}", flush=True)
    br.close()
