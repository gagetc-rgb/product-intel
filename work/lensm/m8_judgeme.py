"""M8: Judge.me public widget endpoint (as in work/review_fetch.py): all reviews for one store, product_id=0 (store-level reviews).
Usage: python m8_judgeme.py <label> <shop>.myshopify.com   Output raw_rev/<label>_jm_low.json (dist over all reads, text of 1-3 star reviews)"""
import sys, re, json, time, html, urllib.request, pathlib
label, shop = sys.argv[1], sys.argv[2]; pid = sys.argv[3] if len(sys.argv) > 3 else "0"
R = pathlib.Path(__file__).parent
def get(u):
    for k in range(2):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read().decode("utf-8", "replace")
        except Exception: time.sleep(5)
    return ""
allr = []; seen = set(); total = None; p = 1
while p <= 300:
    raw = get(f"https://judge.me/reviews/reviews_for_widget?url={shop}&shop_domain={shop}&platform=shopify&page={p}&per_page=20&sort_by=created_at&sort_dir=desc&product_id={pid}"); time.sleep(2)
    if not raw: break
    try: j = json.loads(raw)
    except Exception: break
    total = j.get("total_count", total); h = j.get("html", "")
    parts = re.split(r"(?=<div class='jdgm-rev jdgm-divider-top')", h)[1:]
    new = 0
    for s in parts:
        i = re.search(r"data-review-id='([^']+)'", s).group(1)
        if i in seen: continue
        seen.add(i); new += 1
        sc = re.search(r"data-score='(\d)'", s); b = re.search(r"jdgm-rev__body'>(.*?)</div>", s, re.S); t = re.search(r"jdgm-rev__timestamp[^>]*data-content='([^']+)'", s)
        pt = re.search(r"data-product-title='([^']*)'", s)
        allr.append({"id": i, "stars": int(sc.group(1)) if sc else None, "text": html.unescape(re.sub(r"<[^>]+>", " ", b.group(1))).strip() if b else "", "date": t.group(1)[:10] if t else "", "product": html.unescape(pt.group(1)) if pt else ""})
    if not new or len(seen) >= (total or 0): break
    p += 1
dist = [sum(1 for r in allr if r["stars"] == k) for k in range(1, 6)]
low = [r for r in allr if r["stars"] and r["stars"] <= 3]
(R / f"raw_rev/{label}_jm{"" if pid == "0" else "p"}_low.json").write_text(json.dumps({"label": label, "shop": shop, "total_count": total, "read": len(allr), "dist": dist, "reviews": low}, ensure_ascii=False, indent=1), encoding="utf-8")
print(label, "total", total, "read", len(allr), "dist", dist, "low", len(low))
