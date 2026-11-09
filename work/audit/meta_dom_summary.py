"""Summarise Meta Ad Library counts searched by store domain (meta_ages/dom_*.json) vs the earlier category-phrase and Page-ID counts."""
import json, glob, collections, pathlib
B = pathlib.Path("../blind/meta_ages"); rows = []
for f in sorted(B.glob("dom_*.json")):
    d = json.load(open(f, encoding="utf-8")); q = d.get("phrase") or f.stem[4:]
    s = d.get("sample") or []
    dom = [(a.get("domain") if isinstance(a, dict) else None) or "" for a in s]
    known = [x for x in dom if x]; own = sum(1 for x in known if x.split(".")[0] in q)
    rows.append({"domain": q, "active": d.get("active"), "aged30": d.get("aged30"), "aged90": d.get("aged90"), "aged180": d.get("aged180"),
                 "sample": len(s), "landing_known": len(known), "landing_own": own})
json.dump(rows, open("meta_by_domain.json", "w", encoding="utf-8"), indent=1)
for r in sorted(rows, key=lambda r: -(r["active"] or 0)):
    print(f"{r['domain']:24} active {r['active'] or 0:>6,}  30d+ {r['aged30'] or 0:>6,}  90d+ {r['aged90'] or 0:>5,}  180d+ {r['aged180'] or 0:>4,}  own landing {r['landing_own']}/{r['landing_known']}")
