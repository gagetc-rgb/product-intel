# Acceptance and reading of Codex's interim lens-M data (2026-11-10)

Input: `INTERIM_STATUS_2026-11-10.md` and the files beside it. Checked by Opus on 2026-11-10. Nothing here is on the site.

## 1. Spot-check against sources (12 rows)

| # | Row | Codex | Source, read 2026-11-10 | Result |
|---|---|---|---|---|
| 1 | Stepprs price and bundles | $22; 2 × $17.60; 3 × $13.20; 5 × $11; 88,552 reviews | same (stepprs.com/products/massage) | ✓ |
| 2 | Hanae price | $34.95 | $34.95 | ✓ |
| 3-6 | Kaori ads 967935396231214, 1621971626261673, 1804257660950823, 1565581295012773: start dates and pages | 05-18 Kaori, 08-01 Margaret Whittaker, 07-04 Sara Garret, 07-29 Kaori | same (Ad Library, US, q=try-kaori.com) | ✓ ×4 |
| 7 | Smooche Trustpilot notice; latest 200 within 11-09…11-10 | as stated | notice present; page 1 dated 11-08…11-10 | ✓ |
| 8 | Ancestral Trustpilot total | 92 | 88 in a 2026-10-09 copy | ✓ (consistent) |
| 9 | Mirai: latest 200 reviews dated 2026-10-28…11-10 | as stated | a 2026-10-28 copy shows 259 reviews in total, newest dated 10-14…10-19; Codex's own total on 11-10 is 271 | ✗ only ~12 reviews can fall in that window; the date range is wrong. The coding of the 35 low reviews may stand, but its period is unknown |
| 10 | Bare Ritual price | $47.99 (subscription preselected) | page text shows $87 for the balm, subscription "every four weeks"; selected price not readable | unresolved |
| 11 | Prime Prometics total | 4,475 (merged profiles) | 2,271 in a 2026-11-09 copy | unresolved (merging) |
| 12 | Kaori bundles | 2 bars $29.90 … 6 bars $59.94 | page text unreadable | unresolved |

Score: 9 of 12 confirmed, 1 wrong, 2 not checkable. No invented numbers found; the error is a date range, not a count.

## 2. The blocker in block A is not real

Codex left every 30+/90+/180+ count "unknown" because the Ad Library filter is labelled "Impressions by date". Checked: `try-kaori.com`, active, US, `start_date[max]=2026-08-12` → the label reads "Impressions by date: on or before 11 Aug 2026", ~210 results, and the newest start date among the cards is 2026-07-31. For **active** ads, "had impressions on or before the cutoff" means "started on or before it" (an ad paused before its first impression is missed, so the count is a floor). ~210 equals the figure we hold from AUDIT §5. Our scripts have used this since 2026-11-07 (`work/blind/meta_ages.py`). Block A can be counted per domain with three URL loads.

## 3. What the data says (◈ unless marked)

1. **Followers advertise through persona pages.** Kaori, the strongest young follower: 3 of 5 sampled ads run from pages named as people or characters ("Margaret Whittaker", "Sara Garret", "Grandma's Glow") ◆. Silvervine: "Susan Mitchell", "Lauren Patterson", "Dr. Mia's Cat Journal", "Vet Visit Diaries", "Cat Wellness Research Center" ◆. Whether these personas are invented is not verified. If a follower's surviving ads rest on invented people, they are evidence for a funnel we will not copy (FTC 16 CFR 465 and endorsement guides). M2 should report, per follower, the share of its 90+ ads that run from its own brand page.
2. **Repeat purchase is often a preselected box.** Preselected subscription or auto-refill: Bare Ritual, Sofyre, Petmizer, Honey Glow ◆. Minimum terms: Herbneden (three shipments before cancelling), Skult (two billing cycles while the page says "cancel anytime") ◆. Billing complaints at Mirai, Earthly Derm, Skult and Smooche fit this. A lawful copy uses opt-in, so M4/M5 must not take the leader's repeat rate as ours. The legal reading (ROSCA, state auto-renewal laws such as California's affirmative-consent rule) needs a primary-source check before it is written as a finding.
3. **Leader complaints (M8): service is fixable, the product mostly is not.** Low reviews by theme (overlapping) ◈:
   - Mirai: shipping 12 of 35. Fixable (US stock). Strongest case for "copy and fix".
   - Earthly Derm: support or refund 6 of 9, shipping 4 of 9. Fixable, but only 9 reviews.
   - Skult: shipping 11 of 19, support 11 of 19. Fixable, but the whole profile has 19 reviews and M1 is weak.
   - Prime Prometics: product 23 of 39 (shade, texture, applicator). For a colour-changing foundation the shade is the promise, so this is a warning, not an opening.
   - Everstride: product 10 of 13 (holes, heels). Needs a different supplier.
   - Ancestral: product 9 of 13 (smell, breakouts). Needs a different formula.
   Limits: Trustpilot draws service complaints more than store widgets do; samples of 9-39 low reviews give themes, not rates.
4. **Leaders' own review counts are less trustworthy than assumed.** Trustpilot withholds Smooche's rating and says it pressured customers to change or remove negative reviews ◆; it shows a notice that Earthly Derm displayed Trustpilot content incorrectly ◆. The site uses Smooche's photo reviews and Earthly Derm's review growth (×7.6) as signals; both need this caveat.
5. **Insoles.** Stepprs: $22 one pair down to $11 a pair in fives, 5-8 business days "worldwide", 88,552 widget reviews ◆; its sampled ads reach 418-469 days ◆. OrthoFlexx: $64.95 a pair, ships from the US ◆. Both are old domains, so they are leaders; no young follower was checked by Codex (getxstance.com has 6 ads in the sample, age unknown). The slow worldwide shipping is a fixable point if Stepprs is the leader to copy ◈. Open as before: the FDA question on "orthopedic" and "pain relief" wording.
6. **Money (M4).** Too thin to compute. Two usable listing prices: silvervine about $0.45-0.47 a stick (unit unclear) against Purriq's 5 sticks for $29.99; rodent pouches $1.89-1.99 per set of 10. USPS retail postage is $8.40-10.20 up to 4 oz ◆ (commercial rates are lower, not collected). For $25-50 orders, delivery, not the product, is likely the largest cost ◈.

## 4. Status of each block

| Block | Accept? | Note |
|---|---|---|
| A ads | no | redo with `start_date[max]`, counts per domain |
| B/C stores | partly | rows checked are accurate; 22 of 103+ |
| D complaints | yes, as themes | Mirai period wrong; no rates |
| E claims | not read in depth | 13 rows |
| F supply | no | 6 rows, 3 in USD |

## 5. What to ask Codex next (in this order)

1. Block A per domain: active total, `start_date[max]` = today − 30, − 90, − 180, for the follower and leader domains of `M2_RESULT.md` and the five extra products. Prove it on 5 products first.
2. For each 90+ ad of a follower: page name, and whether it is the store's own brand page.
3. Store facts for the followers: price in USD, default option, subscription preselected or not, minimum term.
4. Supplier listings for the products that pass 1-2 only.
5. No more Trustpilot pulls for leaders with zero reviews. Do not press purchase, cart or checkout controls on any store.
