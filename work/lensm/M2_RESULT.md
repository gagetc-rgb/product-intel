# M2 store check, Lens M (collected 2026-11-10)

Input: `m2_candidates.json` (Meta Ad Library US, active ads, sampled 2026-11-07, about 33-70 ads per category). Rows: `m2_stores.csv` (172 rows). Scripts: `m2_fetch.py`, `m2_fetch2.py`, `m2_data.py` (my hand reading of each store), `m2_build.py`. Raw pages: `raw/`.

Marks: ◆ read directly from a platform or registry (Ad Library age, RDAP date, Wayback date, text on the store page). ◈ my reading (sells / does not sell, follower / leader, noise).

## Skipped categories
- `pore_patch`: the phrase "pore patches" returned 1 ad and 1 store (vueswiss.com). Not checked. ◆
- `prewash_oil`: phrase "pre wash" returned car-wash, fashion and sock-catcher advertisers. Not checked. ◆
- `whitening_powder`: phrase "whitening powder" returned a dailysale marketplace, an oral-care review site and similar. Not checked. ◆

## Table (domains with an oldest sampled ad of 90+ days; the <30 column is for M7)

"Sell" = my reading that the store sells the product form of the category (◈). "Unclear" stores are not counted as sellers. Followers exclude the owner-listed leaders and the store marked "leader?" (oldest ad among sellers, in categories without a listed leader). "Young" = earliest of RDAP registration, first Wayback capture and oldest product date is on or after 2024-11-10 (◆ dates, ◈ class).

