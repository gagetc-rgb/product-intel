# Method log — 2026-11-10

## Not done and why
- A: Full 25-product Meta phrase counts, relevance checks, date filters, 200-ad balanced samples, redirects and store-level counts were not completed. Only a small convenience sample from one domain search was read. Its approximately 750 keyword matches are not verified as store-owned ad count.
- B and C: The 103 pre-existing `yes`/`unclear` store rows, other stores, US-country-confirmed prices and independent age evidence were not rechecked. One store was partially read, and its prices remain unconfirmed for US delivery.
- D: The requested roughly latest 200-review sample, all leaders, systematic coding and three examples per theme were not completed. One profile and one 20-review filtered page were read.
- E: The 10 longest-running ads per leader were not identified. One visible ad was coded for illustration only.
- F: Supplier and shipping-rate evidence was not gathered. No contribution margin was calculated.
- G: Not attempted because A–F are incomplete.

## Could not be read or verified
- The Kaori store's explicitly selected delivery country and currency code: the product view displayed dollar signs, but the delivery country was not selected or confirmed.
- Final redirect destinations, creative format and grouped creative counts for most ads in the small sample.
- The product page's review-widget provider and a verified count of reviews; the page's 8,000+ figure is described as customers.
- Age classification for Kaori: prior project rows were not treated as fresh independent registry or archive checks.
- Trustpilot's precise TrustScore: numeric text showed 4.7 while an image accessibility label said 4.5. Both are recorded, rather than silently choosing one.

## Deviations
- Partial collection replaces the specified complete census and balanced sampling; records must not be interpreted as a completed study.
- Site-provided prices were captured only as provisional dollar-sign prices: US destination was not confirmed, so they are not valid as US-price evidence.
- The leader-claims row is a convenience example, not a result of sorting the ten oldest ads.
- No Git commit, no Amazon, no Firecrawl, no bypass of login, captcha or bot checks.

## Source log
| Date | URL | Result | Use |
|---|---|---|---|
| 2026-11-10 | https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=try-kaori.com&search_type=keyword_unordered | Opened in in-app browser; US active keyword search showed ~750 matches and individual ad cards. | Kept as direct page observations; number not attributed to the store without verification. |
| 2026-11-10 | https://try-kaori.com/products/deodorizing-persimmon-soap | Opened in browser. Initial accessibility tree changed after full rendering; final state showed 2/4/6-bar bundles and one-time option selected. | Kept provisionally; US delivery country not confirmed. |
| 2026-11-10 | https://try-kaori.com/policies/shipping-policy | Free shipping, processing and US transit times visible. | Kept as stated policy, not observed fulfillment. |
| 2026-11-10 | https://www.trustpilot.com/review/try-kaori.com | Verification screen resolved itself without bypass; profile and visible reviews loaded logged off. | Kept profile-wide counts; not treated as latest-200 distribution. |
| 2026-11-10 | https://www.trustpilot.com/review/try-kaori.com?stars=1&stars=2&stars=3 | First page of 1–3-star filtered reviews opened. | Qualitative examples only; no complete theme count. |

Files are partial observations, not acceptance-ready. ◆ = direct reading, ◈ = interpretation, ◇ = estimate. Unknown values include a reason where known. Figures can change after collection.

## Subsequent collection on 2026-11-10

The statements above describe the initial pass only. Later checks are recorded in `RESEARCH_NOTES_2026-11-10.md`, `YURI_REVIEW_2026-11-10.md`, and `INSOLES_2026-11-10.md`: three category phrase samples were examined after their K1 cards, 200 unique YURI Trustpilot reviews were counted, registry dates were read for ten domains, and several store and ad rows were added. The specified full coverage and theme coding remain incomplete.

2026-11-10: silvervine K2 was corrected to 17/20 clear, two off-target and one unclear after checking what the ads actually sold. The public Meta result list displayed 27 cards; pressing its visible See more control twice did not add cards. The resulting convenience sample is not the requested 200-ad age-balanced sample. Enzyme-device phrase sample and Petmizer product/registry checks are documented in `RESEARCH_NOTES_2026-11-10.md`.

2026-11-10: three Alibaba product pages opened in the in-app browser and displayed IDR rather than a verified US/USD purchase view; `cogs.csv` records unknown USD prices, with details and links. A rodent product-introduction page displayed USD tiers but explicitly says the actual listing takes precedence and its description may lag; it is retained only as a caveated observation. USPS Notice 123 opened as an official published rate card; actual package weights remain unknown. See `SHIPPING_RATES_2026-11-10.md`.

2026-11-10: a first-20 K2 check of the previously documented `work insoles` keyword found 17 clear product matches, one off-target foot sleeve and two unclear cards. Its first 20 card rows are retained as a convenience sample with individual flags; no category-wide conclusion or 200-ad cohort follows.

