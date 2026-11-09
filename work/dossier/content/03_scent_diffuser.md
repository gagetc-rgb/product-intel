---
id: scent_diffuser
title: Waterless scent diffuser
status: weak
rank: 16
verdict: "A premium-priced, growing product where the money is in the own-store brand: on Amazon half the units go to unbranded sellers, on Meta a few brands keep ads alive for years."
best_channel: own store + Meta; Amazon is a price war
trend_label: growing
trend_x: 2.02
price_median_usd: 64.49
price_p25_p75_usd: [39.99, 89.99]
shelf_units_mo: 58000
new_brand_units_mo: 21200
new_brand_winners: 4
generic_units_mo: 20400
meta_active: 690
meta_aged30: 210
meta_aged90: 110
meta_aged180: 18
compliance_flag: ""
data: digest/scent_diffuser.json
charts:
  - {id: trend, type: line, source: "trends_pulls/pull1_2026-11-08.txt: 'waterless diffuser'"}
  - {id: shelf_by_kind, type: donut, source: "digest.amazon_us.units_by_kind"}
  - {id: meta_brand_ads, type: table, source: "digest.meta_brand_pages"}
  - {id: revenue_floor, type: bar, source: "revenue_floor.json scent_diffuser"}
photos: "digest.amazon_us.top_brands[*].best.img; Scentify creatives: digest.creatives"
---

# Waterless scent diffuser

**Verdict: #3 of 20.** The most expensive product on our list ($64 median), with search interest doubling in a year. On Amazon it is split between a few brands and many unbranded sellers; on Meta a handful of home-fragrance brands keep the same ads running for months and years. The opportunity is a brand with its own store, not another Amazon listing. ◈

## 1. The product and the buyer

A plug-in or cordless device that turns fragrance oil into a dry cold-air mist, no water. Sold as "hotel scent at home": Hotel Collection, Aroma360 and Scentify all sell the device plus refill oils. The buyer is a homeowner who wants the house to smell like a hotel lobby, and keeps buying oils. ◆ product form (listings); ◈ the device-plus-refills model of Hotel Collection, Aroma360 and Scentify (their stores and ads)

Price: $64.49 median on Amazon, half between $39.99 and $89.99; AirScent's leading listing is $99.99. The refills make it a repeat purchase. ◆ price, ◈ repeat.

## 2. How big, and where it is going

**Size.** At least **58,000 purchases a month** on five Amazon pages, about **$4.1 million a month**, because of the high price. ◆ count, ◈ money.

**Trend.** Searches for "waterless diffuser" are **×2.0** versus a year ago (control-corrected); yearly index 0.8 → 2.4 → 5.6 → 9.1 → 34.5. Steady growth for four years, not a single spike. ◆ (one pull of three)

## 3. Who holds the market

| Who | Units/mo | Share |
|---|---|---|
| Brands under 24 months on Amazon | 21,200 | 37% |
| Unbranded sellers, new | 20,400 | 35% |
| Old brands (Airversa, VINEVIDA…) | 13,800 | 24% |
| Unbranded, old | 2,600 | 4% |

Leaders: Airversa (34 months, 11,400/mo, $39.99), **AirScent** (~23 months, 11,100/mo, $99.99, ~$1.1M/mo), ANZ/ScentBots (~13 months, 3,700/mo at $19.98), FEPPO (~9 months, 1,100/mo at $65.99). Unbranded sellers take ~$1.8M/mo together. ◆ units/price, ◈ ages and revenue.

## 4. Can a newcomer get in

On Amazon: four brands under 24 months sell 1,000+ a month, but the unbranded half (NoxLumina at $89.99 with 4,000/mo, many at $20-80) pushes prices down. A newcomer on Amazon competes on price. ◈

Off Amazon the picture is different (section 5): the brands that matter in this category are store brands that barely sell on Amazon. AirScent, the Amazon leader, runs only **4** Meta ads. ◆

## 5. What happens in ads

Meta, US, active, exact phrase "scent diffuser": ◆

| Active | 30+ days | 90+ days | 180+ days |
|---|---|---|---|
| 690 | 210 (30%) | 110 (16%) | 18 (3%) |

A small ad market by count, but with a high share of long-lived ads: when an ad works here, it keeps running. 11 of 13 shops in the sample have an ad 90+ days old; **scentifyhome.com's oldest live ad is 795 days old** (over two years). ◆

On each brand's own Page: ◆

| Brand | Active | 90+ days | 180+ days |
|---|---|---|---|
| Hotel Collection | 563 | 158 | 5 |
| Aroma360 | 370 | 77 | 0 |
| Scentify | 320 | 100 | 89 |
| Aura House | 212 | 22 | 3 |
| AirScent | 4 | 0 | 0 |

## 6. Do the winners keep growing

Not measured (review curves pending). ◈

## 7. What the winners say

Scentify's ads that have run for 796-899 days sell the device with a free scent ("Get a FREE Scent with Your V2 Diffuser"). Aura House's 201-day ad: "Best scent diffuser? · 30 days supply left." The offer is the device plus the first oil; the business is the refills. ◆ ads, ◈ business model.

## 8. Risks and open questions

- **Amazon price war**: unbranded devices at $20-90. ◆
- **Heavy, fragile, electronic**: returns and warranty cost more than for a cream. ◈
- **The brand wins on scent, not on hardware**: the oils are the product to develop. ◈
- **Note:** v2.0 counted AirScent as unbranded (titles start with "The"); fixed in v2.1, new-brand units rose from 8,300 to 19,400 (ID scan). ◆

## 9. Verdict and what would change it

**#3.** Growing (×2.0), new brands take 21,200 units/mo, shops keep ads alive for years. It would drop if search growth stopped (below ×0.8) or if the long-lived Meta advertisers disappeared in the 30-day re-check.

## 10. Methods and sources

- Amazon: `waterless scent diffuser`, ZIP 10001, pages 1-5 → `work/blind/graveyard_us/scent_diffuser.json`.
- Meta: [Ad Library, exact phrase "scent diffuser"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=%22scent%20diffuser%22&search_type=keyword_exact_phrase&media_type=all).
- Trends: [Google Trends, US, 5 years, "waterless diffuser"](https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=waterless%20diffuser).
