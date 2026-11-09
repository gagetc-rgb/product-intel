# usage: python paged_curve.py <label> stamped|yotpo <shop_or_key> [apikey] [cutoff=2024-07]
# Pages a public storefront review feed newest-first back to cutoff and counts reviews per month.
import sys, json, time, collections, urllib.request
label, kind = sys.argv[1], sys.argv[2]
UA = {"User-Agent": "Mozilla/5.0"}
def get(u): return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read())
if kind == "stamped":
    shop, key = sys.argv[3], sys.argv[4]; cutoff = sys.argv[5] if len(sys.argv) > 5 else "2024-07"; per = 100
    url = lambda p: f"https://stamped.io/api/widget/reviews?storeUrl={shop}&apiKey={key}&take={per}&page={p}&sort=recent"
    rows = lambda d: d.get("data", [])
    def ym(r): m, d_, y = r["reviewDate"].split("/"); return f"{y}-{m}"
    rating = lambda r: r.get("reviewRating", 5); prod = lambda r: r.get("productName", "")
    total_of = lambda d: d.get("total")
else:
    key = sys.argv[3]; cutoff = sys.argv[4] if len(sys.argv) > 4 else "2024-07"; per = 100
    url = lambda p: f"https://api-cdn.yotpo.com/v1/widget/{key}/reviews.json?per_page={per}&page={p}&sort=date"
    rows = lambda d: d["response"].get("reviews", [])
    ym = lambda r: r["created_at"][:7]; rating = lambda r: r.get("score", 5)
    groups = {}
    prod = lambda r: ""
    total_of = lambda d: d["response"]["pagination"]["total"]
months = collections.Counter(); low = collections.Counter(); prods = collections.defaultdict(collections.Counter)
total = None; n = 0; oldest = None; p = 1
while True:
    for k in range(3):
        try: d = get(url(p)); break
        except Exception as e: err = e; time.sleep(4)
    else: print("fail page", p, err); break
    if total is None: total = total_of(d)
    rs = rows(d)
    if not rs: break
    stop = False
    for r in rs:
        m = ym(r); oldest = m
        if m < cutoff: stop = True; break
        months[m] += 1; n += 1
        if (rating(r) or 5) < 5: low[m] += 1
        prods[m][prod(r)[:40]] += 1
    if stop: break
    p += 1; time.sleep(0.4)
json.dump({"label": label, "kind": kind, "total": total, "counted": n, "cutoff": cutoff,
           "monthly": {k: {"all": months[k], "below5": low[k], "top_products": prods[k].most_common(3)} for k in sorted(months)}},
          open(f"{label}_{kind}.json", "w"), indent=1)
print(label, kind, "total", total, "counted", n, "pages", p, "oldest seen", oldest)
print(" ".join(f"{k[2:]}:{months[k]}" for k in sorted(months)))
