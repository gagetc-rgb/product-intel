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
res = []
for c in CASES:
    lo = c["claim"][0] / c["visits"][1]; hi = c["claim"][1] / c["visits"][0]
    r = dict(c, rpv=(round(lo, 2), round(hi, 2)), x_median=(round(lo / BENCH["median"], 1), round(hi / BENCH["median"], 1)),
             x_top10=(round(lo / BENCH["top10"], 1), round(hi / BENCH["top10"], 1)))
    if c["store"] == "Skult":  # even if SimilarWeb undercounts traffic tenfold
        r["rpv_if_10x_traffic"] = (round(lo / 10, 2), round(hi / 10, 2))
    res.append(r)
    print(f"{c['store']:13} claim ${c['claim'][0]/1e6:.1f}-{c['claim'][1]/1e6:.1f}M / visits {c['visits'][0]/1e3:.0f}-{c['visits'][1]/1e3:.0f}K "
          f"-> ${r['rpv'][0]}-{r['rpv'][1]} per visit = x{r['x_median'][0]}-{r['x_median'][1]} median, x{r['x_top10'][0]}-{r['x_top10'][1]} top-10%"
          + (f" | if traffic x10: ${r['rpv_if_10x_traffic'][0]}-{r['rpv_if_10x_traffic'][1]}" if "rpv_if_10x_traffic" in r else ""))
json.dump({"bench": BENCH, "cases": res}, open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
