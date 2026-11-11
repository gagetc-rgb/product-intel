import json, sys, pathlib
sys.argv = ["x", "me"]; P = pathlib.Path(__file__).resolve().parent
src = open(P / "apify.py", encoding="utf-8").read().split("cmd = sys.argv[1]")[0]
exec(src.replace("pathlib.Path(__file__)", f"pathlib.Path(r'{P / 'apify.py'}')"))
for a in ["curious_coder~facebook-ads-library-scraper", "harshmaur~facebook-ads-library-scraper"]:
    d = call(f"/acts/{a}")["data"]; s = d.get("stats", {})
    print(a, {k: s.get(k) for k in ("totalUsers", "totalUsers30Days", "publicActorRunStats30Days", "actorReviewRating", "actorReviewCount", "bookmarkCount")}, "created", d.get("createdAt", "")[:10], "modified", d.get("modifiedAt", "")[:10])
def flat(o, p=""):
    out = {}
    for k, v in (o.items() if isinstance(o, dict) else []):
        if isinstance(v, dict): out.update(flat(v, p + k + "."))
        else: out[p + k] = v
    return out
for f in ["pilot_cc", "pilot_hm"]:
    X = json.load(open(P / f"{f}.json", encoding="utf-8")); fx = flat(X[0]); print("\n==", f, len(fx), "fields")
    for k, v in fx.items():
        if v not in (None, "", [], {}): print("  ", k, "=", str(v)[:90])
