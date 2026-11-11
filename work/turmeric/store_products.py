"""Turmeric soap stores (2026-11-11): read public Shopify /products.json, keep soap products, print variants and prices."""
import json, sys, urllib.request, pathlib
P = pathlib.Path(__file__).parent
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/131.0 Safari/537.36"}
for dom in sys.argv[1:]:
    allp = []
    for page in range(1, 6):
        try:
            with urllib.request.urlopen(urllib.request.Request(f"https://{dom}/products.json?limit=250&page={page}", headers=UA), timeout=30) as r:
                ps = json.loads(r.read())["products"]
        except Exception as e:
            print(dom, "ERR", e); break
        if not ps: break
        allp += ps
    json.dump(allp, open(P / f"products_{dom}.json", "w", encoding="utf-8"), ensure_ascii=False)
    print(f"\n=== {dom}: {len(allp)} products")
    for p in allp:
        if any(w in (p["title"] + " " + " ".join(p.get("tags") or [])).lower() for w in ("soap", "bar", "turmeric", "kojic")):
            vs = "; ".join(f"{v['title']} ${v['price']}" + (f" (было ${v['compare_at_price']})" if v.get("compare_at_price") else "") for v in p["variants"][:8])
            print(f"- {p['title'][:70]} | created {p['created_at'][:10]} | {vs[:300]}")