| Category | Ad sample (ads, ◆) | 90+ day domains / sell / unclear / no (◈) | 90+ sellers (names) | Followers among them | Young followers (date proving it, ◆) | Under-30-day sellers (M7) | Leader price and usual bundle (◆ as far as read) | Off-target noise among 90+ domains (◈) |
|---|---|---|---|---|---|---|---|---|
| persimmon_soap | 47 | 2 / 2 / 0 / 0 | miraiclinical.com (leader), try-kaori.com | 1 | **1**: try-kaori.com (RDAP 2026-02-11; first capture 2026-10-05) | 0 | Mirai: price not read; free shipping $70+. Kaori: upsells soap bag 2-pack $12.99, deodorant $14.99, body wash $19.99; "up to 30% off" | 0 of 2 (0%) |
| turmeric_soap | 45 | 8 / 2 / 6 / 0 | earthlyderm.com (leader), glomelanin.com | 1 (glomelanin, old: RDAP 2022-02-10) | **0** (stemandsoul.co is young by Wayback 2026-05-15 and product date 2025-08-28 but its soap is "Superfood Soap", turmeric not named: unclear) | 1 (trykaoli.com, RDAP 2026-05-10, 9-day ad) | Earthly Derm: page text empty when read, price unknown | 0 of 8 (0%); 6 of 8 unclear |
| body_oil | 63 | 11 / 2 / 2 / 7 | goda.co (leader), vitaecharm.com | 1 (old: RDAP 2022-10-05) | **0** | 0 | Goda Silk Body Oil $39.00 and $49.00 (products.json); body butter $39 | 7 of 11 (64%): clinics, med spas |
| color_foundation | 70 | 8 / 5 shops (6 domains) / 2 / 0 (luxe.com not in sample) | luxe.com (not in sample; sells it), primeprometics.com, hestiacosmetics.com = trylumineskin.com (same shop), smooche.com (leaders); vimacosmetics.com, shopbeautylust.com | 2 (both old: RDAP 2021-12-30; 2018-12-05) | **0** | 1 (dermamuse.co, RDAP unknown, first capture 2025-12-05) | Luxe: By Luxe Color Changing Foundation $39.95 (home page). Hestia: buy 1 get 1 free (Black Friday); price not matched. Smooche and Prime read in IDR | 0 of 8 |
| tallow_balm | 59 | 13 / 11 / 0 / 2 | ancestralcosmetics.com (leader) + 10 | 10 | **2**: wildgoldtallow.com (RDAP 2025-03-17), bare-ritual.com (RDAP 2025-08-04) | 0 | Ancestral: bundles up to 35% off, free ship over $60; price not matched. Papabear kit $29 (reg $121) | 2 of 13 (15%): decor retailer, skincare brand without tallow |
| lash_serum | 57 | 9 / 3 / 2 / 4 | borboleta.com, babeoriginal.com (leaders), hanaekorea.com | 1 | **1**: hanaekorea.com (RDAP 2025-11-02) | 0 | Borboleta: Lash + Brow serum bundle, free ship $65+; prices not matched | 4 of 9 (44%): lash clusters, extensions, Sephora, analytics host |
| shower_filter | 33 | 3 / 0 / 3 / 0 | none confirmed (santevia.com, aquatru.com, purewaterfreedom.com unclear); sproos.co is not in the sample | 0 | **0** | 0 | Sproos: price not read (not in sample) | 0 of 3; 3 of 3 unclear |
| scent_diffuser | 42 | 8 / 4 / 3 / 1 | scentifyhome.com, aurahouse.com, aroma360.com (leaders), scentfinity.com | 1 (old: RDAP 2018-10-03) | **0** | 1 (scentiment.com, RDAP 2004-06-03: old domain) | Aura Diffuser $79; Aroma360 Mini Pro $99.95, $49.95 with one-oil-a-month subscription; Scentify $99/$199/$249 on page, unmatched | 1 of 8 (13%): HVAC |
| hair_serum | 50 | 17 / 4 / 9 / 4 | hinu.co (leader?), vedix.com, ekmiveda.com, curlmix.com | 3 (all old: RDAP 1999, 2024-09-29, 2015) | **0** | 0 (peptonix.com unclear, young) | not read | 4 of 17 (24%); 9 of 17 unclear |
| compression_socks | 33 | 8 / 5 / 1 / 2 | everstridesocks.com (leader), hushedsocks.com, onecompress.com, comradsocks.com, sockwellusa.com | 4 (all old: RDAP 2023-01-09 and earlier) | **0** | 0 (bombas.com unclear, old) | Everstride Bamboo Wide $34 (reg $39); Black Friday buy 2 get 2 free | 2 of 8 (25%) |
| chin_wrap | 63 | 17 / 2 / 4 / 11 | tryskult.com (leader), buykglow.com | 1 | **1**: buykglow.com (RDAP 2025-12-02) | 0 (restoradaily.com unclear) | Skult: Collagen Face Sculpt Wrap; price read in IDR only; "up to 50% off" | 11 of 17 (65%): clinics, med spas, WhatsApp, Google |
| dog_fountain | 50 | 10 / 2 / 5 / 3 | selenepets.com (leader?), petkit.com | 1 (petkit, old: RDAP 2003) | **0** (selenepets.com is itself young: RDAP 2025-08-16, but it has the oldest ad here, so I treat it as the leader) | 0 | Selene: sale "up to $70 off", bundles; $70 and $135 on page unmatched | 3 of 10 (30%); phrase "water fountain" brings garden/pond ads |
| hair_removal_cream | 63 | 7 / 3 / 1 / 3 | simplesnatched.com (leader?), nohaircrew.us, meravae.co | 2 (nohaircrew.us old: first capture 2021-08-03; meravae.co age unknown: RDAP and Wayback both empty) | **0** | 0 | Snatched: Black Friday up to 60% off + 2 free gifts; price not read | 3 of 7 (43%) |
| neck_cream | 54 | 8 / 0 / 4 / 4 | none confirmed | 0 | **0** | 0 | n/a | 4 of 8 (50%) |
| rosemary_oil | 59 | 15 / 0 / 9 / 6 | none confirmed | 0 | **0** | 0 (azureboutique.co unclear) | n/a | 6 of 15 (40%); 9 of 15 unclear |
| magnesium_spray | 51 | 4 / 1 / 2 / 1 | ozcogoods.com (leader?) | 0 | **0** (ozcogoods.com is young: RDAP 2024-11-27, 17 days after the cut-off; it is the only seller, so treated as leader) | 0 | Ozco: $36 or $49 on page, unmatched | 1 of 4 (25%) |
| exfoliating_towel | 54 | 3 / 2 / 1 / 0 | goshi.com (leader?), simabrand.com | 1 (old: RDAP 2021-10-20) | **0** | 0 (ecoviabrand.com unclear, young) | Goshi: price not read | 0 of 3 |

