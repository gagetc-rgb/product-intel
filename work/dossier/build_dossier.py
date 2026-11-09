"""Assemble every measured fact per category into one file: dossier_data.json (+ gap report). 2026-11-08, method v2.0.
Reads only existing outputs; computes nothing new except per-brand rollups of graveyard data.
Run: python build_dossier.py   (from work/dossier)
"""
import json, sys, pathlib, collections
B = pathlib.Path(__file__).resolve().parents[1] / "blind"
sys.path.insert(0, str(B))
import os; os.chdir(B)
import graveyard_stats2 as g
from graveyard_table import EST, row
from products import P

CATS = ["color_foundation", "body_oil", "scent_diffuser", "tallow_balm", "persimmon_soap", "shower_filter", "neck_cream",
        "rosemary_oil", "turmeric_soap", "dog_fountain", "chin_wrap", "pore_patch", "exfoliating_towel", "magnesium_spray",
        "hair_removal_cream", "compression_socks", "whitening_powder", "lash_serum", "hair_serum", "prewash_oil"]
STATUS = {  # from FINAL_V2.md (verdict 2026-11-07)
    "color_foundation": ("top5", 1), "body_oil": ("top5", 2), "scent_diffuser": ("top5", 3), "tallow_balm": ("top5", 4),
    "persimmon_soap": ("top5", 5), "shower_filter": ("reserve", 6), "neck_cream": ("not_ranked_data_issue", 7),
    "rosemary_oil": ("dropped_falling_trend", 8), "turmeric_soap": ("dropped_falling_trend", 9)}
for i, c in enumerate(CATS[9:17], 10): STATUS[c] = ("weak_amazon_meta_unchecked", i)
for i, c in enumerate(CATS[17:], 18): STATUS[c] = ("not_measured", i)

PROD = {p[0]: p for p in P}
SL = {x["id"]: x for x in json.load(open("shortlist.json", encoding="utf-8"))}
TR = json.load(open("trends_v2.json", encoding="utf-8"))["categories"]
MB = json.load(open("meta_brands.json", encoding="utf-8"))
LR = json.load(open(B.parent / "ads" / "longrunning.json", encoding="utf-8"))
# phase B additions (2026-11-08)
MP = json.load(open("meta_pages.json", encoding="utf-8"))
TS = json.load(open("trends_series_summary.json", encoding="utf-8"))
LR2 = json.load(open(B.parent / "ads" / "longrunning_v2.json", encoding="utf-8"))
import statistics, re as _re
def amazon_us(pid):
    f = B / "graveyard_us" / f"{pid}.json"
    if not f.exists(): return None
    L = {a: x for a, x in json.load(open(f, encoding="utf-8"))["listings"].items() if g.on_target(pid, x["title"])}
    pr = [float(_re.sub(r"[^\d.]", "", x["price"])) for x in L.values() if x.get("price")]
    top = sorted(L.items(), key=lambda kv: -kv[1]["b"])[:12]
    return {"row": row(pid, "graveyard_us"), "zip": "10001", "price_usd_median": round(statistics.median(pr), 2) if pr else None,
            "price_usd_p25_p75": [round(x, 2) for x in statistics.quantiles(pr, n=4)[::2]] if len(pr) > 3 else None,
            "top_listings": [{"asin": a, "title": x["title"], "units_floor": x["b"], "price": x["price"], "stars": x["stars"], "img": x["img"]} for a, x in top]}

