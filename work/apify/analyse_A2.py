"""Run A, our product only: which 90+ ads sell the category product, and from which pages."""
import json, collections, datetime as dt, re, pathlib
P = pathlib.Path(__file__).parent; T = dt.date(2026, 11, 11)
X = json.load(open(P / "runA_2026-11-11.json", encoding="utf-8"))
dom = lambda x: re.search(r"q=([^&]+)", x["url"]).group(1)
txt = lambda x: " ".join(str(x["snapshot"].get(k) or "") for k in ("link_url", "title", "caption")) + " " + str((x["snapshot"].get("body") or {}).get("text") or "")
OUR = {"hanaekorea.com": r"lash", "try-kaori.com": r"persimmon|nonenal|odor|soap", "wildgoldtallow.com": r"tallow|balm",
       "bare-ritual.com": r"tallow", "getmyto.com": r"tooth|powder|hydroxyapatite|whiten", "trymooths.com": r"tooth|powder|whiten",
       "facelove-cosmetics.com": r"foundat|stick", "buykglow.com": r"chin|strap|wrap|v.?line|jaw"}
OWN = {"hanaekorea.com": {"Hanae Korea", "Trending In Korea"}, "try-kaori.com": {"Kaori", "Kaori Shop"}, "wildgoldtallow.com": {"Wild Gold Tallow"},
       "bare-ritual.com": {"Bare Ritual"}, "getmyto.com": {"Myto Oral Care"}, "trymooths.com": {"Mooths"}, "facelove-cosmetics.com": {"Facelove Cosmetics", "Facelove Deals"}, "buykglow.com": {"K Glow"}}
res = {}
for d in OUR:
    L = [x for x in X if dom(x) == d]; M = [x for x in L if re.search(OUR[d], txt(x), re.I)]
    age = [(T - dt.date.fromtimestamp(x["start_date"])).days for x in M]
    own = sum(x["page_name"] in OWN[d] for x in M)
    res[d] = {"ads90": len(L), "ours90": len(M), "ours180": sum(a >= 180 for a in age), "oldest_ours": max(age or [0]),
              "ours_creatives": len({x["collation_id"] for x in M}), "ours_own_page": own, "pages": collections.Counter(x["page_name"] for x in M).most_common(6)}
    print(d, json.dumps(res[d], ensure_ascii=False))
json.dump(res, open(P / "runA_summary.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
# K-Glow: what does the balm ad say
for x in [x for x in X if dom(x) == "buykglow.com"][:4]:
    print("KGLOW:", x["snapshot"].get("title"), "|", str((x["snapshot"].get("body") or {}).get("text"))[:220].replace("\n", " "))
