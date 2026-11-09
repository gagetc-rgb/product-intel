"""Summarise meta_ages/<pid>.json: ad longevity (Meta counts) and stores (sample grouped by landing domain). Frozen 2026-11-07.
Store = registrable landing domain (persona pages and creators pointing to one shop count once);
if the ad lands on a marketplace (amazon, tiktok, walmart) or has no domain, store = page name.
"""
import json, re, sys, pathlib, datetime as dt
TODAY = dt.date(2026, 11, 7)
D = pathlib.Path(__file__).with_name("meta_ages")
MKT = ("amazon.", "tiktok.", "walmart.", "etsy.", "ebay.", "target.", "facebook.", "instagram.", "fb.me", "fb.com")

def reg(dom):
    p = dom.split(".")
    return ".".join(p[-3:]) if len(p) >= 3 and p[-2] in ("co", "com") and len(p[-1]) == 2 else ".".join(p[-2:])

def pagekey(p): return re.sub(r"^(in creates with|.* with) ", "", p.lower()).strip()

def store_of(a, p2d):
    d = a["domain"]
    if d and not any(m in d for m in MKT): return reg(d)
    k = pagekey(a["page"])
    return p2d.get(k) or ("page:" + k)  # a page seen elsewhere with its own shop domain counts as that shop

def summary(pid):
    d = json.loads((D / f"{pid}.json").read_text(encoding="utf-8"))
    p2d = {}
    for a in d["ads"]:
        if a["domain"] and not any(m in a["domain"] for m in MKT): p2d.setdefault(pagekey(a["page"]), reg(a["domain"]))
    st = {}
    for a in d["ads"]:
        if not a["start"]: continue
        age = (TODAY - dt.date.fromisoformat(a["start"])).days
        s = st.setdefault(store_of(a, p2d), {"ads": 0, "max_age": 0, "pages": set()})
        s["ads"] += a["n"]; s["max_age"] = max(s["max_age"], age); s["pages"].add(a["page"])
    surv = {k: v for k, v in st.items() if v["max_age"] >= 90}
    return dict(pid=pid, phrase=d["phrase"], active=d["active"], aged90=d["aged90"], aged180=d["aged180"],
                p90=round(d["aged90"] / d["active"], 3) if d["active"] else None,
                p180=round(d["aged180"] / d["active"], 3) if d["active"] else None,
                sample=len(d["ads"]), stores=len(st), stores90=len(surv),
                top=sorted(((k, v["ads"], v["max_age"], len(v["pages"])) for k, v in st.items()), key=lambda t: (-t[2], -t[1]))[:12])

if __name__ == "__main__":
    pids = sys.argv[1:] or sorted(f.stem for f in D.glob("*.json") if f.stem != "summary")
    out = [summary(p) for p in pids]
    for r in sorted(out, key=lambda r: -(r["active"] or 0)):
        print(f"\n{r['pid']:17} '{r['phrase']}': active {r['active']:,}  >=90d {r['aged90']:,} ({r['p90']:.0%})  >=180d {r['aged180']:,} ({r['p180']:.1%})"
              f" | sample {r['sample']} ads -> {r['stores']} stores, {r['stores90']} with an ad >=90d")
        for k, n, age, pages in r["top"]: print(f"     {k[:38]:38} ads {n:>3}  oldest {age:>4}d  pages {pages}")
    (D / "summary.json").write_text(json.dumps(out, indent=1, default=list), encoding="utf-8")
