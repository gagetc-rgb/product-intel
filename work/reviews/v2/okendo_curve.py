# usage: python okendo_curve.py <label> <domain> [cutoff=2024-07]
# Finds the Okendo subscriberId on the store homepage, pages the public storefront feed
# api.okendo.io/v1/stores/{id}/reviews (newest first, cursor via nextUrl) back to cutoff, counts reviews per month.
import sys, re, json, time, collections, urllib.request
label, domain = sys.argv[1], sys.argv[2]
cutoff = sys.argv[3] if len(sys.argv) > 3 else "2024-07"
UA = {"User-Agent": "Mozilla/5.0"}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40).read().decode("utf-8", "ignore")
html = get("https://" + domain + "/")
m = re.search(r'subscriberId"\s*:\s*"([0-9a-f-]{36})', html)
sid = m.group(1)
agg = json.loads(get(f"https://api.okendo.io/v1/stores/{sid}/review_aggregate")).get("reviewAggregate", {})
total = agg.get("ratingAndReviewCount")
url = f"/stores/{sid}/reviews?limit=100&orderBy=date%20desc"
months = collections.Counter(); low = collections.Counter(); prods = collections.defaultdict(collections.Counter)
n = 0; last = None
while url:
    d = json.loads(get("https://api.okendo.io/v1" + url))
    rs = d.get("reviews", [])
    if not rs: break
    for r in rs:
        dt = r.get("dateCreated", "")[:7]; last = dt
        if dt < cutoff: url = None; break
        months[dt] += 1; n += 1
        if (r.get("rating") or 5) < 5: low[dt] += 1
        prods[dt][(r.get("productName") or "")[:40]] += 1
    else:
        url = d.get("nextUrl")
    time.sleep(0.4)
out = {"label": label, "domain": domain, "subscriberId": sid, "total": total, "counted": n, "cutoff": cutoff,
       "monthly": {k: {"all": months[k], "below5": low[k], "top_products": prods[k].most_common(3)} for k in sorted(months)}}
json.dump(out, open(f"{label}_okendo.json", "w"), indent=1)
print(label, "sid", sid, "total", total, "counted", n, "oldest seen", last)
print(" ".join(f"{k[2:]}:{months[k]}" for k in sorted(months)))
