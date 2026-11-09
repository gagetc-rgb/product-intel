"""Verdict table v2.1 (2026-11-08): applies RUNBOOK rules 1-6 to all 20 categories from dossier_data.json.
Amazon layer = US-ZIP scan (graveyard_us/, 16 by script + 4 manual by the owner); the Indonesia-delivery scan is shown for comparison.
Meta = meta_ages (category phrase) + meta_stats (stores with a 90d+ ad). Trend = Google Trends pull(s), rel_yoy vs controls.
Writes FINAL_V21.md table part (the written verdict is added by hand below the table, marked as judgment)."""
import json, pathlib, sys
H = pathlib.Path(__file__).parent
B = H.parent / "blind"
D = json.load(open(H / "dossier_data.json", encoding="utf-8"))["categories"]
S = {r["pid"]: r for r in json.load(open(B / "meta_ages" / "summary.json"))}
# Meta phrases that measure something broader than the product (checked in the store sample)
PHRASE_NOTE = {"prewash_oil": "phrase 'pre wash' hits laundry and car-detailing ads", "chin_wrap": "phrase 'double chin' hits med-spas / surgery",
               "dog_fountain": "phrase 'water fountain' hits pond and garden fountains", "body_oil": "phrase 'crepey skin' also covers creams",
               "pore_patch": "phrase 'pore patches' finds 1 ad"}
rows = []
for pid, d in D.items():
    us = (d.get("amazon_us") or {}).get("row") or {}
    m, t, s = d["meta_category"] or {}, d.get("trend_pulls") or {}, S.get(pid, {})
    nb = us.get("brand_units"); r = t.get("rel_yoy_mean")
    kill_a = r is not None and r < 0.8
    kill_b = nb is not None and nb < 10000 and s.get("stores90", 0) == 0
    rows.append(dict(pid=pid, name=d["name"], flag=d["compliance_flag"], shelf=us.get("units"), nb=nb, gen=us.get("generic_units"),
                     winB=us.get("win_brand"), winG=us.get("win_generic"), price=(d.get("amazon_us") or {}).get("price_usd_median"),
                     act=m.get("active"), a30=m.get("aged30"), a90=m.get("aged90"), a180=m.get("aged180"),
                     stores=s.get("stores"), stores90=s.get("stores90"), trend=r,
                     zeros=(list(t.get("pulls", {}).values()) or [{}])[-1].get("zero_share_2y"),
                     kill=("a: falling demand" if kill_a else "") + ("b: no open space" if kill_b else ""),
                     note=PHRASE_NOTE.get(pid, ""), nb_id=(d.get("amazon") or {}).get("brand_units")))
def pct(a, b): return f"{a / b:.0%}" if a is not None and b else "—"
def f(x): return f"{x:,}" if isinstance(x, int) else ("—" if x is None else str(x))
L = ["| Category | Flag | Shelf units/mo | To NEW brands/mo (ID scan) | NEW brand winners | To generics/mo | Median price $ | Meta active | 30d+ | 90d+ | 180d+ | Shops with 90d+ ad | Trend ×YoY | Kill rule |",
     "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for x in sorted(rows, key=lambda x: (bool(x["kill"]), -(x["nb"] or 0))):
    L.append(f"| {x['name']} | {x['flag'] or ''} | {f(x['shelf'])} | {f(x['nb'])} ({f(x['nb_id'])}) | {f(x['winB'])} | {f(x['gen'])} | {f(x['price'])} | "
             f"{f(x['act'])} | {pct(x['a30'], x['act'])} | {pct(x['a90'], x['act'])} | {pct(x['a180'], x['act'])} | {f(x['stores90'])}/{f(x['stores'])} | "
             f"{f(x['trend'])}{' (noisy: ' + format(x['zeros'], '.0%') + ' zero weeks)' if (x['zeros'] or 0) > 0.2 else ''} | {x['kill'] or '—'}{'; ' + x['note'] if x['note'] else ''} |")
json.dump(rows, open(H / "verdict_v21.json", "w", encoding="utf-8"), indent=1)
print("\n".join(L))
