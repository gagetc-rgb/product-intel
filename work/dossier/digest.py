"""Per-category fact digest for writing the texts (2026-11-08). Every number printed here comes from a file;
the texts may only use numbers that appear in this digest (or in verdict_v21.json).
Amazon = US-ZIP scan (graveyard_us). Output: digest/<pid>.json and a compact printout."""
import json, sys, pathlib, collections, statistics, re
H = pathlib.Path(__file__).parent; B = H.parent / "blind"
sys.path.insert(0, str(B)); import os; os.chdir(B)
import graveyard_stats2 as g
from graveyard_table import EST
D = json.load(open(H / "dossier_data.json", encoding="utf-8"))["categories"]
V = {r["pid"]: r for r in json.load(open(H / "verdict_v21.json", encoding="utf-8"))}
S = {r["pid"]: r for r in json.load(open("meta_ages/summary.json"))}
BR = json.load(open("amazon_manual/brands_us.json", encoding="utf-8"))
OUT = H / "digest"; OUT.mkdir(exist_ok=True)

def amazon(pid):
    L = {a: x for a, x in json.load(open(f"graveyard_us/{pid}.json", encoding="utf-8"))["listings"].items() if g.on_target(pid, x["title"])}
    ent = {}
    for a, x in L.items():
        k = g.norm(x["brand"]) or g.title_brand(x["title"]) or "solo:" + a
        x["_k"] = k; x["_age"] = g.age_m(a, x); ent[k] = max(ent.get(k, 0), x["_age"])
    U = sum(x["b"] for x in L.values()) or 1
    bands = collections.Counter()
    for x in L.values():
        a = ent[x["_k"]]; bands["0-6" if a < 6 else "6-12" if a < 12 else "12-24" if a < 24 else "24+"] += x["b"]
    kinds = collections.Counter()
    for x in L.values():
        k = x["_k"]; new = ent[k] < 24
        kinds["generic_new" if k.startswith("solo:") and new else "generic_old" if k.startswith("solo:") else
              "older_brand_new_here" if k in EST else "new_brand" if new else "old_brand"] += x["b"]
    br = collections.defaultdict(lambda: {"units": 0, "listings": 0, "best": None})
    for a, x in L.items():
        if x["_k"].startswith("solo:"): continue
        r = br[x["_k"]]; r["units"] += x["b"]; r["listings"] += 1
        if not r["best"] or x["b"] > r["best"]["units"]:
            r["best"] = {"asin": a, "title": x["title"][:110], "units": x["b"], "price": x.get("price"), "stars": x.get("stars"), "img": x.get("img"),
                         "amazon_brand": BR.get(a, {}).get("brand")}
        r["entry_months"] = round(ent[x["_k"]]); r["status"] = "older brand, new here" if x["_k"] in EST else ("NEW" if ent[x["_k"]] < 24 else "old")
    top = sorted(br.items(), key=lambda kv: -kv[1]["units"])[:10]
    gen_top = sorted(((x["b"], a, x["title"][:80], x.get("price"), BR.get(a, {}).get("brand")) for a, x in L.items() if x["_k"].startswith("solo:")), reverse=True)[:4]
    return {"listings_on_target": len(L), "shelf_units": U, "units_by_brand_age": dict(bands),
            "units_by_kind": dict(kinds), "top_brands": [{"key": k} | v for k, v in top], "top_generics": gen_top,
            "winners_1k": sum(1 for x in L.values() if x["b"] >= 1000)}

for pid, d in D.items():
    m = d["meta_category"] or {}; t = d.get("trend_pulls") or {}
    cre = []
    for c in d.get("creatives_v2") or []:
        old = sorted((a for a in c["ads"] if a.get("days")), key=lambda a: -a["days"])[:4]
        cre.append({"domain": c["domain"], "ads_180d_total_meta": c["total"], "loaded": c["loaded"], "product": c["productTitle"],
                    "oldest": [{"days": a["days"], "page": a["page"], "headline": a["headline"][:90], "body": a["body"][:160], "img": a["imgLocal"]} for a in old]})
    out = {"pid": pid, "name": d["name"], "verdict_row": V[pid], "amazon_us": amazon(pid),
           "price_us": {k: (d.get("amazon_us") or {}).get(k) for k in ("price_usd_median", "price_usd_p25_p75")},
           "meta_category": {k: m.get(k) for k in ("phrase", "active", "aged30", "aged90", "aged180", "date")},
           "meta_stores_top": S.get(pid, {}).get("top", [])[:8],
           "meta_brand_pages": {k: {"own": v["own_pages"], "phrase_sample": v["phrase_sample"], "own_domain": v["phrase_sample_own_domain"]} for k, v in (d.get("meta_pages") or {}).items()},
           "meta_brand_phrase_v20": {k: {kk: v[kk] for kk in ("active", "aged90", "aged180")} for k, v in (d.get("meta_brands") or {}).items()},
           "trend": {"term": t.get("term"), "rel_yoy": t.get("rel_yoy_mean"), "yearly_means_v20": (d.get("trend") or {}).get("yearly_means"),
                     "zero_share_2y": (list(t.get("pulls", {}).values()) or [{}])[-1].get("zero_share_2y")},
           "tiktok_top_item_sold_k": d["tiktok_top_item_sold_k"], "creatives": cre}
    (OUT / f"{pid}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("digest written:", len(D))
