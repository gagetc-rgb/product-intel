"""Detect the review widget of each leader store (homepage HTML): Loox widget id, Judge.me / myshopify name, others. 2026-11-07."""
import json, re, urllib.request, concurrent.futures as cf
D = json.load(open("traffic_domains.json", encoding="utf-8"))
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36"}
def get(u):
    try: return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read().decode("utf-8", "ignore")
    except Exception as e: return "ERR " + str(e)[:60]
def probe(dom):
    h = get(f"https://{dom}/")
    shop = (re.search(r"([a-z0-9-]+)\.myshopify\.com", h) or [None, None])[1]
    loox = (re.search(r"loox\.io/widget/([A-Za-z0-9_-]+)/", h) or [None, None])[1]
    kinds = [k for k in ("judge.me", "loox", "okendo", "yotpo", "stamped", "reviews.io", "junip", "trustpilot", "kudobuzz", "opinew") if k in h.lower()]
    return dom, {"shop": shop, "loox": loox, "widgets": kinds, "err": h[:40] if h.startswith("ERR") else ""}
doms = [d for k, c in D.items() if not k.startswith("_") for v in c.values() for d in v]
out = {}
with cf.ThreadPoolExecutor(8) as ex:
    for dom, r in ex.map(probe, doms): out[dom] = r; print(f"{dom:28} {r}")
json.dump(out, open("review_widgets.json", "w", encoding="utf-8"), indent=1)
