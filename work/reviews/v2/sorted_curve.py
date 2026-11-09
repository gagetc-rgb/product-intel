"""Monthly review counts from a review feed sorted newest-first (2026-11-09).
We sample pages across the feed, read the dates on each sampled page, and interpolate the position of every month
boundary: reviews in month M = position(start of M) - position(start of M+1). Exact up to interpolation inside a page gap.
Backends: judgeme (api.judge.me/reviews/all_reviews_js_based, public storefront feed, 25/page).
Usage: python sorted_curve.py judgeme <label> <shop.myshopify.com> [since=2024-11]"""
import sys, re, json, time, math, datetime as dt, urllib.request
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/131.0"}
def get(u):
    for k in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read().decode("utf-8", "replace")
        except Exception as e: err = e; time.sleep(4)
    raise err
def judgeme(shop):
    base = f"https://api.judge.me/reviews/all_reviews_js_based?url={shop}&shop_domain={shop}&platform=shopify&per_page=25&review_type=product-reviews"
    def page(p):
        d = json.loads(get(base + f"&page={p}"))
        ds = [x[:10] for x in re.findall(r"jdgm-rev__timestamp[^>]*data-content='([^']+)'", d["html"])]
        return ds, d.get("number_of_product_reviews")
    return page, 25
def run(backend, label, shop, since):
    page, per = {"judgeme": judgeme}[backend](shop)
    ds, total = page(1); pages = math.ceil(total / per)
    pts = [(0, ds[0])] if ds else []
    for i, x in enumerate(ds): pts.append((i, x))
    # sample ~70 pages spread evenly, stop once dates fall before `since`
    step = max(1, pages // 70); p = 1 + step; oldest = ds[-1] if ds else "9999"
    while p <= pages:
        ds, _ = page(p)
        if not ds: break
        for i, x in enumerate(ds): pts.append(((p - 1) * per + i, x))
        oldest = ds[-1]; time.sleep(0.4)
        if oldest < since + "-01": break
        p += step
    pts.sort()
    # month boundaries: position of the first review older than the month start
    def pos_before(day):  # number of reviews newer than `day`
        prev = None
        for pos, d in pts:
            if d < day:
                if prev is None: return pos
                (p0, d0) = prev; t0 = dt.date.fromisoformat(d0); t1 = dt.date.fromisoformat(d); td = dt.date.fromisoformat(day)
                frac = (t0 - td).days / max(1, (t0 - t1).days)
                return round(p0 + frac * (pos - p0))
            prev = (pos, d)
        return None
    y, m = map(int, since.split("-")); today = dt.date.today(); months = {}
    while (y, m) <= (today.year, today.month):
        start = f"{y}-{m:02d}-01"; ny, nm = (y + (m == 12), m % 12 + 1); end = f"{ny}-{nm:02d}-01"
        a = pos_before(end) if (ny, nm) <= (today.year, today.month) else 0
        b = pos_before(start)
        months[f"{y}-{m:02d}"] = (b - a) if (a is not None and b is not None) else None
        y, m = ny, nm
    out = {"label": label, "backend": backend, "shop": shop, "total": total, "pages": pages, "sampled_points": len(pts),
           "newest": pts[0][1] if pts else None, "monthly": months, "partial_month": f"{today.year}-{today.month:02d}"}
    json.dump(out, open(f"{label}_{backend}.json", "w"), indent=1)
    print(label, "total", total, "points", len(pts)); print(" ".join(f"{k[2:]}:{v}" for k, v in months.items()))
if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "2024-11")
