"""Amazon 'graveyard': survival of newcomer brands in a category (2026-11-07).

Amazon keeps failed listings live, so unlike the US Meta Ad Library the failures are visible.
1. Search pages 1..PAGES for the category query; keep organic, on-target listings (amz_filter).
2. Open each listing: brand (byline), 'Date First Available', badge, reviews.
3. Group by BRAND (one seller can own several ASINs).
4. Cohort = brands whose earliest on-target listing first appeared 6-24 months ago.
   Success = the brand has a listing with 'bought in past month' >= SUCCESS.
Usage: python graveyard_amz.py <product_id> "<query>" [pages]
Output: graveyard/<product_id>.json
"""
import json, re, sys, pathlib, urllib.parse, datetime as dt
from playwright.sync_api import sync_playwright
from amz_filter import MUST, NOT
from graveyard_def import on_target
import time
T0 = time.time()
BUDGET = int(next((a.split("=")[1] for a in sys.argv if a.startswith("--budget=")), "100000"))

pid, query = sys.argv[1], sys.argv[2]
PAGES = int(sys.argv[3]) if len(sys.argv) > 3 else 4
OUTD = pathlib.Path(__file__).with_name("graveyard"); OUTD.mkdir(exist_ok=True)
OUT = OUTD / f"{pid}.json"
data = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {"q": query, "listings": {}}
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"

SEARCH_JS = r"""()=>[...document.querySelectorAll('div[data-component-type="s-search-result"]')].map(d=>{
  const t=d.innerText; const h=d.querySelector('h2');
  const r=d.querySelector('a[href*="customerReviews"] span, span.s-underline-text');
  const b=(t.match(/([\d,.]+K?\+?) bought in past month/)||[])[1]||'';
  return {asin:d.getAttribute('data-asin'), title:(h?h.innerText:'').slice(0,120), rev:r?r.innerText:'',
          bought:b, sp:/\bSponsored\b/.test(t)};})"""
PAGE_JS = r"""()=>{const t=document.body.innerText;
  const by=document.querySelector('#bylineInfo');
  const d=(t.match(/Date First Available\s*[:‏‎ ]*\s*([A-Z][a-z]+ \d{1,2}, \d{4})/)||[])[1]||'';
  const b=(t.match(/([\d,.]+K?\+?) bought in past month/)||[])[1]||'';
  const r=document.querySelector('#acrCustomerReviewText');
  const m=(t.match(/Manufacturer\s*[:‏‎ ]*\s*([^\n]{2,40})/)||[])[1]||'';
  const bad=/Enter the characters|Sorry! Something went wrong|button below to continue shopping/i.test(t) || !document.querySelector('#productTitle');
  return {brand:by?by.innerText:'', mfr:m, first:d, bought:b, rev:r?r.innerText:'', title:document.title.slice(0,120), bad:bad};}"""

def num(s):
    s = (s or "").replace("ratings", "").replace("rating", "").strip("()+ ").replace(",", "")
    if not s: return 0
    m = 1000 if s.endswith("K") else 1
    try: return int(float(s.rstrip("K")) * m)
    except ValueError: return 0

def brand_of(s):
    s = re.sub(r"^(Visit the |Brand: )", "", s or "").replace(" Store", "").strip()
    return s.lower()

must, nott = MUST.get(pid), NOT.get(pid)
with sync_playwright() as pw:
    br = pw.chromium.launch(headless=True)
    ctx = br.new_context(user_agent=UA, locale="en-US", viewport={"width": 1280, "height": 900})
    pg = ctx.new_page()
    cand = {}
    if not data.get("cand") or "--rescan" in sys.argv:
        pg.goto(f"https://www.amazon.com/s?k={urllib.parse.quote_plus(query)}", wait_until="domcontentloaded", timeout=60000)
        pg.wait_for_timeout(3000)
        for p in range(1, PAGES + 1):
            items = pg.evaluate(SEARCH_JS)
            print("page", p, len(items), flush=True)
            for i in items:
                if not i["asin"] or i["sp"]: continue
                if must and not re.search(must, i["title"], re.I): continue
                if nott and re.search(nott, i["title"], re.I): continue
                if not on_target(pid, i["title"]): continue
                cand.setdefault(i["asin"], i)
            nxt = pg.locator("a.s-pagination-next")
            if p == PAGES or not nxt.count(): break
            nxt.first.click(); pg.wait_for_timeout(4000)
    data.setdefault("cand", {}).update(cand); cand = data["cand"]
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print("on-target organic (cumulative):", len(cand), flush=True)
    todo = [a for a, i in cand.items() if on_target(pid, i["title"]) and not data["listings"].get(a, {}).get("brand")]
    print("to fetch:", len(todo), flush=True)
    fails = 0
    for asin in todo:
        if time.time() - T0 > BUDGET: print("budget reached; rerun to continue", flush=True); break
        i = cand[asin]
        try:
            pg.goto(f"https://www.amazon.com/dp/{asin}", wait_until="domcontentloaded", timeout=60000)
            pg.wait_for_timeout(1800)
            d = pg.evaluate(PAGE_JS)
        except Exception as e:
            d = {"bad": True, "err": str(e)[:100]}
        if d.get("bad"):  # never store a failed fetch as an empty record
            fails += 1; print(asin, "FETCH FAILED", d.get("err", ""), flush=True)
            if fails >= 8: print("too many failures; stopping", flush=True); break
            pg.wait_for_timeout(5000); continue
        fails = 0
        brand = brand_of(d.get("brand")) or brand_of(d.get("mfr"))
        rec = {"title": i["title"], "brand": brand, "first": d.get("first", ""),
               "b": max(num(i["bought"]), num(d.get("bought"))), "r": max(num(i["rev"]), num(d.get("rev")))}
        data["listings"][asin] = rec
        print(asin, rec["brand"][:25], rec["first"], rec["b"], rec["r"], flush=True)
        OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
        pg.wait_for_timeout(1200)
    br.close()
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
