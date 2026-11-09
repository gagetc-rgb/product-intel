"""B4 (2026-11-08): brand-level Meta ad counts scoped to the brand's own Facebook Page (Page ID),
next to the exact-phrase count (meta_brands.py). Why both:
  - phrase search matches ad TEXT, so it can pull in other advertisers (over-count);
  - page search misses the brand's ads run from creator / persona pages (whitelisting), e.g. GODA (under-count).
So per brand we record: own page id(s) + their active / 30d+ / 90d+ / 180d+ counts (Meta's counter),
and, from the first ~30 phrase-search ads, the share whose landing domain is the brand's own domain.
Usage: python meta_pages.py "cat|Brand|exact phrase|domain|page-name regex" ...  -> meta_pages.json
"""
import json, re, sys, pathlib, urllib.parse
from playwright.sync_api import sync_playwright
import meta_ages as M
OUT = pathlib.Path(__file__).with_name("meta_pages.json")
res = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}

def page_url(pid, maxdate=None):
    u = ("https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US"
         f"&view_all_page_id={pid}&search_type=page&media_type=all")
    return u + (f"&start_date[max]={maxdate}" if maxdate else "")

def pages_in(html):
    pairs = re.findall(r'"page_id":"(\d+)"[^{}]{0,400}?"page_name":"([^"]+)"', html)
    pairs += [(b, a) for a, b in re.findall(r'"page_name":"([^"]+)"[^{}]{0,400}?"page_id":"(\d+)"', html)]
    return {pid: json.loads(f'"{name}"') for pid, name in pairs}

if __name__ == "__main__":
    with sync_playwright() as pw:
        br = pw.chromium.launch(headless=True)
        pg = br.new_page(user_agent=M.UA, viewport={"width": 1280, "height": 900}, locale="en-US")
        jf = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--jobs=")), None)
        jobs = [a for a in sys.argv[1:] if a.count("|") == 4]
        if jf: jobs += [l.strip() for l in pathlib.Path(jf).read_text(encoding="utf-8").splitlines() if l.count("|") == 4]
        for job in jobs:
            cat, brand, phrase, domain, rx = job.split("|")
            if brand in res and "--force" not in sys.argv: print(brand, "done"); continue
            pg.goto(M.url(phrase), wait_until="domcontentloaded", timeout=60000); pg.wait_for_timeout(6000)
            pages = pages_in(pg.content())
            ads = [M.parse(l, t) for l, t in pg.evaluate(M.CARDS)]
            own_dom = [a for a in ads if a["domain"].replace("www.", "").endswith(domain)]
            own = {pid: n for pid, n in pages.items() if re.search(rx, n, re.I)}
            r = {"cat": cat, "phrase": phrase, "domain": domain, "date": M.TODAY.isoformat(),
                 "phrase_sample": len(ads), "phrase_sample_own_domain": len(own_dom),
                 "phrase_sample_pages": sorted({a["page"] for a in ads})[:12], "own_pages": {}}
            for pid, name in own.items():
                c = {"name": name, "active": M.count(pg, page_url(pid))}
                for d in (30, 90, 180): c[f"aged{d}"] = M.count(pg, page_url(pid, M.ago(d)))
                r["own_pages"][pid] = c
            res[brand] = r
            OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
            tot = {k: sum(p[k] or 0 for p in r["own_pages"].values()) for k in ("active", "aged30", "aged90", "aged180")}
            print(f"{cat:16} {brand:20} own pages {len(own)} {tot} | phrase sample {len(ads)}, own domain {len(own_dom)}", flush=True)
            pg.wait_for_timeout(4000)
        br.close()
