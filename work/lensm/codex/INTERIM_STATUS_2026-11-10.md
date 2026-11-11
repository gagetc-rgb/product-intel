# Interim status — Lens M, 2026-11-10

This is an **incomplete handoff**, not the final report. Data collection is ongoing.

## Not done and why

- Meta A: 119 raw card rows across nine categories, versus at least 5,000 requested across 25 categories. Samples are neither complete nor evenly distributed across age bands. Store-by-store 30+/90+/180+ counts remain largely unknown. Meta's available date filter concerns impressions, not a verified ad-start cutoff; no substitute count was invented.
- Store facts B and age C: 22 store/category rows, many partial, versus the original 103 stores plus new discoveries. Full Wayback, oldest product/review, page transparency and business-age classification remain outstanding. A domain-registration date alone is not brand age.
- Leader complaints D: five requested leaders (Mirai, EarthlyDerm, Prime Prometics, Everstride, Smooche) have 200-card samples, in addition to the 200-card YURI sample in a separate file. Several other exact-domain profiles have few or zero reviews; additional leaders still need review and coded examples.
- Leader ads E: 13 preliminary claim rows, not 10 longest-running active ads for each leader. Video and audio have not been systematically reviewed.
- Supplier economics F: six supplier rows, of which three have live USD price tiers; many product/pack units and production terms need confirmation. At least five listings per 15 priority-1 products were requested. USPS published rate information is separate and is not a product-level fulfillment quote.
- EU/UK cohort G is optional after A–F and not done. No survival estimate can be inferred from these partial active-ad samples.

## Could not read or verify

- GODA's exact-domain Trustpilot page showed connection verification on 2026-11-10; no bypass. `goda.co` and `godaperfume.com` Trustpilot profiles have not been merged.
- Several product pages showed non-US currency or no confirmed delivery destination. Unknown US pricing remains unknown. Review samples are global, self-selected, and often multi-product; they are not sales-weighted or US-only.
- `luxe.com` Trustpilot profile is categorized as a valet-parking service; its identity with the intended beauty store is unclear. No similarly named brand was substituted.
- Some supplier pages timed out, redirected to generic pages, or displayed inconsistent packaging/unit information. Historical search snapshots are not current quotes.

## Deviations from the task

- Current data are convenience samples and partially completed records, not age-balanced 200-ad category pulls or a finished census. Keyword K2 is incomplete, and below-threshold keyword results are marked as such.
- Some claim rows use visible ad text only, not the first three seconds of the video; the precise ten longest-running ads are not established. ◆ platform observation, ◈ interpretation, ◇ estimate as indicated in individual files.
- During TrySkult review, clicking the page's one-time-purchase link unexpectedly added two items to the initially empty session cart; both were removed and the empty cart verified. No order was placed. The public page says cancel anytime, while its subscription policy states a two-billing-cycle minimum.
- Firecrawl, Amazon, logins and bypasses were not used. The optional December 8 repeat has not happened.

## Files to open

- `meta_ads.csv`, `meta_stores.csv`, `store_facts.csv` — raw ads, identity-level observations and store facts.
- `leader_complaints.csv`, `LEADER_COMPLAINTS.md`, `*_low_review_codes.csv` — review summaries and links to coded reviews. YURI is in `YURI_REVIEW_2026-11-10.md`.
- `leader_claims.csv`, `cogs.csv`, `SHIPPING_RATES_2026-11-10.md` — preliminary creative claims and supplier/shipping information.
- `KEYWORD_CARDS.md`, `METHOD_LOG.md`, `RESEARCH_NOTES_2026-11-10.md`, `INSOLES_2026-11-10.md` — query definitions, collection notes and limitations. Scripts are included for reproducibility.

Important: figures are snapshots read on 2026-11-10. A platform's domain-keyword results are not automatically the number of advertisements owned by that store, nor evidence of sales or profit.
