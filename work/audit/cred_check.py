"""Credibility check of the channel's revenue claims (2026-11-09). Built to be beyond dispute:
only claims quoted from the transcript with an explicit period ("a month"), and only benchmarks published by others.
Test: revenue per visit the claim implies = claimed monthly revenue / monthly visits, compared with Littledata's
Shopify benchmark of revenue per session (438 stores, Oct 2026: median $1.98, top 10% $6.30). No assumptions of ours
about conversion, order value or review rates are used.
Dropped on purpose: Everstride ($2-3.9M "in sales", no period said in the video), Luhxe/Menvault (claims not found
in the transcripts), review-based bands (the 3-10% review rate has no published source we could cite)."""
import json, pathlib
OUT = pathlib.Path(__file__).parent / "cred_check.json"
BENCH = {"median": 1.98, "top10": 6.30, "src": "https://littledata.io/average-website-performance",
         "beauty_cr_max": 5.38, "beauty_src": "https://marketing.dynamicyield.com/benchmarks/conversion-rate/"}
CASES = [
 {"store": "Earthly Derm", "pid": "turmeric_soap", "video": "zRMForJwsy8",
  "quote": "Just look at the revenue numbers 7 to $14 million a month ... close to a million monthly visitors or 900,000",
  "claim": (7e6, 14e6), "visits": (900e3, 913e3),
  "visits_src": "author's own figure (~900K); SimilarWeb Sep 2026: 913K (work/market_system.md)", "tier": "◆"},
 {"store": "Skult", "pid": "chin_wrap", "video": "dZRoQlQF9WQ",
  "quote": "with a 2,000 active ads number we're looking at $8.2 million every single month ... anywhere between 4 to 7 million",
  "claim": (4e6, 8.2e6), "visits": (16e3, 27e3),
  "visits_src": "SimilarWeb Jun-Sep 2026 (work/market_system.md); weak for sites under ~50K visits, so x10 slack is tested", "tier": "◈"},
]
# v2 (2026-11-10): the site no longer leans on the Littledata benchmark (438 stores, not shown to be representative) and
# reads visits as a floor: traffic estimators miss much of the Facebook/Instagram in-app browser traffic that ad-driven
# stores live on. What is left is arithmetic on the author's own numbers: orders implied = claim / average order,
# buyers per 100 visitors, and (traffic-free) orders per review. AOV from work/market_system.py (store prices) ◈.
EXTRA = {
 "Earthly Derm": {"aov": 45, "reviews_mo": (853, 957), "reviews_src": "Loox, main bar only, Sep-Oct 2026 (work/reviews/RESULTS.md)"},
 "Skult": {"aov": 50, "us_share": 0, "amazon_mo": 1000, "amazon_src": "Amazon badge 1K+ (work/audit/brand_age.json)",
           "basis": "derived by the author from '2,000 active ads'"},
}
res = []
for c in CASES:
    c = dict(c, **EXTRA[c["store"]])
    orders = (c["claim"][0] / c["aov"], c["claim"][1] / c["aov"])
    c["orders"] = (round(orders[0]), round(orders[1]))
    c["buyers_per_100"] = (round(orders[0] / c["visits"][1] * 100), round(orders[1] / c["visits"][0] * 100))
    if "reviews_mo" in c:
        c["orders_per_review"] = (round(orders[0] / c["reviews_mo"][1]), round(orders[1] / c["reviews_mo"][0]))
    lo = c["claim"][0] / c["visits"][1]; hi = c["claim"][1] / c["visits"][0]
    r = dict(c, rpv=(round(lo, 2), round(hi, 2)), x_median=(round(lo / BENCH["median"], 1), round(hi / BENCH["median"], 1)),
             x_top10=(round(lo / BENCH["top10"], 1), round(hi / BENCH["top10"], 1)))
    if c["store"] == "Skult":  # even if SimilarWeb undercounts traffic tenfold
        r["rpv_if_10x_traffic"] = (round(lo / 10, 2), round(hi / 10, 2))
    res.append(r)
    print(c["store"], "orders", c["orders"], "buyers/100", c["buyers_per_100"], "orders/review", c.get("orders_per_review"))
    print(f"{c['store']:13} claim ${c['claim'][0]/1e6:.1f}-{c['claim'][1]/1e6:.1f}M / visits {c['visits'][0]/1e3:.0f}-{c['visits'][1]/1e3:.0f}K "
          f"-> ${r['rpv'][0]}-{r['rpv'][1]} per visit = x{r['x_median'][0]}-{r['x_median'][1]} median, x{r['x_top10'][0]}-{r['x_top10'][1]} top-10%"
          + (f" | if traffic x10: ${r['rpv_if_10x_traffic'][0]}-{r['rpv_if_10x_traffic'][1]}" if "rpv_if_10x_traffic" in r else ""))
json.dump({"bench": BENCH, "cases": res}, open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
