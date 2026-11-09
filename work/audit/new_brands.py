"""All brands counted as NEW (<24 months on Amazon, not in EST) with >=1,000 units/mo, per category: key, units, a title."""
import json, sys
sys.path.insert(0, "."); import graveyard_stats2 as g, graveyard_table as t
out = []
for pid in t.CATS + t.CATS_NEW:
    src = "graveyard_us"
    L = {a: x for a, x in json.load(open(f"{src}/{pid}.json", encoding="utf-8"))["listings"].items() if g.on_target(pid, x["title"])}
    ent, bu, tit = {}, {}, {}
    for a, x in L.items():
        k = g.norm(x["brand"]) or g.title_brand(x["title"]) or "solo:" + a; age = g.age_m(a, x)
        ent[k] = max(ent.get(k, 0), age); bu[k] = bu.get(k, 0) + x["b"]; tit.setdefault(k, (x.get("brand") or "") + " | " + x["title"][:60])
    tot = sum(bu.values()) or 1
    for k, u in sorted(bu.items(), key=lambda kv: -kv[1]):
        if k.startswith("solo:") or k in t.EST or ent[k] >= 24 or u < 1000: continue
        out.append({"pid": pid, "key": k, "units": u, "amz_months": ent[k], "share": round(u / tot, 3), "title": tit[k]})
json.dump(out, open("../audit/new_brands.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
for r in out: print(f"{r['pid'][:13]:13} {r['key'][:14]:14} {r['units']:>7,} {r['amz_months']:>3}m  {r['title'][:70]}")
print(len(out))
