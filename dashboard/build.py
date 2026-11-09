"""Build product-intel-dashboard.html and long-running-ads.html.

Inputs: dashboard/template.html + data.json + work/reviews/curves.json (dashboard),
        dashboard/ads_template.html + work/ads/longrunning.json (ads page; refresh with work/ads/fetch_longrunning.py).
"""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent
proj = root.parent
data = json.loads((root / "data.json").read_text(encoding="utf-8"))
curves = json.loads((proj / "work" / "reviews" / "curves.json").read_text(encoding="utf-8"))
ads = json.loads((proj / "work" / "ads" / "longrunning.json").read_text(encoding="utf-8"))

# Official brand pages; anything else is a creator / persona page running the brand's ads.
BRAND_PAGES = {"turmeric": {"Earthly Derm"}, "socks": {"Everstride"}, "persimmon": {"Kaori"},
               "boxers": {"Shopmenvault"}, "duffel": {"Luhxe"}}
for b in ads["brands"]:
    for a in b["ads"]:
        a["brand"] = a["page"] in BRAND_PAGES.get(b["id"], set())
    b["ads"].sort(key=lambda a: -(a["days"] or 0))

# Short ad summary for the dashboard (photos + oldest creatives teaser).
by_id = {b["id"]: b for b in ads["brands"]}
for p in data["products"]:
    b = by_id.get(p["id"])
    if not b:
        continue
    p["photos"] = b["photos"]
    p["productUrl"] = b["productUrl"]
    p["adTeaser"] = {"minDays": b["minDays"], "total": b["total"], "loaded": b["loaded"],
                     "oldest": max(a["days"] for a in b["ads"]),
                     "top": [{"id": a["id"], "img": a["imgLocal"], "days": a["days"], "video": a["video"]}
                             for a in b["ads"][:6]]}

# Shortlist v3: category-level evidence from the blind pass (work/blind/shortlist.json + openness_raw.txt).
blind = proj / "work" / "blind"
sl = json.loads((blind / "shortlist.json").read_text(encoding="utf-8"))
openness = {}
for line in (blind / "openness_raw.txt").read_text(encoding="utf-8").splitlines()[1:]:
    f = line.split()
    if len(f) >= 9:  # id tier n units top3 new% newHit $med rep [TTk M180 adv]
        openness[f[0]] = {"top3": float(f[4]), "newShare": float(f[5]), "newHit": f[6]}
# Meta 180+ by the leader's landing domain where we measured it (phrase search undercounts DTC brands).
DOMAIN_META = {"turmeric_soap": 44, "persimmon_soap": 53, "compression_socks": 190, "chin_wrap": 160, "exfoliating_towel": 1}
def num(x):
    try: return float(x)
    except (TypeError, ValueError): return None
cat = {}
for x in sl:
    if x["tier"] not in ("A", "B"):
        continue
    m = max(num(x["meta_180"]) or 0, DOMAIN_META.get(x["id"], 0))
    cat[x["id"]] = {"id": x["id"], "name": x["name"], "block": x["block"], "tier": x["tier"], "flag": x["flag"],
                    "amz": num(x["amz_bought"]), "amz1k": int(x["amz_1k"] or 0), "tt": num(x["tt_k"]), "meta": m,
                    "price": x["price"], "trust": x["TRUST"], "total": x["TOTAL"], **openness.get(x["id"], {})}
data["tierA"] = [cat[x["id"]] for x in sl if x["tier"] == "A"]
data["cat"] = cat
for p in data["products"]:
    p["cat"] = cat.get(p.get("catId"))

tpl = (root / "template.html").read_text(encoding="utf-8")
out = tpl.replace("/*DATA*/null", json.dumps(data, ensure_ascii=False)).replace("/*CURVES*/null", json.dumps(curves))
(proj / "product-intel-dashboard.html").write_text(out, encoding="utf-8")

prods = [{"id": p["id"], "name": p["name"], "heroIdx": p.get("heroIdx", 0)} for p in data["products"]]
ads["brands"] = [b for b in ads["brands"] if b["id"] in {p["id"] for p in prods}]  # dropped products leave the ads page
atpl = (root / "ads_template.html").read_text(encoding="utf-8")
aout = atpl.replace("/*ADS*/null", json.dumps(ads, ensure_ascii=False)).replace("/*PRODUCTS*/null", json.dumps(prods, ensure_ascii=False))
(proj / "long-running-ads.html").write_text(aout, encoding="utf-8")
print("ok", len(out), len(aout))
