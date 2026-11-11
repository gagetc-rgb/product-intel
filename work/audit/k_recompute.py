"""Keyword audit (METRICS.md K), 2026-11-10: recompute Amazon B1/B2/B3 for all 20 categories under three variants.
v22   = as on the site (graveyard_def filters, graveyard_table.EST)
filt  = corrected title filters (written after seeing results; see KEYWORD_AUDIT_2026-11-10.md)
full  = filt + verified old brands removed from newcomers + same-title unbranded listings merged into one seller
Usage (from work/blind): python ../audit/k_recompute.py"""
import json, re, sys, statistics as st
sys.path.insert(0, ".")
import graveyard_stats2 as g, graveyard_table as t, graveyard_def as gd

FIX = {  # pid: (MUST, NOT); None = keep the v2.2 filter
 "lash_serum": (r"^(?=.*lash)(?=.*(serum|growth|enhanc|conditioner))",
                r"glue|adhesive|curler|mascara|remover|false|magnetic|tint|lift kit|cluster|castor"),
 "dog_fountain": (r"^(?=.*fountain)(?=.*(\bpet|\bcat|\bdog))",
                  r"filters?\b.{0,25}(replacement|pack|pcs)|replacement|\d+\s*(pack|pcs).{0,20}filter|filters? only|pump only|garden|outdoor|solar|chocolate"),
 "hair_removal_cream": (r"^(?=.*hair remov)(?=.*(cream|lotion|\bgel|depilat))",
                        r"laser|\bipl\b|device|\bepilator|razor|wax strip|powder|trimmer|shaver"),
 "body_oil": (r"^(?=.*(body oil|crep))(?=.*(firm|crep|tighten|lift|aging|ageing|elastic|sagg))",
              r"hair|lotion|cream|serum|wash|scrub|baby|massage|cellulite"),
 "prewash_oil": (r"pre.?wash|pre.?shampoo", r"\bbody\b|\bface\b|conditioner|\bmask|spray"),
 "hair_serum": (r"^(?=.*(hair|scalp))(?=.*(serum|\boil|spray|foam|tonic))(?=.*(growth|regrow|thinning|loss|thicken))",
                r"supplement|gumm|capsule|tablet|vitamin|softgel|shampoo|conditioner|minoxidil|eyelash|\blash|brow"),
}
SHORT_OK = {"compression_socks"}  # scan saved only the brand as title; the query is the product itself
OLD = {"luxe", "smooche", "prime", "magichome", "upnature", "cliganic", "foltene", "airscent", "aussie", "eight",
       "kittyspout", "feppo", "kakiyu", "morovan"}  # verified businesses older than 3 years (◈, by hand)

def on(pid, title, variant):
    if variant != "v22" and pid in SHORT_OK and len(title) < 25:
        return True
    if variant != "v22" and pid in FIX:
        m, n = FIX[pid]; return bool(re.search(m, title, re.I)) and not re.search(n, title, re.I)
    return gd.on_target(pid, title)

def calc(pid, variant):
    L = {a: x for a, x in json.load(open(f"graveyard_us/{pid}.json", encoding="utf-8"))["listings"].items()
         if on(pid, x["title"], variant)}
    ent, bu = {}, {}
    for a, x in L.items():
        k = g.norm(x["brand"]) or g.title_brand(x["title"])
        if not k:
            k = "solo:" + (re.sub(r"[^a-z ]", "", x["title"].lower())[:40] if variant == "full" else a)
        ent[k] = max(ent.get(k, 0), g.age_m(a, x)); bu[k] = bu.get(k, 0) + x["b"]
    U = sum(bu.values()) or 1
    est = set(t.EST) | (OLD if variant == "full" else set())
    E = {k for k in ent if 3 <= ent[k] < 24 and k not in est}
    win = {k for k in E if bu[k] >= 1000}; mid = {k for k in E if bu[k] >= 300}
    return {"A2": U, "B1": round(len(win) / len(E), 3) if E else None, "n": len(E), "B2": len(win),
            "HHI": round(sum((100 * v / U) ** 2 for v in bu.values())),
            "B2_300": len(mid), "unbranded_1k": sum(k.startswith("solo:") for k in win),
            "top3": round(sum(sorted(bu.values(), reverse=True)[:3]) / U, 2)}

def ranks(res):
    """Decision rule step 2: rank by B1 and B2 together (mean of the two ranks), then HHI (lower is better)."""
    ids = [p for p in res if res[p]["B1"] is not None]
    r1 = {p: i for i, p in enumerate(sorted(ids, key=lambda p: -res[p]["B1"]))}
    r2 = {p: i for i, p in enumerate(sorted(ids, key=lambda p: -res[p]["B2"]))}
    return sorted(ids, key=lambda p: ((r1[p] + r2[p]) / 2, res[p]["HHI"]))

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    pids = sorted(json.load(open("../audit/metrics_v22.json", encoding="utf-8")))
    R = {v: {p: calc(p, v) for p in pids} for v in ("v22", "filt", "full")}
    order = {v: ranks(R[v]) for v in R}
    print(f"{'category':19}" + "".join(f"{v:>34}" for v in R))
    for p in order["full"]:
        print(f"{p:19}" + "".join(f"   #{order[v].index(p)+1:<2} B1 {R[v][p]['B1']:.1%} ({R[v][p]['B2']:>2}/{R[v][p]['n']:<3}) HHI {R[v][p]['HHI']:>5}" for v in R))
    json.dump({"results": R, "order": order}, open("../audit/k_recompute.json", "w", encoding="utf-8"), indent=1)

    # metrics_v23.json (site edits v2.3, section 2): metrics_v22.json with the `filt` values + Wilson interval and group
    def wilson(k, n, z=1.96):
        p = k / n; d = 1 + z * z / n
        c = (p + z * z / (2 * n)) / d; h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
        return c - h, c + h
    M = json.load(open("../audit/metrics_v22.json", encoding="utf-8"))
    F = R["filt"]; pooled = sum(F[p]["B2"] for p in F) / sum(F[p]["n"] for p in F)
    for p, m in M.items():
        f = F[p]
        m.update({"A2": f["A2"], "B1": f["B1"], "B1_n": f["n"], "B2_1k": f["B2"], "B2_300": f["B2_300"],
                  "B3_hhi": f["HHI"], "B3_top3": f["top3"], "D1_unbranded_1k": f["unbranded_1k"]})
        lo, hi = wilson(f["B2"], f["n"]) if f["n"] else (None, None)
        m["B1_lo"], m["B1_hi"] = round(lo, 3), round(hi, 3)
        m["B1_grp"] = "above" if lo > pooled else "below" if hi < pooled else "middle"
        fl = [x for x in m["flags"] if x not in ("shelf = all body oils, not only firming/crepey", "brand-only titles: shelf undercounted by ~43K/mo")]
        fl = [x for x in fl if x != "small sample: under 20 entrants"]
        if f["n"] < 20: fl.insert(0, "small sample: under 20 entrants")
        m["flags"] = fl
    M["_pooled_B1"] = round(pooled, 4)
    json.dump(M, open("../audit/metrics_v23.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("pooled", pooled)
    for p in sorted(M, key=lambda p: -(M[p]["B1"] or 0) if not p.startswith("_") else 0):
        if p.startswith("_"): continue
        m = M[p]; print(f"{p:19}{m['B2_1k']:>3}/{m['B1_n']:<4}{m['B1']:.1%} {m['B1_lo']:.0%}-{m['B1_hi']:.0%} {m['B1_grp']:7}{m['A2']:>8,} {m['B3_hhi']:>5} {m['flags']}")
