"""Lens M, metric M2 (METRICS.md v2.4): follower stores that keep ads alive 90+ days.
Step 1: from the saved category samples (work/blind/meta_ages/<pid>.json, Meta Ad Library US, 2026-11-07)
list every landing domain with its oldest sampled ad. No network. Output: work/lensm/m2_candidates.json
Limits: the sample is ~60 ads per category found by a category phrase, so it is a floor and contains off-target
advertisers (clinics, dealers); step 2 (m2_check.py) reads each store."""
import json, pathlib, datetime as dt, sys
sys.path.insert(0, str(pathlib.Path(__file__).parents[1] / "blind"))
from meta_stats import reg, pagekey, MKT
R = pathlib.Path(__file__).parents[2]
D = R / "work/blind/meta_ages"
out = {}
for f in sorted(D.glob("*.json")):
    if f.stem.startswith("dom_") or f.stem in ("summary", "carplay", "steam_cleaner"): continue
    d = json.loads(f.read_text(encoding="utf-8"))
    if not isinstance(d, dict) or "ads" not in d: continue
    day = dt.date.fromisoformat(d["date"]); st = {}
    for a in d["ads"]:
        if not a.get("start") or not a.get("domain") or any(m in a["domain"] for m in MKT): continue
        s = st.setdefault(reg(a["domain"]), {"ads": 0, "max_age": 0, "pages": set(), "hosts": set()})
        s["ads"] += a["n"]; s["max_age"] = max(s["max_age"], (day - dt.date.fromisoformat(a["start"])).days)
        s["pages"].add(a["page"]); s["hosts"].add(a["domain"])
    nodom = sum(1 for a in d["ads"] if not a.get("domain"))
    out[f.stem] = {"phrase": d["phrase"], "date": d["date"], "active": d["active"], "aged90": d["aged90"], "aged180": d.get("aged180"),
                   "sample": len(d["ads"]), "sample_no_domain": nodom,
                   "stores": sorted(({"domain": k, "ads": v["ads"], "max_age": v["max_age"], "pages": sorted(v["pages"]), "hosts": sorted(v["hosts"])}
                                     for k, v in st.items()), key=lambda s: -s["max_age"])}
(R / "work/lensm/m2_candidates.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
for p, v in out.items():
    s90 = [s for s in v["stores"] if s["max_age"] >= 90]
    print(f"{p:20s} phrase={v['phrase']!r:32s} active={v['active']:>6} 90+={v['aged90']:>5} sample={v['sample']:>3} nodom={v['sample_no_domain']:>2} stores={len(v['stores']):>2} stores90={len(s90):>2}")
    print("    " + ", ".join(f"{s['domain']}({s['max_age']}d)" for s in s90[:14]))
