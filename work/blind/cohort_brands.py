"""Cohort for the cross-channel check (2026-11-07): brands that entered Amazon 12-24 months ago.
Uses the v2 definitions (graveyard_def.on_target, graveyard_stats2 brand keys) so it matches survival2.json.
Output: cohort/brands.json, one row per brand: best badge, max reviews, listing count, best ASIN + title."""
import json, sys, io, contextlib, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import types
HERE = pathlib.Path(__file__).parent
# graveyard_stats2 imports graveyard_stats, whose file glob also picks up survival2.json; patch the glob, not their files
src2 = (HERE / "graveyard_stats2.py").read_text(encoding="utf-8").split('if __name__ == "__main__":')[0]
src2 = src2.replace("exec(src)", "exec(src.replace('f.stem != \"survival\"', 'not f.stem.startswith(\"survival\")'))")
g2 = types.ModuleType("g2"); g2.__dict__["__file__"] = str(HERE / "graveyard_stats2.py")
with contextlib.redirect_stdout(io.StringIO()):
    exec(src2, g2.__dict__)
from graveyard_def import on_target
CATS = sys.argv[1:] or ["exfoliating_towel", "turmeric_soap", "magnesium_spray"]
rows = []
for pid in CATS:
    L = json.loads((g2.D / f"{pid}.json").read_text(encoding="utf-8"))["listings"]
    L = {a: x for a, x in L.items() if on_target(pid, x["title"])}
    ent = {}
    for a, x in L.items():
        k = g2.norm(x["brand"]) or g2.title_brand(x["title"]) or ("solo:" + a)
        e = ent.setdefault(k, {"cat": pid, "key": k, "byline": x["brand"], "age": 0, "b": -1, "r": 0, "n": 0})
        e["n"] += 1; e["age"] = max(e["age"], g2.age_m(a, x)); e["r"] = max(e["r"], x["r"])
        if x["b"] > e["b"]: e.update(b=x["b"], asin=a, title=x["title"])
        if x["brand"] and not e["byline"]: e["byline"] = x["brand"]
    rows += [dict(e, age=round(e["age"], 1)) for e in ent.values() if 12 <= e["age"] < 24]
out = pathlib.Path(__file__).parent / "cohort"; out.mkdir(exist_ok=True)
(out / "brands.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(rows), {c: sum(r["cat"] == c for r in rows) for c in CATS})
for r in rows: print(r["cat"][:5], r["key"][:16].ljust(16), (r["byline"] or "")[:22].ljust(22), r["b"], r["r"], r["title"][:50].encode("ascii", "replace").decode())
