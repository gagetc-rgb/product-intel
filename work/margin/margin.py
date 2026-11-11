"""Unit economics on Amazon FBA for all 20 categories (2026-11-10): what one sale leaves before advertising.
Same model for every category; ranges come from the supplier price range only.

before_ads = price - referral fee - FBA fulfillment fee (+3.5% surcharge) - storage - returns - landed cost
landed     = supplier price x (1 + duty) + freight to the Amazon warehouse + prep/inbound

Inputs and where they come from:
- price: typical Amazon price = median of listings selling 1,000+ a month (amazon_prices.json, saved US scans) ◆
- referral and FBA fees: Amazon's own pages, 2027 non-peak card (amazon_fees.json, read 2026-11-10) ◆
- supplier price: Made-in-China.com search pages, 2026-11-10, typical FOB range for the format sold on Amazon ◈
  (Alibaba showed a bot check and was not used)
- duty: China = MFN + Section 301 list rate + 12.5% Section 301 forced-labor duty (since 2026-07-24); HTS lines are
  our reading, not a broker's ruling ◈. Soap 37.5% as in work/full_list_analysis.md.
- size tier, freight, prep, returns, storage months: our estimates ◈
Verdict on the middle of the range: 40%+ of price before ads = room for ads and profit; 25-40% = tight; under 25% =
ads will eat it (METRICS.md D5: under 20-25% net is a red flag).
Usage: python work/margin/margin.py -> work/margin/margin.json"""
import json, math, pathlib
H = pathlib.Path(__file__).parent
FEES = json.load(open(H / "amazon_fees.json", encoding="utf-8"))
PRICES = json.load(open(H / "amazon_prices.json", encoding="utf-8"))
CARD = "nonpeak_2027"; SURCH = FEES["surcharge"]; STORE_MONTH = (9 * 0.78 + 3 * 2.40) / 12; MONTHS = 2; PREP = 0.30

# pid: (format sold, units per listing note, supplier $ low-high per listing, duty, tier, weight step oz, freight $, cu ft,
#       returns share, referral class)
IN = {
 "dog_fountain":      ("поилка на 2–3 л со стальной чашей", (6.5, 12.0), 0.40, "large_standard", 48, 2.00, 0.24, 0.05, "pet"),
 "color_foundation":  ("флакон 30–40 мл в коробке",        (1.8, 3.0), 0.20, "large_standard", 4, 0.30, 0.02, 0.02, "beauty"),
 "lash_serum":        ("тюбик 3–6 мл в коробке",            (1.5, 2.8), 0.20, "large_standard", 4, 0.20, 0.01, 0.02, "beauty"),
 "tallow_balm":       ("баночка ~60 мл",                        (1.3, 2.5), 0.20, "large_standard", 8, 0.40, 0.02, 0.02, "beauty"),
 "shower_filter":     ("ручная лейка с фильтром",       (3.0, 6.5), 0.40, "large_standard", 20, 1.00, 0.07, 0.04, "home"),
 "hair_serum":        ("флакон или спрей 60–120 мл",          (1.5, 4.0), 0.249, "large_standard", 8, 0.40, 0.02, 0.02, "beauty"),
 "body_oil":          ("флакон 150–200 мл",               (1.0, 3.0), 0.20, "large_standard", 12, 0.60, 0.03, 0.02, "beauty"),
 "persimmon_soap":    ("2 бруска по ~100 г",             (1.3, 3.5), 0.375, "large_standard", 12, 0.50, 0.02, 0.02, "beauty"),
 "compression_socks": ("набор из 3–4 пар",                       (3.5, 7.0), 0.346, "large_standard", 12, 0.40, 0.04, 0.05, "clothing"),
 "pore_patch":        ("коробка на 10–20 полосок",             (0.5, 1.2), 0.20, "large_standard", 4, 0.15, 0.01, 0.02, "beauty"),
 "rosemary_oil":      ("флакон 60–180 мл",                   (1.0, 2.5), 0.249, "large_standard", 8, 0.40, 0.02, 0.02, "beauty"),
 "prewash_oil":       ("флакон 60–100 мл",                 (1.0, 2.5), 0.249, "large_standard", 8, 0.30, 0.02, 0.02, "beauty"),
 "whitening_powder":  ("баночка 30–60 г",                     (0.6, 1.5), 0.20, "large_standard", 4, 0.15, 0.01, 0.02, "beauty"),
 "turmeric_soap":     ("2 бруска по ~100 г",             (1.3, 3.3), 0.375, "large_standard", 12, 0.50, 0.02, 0.02, "beauty"),
 "hair_removal_cream":("тюбик 100–200 мл",                 (0.9, 1.7), 0.20, "large_standard", 12, 0.60, 0.02, 0.03, "beauty"),
 "scent_diffuser":    ("безводный диффузор с аккумулятором", (15.0, 45.0), 0.40, "large_standard", 28, 1.20, 0.13, 0.05, "home"),
 "neck_cream":        ("баночка 50 мл",                       (1.5, 2.8), 0.20, "large_standard", 8, 0.40, 0.02, 0.02, "beauty"),
 "chin_wrap":         ("5–10 масок V-line или бандаж",    (1.5, 4.0), 0.25, "large_standard", 4, 0.20, 0.02, 0.03, "beauty"),
 "exfoliating_towel": ("одно длинное нейлоновое полотенце",            (0.5, 1.0), 0.35, "large_standard", 8, 0.30, 0.03, 0.03, "beauty"),
 "magnesium_spray":   ("спрей 240–350 мл",            (1.2, 3.0), 0.25, "large_standard", 16, 0.70, 0.03, 0.02, "beauty"),
}

