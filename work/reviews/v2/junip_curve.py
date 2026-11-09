# usage: python junip_curve.py <label> <store_key> [cutoff=2024-07]
# Public Junip storefront feed (header Junip-Store-Key), newest first, cursor page[after]; counts reviews per month.
import sys, json, time, collections, urllib.request, urllib.parse
label, key = sys.argv[1], sys.argv[2]; cutoff = sys.argv[3] if len(sys.argv) > 3 else "2024-07"
H = {"User-Agent": "Mozilla/5.0", "Junip-Store-Key": key}
base = "https://api.juniphq.com/v1/product_reviews?page%5Bsize%5D=100&sort%5Bfield%5D=created_at&sort%5Border%5D=desc"
months = collections.Counter(); low = collections.Counter(); prods = collections.defaultdict(collections.Counter)
after = None; n = 0; oldest = None
while True:
    u = base + (f"&page%5Bafter%5D={urllib.parse.quote(after)}" if after else "")
    d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=60).read())
    rs = d.get("product_reviews", [])
    if not rs: break
    stop = False
    for r in rs:
        m = r["created_at"][:7]; oldest = m
        if m < cutoff: stop = True; break
        months[m] += 1; n += 1
        if (r.get("rating") or 5) < 5: low[m] += 1
        prods[m][(r.get("target_title") or "")[:40]] += 1
    after = d.get("meta", {}).get("page", {}).get("after")
    if stop or not after: break
    time.sleep(0.4)
json.dump({"label": label, "kind": "junip", "counted": n, "cutoff": cutoff,
           "monthly": {k: {"all": months[k], "below5": low[k], "top_products": prods[k].most_common(3)} for k in sorted(months)}},
          open(f"{label}_junip.json", "w"), indent=1)
print(label, "junip counted", n, "oldest seen", oldest)
print(" ".join(f"{k[2:]}:{months[k]}" for k in sorted(months)))
