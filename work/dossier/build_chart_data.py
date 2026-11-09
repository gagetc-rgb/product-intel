"""chart_data.json for the future HTML: one block per category, every series taken from a file (no hand numbers)."""
import json, pathlib, datetime as dt, sys
H = pathlib.Path(__file__).parent; B = H.parent / "blind"
sys.path.insert(0, str(B)); from trends_calc import TERM, CONTROLS, load
P = load(B / "trends_pulls" / "pull1_2026-11-08.txt")
last = dt.date(2026, 11, 8)
def dates(n): return [(last - dt.timedelta(weeks=n - 1 - i)).isoformat() for i in range(n)]
REV = json.load(open(H / "revenue_floor.json"))
out = {"built": "2026-11-08", "notes": {"trend": "Google Trends US weekly index 0-100 (pull 1, 2026-11-08); last week partial; Apr-Jun 2026 spike also on controls = artifact",
       "units": "Amazon 'bought in past month' floors summed over search pages 1-5, US ZIP 10001", "meta": "Meta Ad Library US active ads, exact phrase"},
       "controls": {c: {"dates": dates(len(P[c])), "values": P[c]} for c in CONTROLS}, "categories": {}}
for f in sorted((H / "digest").glob("*.json")):
    d = json.load(open(f, encoding="utf-8")); pid = d["pid"]; a = d["amazon_us"]; m = d["meta_category"]
    t = TERM.get(pid)
    out["categories"][pid] = {
        "trend": {"term": t, "dates": dates(len(P[t])), "values": P[t]} if t in P else None,
        "shelf_by_kind": a["units_by_kind"], "shelf_by_brand_age": a["units_by_brand_age"],
        "meta_ages": {k: m[k] for k in ("active", "aged30", "aged90", "aged180")},
        "brand_pages": {k: {kk: sum((p.get(kk) or 0) for p in v["own"].values()) for kk in ("active", "aged30", "aged90", "aged180")} | {"own_domain_share": f"{v['own_domain']}/{v['phrase_sample']}"} for k, v in d["meta_brand_pages"].items()},
        "revenue_floor_top": REV.get(pid, {}).get("top"), "top_brands": [{"brand": b["best"]["amazon_brand"] or b["key"], "units": b["units"], "months": b["entry_months"], "status": b["status"], "price": b["best"]["price"], "img": b["best"]["img"]} for b in a["top_brands"][:8]],
        "creatives": [{"domain": c["domain"], "oldest": c["oldest"]} for c in d["creatives"]]}
(H / "chart_data.json").write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
print("categories", len(out["categories"]), "size KB", round((H / "chart_data.json").stat().st_size / 1024))
