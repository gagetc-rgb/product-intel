---
id: tallow_balm
title: Beef tallow balm
status: top5
rank: 4
verdict: "The most newcomer wins of any category: nine young brands sell 1,000+ a month and many small shops keep ads alive for a year. But search growth has stopped."
best_channel: both
trend_label: flat
trend_x: 1.05
price_median_usd: 16.95
price_p25_p75_usd: [9.99, 22.99]
shelf_units_mo: 122850
new_brand_units_mo: 45550
new_brand_winners: 9
generic_units_mo: 29400
meta_active: 2500
meta_aged30: 500
meta_aged90: 220
meta_aged180: 52
compliance_flag: ""
data: digest/tallow_balm.json
charts:
  - {id: trend, type: line, source: "trends_pulls/pull1_2026-11-08.txt: 'tallow balm'", note: "4 rising years, then flat"}
  - {id: shelf_by_brand_age, type: stacked_bar, source: "digest.amazon_us.units_by_brand_age"}
  - {id: shelf_by_kind, type: donut, source: "digest.amazon_us.units_by_kind"}
  - {id: meta_brand_ads, type: table, source: "digest.meta_brand_pages"}
  - {id: revenue_floor, type: bar, source: "revenue_floor.json tallow_balm"}
photos: "digest.amazon_us.top_brands[*].best.img; Ancestral / Bare Ritual creatives: digest.creatives"
---

# Beef tallow balm

**Verdict: #4 of 20.** If the question is "do new brands win here?", tallow is the strongest answer of all 20 categories: **nine brands under 24 months** sell 1,000+ a month on Amazon, and a dozen small shops keep Meta ads running for 300-700 days. What holds it back is demand: after four years of steep growth, searches are flat. Entering now means fighting for share in a market that has stopped expanding. ◈

## 1. The product and the buyer

A face and body balm made from rendered grass-fed beef fat, often whipped with honey or essential oils. It sells on "ancestral", "clean", "one ingredient" skincare: Ancestral Cosmetics' oldest ad opens with "I made a face cream from BEEF FAT". Buyers are people who distrust conventional skincare, men included (Forge Skin sells "for Men"). ◆ (listings, ads)

Price: $16.95 median on Amazon (half between $9.99 and $22.99); Terra Lotus $19.99, Hearth & Homestead $29.97, Forge $39.95. ◆

## 2. How big, and where it is going

**Size.** At least **122,850 purchases a month** on five Amazon pages, about **$2.8 million a month**. ◆ count, ◈ money.

**Trend.** ×1.05 versus a year ago (control-corrected): **flat**. The yearly index shows why it looked so good before: 0.9 → 3.3 → 8.3 → 21.2 → 35.3 — four years of steep growth that has now levelled off. ◆ (one pull of three)

## 3. Who holds the market

| Who | Units/mo | Share |
|---|---|---|
| Brands under 24 months on Amazon | 45,550 | 37% |
| Old brands (Hearth & Homestead, Forge, Santa Cruz Paleo…) | 41,700 | 34% |
| Unbranded sellers, new | 29,400 | 24% |
| Unbranded, old | 6,200 | 5% |

Most units go to sellers **12-24 months old** (55,350/mo): the wave of 2025 entrants is now the core of the shelf. ◆

| Brand | Units/mo | Months on Amazon | Price | Revenue floor/mo |
|---|---|---|---|---|
| Terra Lotus | 22,000 | ~18 | $19.99 | ~$0.50M |
| Hearth & Homestead | 18,000 | ~51 | $29.97 | ~$0.57M |
| Forge Skin | 10,800 | ~31 | $39.95 | ~$0.42M |
| RICHGRAND | 8,600 | ~22 | $21.99 | ~$0.20M |
| ELBBUB | 3,000 | ~21 | $11.19 | — |

◆ units/price, ◈ ages and revenue.

## 4. Can a newcomer get in

Yes: 9 young brands above 1,000/mo, plus 8 unbranded listings. The shelf is fragmented: the top three brands hold 41% of units (the lowest concentration among our top 5). Room for one more brand, but the newest cohort (under 6 months) takes only 2,650 units/mo: the door was wider in 2025 than it is now. ◆ counts, ◈ reading.

## 5. What happens in ads

Meta, US, active, exact phrase "tallow balm": ◆

| Active | 30+ days | 90+ days | 180+ days |
|---|---|---|---|
| 2,500 | 500 (20%) | 220 (9%) | 52 (2%) |

16 of 19 shops in the sample have an ad 90+ days old. The oldest: Hibi Youth Skincare (703 days), ancestralcosmetics.com (348), byminus.com (310), bare-ritual.com (301). ◆

On each brand's own Page: ◆

| Brand | Active | 90+ days | 180+ days | Reading |
|---|---|---|---|---|
| byminus | 150 | 38 | 17 | evergreen |
| Ancestral Cosmetics | 130 | 77 | 55 | most evergreen: 42% of its ads live 180+ days |
| Terra Lotus | 130 | 0 | 0 | Amazon leader, only now testing Meta |
| Bare Ritual | 77 | 43 | 21 | evergreen |
| Forge | 74 | 4 | 0 | rotates fast |

Two different winning models are visible: Terra Lotus wins on Amazon without Meta; Ancestral, Bare Ritual and byminus win on their own stores with small but very long-lived ad sets. ◈

## 6. Do the winners keep growing

Not measured (review curves pending). With demand flat, this is the key open question for tallow. ◈

## 7. What the winners say

Ancestral: "I made a face cream from BEEF FAT" (349 days), "Handmade tallow products" (341 days). Bare Ritual: "Someone asked if I got BOTOX. I didn't." (263 days). Founder story and shock-value honesty, not clinical claims. ◆

## 8. Risks and open questions

- **Growth has stopped** (×1.05) after a 4-year boom; late entrants fight for share. ◆/◈
- **Low price floor**: unbranded tallow at $9.99-19.99. ◆
- **Perishability and smell** (animal fat): shelf life and complaints. ◈
- **Forge is not a new brand** (~31 months on Amazon); corrected in v2.0 errata. ◆

## 9. Verdict and what would change it

**#4.** Not falling (×1.05), most new-brand winners of all categories, many shops with 90+ day ads. It would drop if search fell below ×0.8. It would rise if pulls 2-3 or the next months show growth returning.

## 10. Methods and sources

- Amazon: `beef tallow balm`, ZIP 10001 → `work/blind/graveyard_us/tallow_balm.json`.
- Meta: [Ad Library, exact phrase "tallow balm"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=%22tallow%20balm%22&search_type=keyword_exact_phrase&media_type=all).
- Trends: [Google Trends, US, 5 years, "tallow balm"](https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=tallow%20balm).
