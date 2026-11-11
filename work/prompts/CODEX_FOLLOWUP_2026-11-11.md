# Follow-up task for Codex: lens M, second pass

Written 2026-11-11. Continues `work/prompts/CODEX_SCRAPE_LENS_M.md` (its **Rules** section still applies in full). Our review of your interim hand-in: `work/lensm/codex/ACCEPTANCE_INTERIM_2026-11-10.md`. Read both first.

## 1. What we accepted from the first pass

Thank you for the honest gaps list: nothing invented was found.

- We checked 12 rows against their sources: 9 match, 1 is wrong, 2 could not be checked.
- **Accepted:** store facts B/C that you read (Stepprs and Hanae prices, Kaori ad start dates); complaint themes D for Mirai, Earthly Derm, Prime Prometics, Skult, Ancestral, Everstride, Smooche (as themes, not rates).
- **Wrong, fix it:** Mirai's latest-200 date window "2026-10-28 to 2026-11-10". On 2026-10-28 the profile had 259 reviews in total and its newest were dated 10-14 to 10-19, so 200 reviews cannot fall in those two weeks. Re-read the dates of the 200 reviews you coded and write the true first and last date in `leader_complaints.csv`. Keep the coding.
- **Not accepted yet:** block A (no age counts), F (six supplier rows).

## 2. Block A is not blocked: use `start_date[max]`

You stopped because the Ad Library date filter is labelled "Impressions by date". For **active** ads it still works as an age floor: an active ad that had impressions on or before a date started on or before that date. We checked it on 2026-11-10: `try-kaori.com`, active, US, `start_date[max]=2026-08-12` returned ~210 results, the label read "Impressions by date: On or before 11 Aug 2026", and the newest "Started running on" among the cards was 31 Jul 2026. The count is a floor (an ad paused before its first impression is missed). Our own scripts have used this since 2026-11-07 (`work/blind/meta_ages.py`).

URL pattern (one page load per count):

```
https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=<DOMAIN>&search_type=keyword_unordered&start_date[max]=<RUN_DATE minus N days>
```

For each domain record, with the run date:
- `active_total` (no date filter), `active_30_plus`, `active_90_plus`, `active_180_plus` (N = 30, 90, 180);
- a check for each filtered count: the newest "Started running on" among the visible cards, which must be on or before the cutoff. If it is not, write "filter check failed" and do not use the count.

Note: a domain-keyword search can also match other advertisers that mention the domain. On the first 20 cards of each search, record how many link to the domain itself (`own_share_first20`).

## 3. Order of work (prove the method on 5 products before the rest)

**Step 1, five products only:** persimmon soap, tallow balm, turmeric soap, work insoles, silvervine cat dental chew sticks. For each: the leader and every follower domain listed in `work/lensm/M2_RESULT.md` (for insoles and silvervine, `work/lensm/rp/RP_RESULT.md` and your own `meta_ads.csv`; for insoles also stepprs.com, orthoflexx.com, getxstance.com; for silvervine also purriq.com, heycomfora.com, clawval.com, tryarleo.com).

Lash serum is set aside for now (owner, 2026-11-11): its main demand rests on a growth claim a lawful seller cannot make in an ad funnel. Do not spend time on it in this pass. Do sections 2, 4 and 5 for these. Hand in, stop, and wait for our check.

**Step 2, after our check:** the other products of priority 1 and 2, same sections.

## 4. Who is speaking in the ads (new field, M2)

For every follower domain with any 90+ day ad, open its 90+ day ads (the filtered search from section 2) and record per ad: library ID, start date, page name, and `page_type`:
- `brand` (the page name is the store or brand name);
- `person` (a human name, e.g. "Margaret Whittaker");
- `expert` (a title or expert-style name, e.g. "Dr. ...", "... Journal", "Vet Visit Diaries", "Research Center");
- `other` (describe).

Per domain report `ads_90_plus_brand_page` and `ads_90_plus_other_pages`. Do not judge whether a person is real; only classify the page name. Output `follower_pages.csv`.

Why: in your sample, 3 of Kaori's 5 ads run from pages named as people. If a follower's surviving ads come mostly from persona pages, that is a funnel we will not copy, and it must not count as proof that a lawful copy can hold.

## 5. Store facts for followers (B, M4, M5)

For each follower domain of step 1 (not the leaders, which you mostly have):
- price in USD with US delivery selected, for one unit and for each bundle; which option is selected when the page opens;
- subscription: offered or not, **pre-selected or not**, discount, interval, minimum number of payments or shipments, cancellation method as stated;
- shipping: stated time to the US, ships from where, free-shipping threshold;
- guarantee and returns as stated.

Also re-read **Kaori's** bundles by hand (`try-kaori.com/products/deodorizing-persimmon-soap`): on 2026-11-10 the page did not give its prices to us; your values (2 bars $29.90, 4 bars $48.00, 6 bars $59.94) need a second read with US/USD confirmed.

Output: rows added to `store_facts.csv`.

## 6. Smaller items

- **Insoles:** are there followers younger than 24 months with ads alive 90+ days? Start from getxstance.com (6 ads in your sample, age unknown): domain registration (RDAP), first Wayback capture, section 2 counts.
- **Suppliers (F):** wait until step 1 is checked. Then only for products that still have a young follower holding 90+ days.
- **Trustpilot:** no more pulls for leaders with zero or a handful of reviews (Borboleta, Luxe, Terra Lotus, Sproos, Scentify, Babe). Their profiles say nothing.
- **Checkout:** never press add-to-cart, buy, subscribe or checkout controls on any store, even to read a price. Read prices from the product page and its JSON only. If a price shows only in the cart, write "price visible only in cart" and move on.

## 7. Hand-in for step 1

1. `meta_stores.csv` with the section-2 columns for every domain of step 1.
2. `follower_pages.csv` (section 4).
3. Updated `store_facts.csv` (section 5) and `leader_complaints.csv` (Mirai dates).
4. A short `STEP1_STATUS_<date>.md`: what is done, what could not be read and why, and any URL where the filter check failed.
5. Keep every search URL: the same searches are repeated on 2026-12-08 to count followers that stopped.
