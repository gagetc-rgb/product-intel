# Step 1 working status — 2026-11-11

**Incomplete.** This is a working checkpoint, not the requested completed hand-in. Step 2 has not been started. US soap suppliers were added under the owner's new instructions.

## Completed checks

- Thirty-one domain searches have total, 30+, 60+, 90+ and 180+ counts, cutoff URLs and visible-card date checks in `meta_stores.csv`. Searches use the US active library; cutoffs are 2026-10-12, 2026-09-12, 2026-08-13 and 2026-05-15. Trykaoli returned Meta's explicit no-match state for all filtered searches, so there were no dates to check. No date-filter check failures were observed in the checked cards.
- `follower_pages.csv` has 383 directly observed 90+ filtered cards for 19 followers. These are only the visible initial samples, **not** all results. Page types are interpretations from names, not findings about the people or ownership. Meta can group multiple ads under a creative; the rounded result counts and visible cards are not directly interchangeable.
- `store_facts.csv` updated for Kaori, Bare Ritual and GetXstance. Kaori's settled page again showed 2 bars $29.90, 4 $48 and 6 $59.94, with 4 and one-time purchase selected; USD was requested, but US delivery-country selection was not confirmed. Bare Ritual's site displayed Indonesia shipping, so prices are not accepted as confirmed US prices.
- Cattle Creek: the 90+ keyword search includes 20 unrelated page names among 25 visible cards; only 5 brand cards were retained. The rounded domain-search count cannot be attributed to the store.
- Wild Gold: on 2026-11-11, the 90+ search displayed ~35 results and 29 cards; its `See more` control was pressed twice without adding cards. One card reports a two-ad creative group, but the difference from the rounded result count remains unresolved. The 29-card page-name counts are therefore a sample, not the full inventory. [Search URL](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=wildgoldtallow.com&search_type=keyword_unordered&start_date[max]=2026-08-13).
- Movara: the first 20 unfiltered ad links point to work boots; visible 90+ ads are for boots. Do not count these domain ads as proof of longevity for standalone insoles.
- GetXstance: RDAP says getxstance.com registered 2024-12-13. The first CDX capture is 2024-12-17 but returns HTTP 406; do not represent it as a successful page capture. Its homepage links to thexstance.com and uses its email domain; the latter domain was registered 2020-11-26. Store/business age is therefore unclear, not proven under 24 months. Source URLs are in `store_facts.csv`.
- Mirai complaint coding preserved, erroneous latest-200 date window removed. The original full set of 200 review IDs/dates was not saved, so its exact endpoints cannot be recovered from the surviving 35 coded low-review records. Endpoints remain unknown, rather than substituting a newly retrieved sample.

## Remaining

Additional candidate domains still need searches, and the full 90+ card lists and complete follower store facts remain to be gathered. 30/60/90/180 counts are domain-keyword results filtered by impressions date, not product-specific advertising counts or proof of paid sales. Domain matches can include other advertisers; GloMelanin and Trykaoli samples include other products. Results are not a survival rate.

All URLs for checked searches are in `meta_stores.csv`; source dates and unresolved US/price fields are retained in `store_facts.csv`. No filter failure URL to list so far. Do not treat this checkpoint as the requested final stage-1 delivery.

## Owner update: additional scope (in progress)

- Added 60+ column with cutoff 2026-09-12. All 31 domains checked in the new pass have a dated 60+ result and check; legacy rows are explicitly unknown.
- Tooth powder keyword cards and first-20 checks are in KEYWORD_CARDS.md. MYTO domain counts, 27 visible 90+ cards and initial US store facts are recorded. MOOTHS counts, 7 visible cards and preliminary store facts are recorded. Leader comparison remains. Three additional candidates are discussed in TOOTH_POWDER_CANDIDATES_2026-11-11.md.
- Beamach candidate site and TikTok/Mirai findings are in TIKTOK_PERSIMMON_2026-11-11.md; common ownership not independently confirmed and Kaori status remains unknown.
- Four US soap manufacturers added to cogs.csv; prices for stock bars must not be treated as custom persimmon quotes.
- Both pre-wash persona ads link to bekyndbeauty.com, registered 2020-02-16; see PREWASH_PERSONAS_2026-11-11.md.
- Additional searches now include Pure Good, Forge and NylaTails within the 31 checked domains. Forge's search is particularly noisy: only 3 of the first 20 unfiltered links go to the store, so its rounded result counts cannot be attributed to the store. Pure Good's first 25 older cards include other product forms.
- Store facts updated for GloMelanin, Neptune, Wild Gold, Purriq, Kitty Ka-Zoom and Comfora. Several prices remain provisional: Purriq's main and sticky prices conflict; Comfora's US selector conflicts with an Indonesia shipping notice. Individual fields record the uncertainty.
- Lash-serum scope remains unfinished: `HANAE_AD_CHECK_2026-11-11.md` documents the mixed-product domain results and two lash ads. The Trending In Korea profile requires Facebook login, so its profile claims remain unknown. Hanae's product page was refreshed in `store_facts.csv`; full 90+ page classifications and Hanae/Babe low-star complaint counts remain outstanding. No sortable Hanae review widget was found on that page.