def band(p): return 0 if p < 10 else 1 if p <= 50 else 2
def fba(tier, step, p):
    t = FEES[tier][CARD]
    if step <= 48: return t[str(step)][band(p)] * (1 + SURCH)
    return (t["over48_base"][band(p)] + t["over48_per4oz"] * math.ceil((step - 48) / 4)) * (1 + SURCH)
def referral(cls, p):
    r = {"beauty": 0.08 if p <= 10 else 0.15, "pet": 0.15, "home": 0.15,
         "clothing": 0.05 if p <= 15 else 0.10 if p <= 20 else 0.17}[cls]
    return max(r * p, 0.30)
def verdict(pct): return "good" if pct >= 0.40 else "tight" if pct >= 0.25 else "bad"

out = {}
for pid, (fmt, (c_lo, c_hi), duty, tier, step, freight, cuft, ret, cls) in IN.items():
    p = PRICES[pid]["typical"]
    fees = {"referral": referral(cls, p), "fba": fba(tier, step, p), "storage": cuft * STORE_MONTH * MONTHS, "returns": ret * p}
    land = lambda c: c * (1 + duty) + freight + PREP
    left = lambda c: p - sum(fees.values()) - land(c)
    hi, lo = left(c_lo), left(c_hi)
    mid = (hi + lo) / 2
    out[pid] = {"format": fmt, "price": p, "price_low_q1": PRICES[pid]["q1"], "supplier": [c_lo, c_hi], "duty": duty,
                "fees": {k: round(v, 2) for k, v in fees.items()}, "amazon_take": round(fees["referral"] + fees["fba"], 2),
                "landed": [round(land(c_lo), 2), round(land(c_hi), 2)],
                "before_ads": [round(lo, 2), round(hi, 2)], "before_ads_pct": [round(lo / p, 2), round(hi / p, 2)],
                "verdict": verdict(mid / p),
                # the same sale at the cheap end of the shelf (lower quartile of 1,000+ sellers), mid supplier price
                "at_q1_price": round(PRICES[pid]["q1"] - referral(cls, PRICES[pid]["q1"]) - fba(tier, step, PRICES[pid]["q1"])
                                     - fees["storage"] - ret * PRICES[pid]["q1"] - land((c_lo + c_hi) / 2), 2)}
    o = out[pid]
    print(f"{pid:19} ${p:>6}  Amazon ${o['amazon_take']:>5}  landed ${o['landed'][0]}-{o['landed'][1]}  "
          f"left ${o['before_ads'][0]}..{o['before_ads'][1]} ({o['before_ads_pct'][0]:.0%}..{o['before_ads_pct'][1]:.0%}) "
          f"{o['verdict']:6} | at q1 ${PRICES[pid]['q1']}: ${o['at_q1_price']}")
json.dump({"model": __doc__.split("Usage")[0].strip(), "card": CARD, "cases": out}, open(H / "margin.json", "w", encoding="utf-8"),
          indent=1, ensure_ascii=False)
