"""Shop-wide Loox review curve (all products of a store), 2026-11-07.
Endpoint: loox.io/widget/<wid>/reviews?limit=L&page=P (public widget, no token). The server returns at most ~20 reviews
per call but pages advance by L, so with L=100 we read a systematic ~20% sample spread evenly over the whole history
(reviews come newest first); monthly counts are scaled by L/returned. Usage: python loox_shop.py <label> <wid> <total> [L]
Output: <label>_shop.json {month: est_reviews}
"""
import sys, re, json, time, collections, urllib.request
label, wid, total = sys.argv[1], sys.argv[2], int(sys.argv[3]); L = int(sys.argv[4]) if len(sys.argv) > 4 else 100
c = collections.Counter(); got = 0
for p in range(1, (total + L - 1) // L + 1):
    for k in range(3):
        try:
            h = urllib.request.urlopen(urllib.request.Request(f"https://loox.io/widget/{wid}/reviews?limit={L}&page={p}",
                headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read().decode("utf-8", "replace"); break
        except Exception: time.sleep(5)
    else: continue
    ds = re.findall(r"\b(\d{1,2})/(\d{1,2})/(20\d\d)\b", h)
    if not ds: continue
    w = min(L, total - (p - 1) * L) / len(ds)
    for m, d, y in ds: c[f"{y}-{int(m):02d}"] += w
    got += len(ds); time.sleep(0.3)
out = {k: round(c[k]) for k in sorted(c)}
json.dump({"label": label, "wid": wid, "total": total, "sampled": got, "monthly_est": out}, open(f"{label}_shop.json", "w"), indent=1)
print(label, "sampled", got, "of", total); peak = max(out.values())
for k, v in out.items(): print(k, f"{v:6d}", "#" * round(40 * v / peak))
