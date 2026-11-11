"""M8: Judge.me public widget (as in work/review_fetch.py) with filter_rating=N. Star counts for 1-5 and text of all 1-3 star reviews.
Usage: python m8_judgeme2.py <label> <shop>.myshopify.com <product_id|0>   (0 = store-level reviews)
Output raw_rev/<label>_jm_low.json in the same shape as m8_loox.py (dist = [1*,2*,3*,4*,5*])."""
import sys, re, json, time, html, urllib.request, pathlib
label, shop, pid = sys.argv[1], sys.argv[2], sys.argv[3]
R = pathlib.Path(__file__).parent
def get(r, p):
    u = f"https://judge.me/reviews/reviews_for_widget?url={shop}&shop_domain={shop}&platform=shopify&page={p}&per_page=20&sort_by=created_at&sort_dir=desc&product_id={pid}&filter_rating={r}"
    for k in range(2):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read().decode("utf-8", "replace"))
        except Exception: time.sleep(5)
    return None
dist = []; low = []
for r in (1, 2, 3, 4, 5):
    j = get(r, 1); time.sleep(2)
    tot = (j or {}).get("total_count", 0) if j else None; dist.append(tot)
    if r > 3 or not j: continue
    seen = set(); p = 1
    while j and p <= 100:
        parts = re.split(r"(?=<div class='jdgm-rev jdgm-divider-top')", j.get("html", ""))[1:]; new = 0
        for s in parts:
            i = re.search(r"data-review-id='([^']+)'", s).group(1)
            if i in seen: continue
            seen.add(i); new += 1
            sc = re.search(r"data-score='(\d)'", s); b = re.search(r"jdgm-rev__body'>(.*?)</div>", s, re.S); t = re.search(r"jdgm-rev__timestamp[^>]*data-content='([^']+)'", s); pt = re.search(r"data-product-title='([^']*)'", s)
            low.append({"id": i, "stars": int(sc.group(1)) if sc else r, "text": html.unescape(re.sub(r"<[^>]+>", " ", b.group(1))).strip() if b else "", "date": t.group(1)[:10] if t else "", "product": html.unescape(pt.group(1)) if pt else ""})
        if not new or len(seen) >= (tot or 0): break
        p += 1; time.sleep(2); j = get(r, p)
    print(label, r, tot, len(seen), flush=True)
(R / f"raw_rev/{label}_jm_low.json").write_text(json.dumps({"label": label, "shop": shop, "pid": pid, "dist": dist, "reviews": low}, ensure_ascii=False, indent=1), encoding="utf-8")
print(label, dist, len(low))
