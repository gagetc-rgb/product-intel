"""Join cohort brands with own site (classes B/C) to Meta Ad Library presence. Own-page rule: an ad counts as the brand's
when the advertiser page carries the brand name or the landing domain is the brand's site (resellers, namesakes dropped).
Run: python meta_join.py -> prints table, writes meta_join.json"""
import json, pathlib, re
H = pathlib.Path(__file__).parent
c = json.load(open(H / "classified.json", encoding="utf-8")); m = json.load(open(H / "meta_brands.json", encoding="utf-8"))
names = json.load(open(H / "brand_names.json", encoding="utf-8"))
ALIAS = {"winknaturals.com": ["winkwell.com", "wink well"], "pixiecup.com": ["itspixie.com"], "drteals.com": ["dr teal"], "purador.com": ["pura d'or"]}
# namesakes checked by hand 2026-11-07 (people, a sushi bar, a clinic, a safari operator, a different derma domain)
NAMESAKE = ("lemonier", "brian monier", "kaisen", "dermacure of valencia", "officialdermacure", "rift valley explorer")
rows = []
for b in c:
    d = b["site"]
    if not d: continue
    keys = [d.split(".")[0], names.get(d, "").lower()] + ALIAS.get(d, [])
    own = []
    for k in (d, "name:" + d):
        for a in m.get(k, {}).get("ads", []):
            txt = (a["page"] + " " + a["domain"]).lower()
            if any(x and x.lower() in txt for x in keys) and not any(n in txt for n in NAMESAKE): own.append(a)
    own = list({a["id"]: a for a in own}.values())
    st = sorted(a["start"] for a in own if a["start"])
    a90 = sum(a["start"] <= "2026-08-09" for a in own if a["start"]); a180 = sum(a["start"] <= "2026-05-11" for a in own if a["start"])
    meta_total = max(m.get(d, {}).get("active") or 0, (m.get("name:" + d, {}).get("active") or 0) if own else 0)
    rows.append({**{k: b[k] for k in ("cat", "brand", "cls", "site", "first_web", "badge", "reviews")}, "own_sample": len(own),
                 "own_90d": a90, "own_180d": a180, "oldest_own": st[0] if st else None, "meta_count_upper": meta_total if own else 0})
rows.sort(key=lambda r: (r["cat"], -r["own_sample"]))
json.dump(rows, open(H / "meta_join.json", "w", encoding="utf-8"), indent=1)
print(f"{'cat':18}{'brand':12}{'cls':4}{'badge':>6}{'rev':>7}{'own':>5}{'90d':>5}{'180d':>5}  oldest      cnt")
for r in rows:
    print(f"{r['cat'][:17]:18}{r['brand'][:11]:12}{r['cls']:4}{r['badge'] or 0:>6}{r['reviews'] or 0:>7}{r['own_sample']:>5}{r['own_90d']:>5}{r['own_180d']:>5}  {r['oldest_own'] or '-':11} {r['meta_count_upper']}")
on = [r for r in rows if r["own_sample"]]
print(f"\nbrands with own site: {len(rows)}; running own Meta ads now: {len(on)}; with any own ad 180+ days: {sum(r['own_180d']>0 for r in rows)}")
