---
id: persimmon_soap
title: Persimmon soap
status: reserve
rank: 8
verdict: "The fastest-growing search on the list and lively Meta testing, but a small, cheap market where one older brand holds a third and new brands so far take little."
best_channel: own store + Meta
trend_label: growing
trend_x: 4.59
price_median_usd: 12.99
price_p25_p75_usd: [9.99, 17.99]
shelf_units_mo: 69550
new_brand_units_mo: 7350
new_brand_winners: 3
generic_units_mo: 25450
meta_active: 2700
meta_aged30: 830
meta_aged90: 130
meta_aged180: 11
compliance_flag: ""
data: digest/persimmon_soap.json
charts:
  - {id: trend, type: line, source: "trends_pulls/pull1_2026-11-08.txt: 'persimmon soap'", note: "own peak in Oct 2026, separate from the spring artifact"}
  - {id: shelf_by_kind, type: donut, source: "digest.amazon_us.units_by_kind"}
  - {id: meta_ages, type: bar, source: "digest.meta_category"}
  - {id: revenue_floor, type: bar, source: "revenue_floor.json persimmon_soap"}
photos: "digest.amazon_us.top_brands[*].best.img; Kaori / Mirai creatives: digest.creatives"
---

# Persimmon soap

**Verdict: #5 of 20, with reservations.** Search interest is up ×4.6 in a year, the strongest growth after color foundation, and new brands are testing hard on Meta. But the market is small ($1.2M a month on five Amazon pages), cheap ($13 median), and so far the growth mostly feeds one older brand, Mirai Clinical, and unbranded sellers. It stays in the top 5 because of the trend; it is the most fragile of the five. ◈

## 1. The product and the buyer

A Japanese-style soap bar with persimmon tannin, sold against **"old people smell"** (nonenal body odor that comes with age). Listings say it openly: "Persimmon Soap for Old People Smell", "Body Odor Control". Buyers: people 50+, and their adult children buying for them. ◆ (listing titles)

Price: $12.99 median (half between $9.99 and $17.99); Mirai Clinical $19.95, Kakiyu $29.99 (2-pack). ◆

## 2. How big, and where it is going

**Size.** At least **69,550 purchases a month** on five Amazon pages, about **$1.2 million a month**: the smallest market in our top 5. ◆ count, ◈ money.

**Trend.** ×4.6 versus a year ago (control-corrected). Yearly index 0.2 → 0.7 → 1.8 → 6.4 → 45.3. Unlike most terms, it has its own peak in October 2026, separate from the spring Google artifact, so the growth is real. Note: 13% of the last two years' weeks are zero (low volume), so single pulls are noisy. ◆ (one pull of three)

## 3. Who holds the market

| Who | Units/mo | Share |
|---|---|---|
| Old brands (mainly Mirai Clinical) | 25,450 | 37% |
| Unbranded sellers, new | 25,450 | 37% |
| Unbranded, old | 11,300 | 16% |
| Brands under 24 months | 7,350 | 11% |

**Mirai Clinical** alone: 25,300 units/mo, ~70 months on Amazon, $19.95, ~$0.63M/mo. Unbranded sellers (yoniagood 10,000/mo at $9.99, NXPPYY 8,000 at $7.99) take ~$0.48M. The new brands are tiny on Amazon: Kaori 1,950/mo, Kakiyu 1,300, Morovan 1,100. ◆ units/price, ◈ revenue and ages.

## 4. Can a newcomer get in

On Amazon, barely so far: three young brands just above 1,000/mo, while cheap multi-packs set the price. The real question is whether the new brands' Meta-driven stores are working (section 5). ◈

## 5. What happens in ads

Meta, US, active, exact phrase "persimmon soap": ◆

| Active | 30+ days | 90+ days | 180+ days |
|---|---|---|---|
| 2,700 | 830 (31%) | 130 (5%) | 11 (0.4%) |

Many fresh tests, few survivors: only 5% of active ads are 90+ days old, the lowest of our top 5. Ads die fast here. 7 of 10 shops in the sample have a 90+ day ad: miraiclinical.com (492 days), the persona page "Grandma's Glow" (206), try-kaori.com (173). ◆

On each brand's own Page: Kaori 198 active / 48 at 90+ / 4 at 180+; Mirai Clinical 96 / 19 / 17; **Kakiyu 470 / 0 / 0**: a 2-month-old brand testing hard. Kaori and Kakiyu also run ads through persona pages ("Grandma's Care Journal", "Mari Tanaka"). ◆

## 6. Do the winners keep growing

Not measured (review curves pending). ◈

## 7. What the winners say

Mirai's 517-day ad: "Say Goodbye to 'Old People Smell' for Good". Kaori's ads run from grandmother persona pages. The angle is shame and family, aimed at the user's children as much as at the user. ◆ ads, ◈ reading.

## 8. Risks and open questions

- **Small pie, low price**: a $13 soap needs many orders to pay for ads. ◆/◈
- **Ads die fast** (5% at 90+ days): many testers, few profitable. ◆/◈
- **Noisy trend** (low search volume). ◆
- **Sensitive topic** (age, smell): ad review and tone risk. ◈

## 9. Verdict and what would change it

**#5.** Growing (×4.6); kill rule (b) passes only because shops keep 90+ day ads, as new-brand units (7,350) are under 10,000. It would drop if the trend fell in pulls 2-3 or if Kaori/Kakiyu stop advertising in the 30-day re-check. The shower filter is the reserve to replace it.

## 10. Methods and sources

- Amazon: `persimmon soap`, ZIP 10001 → `work/blind/graveyard_us/persimmon_soap.json`.
- Meta: [Ad Library, exact phrase "persimmon soap"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=%22persimmon%20soap%22&search_type=keyword_exact_phrase&media_type=all).
- Trends: [Google Trends, US, 5 years, "persimmon soap"](https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=persimmon%20soap).
