"""Amazon US search, top organic results: 'bought in past month' badges, review counts, price."""
import json, re, pathlib, urllib.parse
from playwright.sync_api import sync_playwright
from products import P
OUT = pathlib.Path(__file__).with_name("amazon.json")
res = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"
JS = r"""()=>[...document.querySelectorAll('div[data-component-type="s-search-result"]')].slice(0,24).map(d=>{
  const t=d.innerText; const h=d.querySelector('h2');
  const r=d.querySelector('a[href*="customerReviews"] span, span.s-underline-text');
  const b=(t.match(/([\d,.]+K?\+?) bought in past month/)||[])[1]||'';
  const p=d.querySelector('.a-price .a-offscreen');
  return {title:(h?h.innerText:'').slice(0,90), rev:r?r.innerText:'', bought:b, sp:/\bSponsored\b/.test(t), price:p?p.textContent:''};})"""
def num(s):
    s = s.strip("()+ ").replace(",", "")
    if not s: return 0
    m = 1000 if s.endswith("K") else 1
    try: return int(float(s.rstrip("K")) * m)
    except ValueError: return 0
with sync_playwright() as pw:
    br = pw.chromium.launch(headless=True)
    ctx = br.new_context(user_agent=UA, locale="en-US", viewport={"width": 1280, "height": 900})
    pg = ctx.new_page()
    for pid, block, name, meta, amz, flag in P:
        if pid in res and res[pid].get("items"): continue
        try:
            pg.goto("https://www.amazon.com/s?k=" + urllib.parse.quote_plus(amz), wait_until="domcontentloaded", timeout=60000)
            pg.wait_for_timeout(2500)
            items = pg.evaluate(JS)
            if not items: print(pid, "NO ITEMS", pg.title(), flush=True)
            org = [i for i in items if not i["sp"]][:20]
            for i in org: i["b"] = num(i["bought"]); i["r"] = num(i["rev"])
            res[pid] = {"q": amz, "items": org,
                        "sum_bought": sum(i["b"] for i in org), "max_bought": max([i["b"] for i in org] or [0]),
                        "n_1k": sum(i["b"] >= 1000 for i in org), "sum_rev": sum(i["r"] for i in org),
                        "max_rev": max([i["r"] for i in org] or [0])}
            print(pid, res[pid]["sum_bought"], res[pid]["n_1k"], res[pid]["max_rev"], flush=True)
        except Exception as e:
            print(pid, "ERR", str(e)[:150], flush=True)
        OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        pg.wait_for_timeout(1500)
    br.close()
