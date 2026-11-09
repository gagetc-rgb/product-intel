"""Shortlist by fixed gates (v3, after the devil's-advocate pass of 2026-11-07).

Lessons from the AD pass that shaped the rules:
- A low TikTok reading from one keyword page is often wrong (turmeric soap 0.9K -> 819K, exfoliating towel 0.17K -> 79.5K
  on a second page). So a weak channel = 'unknown', never 'no demand'. Demand is proven by the STRONGEST sales channel.
- Amazon top-20 sums move +-20-40% between two runs hours apart; log buckets absorb that.
- Meta exact-phrase counts are noisy (salons, clinics, dealers) and undercount DTC brands whose copy avoids the phrase
  (Earthly Derm: 44 aged ads by domain vs 12 by phrase). Meta is only a confirming channel.

Gates (all must pass):
  G1 DEMAND  strongest sales channel >= 4: Amazon >= 30K units/month on top-20, or TikTok top product >= 50K sold
  G2 ROOM    Amazon: >= 5 different on-target listings each selling 1K+/month (newcomers can sell, not one brand)
  G3 VALUE   repeat purchase (consumable/refill) or median Amazon price >= $40
  G4 LEGAL   not banned / not a false core claim (compliance-route products pass with a flag)
TRUST = channels scoring >= 3 (Amazon, TikTok, Meta if not noisy): 3 high, 2 medium, 1 low.
"""
import csv, json, re, statistics, pathlib
H = pathlib.Path(__file__).parent
rows = list(csv.DictReader(open(H / "blind_rank.csv", encoding="utf-8")))
amz = json.loads((H / "amazon.json").read_text(encoding="utf-8"))
from amz_filter import MUST, NOT

REPEAT = {  # judgement, stated openly: consumable or refill bought again within ~12 months
 "multibalm","lash_serum","color_foundation","tallow_balm","compression_socks","hair_serum","neck_cream","rosemary_oil",
 "hair_removal_cream","magnesium_spray","shower_filter","dog_fountain","scent_diffuser","retinol_cream","collagen_mask",
 "pore_patch","whitening_powder","persimmon_soap","turmeric_soap","rodent_pouch","prewash_oil","mouth_tape","pet_odor",
 "body_oil","body_mousse","exfoliating_towel","hair_inhibitor","ceramide_wash","wrinkle_primer","silvervine","pet_hair_roller",
 "work_insoles","toothbrush","microneedle_patch","chin_wrap","heat_patch","flea_spray","puppy_pad","s_",
}
def repeat(pid):
    return pid in REPEAT or pid.startswith("s_")

def price(pid):
    it = amz.get(pid, {}).get("items") or []
    ps = []
    for i in it:
        if not re.search(MUST[pid], i["title"], re.I) or (pid in NOT and re.search(NOT[pid], i["title"], re.I)):
            continue
        m = re.match(r"\$([\d,.]+)", i.get("price", ""))
        if m:
            ps.append(float(m.group(1).replace(",", "")))
    return round(statistics.median(ps), 2) if ps else None

out = []
for r in rows:
    sA = int(r["sA"]) if r["sA"] else 0
    sT = int(r["sT"]) if r["sT"] else 0
    sM = int(r["sM"]) if r["sM"] else None
    n1k = int(r["amz_1k"] or 0)
    p = price(r["id"])
    g1 = max(sA, sT) >= 4
    g2 = n1k >= 5
    g3 = repeat(r["id"]) or (p or 0) >= 40
    g4 = r["flag"] not in ("BANNED", "FALSE_CLAIM")
    trust = (sA >= 3) + (sT >= 3) + ((sM or 0) >= 3)
    out.append(dict(r, price=p, repeat=repeat(r["id"]), G1=g1, G2=g2, G3=g3, G4=g4, PASS=g1 and g2 and g3 and g4,
                    TRUST=trust, strength=max(sA, sT)))
out.sort(key=lambda x: (-x["PASS"], -x["TRUST"], -x["strength"], -float(x["POP"])))
json.dump(out, open(H / "shortlist.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for b in ("MAIN", "SUPP"):
    print("==", b)
    for x in [x for x in out if x["block"] == b and x["PASS"]]:
        print(f"T{x['TRUST']} S{x['strength']} A{x['amz_bought']:>7} 1k{x['amz_1k']:>3} TT{x['tt_k']:>7} M{x['meta_180']:>5} ${x['price']} rep={int(x['repeat'])} {x['flag'][:5]:5} {x['name'][:50]}")
print("== earlier picks")
for pid in ("turmeric_soap", "persimmon_soap", "compression_socks", "leakproof_boxers", "duffel", "tennis_bracelet"):
    x = next(x for x in out if x["id"] == pid)
    print(pid, "PASS" if x["PASS"] else "fail", {k: x[k] for k in ("G1", "G2", "G3", "G4", "TRUST", "price")})

# ---- v3.1: symmetric Meta rule + brand lock + tiers ----
# Leader-domain Meta counts (180+ day ads) measured earlier in work/market_system.md for corpus leaders.
DOMAIN_META = {"turmeric_soap": 44, "persimmon_soap": 53, "compression_socks": 190, "leakproof_boxers": 8, "duffel": 0,
               "rodent_pouch": 0, "led_mask": 0, "back_stretcher": 0, "compression_tank": 1, "exfoliating_towel": 1,
               "seat_cushion": 43, "silvervine": 130, "ski_sleeve": 60, "chin_wrap": 160, "tennis_bracelet": 26, "massager16": 22}
# Category leaders are big brands holding the top TikTok/Amazon spots (seen in the scan): a newcomer competes with them head-on.
BRAND_LOCK = {"multibalm": "medicube 1.2M + Dr.Melaxin 1.1M sold", "collagen_mask": "medicube 262K; 42% of Amazon top-20",
              "retinol_cream": "medicube / Anua / celimax", "ceramide_wash": "CeraVe / La Roche-Posay", "work_insoles": "Dr. Scholl's"}
M_CUTS = (1, 5, 15, 50, 150)
def mb(x): return sum(x >= c for c in M_CUTS)
for x in out:
    sA = int(x["sA"]) if x["sA"] else 0
    sT = int(x["sT"]) if x["sT"] else 0
    sM = int(x["sM"]) if x["sM"] not in ("", None) else 0
    if x["id"] in DOMAIN_META:
        sM = max(sM, mb(DOMAIN_META[x["id"]]))
    x["sM2"] = sM
    x["TRUST"] = (sA >= 3) + (sT >= 3) + (sM >= 3)
    x["TOTAL"] = sA + sT + sM
    x["lock"] = BRAND_LOCK.get(x["id"], "")
    if not x["PASS"]:
        x["tier"] = "OUT"
    elif x["lock"]:
        x["tier"] = "LOCKED"
    elif x["TRUST"] == 3 and x["flag"] == "":
        x["tier"] = "A"
    else:
        x["tier"] = "B"
out.sort(key=lambda x: ("A B LOCKED OUT".split().index(x["tier"]), -x["TOTAL"], -x["TRUST"]))
json.dump(out, open(H / "shortlist.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("\n==== v3.1 tiers")
for b in ("MAIN", "SUPP"):
    print("==", b)
    for x in out:
        if x["block"] == b and x["tier"] != "OUT":
            print(f"{x['tier']:6} T{x['TRUST']} tot{x['TOTAL']:>2} A{x['sA']} T{x['sT'] or '-'} M{x['sM2']} ${x['price']} {x['flag'][:5]:5} {x['name'][:50]} {x['lock']}")
