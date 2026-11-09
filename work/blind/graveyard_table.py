"""v2 table: indie (new, not older-brand) share of the Amazon shelf per category. Frozen 2026-11-07.
EST = older brands that entered a category recently; they are not newcomers (cohort site/domain check + general knowledge)."""
import json, sys
import graveyard_stats2 as g
EST = {"drteal","plusone","imatchme","pacifica","purador","vitamatic","makari","mainbasics","blissal","medicube","abib","cetaphil",
       "vedix","drmelaxin","luminess","bissell","momcozy","kitsch","strivectin","veken","loreal","neutrogena","aveeno","palmer","osea",
       # added 2026-11-08 for the manual categories: long-established brands with recent ASINs
       "revitalash","olaplex","dralthea"}
CATS = ("color_foundation tallow_balm neck_cream rosemary_oil body_oil compression_socks dog_fountain turmeric_soap scent_diffuser "
        "persimmon_soap shower_filter pore_patch hair_removal_cream exfoliating_towel magnesium_spray chin_wrap whitening_powder").split()
CATS_NEW = ["lash_serum", "hair_serum", "prewash_oil"]  # US-ZIP manual scan only (2026-11-08)
def row(pid, src="graveyard"):
    L = {a: x for a, x in json.load(open(f"{src}/{pid}.json", encoding="utf-8"))["listings"].items() if g.on_target(pid, x["title"])}
    ent = {}
    for a, x in L.items():
        k = g.norm(x["brand"]) or g.title_brand(x["title"]) or "solo:" + a; x["_k"] = k; x["_age"] = g.age_m(a, x); ent[k] = max(ent.get(k, 0), x["_age"])
    U = sum(x["b"] for x in L.values()) or 1
    new = [x for x in L.values() if ent[x["_k"]] < 24 and x["_k"] not in EST]
    bu = {}
    for x in L.values(): bu[x["_k"]] = bu.get(x["_k"], 0) + x["b"]
    coh = [x for x in L.values() if 6 <= x["_age"] < 24 and ent[x["_k"]] < 24 and x["_k"] not in EST]
    return dict(pid=pid, units=U, top3=round(sum(sorted(bu.values(), reverse=True)[:3]) / U, 2),
                indie=round(sum(x["b"] for x in new) / U, 2), indie_units=sum(x["b"] for x in new),
                brand_units=sum(x["b"] for x in new if not x["_k"].startswith("solo:")),
                generic_units=sum(x["b"] for x in new if x["_k"].startswith("solo:")),
                win_brand=len({x["_k"] for x in new if x["b"] >= 1000 and not x["_k"].startswith("solo:")}),
                win_generic=len({x["_k"] for x in new if x["b"] >= 1000 and x["_k"].startswith("solo:")}),
                coh=len(coh), coh_1k=sum(x["b"] >= 1000 for x in coh))
if __name__ == "__main__":
    rows = sorted((row(p) for p in CATS), key=lambda r: -r["brand_units"])
    print(f"{'category':19}{'units':>9}{'top3':>6}{'newBrand_u':>11}{'newGeneric_u':>13}{'winB':>5}{'winG':>5}")
    for r in rows: print(f"{r['pid']:19}{r['units']:>9,}{r['top3']:>6}{r['brand_units']:>11,}{r['generic_units']:>13,}{r['win_brand']:>5}{r['win_generic']:>5}")
    json.dump(rows, open("graveyard/table_v2.1.json", "w", encoding="utf-8"), indent=1)
