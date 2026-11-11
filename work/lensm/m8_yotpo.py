"""M8: Yotpo public widget API, star counts and text of 1-3 star reviews. Usage: python m8_yotpo.py <label> <app_key> <product_id>"""
import sys, json, time, urllib.request, pathlib, html
label, key, pid = sys.argv[1:4]; R = pathlib.Path(__file__).parent
def get(star):
    u = f"https://api-cdn.yotpo.com/v1/widget/{key}/products/{pid}/reviews.json?per_page=100&page=1&star={star}"
    try: return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read())["response"]
    except Exception as e: print("err", star, str(e)[:80]); return None
dist = None; rev = []
for st in (1, 2, 3):
    j = get(st); time.sleep(2)
    if not j: continue
    if dist is None:
        d = j["bottomline"]["star_distribution"]; dist = [d[str(i)] for i in range(1, 6)]
    for r in j["reviews"]:
        rev.append({"id": r["id"], "stars": int(r["score"]), "text": html.unescape((r.get("title") or "") + ". " + (r.get("content") or "")).strip(". "), "date": r["created_at"][:10]})
    print(label, st, len(j["reviews"]), "of", j["pagination"]["total"] if False else "", flush=True)
(R / f"raw_rev/{label}_yotpo_low.json").write_text(json.dumps({"label": label, "dist": dist, "reviews": rev}, ensure_ascii=False, indent=1), encoding="utf-8")
print(label, dist, len(rev))
