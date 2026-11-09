"""Loox shop-wide review curve when the widget hides dates (2026-11-09).
Photo reviews carry their upload date in the image URL (images.loox.io/uploads/YYYY/M/D/...).
We page the shop-wide widget with limit=L (server returns ~20 per call, pages advance by L => systematic sample)
and count, per month, the reviews whose photo is dated. Output is the PHOTO-review curve (shape only).
Usage: python loox_photo.py <label> <wid> <total> [L]"""
import sys, re, json, time, collections, urllib.request
label, wid, total = sys.argv[1], sys.argv[2], int(sys.argv[3]); L = int(sys.argv[4]) if len(sys.argv) > 4 else 100
c = collections.Counter(); seen = 0; dated = 0
for p in range(1, (total + L - 1) // L + 1):
    for k in range(3):
        try:
            h = urllib.request.urlopen(urllib.request.Request(f"https://loox.io/widget/{wid}/reviews?limit={L}&page={p}",
                headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read().decode("utf-8", "replace"); break
        except Exception: time.sleep(5)
    else: continue
    ids = list(dict.fromkeys(re.findall(r'id="review-([A-Za-z0-9_-]+)-stars"', h)))
    if not ids: continue
    seen += len(ids); w = min(L, total - (p - 1) * L) / len(ids)
    # split html per review and take the first dated upload in each block
    for i, rid in enumerate(ids):
        a = h.find(f'review-{rid}-'); b = h.find(f'review-{ids[i+1]}-') if i + 1 < len(ids) else len(h)
        m = re.search(r'images\.loox\.io/uploads/(20\d\d)/(\d{1,2})/\d{1,2}/', h[a:b])
        if m: c[f"{m.group(1)}-{int(m.group(2)):02d}"] += w; dated += 1
    time.sleep(0.3)
out = {k: round(c[k]) for k in sorted(c)}
json.dump({"label": label, "wid": wid, "total": total, "sampled": seen, "with_photo_date": dated, "photo_reviews_monthly_est": out},
          open(f"{label}_loox_photo.json", "w"), indent=1)
print(label, "sampled", seen, "dated", dated)
for k, v in list(out.items())[-24:]: print(k, v)
