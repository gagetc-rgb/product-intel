"""Judge.me monthly review curve (2026-11-09).
Public storefront feed api.judge.me/reviews/all_reviews_js_based (newest first, 25/page) stops at page 40 (1,000 reviews).
So: (1) ALL feed -> exact monthly counts for the months it fully covers (recent);
    (2) feeds filtered to 1,2,3,4 stars -> go much deeper because they are rarer -> exact monthly NON-5-star counts;
    (3) estimate for older months = non5(month) * k, k = all/non5 measured on the fully covered recent months.
(3) assumes a stable star mix (marked ◈). Usage: python jm_curve.py <label> <shop.myshopify.com>"""
import sys, re, json, time, collections, urllib.request, datetime as dt
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/131.0"}
label, shop = sys.argv[1], sys.argv[2]
base = f"https://api.judge.me/reviews/all_reviews_js_based?url={shop}&shop_domain={shop}&platform=shopify&per_page=25&review_type=product-reviews"
def page(p, extra=""):
    for k in range(3):
        try:
            d = json.loads(urllib.request.urlopen(urllib.request.Request(base + f"&page={p}{extra}", headers=UA), timeout=60).read())
            return [x[:10] for x in re.findall(r"data-content='(20\d\d-\d\d-\d\d)[^']*'", d["html"])], d
        except Exception: time.sleep(4)
    return [], {}
def feed(extra=""):
    dates, last_first = [], None
    for p in range(1, 41):
        ds, d = page(p, extra)
        fid = (re.findall(r"data-review-id='([^']+)'", d.get('html','')) or [None])[0]
        if not ds or fid == last_first: break
        if len(ds) != 25: print('  page', p, extra, 'dates', len(ds))
        last_first = fid; dates += ds; time.sleep(0.3)
        if len(ds) < 20 and len(d.get('html','')) < 2000: break
    return dates
all_d = feed(); _, d1 = page(1); total = d1.get("number_of_product_reviews")
capped = len(all_d) >= 1000
non5 = []; non5_capped = False
for s in (1, 2, 3, 4):
    f = feed(f"&filter_rating={s}"); non5 += f; non5_capped |= len(f) >= 1000
M = lambda ds: collections.Counter(x[:7] for x in ds)
ma, mn = M(all_d), M(non5)
oldest_all = min(all_d) if all_d else None
full_months = sorted(m for m in ma if (not capped) or m > oldest_all[:7])  # months fully inside the ALL window
cur = dt.date.today().strftime("%Y-%m")
calib = [m for m in full_months if m != cur]
k_recent = (sum(ma[m] for m in calib) / max(1, sum(mn[m] for m in calib))) if calib else None
# level: whole-history ratio when the non-5 feeds are complete (not capped); else the recent ratio
k = (total / len(non5)) if (total and non5 and not non5_capped) else k_recent
months = sorted(set(ma) | set(mn))
rows = {m: {"all_exact": ma[m] if m in full_months else None, "non5": mn[m],
            "est": ma[m] if m in full_months else (round(mn[m] * k) if k else None)} for m in months}
out = {"label": label, "shop": shop, "total_product_reviews": total, "all_feed_n": len(all_d), "all_feed_capped": capped,
       "all_window_from": oldest_all, "non5_n": len(non5), "non5_from": min(non5) if non5 else None,
       "k_all_per_non5": round(k, 2) if k else None, "k_recent": round(k_recent, 2) if k_recent else None, "non5_capped": non5_capped, "calib_months": calib, "monthly": rows, "partial_month": cur}
json.dump(out, open(f"{label}_judgeme.json", "w"), indent=1)
print(f"{label}: total {total}, all-feed {len(all_d)} from {oldest_all}, non5 {len(non5)} from {out['non5_from']}, k={out['k_all_per_non5']} k_recent={out['k_recent']}")
print(" ".join(f"{m[2:]}:{r['est']}{'' if r['all_exact'] is not None else '~'}" for m, r in rows.items() if m >= "2024-11"))
