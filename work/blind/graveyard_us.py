"""B3 (2026-11-08): the same search-card scrape as graveyard_search.py, but with the delivery location set to a
US ZIP first (the v2.0 scans showed 'Deliver to Indonesia' and IDR prices). Adds price (USD), rating and main image.
Writes graveyard_us/<pid>.json. If the ZIP cannot be set, the script stops (no scan under the wrong location).
--- original notes ---
Search-card-only graveyard scrape (2026-11-07). No product pages (they hit Amazon's bot wall when fetched in bulk).

For each category: Amazon search, pages 1..5 (clicking Next), slow pacing. Keeps organic listings
(sponsored dropped). Stores ASIN, title, badge units, reviews into graveyard/<pid>.json (same schema
as graveyard_amz.py; brand/first left empty unless already known).
If Amazon shows a robot check or the 'continue shopping' wall, the script STOPS (no bypass) and reports.
Usage: python graveyard_search.py pid=query [pid=query ...] [--budget=540]
"""
import json, sys, time, pathlib, urllib.parse
from playwright.sync_api import sync_playwright
T0 = time.time()
BUDGET = int(next((a.split("=")[1] for a in sys.argv if a.startswith("--budget=")), "540"))
JOBS = [a.split("=", 1) for a in sys.argv[1:] if not a.startswith("--")]
D = pathlib.Path(__file__).with_name("graveyard_us")
ZIP = "10001"; D.mkdir(exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"
SEARCH_JS = r"""()=>[...document.querySelectorAll('div[data-component-type="s-search-result"]')].map(d=>{
  const t=d.innerText; const h=d.querySelector('h2');
  const r=d.querySelector('a[href*="customerReviews"] span, span.s-underline-text');
  const b=(t.match(/([\d,.]+K?\+?) bought in past month/)||[])[1]||'';
  return {asin:d.getAttribute('data-asin'), title:(h?h.innerText:'').slice(0,160), rev:r?r.innerText:'',
          bought:b, sp:/\bSponsored\b/.test(t),
          price:(d.querySelector('span.a-price:not([data-a-strike]) span.a-offscreen')||{}).textContent||'',
          stars:(()=>{const e=d.querySelector('[aria-label*="out of 5 stars"]');return e?e.getAttribute('aria-label'):''})(),
          img:(d.querySelector('img.s-image')||{}).src||''};})"""
WALL = "Access restricted|unauthorized AI agent|Enter the characters|button below to continue shopping|Sorry! Something went wrong"

def num(s):
    s = (s or "").replace("ratings", "").replace("rating", "").strip("()+ ").replace(",", "")
    if not s: return 0
    m = 1000 if s.endswith("K") else 1
    try: return int(float(s.rstrip("K")) * m)
    except ValueError: return 0

with sync_playwright() as pw:
    br = pw.chromium.launch(headless=True)
    pg = br.new_context(user_agent=UA, locale="en-US", viewport={"width": 1280, "height": 900}).new_page()
    # set a US delivery ZIP through Amazon's own 'Deliver to' dialog (ordinary site use)
    pg.goto("https://www.amazon.com/", wait_until="domcontentloaded", timeout=60000); pg.wait_for_timeout(5000)
    loc = ""
    try:
        pg.locator("#nav-global-location-popover-link").first.click(); pg.wait_for_timeout(3000)
        pg.locator("#GLUXZipUpdateInput").fill(ZIP); pg.locator("#GLUXZipUpdate input, #GLUXZipUpdate").first.click()
        pg.wait_for_timeout(3000); pg.reload(wait_until="domcontentloaded"); pg.wait_for_timeout(4000)
        loc = pg.locator("#glow-ingress-line2").first.inner_text().strip()
    except Exception as e:
        print("could not set ZIP:", e, flush=True)
    print("Deliver to:", loc, flush=True)
    if ZIP not in loc and "New York" not in loc:
        print("US location not set - stopping", flush=True); br.close(); sys.exit(1)
    for pid, q in JOBS:
        f = D / f"{pid}.json"
        data = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {"q": q, "listings": {}}
        if data.get("pages_done", 0) >= 5 or len(data["listings"]) > 100:
            print(pid, "already done", flush=True); continue
        if time.time() - T0 > BUDGET: print("budget reached; rerun to continue", flush=True); break
        for attempt in range(3):  # empty page = transient throttling: wait and reload (no bypass of any check)
            pg.goto(f"https://www.amazon.com/s?k={urllib.parse.quote_plus(q)}", wait_until="domcontentloaded", timeout=60000)
            pg.wait_for_timeout(5000)
            if pg.locator('div[data-component-type="s-search-result"]').count(): break
            print(pid, "empty results page, waiting", flush=True); pg.wait_for_timeout(30000)
        done, walled = 0, False
        for p in range(1, 6):
            if pg.get_by_text(__import__("re").compile(WALL)).count():
                walled = True; break
            items = pg.evaluate(SEARCH_JS)
            for i in items:
                if not i["asin"] or i["sp"]: continue
                old = data["listings"].get(i["asin"], {})
                data["listings"][i["asin"]] = {"title": i["title"], "brand": old.get("brand", ""), "first": old.get("first", ""),
                                               "b": max(num(i["bought"]), old.get("b", 0)), "r": max(num(i["rev"]), old.get("r", 0)),
                                               "price": i["price"], "stars": i["stars"][:3], "img": i["img"], "page": p, "zip": ZIP}
            done = p
            nxt = pg.locator("a.s-pagination-next")
            if p == 5 or not nxt.count(): break
            nxt.first.click(); pg.wait_for_timeout(7000)
        data["pages_done"] = done
        f.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{pid}: pages {done}, listings {len(data['listings'])}", flush=True)
        if walled:
            print("BOT WALL shown by Amazon - stopping without bypass", flush=True); break
        pg.wait_for_timeout(45000)
    br.close()
