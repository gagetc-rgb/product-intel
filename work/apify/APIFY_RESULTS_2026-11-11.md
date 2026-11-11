# Apify Meta Ad Library pull, 2026-11-11

Scraper: `curious_coder/facebook-ads-library-scraper` (≈52K users, 4.8 rating over 114 reviews, 99.8% of runs succeed; $0.75 per 1K ads). Chosen over `harshmaur` (cheaper at $0.50 per 1K, but 121 users and 3 reviews, created June 2026) because the 2026-12-11 repeat must use the same tool. Client: `work/apify/apify.py` (token from `.env`).
Spent: $1.97 of $5 (pilot $0.05, run A $0.59, run B $1.31, date test ~$0).

## Run A: the 8 young copies, ads alive 90+ days (US, active, ran before 2026-08-13)
Input `runA_input.json`, raw `runA_2026-11-11.json` (783 ads, all of them: each store's count equals Meta's total), per-product summary `runA_summary.json`.
Check: Hanae 251 = the "~250" counted by hand; ad 2160249871380670 matches the manual record exactly. ◆

| Store | 90+ ads, all products | 90+ ads, our product | of them 180+ | oldest, our product | own page (our product) | Reading |
|---|---|---|---|---|---|---|
| Hanae (lash serum) | 251 | **185** (74%) | **0** | **124 d** | 185 of 185 (Hanae Korea 56, Trending In Korea 129) | Lash holds 90+, but every 180+ ad (12) and the 246-day ad sell the **color-adapting concealer/foundation stick**, not the serum. ◆ |
| Kaori (persimmon soap) | 209 | 179 | 58 | 230 d | **48 of 179 (27%)**; the rest are persona pages (Grandma's Glow, Patti Clayton, Linda Doxey, Margaret Whittaker, Barbara Robertson) | The 30-ad sample said 11 of 30 own; the full count is worse. ◆ |
| Wild Gold (tallow) | 35 | 35 | 24 | 272 d | 35 of 35 | Confirmed. ◆ |
| Bare Ritual (tallow) | 175 | **44** | 21 | 305 d | 43 of 44 | Tallow ads are own-name, but the store mostly sells a rosemary hair spray (83 ads) through persona page "Eleanor Roseford Bennett" and advertorial sites. ◆ |
| MYTO (tooth powder) | 27 | 27 | 0 | 134 d | 27 of 27 | Confirmed. ◆ |
| MOOTHS (tooth powder) | 7 | 7 | 0 | 100 d | 6 of 7 | Confirmed. ◆ |
| Facelove (color foundation) | 40 | 14 | 0 | 167 d | 9 of 14 | Most long ads sell mascara (25); the stick holds 14. ◆ |
| K-Glow (chin wrap) | 39 | **0 chin wraps** | – | – | – | Main product is a "V-volume PDRN pink balm" (28); the "double chin" ad (172 d) sells a **facial drainage brush**. K-Glow is not a chin-wrap copy. ◆ |

Consequences for the site (not applied yet, owner to decide):
1. Chin wrap has no young copy → "Копия держится" no longer holds (6 → 5 products; copies 8 → 7).
2. Hanae: "246 дней" in the copies chart is the concealer stick; the lash serum's oldest ad is 124 days, none at 180+. Hanae is also a young holding copy in **color-changing foundation** (66 ads 90+, 12 at 180+, oldest 245 d; the stick "adapts to your skin tone"), so color foundation gets a second young copy.
3. Kaori: own-page share 27% (48 of 179), not 11 of 30.
4. Bare Ritual: honest for tallow, but most of its spend goes to another product through a persona page; "рекламируются только от своего имени" is true only of its tallow ads.

## Run B: the new wave by product phrase (US, active, ran 2026-08-13..10-12)
Note: Meta's date filter means "delivered in the window", not "started in it", so the pull also holds old ads; start dates were filtered afterwards. Sample: up to 300 ads per phrase, Meta's order (impressions), so a floor. Raw `runB_2026-11-11.json`, by domain `runB_domains.json`, candidates with RDAP dates `newcomers_2026-11-11.json`.

Young stores (domain under 24 months) whose ads in the sample are all 30-100 days old, 3+ ads:

| Product | Store (domain, registered) | Ads | Oldest | Note |
|---|---|---|---|---|
| Persimmon soap | kakiyucare.com (2026-08-16) | 74 | 82 d | Kakiyu is an older Amazon brand (◈); new domain, persona pages "Mari Tanaka", "Dr. Margaret Ellis" |
| Persimmon soap | skinscienceinsider.com (2026-07-06) | 28 | 76 d | advertorial-style name |
| Persimmon soap | bellaviashop.com (2026-03-25) | 15 | 90 d | page "Mari Tanaka" |
| Persimmon soap | cachinaturals.com (2026-08-03) | 12 | **91 d** | crossing 90 now |
| Color foundation | beaumontvoss.store (2026-05-15) | 6 | **92 d** | crossing 90 now |
| Color foundation | trynova.store (2026-04-09) | 9 | **100 d** | page "Trending On K-Beauty" |
| Color foundation | mushicosmetics.com (2026-07-05) | 8 | 78 d | |
| Lash serum | serevedeals.com, brand Renora (2026-06-21) | 8 | 46 d | |
| Lash serum | glaume.com (2026-06-23) | 5 | 58 d | |
| Tallow balm | trybullbee.com (2025-11-14) | 4 | 51 d | |
| Chin wrap | try-chinology.com (2025-03-20) | 8 | 77 d | product not checked |
| Tooth powder | none new besides Mooths | | | MYTO 70 and MOOTHS 15 ads hold the phrase; the niche is barely contested |

Not yet checked: that each candidate sells the category product (landing pages not opened), and run A for the 90+ candidates (cachinaturals, beaumontvoss, trynova).

## Repeat on 2026-12-11 (moved from 12-08: the Apify credit cycle runs 11 Nov - 10 Dec, the repeat needs the new $5)
Rerun `runA_input.json` and `runB_input.json` with the same scraper (cost ≈ $2). Compare by `ad_archive_id`: which 90+ ads stopped, and which newcomers crossed 90 days.

## Full 90+ day phrase pulls, 2026-11-11 (afternoon)
Method: every active US ad that contains the exact product phrase and has run since before 2026-08-14 (Meta's upper bound excludes the start day, hence the margin), grouped by landing domain, RDAP / Wayback for domain age, then each candidate pulled by domain. Owner's bar for the site: 5+ ads alive 90+ days (US impressions are not public).
- Soaps (`runSoap*`, `runSoapDom*`, `soap_candidates_2026-11-11.json`): persimmon young copies Kaori, Cachi Naturals (7 ads, 91 d), Bella Via (6, 90 d, persona page); old Swarva (13, 124 d). Turmeric young copies Solrise (6, 5 at 180+, 477 d), Glowvani (14, 112 d), Derm Glow (16, 112 d); STEM & SOUL 166 ads 90+ (91 at 180+, 371 d) but domain age unknown (.co registry silent, first Wayback 2026-05-15).
- Watch products (`runW*`, `runWDom*`, `watch_candidates_2026-11-11.json`, `watch_rdap_2026-11-11.json`): color foundation young copies Hestia (the video's store; hestiacosmetics.com 2026-03 + trylumineskin.com 2025-09; 383 + 40 ads 90+, oldest 371 d), Yuki (40, 125 d, page "Korean Foundation Tips"), TryNova (5, 100 d); tallow Holicow (7, 163 d); lash serum and tooth powder: nothing new.
- Below the bar, left off the site: Aurellee (3), Beaumont Voss (1), Kreain (gum, 1), Honey Glow (1), Herbal Ciddy (1).
Spent this cycle: about $4.6 of $5.