Overall (◈): 172 rows = 151 domain-category rows with a 90+ day ad, 18 with an oldest ad under 30 days, and 3 owner-listed leaders that are not in the sample (luxe.com, terralotus.shop, sproos.co); 164 distinct domains. Of the 151 rows with a 90+ day ad: 49 sell the product (48 shops, because trylumineskin.com and hestiacosmetics.com are one shop), 54 unclear, 48 not sellers (32% off-target noise). Of the 18 rows under 30 days: 3 sell (trykaoli.com, dermamuse.co, scentiment.com), 6 unclear, 9 not sellers.

Young followers with a 90+ day ad, total: 5 shops in 4 categories: try-kaori.com (persimmon soap), wildgoldtallow.com and bare-ritual.com (tallow balm), hanaekorea.com (lash serum), buykglow.com (chin wrap). Three more young sellers with a 90+ day ad are the oldest-ad seller of their category, so I class them "leader?" rather than followers: selenepets.com (dog fountain), simplesnatched.com (hair removal cream), ozcogoods.com (magnesium spray). ◆◈

## What could not be read, and why
- `products.json` (Shopify) returned HTTP 429 `local_rate_limited` (retry-after 60 s) for 117 of 161 stores, 404 for 20 and 403 for 5. I treated 429 as a block and did not work around it. Readable: goda.co, stemandsoul.co, trynova.store, aquatru.com, boxiecat.com. So `shopify_created` is unknown for almost every store, and product titles and prices come from the home page text only. A second page per store (`/collections/all`) also returned 429 for 114 of the stores that were tried; I stopped there.
- Prices: most stores' product prices were not readable. Smooche, PrimePrometics and Skult showed IDR (the server is in Indonesia). Where the page listed prices without a product label, I wrote "unmatched" and did not pick one. The leader price column is therefore thin.
- Pages blocked (403 or empty 202) or not loading: purewaterfreedom.com, mommycarekits.com, thestudiomd.com, clueblog.com, spoiledchild.com, osanyinherbs.com, formulaaffiliate.com, lilesy.com, whatgracebought.com, bombas.com (429).
- RDAP gave no registration date for .co and .us names: goda.co, sproos.co, meravae.co, dermamuse.co, hinu.co, averastore.co, aurlux.co, drift.co, lymphoria.co, nohaircrew.us, hairqare.co, azureboutique.co, trylumin.co, happywags.co, spaoffers.co. For these the age comes from Wayback only (a floor), or is "unknown" (meravae.co, averastore.co: no Wayback capture either).
- 54 "unclear" stores had home pages with no product names (cart overlay, quiz page, or only banner text). I did not guess.

## Findings
1. Only 5 young follower shops with a 90+ day ad turned up in 17 categories (try-kaori.com, wildgoldtallow.com, bare-ritual.com, hanaekorea.com, buykglow.com). Tallow balm has 2; persimmon soap, lash serum and chin wrap 1 each; 13 categories have none. ◆◈
2. Tallow balm is the only category with a crowd of sellers: 11 sellers with 90+ day ads (10 followers, 8 of them registered before 2024-11-10), which is also the clearest sign of crowding (M7). ◆◈
3. The persimmon-soap sample is tiny: 4 stores in total, 2 with 90+ day ads (the leader and Kaori). Kaori's domain is 9 months old and its oldest ad is 173 days old, i.e. it has run for most of its life. ◆
4. Several "followers" are old businesses that have been selling for years (compression socks: 4 of 4 followers registered 2016-2023; scent diffusers; foundation). An ad that survives 90 days there says little about a copyable newcomer. ◆◈
5. Chin wrap, body oil and rosemary oil, plus neck cream, are dominated by noise (40-65% off-target among 90+ domains) or by stores I could not read; their M2 numbers are the least reliable. ◈
6. Hestia: hestiacosmetics.com was registered 2026-03-08 but has Wayback captures from 2018 (earlier owner) and its twin domain trylumineskin.com was registered 2025-09-25: the shop moved domains; I class the shop as the leader and not as a follower. ◆◈

## Limits
The sample is about 60 ads per category found by one generic phrase, so every number is a floor. The US Ad Library lists only active ads, so stopped ads are invisible and only survivors can be seen (survivor view, no failure rate). Nothing here says how many followers failed. ◆
