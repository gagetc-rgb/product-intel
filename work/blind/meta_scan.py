"""Meta Ad Library US, active ads, category exact phrase: total, 180+ days, distinct advertisers in loaded ads."""
import json, sys, time, pathlib, urllib.parse, datetime as dt
from playwright.sync_api import sync_playwright
from products import P
OUT = pathlib.Path(__file__).with_name("meta.json")
res = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"
CUT = (dt.date(2026, 11, 7) - dt.timedelta(days=180)).isoformat()
PAGES = r"""() => { const out=[]; for (const s of document.querySelectorAll('span')) {
  if (!/^Library ID: \d+$/.test(s.textContent.trim())) continue; let el=s; for(let i=0;i<8;i++) el=el.parentElement;
  const L=el.innerText.split('\n').map(x=>x.trim()).filter(Boolean); const i=L.indexOf('Sponsored');
  out.push(i>0?L[i-1]:''); } return out; }"""
def run(pg, phrase, cutoff=None):
    q = urllib.parse.quote(f'"{phrase}"')
    url = ("https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US"
           f"&q={q}&search_type=keyword_exact_phrase&media_type=all")
    if cutoff: url += f"&start_date[max]={cutoff}"
    pg.goto(url, wait_until="domcontentloaded", timeout=60000)
    pg.wait_for_timeout(5000)
    txt = pg.evaluate("document.body.innerText")
    import re
    m = re.search(r"~?([\d,]+) results?", txt)
    n = int(m.group(1).replace(",", "")) if m else (0 if "No ads match" in txt or "no results" in txt.lower() else None)
    for _ in range(2):
        pg.mouse.wheel(0, 20000); pg.wait_for_timeout(1500)
    pages = pg.evaluate(PAGES)
    return n, len(pages), sorted(set(p for p in pages if p))
with sync_playwright() as pw:
    br = pw.chromium.launch(headless=True)
    pg = br.new_page(user_agent=UA, viewport={"width": 1280, "height": 900}, locale="en-US")
    for pid, block, name, meta, amz, flag in P[:62]:
        if pid in res and res[pid].get("all") is not None: continue
        try:
            a, la, pa = run(pg, meta)
            o, lo, po = run(pg, meta, CUT)
            res[pid] = {"phrase": meta, "all": a, "loaded": la, "advertisers": pa, "aged180": o, "loaded180": lo, "advertisers180": po}
        except Exception as e:
            res[pid] = {"phrase": meta, "all": None, "err": str(e)[:200]}
        print(pid, res[pid].get("all"), res[pid].get("aged180"), len(res[pid].get("advertisers", [])), len(res[pid].get("advertisers180", [])), flush=True)
        OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    br.close()