2026-11-10: Trustpilot Earthly Derm, most-recent order, pages 1–10 read through the public browser. Pagination initially produced duplicate readings; the collection was deduplicated by review URL and verified to contain 200 unique reviews. All nine visible 1-star reviews were coded into non-exclusive themes with review links in `LEADER_COMPLAINTS.md`; this coding does not include the remaining 179 older profile reviews or other sources.

2026-11-10: Trustpilot Mirai Clinical pages 1–10 in most-recent order contained 200 unique review URLs; rating distribution, dates and four preliminary complaint examples are recorded in `LEADER_COMPLAINTS.md`. Full coding of the 35 low-star reviews remains outstanding.

Subsequent continuation: all 35 low-star Mirai reviews in the retained latest-200 browser snapshot were coded individually into overlapping themes; `mirai_low_review_codes.csv` contains the identifiers and flags. The earlier sentence describing coding as outstanding is a historical state only. Counts depend on the stated coding definitions and include all locations and product lines, not only the target soap.

Subsequent continuation: product pages for Herb'n Eden, Honey Glow and Stem & Soul established that these formerly unclear stores sell a turmeric-containing bar. Their facts and links are in `store_facts.csv`. Stem & Soul US active Meta domain search returned about 1,000 keyword results and Honey Glow about 46, including other products; these are not owner-specific ad counts. The first 20 Stem cards, including two off-target balm ads, and one Honey Glow card are retained individually. A Stem soap ad dated 2025-11-09 was active at collection, but age classification and complete store-level counts remain unresolved. The .co creation date was found on a third-party site; the official registry's WHOIS remains to be checked. The Stem homepage says ships from Arkansas while the product page says Phoenix, Arizona; neither should be asserted as the actual fulfillment origin without resolution.

Subsequent continuation: Diablo Cosmetics and Facelove product pages both explicitly sell eyelash serum. Meta domain searches showed approximately 230 and 1,100 keyword results, respectively, but Facelove's visible older ads included foundation or mascara; they cannot be counted as serum ads. Diablo serum ad 1479795590467005 started 2026-04-29 and was active at collection. Store prices lack confirmed US delivery country. The Facelove page states a six-week result and a four-week panel in the same passage; this is recorded as a seller-page contradiction, not validated evidence.

Subsequent continuation: direct product pages established that JCS Miracle, Body Wise and CPH Grooming sell hair serum. JCS displayed $12.99 with `?currency=USD` but US delivery country was not confirmed. Body Wise displayed US/USD and $35.99. CPH displayed Germany/EUR; an attempt to select another country did not succeed, so US price remains unknown. Verisign RDAP showed JCS domain registration 2020-09-11 and Body Wise 2025-10-27, not necessarily business ages. Body Wise Meta domain search showed about 110 matches including its micro-roller; the old sample ad is flagged ambiguous, not presumed to advertise the serum.

Subsequent continuation: K1 for all 20 original categories was documented before new category phrase searches. The `tallow balm` search then returned about 4,800 active keyword results; first-20 K2 17/20 target, two off-target and one mixed. The 20 card records were added to `meta_ads.csv`, excluding any already present by library ID; the count is a convenience sample, not the required balanced census. F-Balm opened with Canada/CAD selected; an attempt to change country timed out, so no US price was recorded.

Subsequent continuation: the in-app browser timed out twice, including once while reopening its inventory. Public search-service snapshots were used for Trustpilot profiles and GODA's product page; crawl recency is stated separately because read date does not mean the underlying page was fetched live. Exact Trustpilot profiles goda.co and godaperfume.com are separate and both link to goda.co; Smooche displays a Trustpilot warning and suppressed rating. No attempt was made to bypass a captcha or login. See `LEADER_COMPLAINTS.md`.

Subsequent continuation: search-service product copies identify waterless cold-air diffusers at House of Duaa and Hotel Collection. The Drift page confirms a home fragrance plug-in with replaceable refill but does not establish a waterless cold-air mechanism; its classification stays unclear. These snapshots did not establish current US-selected prices. The Hotel Collection seller widget snapshot showed no low-star ratings, a disputed indicator ◇ rather than a quality measure.

- 2026-11-10: Trustpilot Prime Prometics via logged-off in-app browser, https://www.trustpilot.com/review/primeprometics.com?sort=recency; kept 200 distinct cards from pages 1–10, and coded 39 low-star IDs. Pagination initially returned previous DOM immediately after URL changed; discarded duplicate and waited for old card to detach. Trustpilot reports profile merges. ◈ Sample is global and multi-product.

- 2026-11-10: live logged-off browser, exact-domain Trustpilot profiles tryskult.com and sproos.co. All 19 TrySkult reviews coded with IDs; sproos.co had no reviews. Distinct skult.com profile not merged.

