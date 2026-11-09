"""Survival of newcomer brands from graveyard/<pid>.json (Amazon, 2026-11-07).

Entry date of a listing: 'Date First Available' if shown; otherwise estimated from the ASIN.
ASINs starting 'B0' have been issued in increasing order since ~2020; we calibrate on every dated
listing across all files (piecewise-linear interpolation over a running median). Older ASINs -> 24+ months.
Brand: byline; if missing, the first two words of the title.
Brand entry = its oldest on-target listing. Success = any listing with 'bought in past month' >= 100.
"""
import json, re, pathlib, datetime as dt, statistics as st
TODAY = dt.date(2026, 11, 7)
D = pathlib.Path(__file__).with_name("graveyard")
FILES = sorted(f for f in D.glob("*.json") if not f.stem.startswith(("survival", "table")))
COH = [("0-6 mo", 0, 6), ("6-12 mo", 6, 12), ("12-24 mo", 12, 24), ("24+ mo", 24, 9999)]

def aval(a):  # ASIN B0xxxx -> int over chars 2..6
    return int(a[2:7], 36) if a.startswith("B0") and re.fullmatch(r"[0-9A-Z]{10}", a) else None
def pdate(s):
    try: return dt.datetime.strptime(s, "%B %d, %Y").date()
    except (ValueError, TypeError): return None

pts = []
for f in FILES:
    for a, x in json.loads(f.read_text(encoding="utf-8"))["listings"].items():
        v, d = aval(a), pdate(x["first"])
        if v and d and d.year >= 2019: pts.append((v, d.toordinal()))
pts.sort()
# running median of 5 to drop outliers (old products relisted etc.), then keep monotone
sm = []
for i in range(len(pts)):
    w = [p[1] for p in pts[max(0, i-2):i+3]]
    sm.append((pts[i][0], st.median(w)))
mono = []
for v, o in sm:
    if not mono or o >= mono[-1][1]: mono.append((v, o))

def est(a):
    v = aval(a)
    if v is None: return None  # pre-2020 style ASIN
    if v <= mono[0][0]: return dt.date.fromordinal(int(mono[0][1]))
    for (v1, o1), (v2, o2) in zip(mono, mono[1:]):
        if v1 <= v <= v2:
            return dt.date.fromordinal(int(o1 + (o2 - o1) * (v - v1) / max(1, v2 - v1)))
    (va, oa), (vb, ob) = mono[-8], mono[-1]  # extrapolate with the recent slope
    o = ob + (ob - oa) * (v - vb) / max(1, vb - va)
    return dt.date.fromordinal(int(min(o, TODAY.toordinal())))

# calibration error on dated points
errs = [abs((est_d - dt.date.fromordinal(o)).days) / 30.44 for v, o in pts
        for est_d in [None] if False]
def age_m(a, x):
    d = pdate(x["first"]) or est(a)
    return 999 if d is None else (TODAY - d).days / 30.44

chk = []
for f in FILES:
    for a, x in json.loads(f.read_text(encoding="utf-8"))["listings"].items():
        d = pdate(x["first"]); e = est(a)
        if d and e and d.year >= 2021: chk.append(abs((d - e).days) / 30.44)
print(f"ASIN-date calibration: {len(pts)} dated points; median error {st.median(chk):.1f} mo, 80th pct {sorted(chk)[int(.8*len(chk))]:.1f} mo")

out = {}
for f in FILES:
    L = json.loads(f.read_text(encoding="utf-8"))["listings"]
    brands = {}
    for a, x in L.items():
        k = x["brand"] or " ".join(re.findall(r"[a-z0-9']+", x["title"].lower())[:2])
        b = brands.setdefault(k, {"age": 0, "b": 0, "r": 0, "n": 0})
        b["n"] += 1; b["age"] = max(b["age"], age_m(a, x)); b["b"] = max(b["b"], x["b"]); b["r"] = max(b["r"], x["r"])
    tot = sum(b["b"] for b in brands.values()) or 1
    print(f"\n== {f.stem}: {len(L)} listings, {len(brands)} brands; badge units on page = {tot:,}")
    print(f"{'cohort':9}{'brands':>7}{'>=100':>7}{'>=1K':>6}{'surv':>6}{'share of units':>15}")
    out[f.stem] = {}
    for name, lo, hi in COH:
        c = [b for b in brands.values() if lo <= b["age"] < hi]
        n = len(c); s = sum(b["b"] >= 100 for b in c); s1 = sum(b["b"] >= 1000 for b in c)
        sh = sum(b["b"] for b in c) / tot
        out[f.stem][name] = dict(brands=n, s100=s, s1k=s1, share=round(sh, 3))
        print(f"{name:9}{n:>7}{s:>7}{s1:>6}{(s/n if n else 0):>6.0%}{sh:>15.0%}")
(D / "survival.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
