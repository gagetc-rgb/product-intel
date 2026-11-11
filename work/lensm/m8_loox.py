"""M8: Loox widget, star distribution (data-dist) and the text of 1-3 star reviews. Usage: python m8_loox.py <label> <wid>
Endpoint: loox.io/widget/<wid>/reviews?limit=20&page=P&rating=R (public widget, as in work/reviews/loox_shop.py). 2 s between calls."""
import sys, re, json, time, html, urllib.request, pathlib
label, wid = sys.argv[1], sys.argv[2]
R = pathlib.Path(__file__).parent
def get(u):
    for k in range(2):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read().decode("utf-8", "replace")
        except Exception: time.sleep(5)
    return ""
out = {"label": label, "wid": wid, "dist": None, "reviews": []}
for rating in (1, 2, 3):
    seen = set(); p = 1
    while p <= 40:
        h = get(f"https://loox.io/widget/{wid}/reviews?limit=20&page={p}&rating={rating}"); time.sleep(2)
        if not h: break
        if out["dist"] is None:
            m = re.search(r'data-dist="([\d,]+)"', h)
            if m: out["dist"] = [int(x) for x in m.group(1).split(",")]
        parts = re.split(r'(?=<div[^>]*data-id="[^"]+"[^>]*class="grid-item-wrap)', h)[1:]
        new = 0
        for s in parts:
            i = re.search(r'data-id="([^"]+)"', s).group(1)
            if i in seen: continue
            seen.add(i); new += 1
            st = re.search(r"Rating icons:\s*(\d) / 5", s); tx = re.search(r'main-text">(.*?)</div>', s, re.S); pr = re.search(r'class="name[^"]*">(.*?)</div>', s, re.S)
            dt_ = re.search(r"data-time='(\d+)'", s)
            out["reviews"].append({"id": i, "stars": int(st.group(1)) if st else rating, "text": html.unescape(re.sub(r"<[^>]+>", "", tx.group(1))).strip() if tx else "", "product": html.unescape(pr.group(1)).strip() if pr else "", "ms": int(dt_.group(1)) if dt_ else None})
        tot = re.search(r"total=(\d+)", h)
        if not new or len(seen) >= (int(tot.group(1)) if tot else 10**9): break
        p += 1
    print(label, rating, len(seen), flush=True)
(R / f"raw_rev/{label}_loox_low.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(out["dist"], len(out["reviews"]))