- 2026-11-10: live logged-off Trustpilot Ancestral Cosmetics exact-domain profile and 1–3-star filters; all 13 low-star review IDs coded, 92 total at time read.
- 2026-11-10: logged-off in-app-browser US active Meta searches `waterless diffuser` (~670) and refined `waterless home diffuser` (~390). Both first-20 conservative K2 checks below 80%; record the noisy searches but do not treat their totals as the size of the target category. See KEYWORD_CARDS.md for numerators and exclusions.

- 2026-11-10: live logged-off Meta work insoles category search; collected visible positions 21–29 including one off-target shoe and one without offsite link. Clicking See more did not load further cards; not retried. Destinations were read from visible Meta links, final redirects not followed.

- 2026-11-10: live logged-off Trustpilot Everstride: 200 unique cards across ten pages, 13 low-star IDs coded. Page-transition timeouts required checking the loaded first review before saving; duplicates were excluded. Exact-domain Scentify Home and Terra Lotus had zero reviews; Babe Original had two.

- 2026-11-10: live logged-off Trustpilot exact-domain checks borboleta.com and luxe.com returned zero reviews; luxe.com is categorized by Trustpilot as valet parking, identity with intended beauty business not established.

- 2026-11-10: live logged-off Made-in-China supplier listing https://cupabear.en.made-in-china.com/product/NmWYAPQxqsVH/China-Wholesale-Natural-Cat-Chew-Catnip-Silvervine-Wooden-Stick-Molar-Interactive-Cat-Toy.html; USD tiers, customization and caveats recorded in cogs.csv. Second product page https://www.made-in-china.com/showroom/449a126ba7addd05/product-detailoRFYzIDuAcVN/China-Natural-Silvervine-Cat-Toy-with-Feather-Catnip-Wood-Stick-Wrapped-with-Jute-Rope.html timed out in browser; search copy last month, not counted as current listing.

- 2026-11-10: live Made-in-China Shandong Super Pet listing https://isuperpet.en.made-in-china.com/product/FwdGoaBOcVUZ/China-Safe-Long-Silvervine-Corn-Feathers-Cat-Teaser-Toy.html; retained prices with explicit product/packaging ambiguity. The search result https://www.made-in-china.com/video-channel/houeware01_wEOYhptkvTUa_Wholesale-Silvervine-Natural-Teeth-Cleaning-Stick-Cat-Interactive-Chew-Toy.html redirected to generic video-channel landing, so historical search-cache prices were not recorded as live.

- 2026-11-10: public Made-in-China rodent pouch listing https://www.made-in-china.com/price/prodetail_Chemical-Pest-Control_uPrpndRATJcD.html was slow and initial navigation timed out, then rendered without retry; USD price tiers and unit uncertainty kept in cogs.csv. Closed agent-created tabs after use at user request.

- 2026-11-10: public Verisign RDAP via logged-off browser: herbneden.com, honeyglownewyork.com, diablocosmetics.com, facelove-cosmetics.com, houseofduaa.com, hotelcollection.com and cphgrooming.com registrations read. Added earlier directly observed try-kaori.com registration to its store row. Other age checks not completed; no brand-age classification inferred from domain alone.

- 2026-11-10: Meta US active identity query https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=tryskult.com&search_type=keyword_unordered displayed ~870 keyword results and 12 initial Tryskult chin-wrap cards with common visible copy; records added to meta_ads.csv and leader_claims.csv. Count is keyword result, not verified total of a single advertiser; sample is not ten longest, and video/audio was not reviewed. Tab closed after collection.

- 2026-11-10: public TrySkult product page https://tryskult.com/products/sculpting-face-wrap?currency=USD and https://tryskult.com/pages/subscription-policy read in built-in browser. One Time Purchase link unexpectedly added two items to empty session cart at $44.99; both removed and empty state verified; no purchase. Product page says cancel anytime whereas policy specifies two-cycle minimum. Browser tab closed.

- 2026-11-10: transcribed earlier live-browser Stepprs and OrthoFlexx product and Meta domain observations from INSOLES_2026-11-10.md into store_facts.csv and meta_stores.csv; preserve unknowns and do not equate domain-keyword counts with store-owned advertising.

- 2026-11-10: live logged-off Trustpilot smooche.com profile: 200 unique most-recent cards, 18 low-star manually coded; Trustpilot rating hidden with guideline-breach notice. Exact-domain goda.co page displayed connection verification and was not bypassed. Both browser tabs closed.

- 2026-11-11: acceptance review identified wrong Mirai 200-review date range. Removed incorrect range and retained theme coding; original 200 IDs were not retained, so exact original endpoints remain unknown pending reconstruction. A new 200-review pull would be a different snapshot, not proof of the old endpoints.
