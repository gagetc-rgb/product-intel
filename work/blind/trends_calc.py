"""B1 (2026-11-08): Google Trends pulls -> YoY per term, same rule as v2.0 (RUNBOOK rule 6).
Each pull file: trends_pulls/pullN_<date>.txt, lines 'term|last week label|v1,...,v262' (5 years weekly, US).
yoy = mean of last 12 FULL weeks / same 12 weeks one year (52 weeks) earlier; rel_yoy = yoy / mean control yoy.
Prints per term every pull and the spread between pulls."""
import json, pathlib, statistics as st
D = pathlib.Path(__file__).with_name("trends_pulls")
TERM = {"color_foundation": "color changing foundation", "persimmon_soap": "persimmon soap", "scent_diffuser": "waterless diffuser",
        "neck_cream": "neck cream", "shower_filter": "shower filter", "tallow_balm": "tallow balm", "body_oil": "crepey skin",
        "rosemary_oil": "rosemary oil for hair", "turmeric_soap": "turmeric soap", "compression_socks": "compression socks",
        "dog_fountain": "pet water fountain", "pore_patch": "pore patches", "hair_removal_cream": "hair removal cream",
        "exfoliating_towel": "exfoliating towel", "magnesium_spray": "magnesium spray", "chin_wrap": "double chin",
        "whitening_powder": "teeth whitening powder", "lash_serum": "lash serum", "hair_serum": "hair growth serum",
        "prewash_oil": "pre wash hair oil"}
CONTROLS = ("shampoo", "body lotion")
def load(f):
    out = {}
    for line in f.read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        t, last, v = line.split("|"); out[t] = [float(x) for x in v.split(",")]
    jl = f.with_suffix(".jsonl")
    if jl.exists():
        for line in jl.read_text(encoding="utf-8").splitlines():
            d = json.loads(line); out.setdefault(d["term"], [float(x) for x in d["v"].split(",")])
    return out
def yoy(v):
    v = v[:-1]  # drop the partial current week
    now, ago = v[-12:], v[-64:-52]
    return round(st.mean(now) / st.mean(ago), 2) if st.mean(ago) > 0 else None
def zero_share(v): return round(sum(1 for x in v[-104:] if x == 0) / 104, 2)
def label(r):
    return None if r is None else "growing" if r >= 1.2 else "flat" if r >= 0.8 else "falling"
if __name__ == "__main__":
    pulls = {f.stem: load(f) for f in sorted(D.glob("pull*.txt"))}
    res = {}
    for name, P in pulls.items():
        c = [yoy(P[t]) for t in CONTROLS if t in P]; cm = st.mean(c)
        for pid, t in TERM.items():
            if t not in P: continue
            y = yoy(P[t]); r = round(y / cm, 2) if y else None
            res.setdefault(pid, {"term": t, "pulls": {}})["pulls"][name] = {"yoy": y, "rel_yoy": r, "controls_yoy": c, "zero_share_2y": zero_share(P[t])}
    for pid, d in res.items():
        rs = [p["rel_yoy"] for p in d["pulls"].values() if p["rel_yoy"]]
        d["rel_yoy_mean"] = round(st.mean(rs), 2) if rs else None
        d["rel_yoy_range"] = [min(rs), max(rs)] if rs else None
        d["label"] = label(d["rel_yoy_mean"])
        d["labels_agree"] = len({label(x) for x in rs}) == 1
        print(f"{pid:19} {d['term']:26} " + " ".join(f"{k[:5]}:{v['rel_yoy']}" for k, v in d["pulls"].items()) +
              f"  mean {d['rel_yoy_mean']} {d['label']} zeros {list(d['pulls'].values())[-1]['zero_share_2y']}")
    json.dump(res, open(pathlib.Path(__file__).with_name("trends_series_summary.json"), "w"), indent=1)
