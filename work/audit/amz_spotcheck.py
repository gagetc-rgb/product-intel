"""Amazon spot-check (2026-11-09): for each category print (1) included listings covering 90% of units, for a manual
'is this our product?' read; (2) possible variant double counts: same brand + same review count (shared parent);
(3) the biggest EXCLUDED listings (filter may cut real products). Reads saved scans only, no Amazon access."""
import json, sys, collections
sys.path.insert(0, "."); import graveyard_stats2 as g
pid = sys.argv[1]; src = sys.argv[2] if len(sys.argv) > 2 else "graveyard_us"
L = json.load(open(f"{src}/{pid}.json", encoding="utf-8"))["listings"]
inc = {a: x for a, x in L.items() if g.on_target(pid, x["title"]) and x["b"] > 0}
exc = sorted([(x["b"], a, x) for a, x in L.items() if not g.on_target(pid, x["title"]) and x["b"] >= 1000], key=lambda t: -t[0])
U = sum(x["b"] for x in inc.values()); acc = 0
print(f"== {pid}: included {len(inc)} listings with sales, {U:,} units")
for a, x in sorted(inc.items(), key=lambda t: -t[1]["b"]):
    k = g.norm(x["brand"]) or g.title_brand(x["title"]) or "-"
    print(f"  {x['b']:>7,} r{x['r']:<6} {k[:12]:12} {x["title"][:75]}")
    acc += x["b"]
    if acc >= 0.75 * U or (U and acc >= 0.5 * U and x["b"] < 2000): break
grp = collections.defaultdict(list)
for a, x in inc.items():
    k = g.norm(x["brand"]) or g.title_brand(x["title"])
    if k and x["r"] >= 30: grp[(k, x["r"])].append((a, x["b"]))
d = [(k, v) for k, v in grp.items() if len(v) > 1]
print("  VARIANTS same brand+review count:", d if d else "none")
print("  EXCLUDED >=1K:", [(b, x["title"][:70]) for b, a, x in exc[:6]] or "none")
