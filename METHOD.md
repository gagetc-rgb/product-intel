# Method log: how we confirm demand from indirect signals

Living document. Started 2026-11-07. **The evaluation method itself (3 questions + fit gate, life-cycle stages, channel-absence rule) is in `EVALUATION_METHOD.md`; visual: `evaluation-method.html`.** Product verdicts live in `CONCLUSIONS.md`; this file records **how** we get evidence and **what we learned about the method itself**.

Rules:
- Every source we try gets a row in the Source log with a date and a verdict, including failures.
- Every insight about the method goes in the Insights ledger with its evidence and a confidence mark: ◆ confirmed / ◈ likely / ◇ disputed.
- Free sources first. Paid APIs only when a free one is proven too weak for a specific signal; record which signal the payment buys.
- Retrospective data beats waiting: prefer sources with history over weekly re-checks.

## 1. Signal catalogue

All demand metrics we have are indirect. Each one is a proxy with known failure modes.

| Signal | What it suggests | Free way to get it | Paid upgrade | Status | Failure modes |
|---|---|---|---|---|---|
| Ad age (Meta Ad Library, ads running 90+/180+ days) | Advertiser keeps paying → ads are profitable | Ad Library UI, filter by start date | Ad Library API / archive tools | ◆ used, core filter | Brand may run ads at a loss for branding; misses TikTok/Amazon sellers |
| Active ad count | Testing intensity, not success | Ad Library UI | same | ◆ used | High counts can be spam/clone volume (Skult: 870 ads, ~16K visits) |
| Site traffic + trend | Ads convert into visits; growth vs fade | adlibraryspy (SimilarWeb data), Hypestat | Similarweb / Semrush paid (multi-year monthly history, countries) | ◈ used, single source | Weak under ~50K visits; traffic split across landers/checkout domains |
| Traffic by country | Which markets are actually bought | adlibraryspy, Hypestat | Similarweb paid | ◇ sources disagree (see log) | Free estimates differ by 2× on share |
| Brand search | Organic pull and returning buyers | Google Trends (5-year history) | Semrush / Ahrefs keyword volumes | ◆ used | Naturally low for impulse DTC products |
| Category search | Market size and seasonality | Google Trends | keyword tools | ◆ used | Judged off-season = wrong answer for seasonal goods |
| Review curve (reviews per month over time) | Proxy for order volume and its trend | Store review widgets (Judge.me, Okendo, Loox) with dates; Trustpilot dates; Wayback snapshots of review counts | Keepa (Amazon review/rank history) | ◇ not yet tested | Review gating, imported/fake reviews, incentive campaigns |
| Price/offer history | Is the offer stable (= working) | Wayback Machine snapshots | none needed | ◇ not yet tested | Sparse snapshots for small stores |
| Customer economics (AOV, repeat) | Whether one buyer pays for acquisition | Store pages, offers, subscriptions | none | ◈ used, assumptions | Conversion 2-3% and 35% repeat share are guesses |
| Complaints (Trustpilot, Reddit, BBB) | Refunds/chargebacks risk; product fails its claims | Manual reading | none | ◈ used ad hoc | Loud minority |

## 2. Source log

