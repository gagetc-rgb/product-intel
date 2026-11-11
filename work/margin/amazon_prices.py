"""Selling price per category for the margin model (2026-11-10), from the saved Amazon US scans (work/blind/graveyard_us),
same on-target filter as metrics_v22.py. 'Typical price' = median price of the listings that sell 1,000+ a month
(what a newcomer has to price against); falls back to 300+ when fewer than 5 listings reach 1,000.
Also prints the top sellers so the format (single item, 2-pack, 5 masks...) can be matched with the supplier quote.
Usage (from work/blind): python ../margin/amazon_prices.py  ->  ../margin/amazon_prices.json"""
import json, sys, pathlib, re, statistics as st
sys.path.insert(0, "."); import graveyard_stats2 as g
OUT = pathlib.Path(__file__).with_name("amazon_prices.json")
def price(x):
    m = re.search(r"\d+(?:\.\d+)?", str(x.get("price") or "").replace(",", ""))
    return float(m.group()) if m else None
res = {}
for f in sorted(pathlib.Path("graveyard_us").glob("*.json")):
    pid = f.stem
    L = [x for x in json.load(open(f, encoding="utf-8"))["listings"].values() if g.on_target(pid, x["title"]) and price(x)]
    L.sort(key=lambda x: -x.get("b", 0))
    top = [x for x in L if x.get("b", 0) >= 1000]; base = "1000+"
    if len(top) < 5: top = [x for x in L if x.get("b", 0) >= 300]; base = "300+"
    if not top: continue
    ps = [price(x) for x in top]
    res[pid] = {"typical": round(st.median(ps), 2), "q1": round(st.quantiles(ps, n=4)[0], 2) if len(ps) > 3 else min(ps),
                "q3": round(st.quantiles(ps, n=4)[2], 2) if len(ps) > 3 else max(ps), "n": len(ps), "base": base,
                "top": [[x.get("b"), price(x), x["title"][:90]] for x in top[:6]]}
    print(f"{pid:19} typical ${res[pid]['typical']:>6} (q1 {res[pid]['q1']}, q3 {res[pid]['q3']}, n={len(ps)} at {base})")
    for b, p, t in res[pid]["top"]: print(f"      {b:>6} ${p:<6} {t}")
json.dump(res, open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