def amazon(pid):
    f = B / "graveyard" / f"{pid}.json"
    if not f.exists() or not json.load(open(f, encoding="utf-8"))["listings"]: return None
    L = {a: x for a, x in json.load(open(f, encoding="utf-8"))["listings"].items() if g.on_target(pid, x["title"])}
    br = {}
    for a, x in L.items():
        k = g.norm(x["brand"]) or g.title_brand(x["title"]) or "solo:" + a
        age = g.age_m(a, x)
        b = br.setdefault(k, {"units": 0, "entry_months": 0, "listings": 0, "top": None})
        b["units"] += x["b"]; b["entry_months"] = max(b["entry_months"], round(age, 1)); b["listings"] += 1
        if not b["top"] or x["b"] > b["top"]["units"]: b["top"] = {"asin": a, "title": x["title"], "units": x["b"], "reviews": x["r"], "age_months": round(age, 1)}
    U = sum(b["units"] for b in br.values()) or 1
    def kind(k, b):
        if k in EST: return "older_brand_new_here"
        if k.startswith("solo:"): return "generic_new" if b["entry_months"] < 24 else "generic_old"
        return "new_brand" if b["entry_months"] < 24 else "old_brand"
    cohort = collections.Counter()
    for k, b in br.items():
        m = b["entry_months"]; band = "0-6" if m < 6 else "6-12" if m < 12 else "12-24" if m < 24 else "24+"
        cohort[band] += b["units"]
    top = sorted(br.items(), key=lambda t: -t[1]["units"])[:12]
    return {"query": json.load(open(f, encoding="utf-8"))["q"], "listings_on_target": len(L), **row(pid),
            "units_by_brand_entry": {k: cohort[k] for k in ("0-6", "6-12", "12-24", "24+")},
            "units_by_kind": dict(collections.Counter({kind(k, b): 0 for k, b in br.items()}) + collections.Counter(
                {kk: sum(b["units"] for k, b in br.items() if kind(k, b) == kk) for kk in {kind(k, b) for k, b in br.items()}})),
            "top_brands": [{"brand": k, "kind": kind(k, b), "units": b["units"], "share": round(b["units"] / U, 3), **{x: b[x] for x in ("entry_months", "listings")}, "best_listing": b["top"]} for k, b in top]}

def meta_cat(pid):
    f = B / "meta_ages" / f"{pid}.json"
    if not f.exists(): return None
    import meta_stats as ms
    s = ms.summary(pid)
    raw = json.load(open(f, encoding="utf-8"))
    return {k: s[k] for k in ("phrase", "active", "aged90", "aged180", "p90", "p180", "sample", "stores", "stores90")} | {"top_stores": s["top"], "aged30": raw.get("aged30"), "date": raw.get("date")}

out, gaps = {}, {}
for pid in CATS:
    p, s = PROD.get(pid), SL.get(pid, {})
    d = {"id": pid, "name": p[2] if p else s.get("name"), "status": STATUS[pid][0], "order": STATUS[pid][1],
         "compliance_flag": s.get("flag") or "", "price_usd_amazon_median": s.get("price"),
         "amazon": amazon(pid), "meta_category": meta_cat(pid),
         "meta_brands": {k: v for k, v in MB.items() if v["cat"] == pid},
         "trend": TR.get(pid), "trend_pulls": TS.get(pid),
         "amazon_us": amazon_us(pid),
         "meta_pages": {k: v for k, v in MP.items() if v["cat"] == pid},
         "creatives_v2": [{k: b[k] for k in ("domain", "total", "loaded", "productTitle", "productUrl", "photos")} | {"ads": b["ads"]} for b in LR2["brands"] if b["id"] == pid],
         "tiktok_top_item_sold_k": s.get("tt_k"), "repeat_purchase": s.get("repeat"),
         "creatives_longrunning": [b["domain"] for b in LR["brands"] if b.get("id") in (pid, pid.split("_")[0])],
         "photos": None, "reviews_monthly": None, "traffic": None}
    out[pid] = d
    gaps[pid] = [k for k, v in [("amazon", d["amazon"]), ("meta_category", d["meta_category"]), ("meta_brands", d["meta_brands"]),
                                 ("trend", d["trend"] or d["trend_pulls"]), ("price", d["price_usd_amazon_median"]), ("tiktok", d["tiktok_top_item_sold_k"]),
                                 ("photos", None), ("reviews_monthly", None), ("creatives", d["creatives_longrunning"] or d["creatives_v2"]), ("amazon_us", d["amazon_us"])] if not v]
here = pathlib.Path(__file__).parent
(here / "dossier_data.json").write_text(json.dumps({"built": "2026-11-08", "method": "v2.1 (/RUNBOOK.md); amazon = Indonesia-delivery scan (v2.1 definitions), amazon_us = US ZIP scan", "categories": out}, ensure_ascii=False, indent=1), encoding="utf-8")
(here / "gaps.json").write_text(json.dumps(gaps, indent=1), encoding="utf-8")
for pid in CATS: print(f"{STATUS[pid][1]:>2} {pid:19} {STATUS[pid][0]:28} missing: {', '.join(gaps[pid])}")