| Date | Source | Used for | Result | Verdict |
|---|---|---|---|---|
| 2026-11-07 | Meta Ad Library (US, active, by landing domain, start-date filters) | Ad age 90+/180+ | Worked; 180+ filter separated established products from spikes | ◆ keep, core |
| 2026-11-07 | adlibraryspy.com store pages | SimilarWeb monthly visits Jun-Sep, countries | Worked earlier the same day; later blocked by Cloudflare (403) in the in-app browser | ◈ useful but unreliable access |
| 2026-11-07 | Google Trends | Brand and category search | Worked | ◆ keep |
| 2026-11-07 | similarweb.com public page via fetch | Traffic, countries | Content could not be extracted | ◇ not usable via fetch |
| 2026-11-07 | hypestat.com | Second traffic source, countries | Worked: try-kaori.com 71% US (Jun-Jul) vs 34% US in our Sep adlibraryspy snapshot | ◈ usable as cross-check; quality unknown |
| 2026-11-07 | Store page fetch (keenable, live) | Offers, prices, claims | Worked for try-kaori.com; in-app browser navigation was denied | ◆ keep for claims/offers |
| 2026-11-07 | Web search (keenable) | Competitor claims, press, science | Worked; found HuffPost coverage, Amazon listings, a critical review of the nonenal evidence | ◆ keep |
| 2026-11-07 | YouTuber revenue claims (Daily Ecommerce corpus) | Revenue | Inflated ~2× to 400× vs our sanity band | ◆ do not use as data, only as leads |
| 2026-11-07 | Loox public widget `loox.io/widget/<clientId>/reviews/<productId>?limit=40&page=N` | Full dated review history | Works without auth. clientId comes from `loox.io/widget/loox.js?shop=<x>.myshopify.com` (`LOOX.clientId`); productId from `/products/<handle>.js`. limit>40 breaks. Order is "featured", not by date, so you need the full set. ~200 reviews/min | ◆ best free review-curve source (script: `work/reviews/loox_curve.sh`) |
| 2026-11-07 | Judge.me public API | Review history | Needs the shop's API token; the public widget did not expose it | ◇ not free; try the Judge.me Reviews site or a paid tool later |
| 2026-11-07 | Shopify stores via curl (products.json, HTML) | Products, apps, shop id | Worked for a while, then Shopify bot check ("Verifying your connection") after ~20 requests. keenable fetch still gets products.json | ◈ use sparingly; fall back to keenable or Wayback |
| 2026-11-07 | Trustpilot in the in-app browser (`__NEXT_DATA__` via JS) | Dated reviews, star distribution | Works, but without login only the latest ~200 reviews (2-3 months). Direct curl gets 403 | ◈ good for the recent pace and 1-2★ share, not for history |
| 2026-11-07 | Wayback CDX + snapshots of Trustpilot pages | Historical review counts | Works; few snapshots per year for small brands | ◆ cheap retrospective point checks |
| 2026-11-07 | Meta Ad Library, "all words" search + start-date max (180+ days) | Angle scan inside a category | Works via URL params `search_type=keyword_unordered`, `start_date[max]`. Needs a ~4 s wait before reading "~N results" | ◆ keep for angle scans |
| 2026-11-07 | Google Trends (in-app browser) | Category/brand search | "Oops! Something went wrong" (rate limit) | ◇ retry later or use another route |
| 2026-11-07 | Amazon US search, headless Playwright (`work/blind/amz_scan.py`) | "bought in past month" badges + review counts, top-20 organic | Works without login (~124 queries, 1 timeout). Search drifts off-target, so filter titles per product | ◆ best free category sales proxy |
| 2026-11-07 | TikTok Shop keyword pages `shop.tiktok.com/us/k/<kw>` via keenable cache | Lifetime "sold" per product | Direct access hits a puzzle captcha; keenable cache works; ~25% of slugs missing | ◈ good for TikTok-native products; lifetime, cache date unknown |
| 2026-11-07 | Amazon top-20 snapshot → newcomer openness (`work/blind/openness.py`) | Share of units held by listings under 500 reviews; newcomers with a badge ÷ all newcomers | Works from the existing scan; separates open categories (magnesium spray 41%, diffuser 27%) from closed ones (socks, rosemary, hair-removal 0%) | ◈ keep; "under 500 reviews" is a proxy for age |
| 2026-11-07 | Amazon "Date First Available" per brand (`work/blind/graveyard_amz.py`) | Newcomer survival by entry cohort | Done for magnesium spray (12-24 mo cohort: 4 of 7 brands at 100+/mo, 1 of 7 at 1K+); later runs failed with ERR_NETWORK_ACCESS_DENIED | ◇ promising, access unreliable; report the 1K+ bar, 100+/mo is too low to mean success (superseded by the next row: access fixed) |
| 2026-11-07 | Meta Ad Library "exact phrase" category search | Category ad volume and 180+ day ads | Matches med-spas, salons, clinics, car dealers and unrelated ads for generic phrases | ◇ noisy at category level; use per landing domain instead |
| 2026-11-07 | Amazon graveyard: search pages 1-5 + product pages, brand + Date First Available / ASIN-estimated date | Newcomer brand survival by entry cohort | Works with click pagination (URL paging blocked after a few requests); Health & Household hides the date, ASIN order estimates it (±1-2 mo); Playwright fails when run as a background task (network denied), run in foreground | ◆ keep: survivorship-light openness (`work/blind/GRAVEYARD.md`) |
| 2026-11-07 | Graveyard weak-brand check: brands with no badge after 12-24 months, looked up on the web | Is "no Amazon sales" a failure or another channel? | 10 brands checked: ~2 Amazon-native failures, ~6 older or multi-channel brands (own site, Meta ads, retail), 1 hobby; listing age ≠ brand age | ◈ survival must be split into Amazon-native vs multi-channel before it is a decision input (`work/blind/GRAVEYARD.md`) |
| 2026-11-07 | Amazon review history for cohort brands: /product-reviews/ page; Keepa public graph image (graph.keepa.com/pricehistory.png) | Review curve per Amazon listing | Reviews page redirects to sign-in when logged off; Keepa public graph shows price only (no sales rank, no review count) | ◆ no free route for Amazon review curves; options: Keepa data access (paid) or a logged-in browser (ToS risk); own-site widgets (Judge.me, Loox, Okendo) stay free for multi-channel brands |
| 2026-11-07 | Cohort cross-channel check (`work/blind/cohort/`): brand site by domain guessing + web search, RDAP registration, first Wayback capture, Judge.me public profile | Is an Amazon newcomer Amazon-native or an older multi-channel brand; brand age | Works: 94 brands classified in ~15 min. Judge.me public profile (judge.me/reviews/stores/<shop>.myshopify.com?format=json) gives total reviews and 'collecting since' without a token; per-review dates need the widget API, which our permission classifier blocked; Trustpilot returns 403 to scripts | ◆ keep; review curves for DTC brands still need a route (rendered page in a browser, or owner's OK for the widget API) |
| 2026-11-07 | Cohort brands on Meta + review curves (`work/blind/cohort/meta_brands.py`, `meta_join.py`; `work/reviews/loox_shop.py`) | Do Amazon newcomers with own stores run Meta ads, how long; do their reviews grow | Meta by domain finds little (domains are rarely in ad text); by brand name works but needs namesake removal by hand. Loox shop-wide widget `loox.io/widget/<wid>/reviews?limit=100&page=P` returns ~20 reviews per call while paging by 100, giving a ~20% systematic sample of all reviews. Curves can break on review-app switches (LivaClean). Trustpilot via Wayback: nothing archived for small brands. adlibraryspy.com blocked our IP after a headless request (Cloudflare); hypestat shows a bot check | ◆ keep Meta-by-name and Loox; ◈ traffic needs another route (owner's Similarweb/Semrush login or retry later in the browser only) |

## 3. Insights ledger (method)

1. ◆ **Ad age matters more than ad count.** "Oldest ad in the top 30" was misleading; counting ads aged 180+ days works. Evidence: Everstride 190 aged ads + stable traffic vs Sofyre with all ads under 90 days.
2. ◆ **Ad count without traffic is a trap.** Skult (870 ads, ~16K visits) and MLMT (238 ads, ~11K visits).
3. ◆ **Guru-sourced revenue numbers are not data.** Inflated 2× to 400×.
4. ◆ **Price assumptions must come from the real leader's store, not from clones.**
5. ◈ **Free traffic sources disagree on geography by up to 2×** (Kaori: 34% vs 71% US). Any country-level decision needs a second source or a paid one.
6. ◈ **Retrospective sources make weekly tracking mostly unnecessary.** Ad start dates, Trends history, Wayback snapshots and paid traffic history already show the past; weekly tracking is only for brand-new spikes.
7. ◇ **Claims are a positioning lever.** In the persimmon niche the leader (Mirai Clinical) claims "97% nonenal removal"; the public evidence is weak (a 2001 Shiseido study on 22 people, a 2012 trial on 20 men). An honest-claims angle may differentiate, untested.
8. ◆ **The review curve confirms the traffic curve.** Earthly Derm: Loox reviews per month rose Mar → Sep 2026 (209 → 957) in step with SimilarWeb traffic. Two independent free signals agreeing is our strongest demand evidence so far.
9. ◈ **Aged-share by angle shows which angles are proven and which are open.** Within one category, compare "active ads" with "ads aged 180+ days" per angle keyword: near-baseline share = proven angle; high activity with near-zero aged ads = tried but not cracked (or failing).
10. ◈ **Trustpilot 1-2★ share is a cheap quality red flag.** Menvault 9.5% vs Kaori 2.0% and Everstride 5.6%.
11. ◆ **Free sources hit rate limits fast** (Shopify bot check, Trustpilot 403, Google Trends). Spread requests over time and keep several routes (curl, keenable, in-app browser, Wayback).

12. ◆ **Brand success ≠ category demand.** Earthly Derm grew fast, but the turmeric-soap category ranks ~60 of 94 on Amazon+TikTok+Meta; rank products at category level as well as by leader brand (`work/blind/BLIND_PASS.md`).
13. ◆ **Meta-only screening misses TikTok/Amazon-native hits** (Cyperus hair inhibitor 597K sold on TikTok with 0 aged Meta ads; teeth-whitening powder, pore patches, lymphatic contour brush).

14. ◆ **Review-count proxies for "newcomers" mislead; date + brand cohorts reverse them.** Magnesium spray looked most open (41% of top-20 units on listings with <500 reviews) but at brand level brands older than 2 years hold 81% of units; turmeric soap looked closed (4%) but brands that entered 12-24 months ago hold 41%. Source: `work/blind/GRAVEYARD.md`.

15. ◆ **Indonesia (2026-11-08): no single "Daily Ecommerce"-style analyst found; use the data sources directly** (Kalodata ID monthly posts, FastMoss ID, Magpie IQ, Cube, Compas, Involve Asia top-30). Panels disagree on TikTok Shop beauty growth (FastMoss +34% YoY vs Magpie -10% Jan-May 2026). Plan: `work/indonesia/ID_CREATOR_PLAN.md`.
16. ◆ **Indonesia: repeat buying looks like cheap consumables re-bought, not device + refill.** Involve Asia ID top-30 by real conversions has no device+refill item; "BPOM" in titles is a selling point. Free ID sales data is thin (FastMoss top-10 without login); a real pass needs a FastMoss/Kalodata login. Details: `work/indonesia/METHOD_AD.md`.

## 4. Backlog: methods to test next (free first)

1. ~~Review curve from Shopify review widgets~~: done for Earthly Derm and Everstride (Loox; a partial sample in Loox's featured order was badly biased, so always pull the full set; the last 4-6 weeks undercount because of review-request lag); Kaori has no review widget (Trustpilot only); Menvault uses Judge.me (blocked). Results: `work/reviews/RESULTS.md`.
2. **Wayback Machine** snapshots of leader stores: review-count growth and offer/price stability over 6-24 months.
3. **Second free traffic source** for every take (Hypestat now; find one more) to bound the SimilarWeb error.
4. **Amazon presence check** (listings, review counts, BSR = Best Sellers Rank) to cover the Amazon blind spot; Keepa later if needed.
5. **TikTok Creative Center / TikTok Shop** visibility to cover the TikTok blind spot.
6. **Ad Library angle scan:** for compression socks, count ads and ad age per angle (wide calf, nurses, men's dress, seniors, travel, pregnancy) to find under-served angles.

7. **From the open-methods review (2026-11-08, `research/OPEN_METHODS_REVIEW.md`), not yet tried:** Amazon Product Opportunity Explorer (first-party units, search growth, new vs successful launches; needs Professional seller account); Shop app "bought in past month" badge (DTC volume floor); ImportYeti import curves + factory lookup; Meta Ad Library EU/UK reach and 1-year retention of stopped ads (spend range + dropout-inclusive survival); smoke test / charge-later pre-orders as a "Test" stage with pre-written kill thresholds; 1-star share and brand-level top-3 share / HHI in crowding.

Paid candidates (only after free methods are evaluated): Similarweb/Semrush traffic history, Keepa, an ad-archive tool. Prices are tracked in `research/APIS.md`.
