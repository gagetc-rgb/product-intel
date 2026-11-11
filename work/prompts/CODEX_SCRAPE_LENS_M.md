# Task for Codex: public data for lens M ("copy the leader's store and scale it with ads")

Written 2026-11-10. Method: `METRICS.md`, section "v2.4" (metrics M1-M8). Read it first; it is the instruction. First reading and its gaps: `work/lensm/M2_RESULT.md`, `work/lensm/M8_RESULT.md`, `work/lensm/m2_stores.csv`.

## Rules

- Public, logged-off pages only. Never bypass a captcha, login wall or bot check. If a source blocks you, write "blocked", the date and the URL, and go on.
- No Amazon in this task.
- Never invent a number or a name. Unknown = "unknown" plus the reason.
- Every value gets its source URL, the date read, and a mark: ◆ read from the platform or registry · ◈ your reading · ◇ estimate.
- Search by identity, not by words, wherever possible: Meta by landing domain, reviews by store (rule K3 in `METRICS.md`).
- Before any phrase search write the keyword card (K1) and record the on-target share of what the phrase returns (K2). Under 80%: change the phrase or filter.
- US view: prices must be read in USD with a US delivery country. The first pass saw IDR prices; set the store's country selector or use `?currency=USD`, and record which.
- Pace requests. Shopify returned 429 on `products.json` for 117 of 161 stores in the first pass: use a real browser session, one store at a time, and do not retry more than once.
- All files in English, under `work/lensm/codex/`. Do not edit `METRICS.md`, `HANDOFF.md`, `work/site/` or `site/`. Do not commit.

## Products, by priority

1. Tallow balm, persimmon soap, turmeric soap, body oil (firming / crepey), color-changing foundation.
2. Lash serum, chin wrap (V-line mask), scent diffuser (waterless), hair growth serum, compression socks.
3. The remaining 10 of the 20 (`work/site/ru.json`, key `name`): task A only.

### Additional products (added 2026-11-10 after the repeat-purchase scan, `research/REPEAT_PURCHASE_SCAN_2026-11-10.md`)

Treat as priority 1 for tasks A-D; they are outside the current 20, so write their keyword cards first:

- Collagen overnight wrapping mask (face; not the chin wrap). Likely leaders are K-beauty brands: record brand age carefully.
- Work insoles / cushioned insoles for people on their feet all day. Check these two stores by domain first and report whether they exist and what they run: Stepprs, OrthoFlexx (named by an outside study, unverified).
- Enzyme pet odor remover sold as a device plus refills (fogger or sprayer with enzyme cartridges).
- Silvervine / matatabi cat dental chew sticks.
- Natural rodent repellent pouches. Also record every claim on the leader's page and whether the page shows an EPA or state registration statement.

For every store of these five, task B must also answer the repeat-purchase questions in full: refill or subscription SKU, its price, whether subscription is pre-selected, the stated refill interval.

## A. Meta Ad Library, US, active ads (M1, M2, M7; baseline for M3)

The first pass used one generic phrase and about 60 ads per category; a third to a half of them had no landing domain and a third of the stores were noise.

A1. Per product: 3-5 product phrasings (take them from `work/audit/KEYWORD_AUDIT_2026-11-10.md` and `work/audit/trends_terms.json`; no symptoms or body features). For each phrasing record Meta's own "~N results" for: all active; started before today−30; before today−90; before today−180.

A2. Per product collect at least 200 ads, spread evenly over four age windows (under 30 days, 30-89, 90-179, 180+). Per ad: library ID, page name, start date, the "N ads use this creative" count, format (image / video / carousel), the landing URL after redirects, the registrable landing domain. An ad with no visible link: open the ad's detail view; if still none, keep the page name and mark "no domain".

A3. Group by store (registrable domain; persona, creator and quiz/offer subdomains that land on one shop count once). For every store that sells the product (see B), run the library search **by its domain** and record: active ads, and how many started before today−30 / −90 / −180. This is the store's own count, not the sample's.

A4. Output `meta_ads.csv` (one row per ad) and `meta_stores.csv` (one row per store × product: active, 30+, 90+, 180+, oldest ad date, pages used, date collected). Keep the exact search URLs: the same searches are repeated on 2026-12-08 to see which stores stopped (M3).

## B. Store facts (M2, M4, M5)

For every store in `meta_stores.csv`, plus the 54 "unclear" and 49 "sells" rows of `work/lensm/m2_stores.csv`:

- sells the product form of the category: yes / no / unclear, with the product page URL;
- price of one unit in USD; every bundle on the page with its price ("3 bars $39", "buy 2 get 1"); which bundle is pre-selected;
- subscription or refill: offered or not, discount, default on or off, how to cancel as stated;
- shipping: cost, free-shipping threshold, stated delivery time, where it ships from if stated;
- returns and guarantee as stated;
- review app on the page (Loox, Judge.me, Yotpo, Stamped, Junip, Okendo) and the total review count shown.

Output `store_facts.csv`.

## C. Store age (M2)

For every selling store: domain registration date (RDAP; for .co, .us, .store, .shop use the registry's own WHOIS when rdap.org has no answer); first Wayback capture; date of the oldest review in the store widget; creation date of the Facebook page from its Page Transparency panel; Shopify `created_at` of the oldest product if readable. Class: young (earliest evidence on or after 2024-11-10) / old / unclear, with the reason. A domain older than its first capture and its products by more than two years = "unclear: possibly a bought domain"; do not guess.

Output: columns added to `store_facts.csv`.

## D. What buyers complain about at the leader (M8)

Leaders: try-kaori.com, miraiclinical.com, earthlyderm.com, goda.co, smooche.com, primeprometics.com, luxe.com, terralotus.shop, ancestralcosmetics.com, borboleta.com, babeoriginal.com, sproos.co, scentifyhome.com, everstridesocks.com, tryskult.com, plus any store that task A shows as the largest advertiser of a priority-1 product.

- Trustpilot (returned 403 to plain requests in the first pass: use a real browser; logged-off it shows the latest ~200 reviews): TrustScore, total, and for the latest 200 the count by stars with dates.
- The 1-3★ reviews you can read (Trustpilot, the store widget, Better Business Bureau, Reddit threads that name the store): sort each into product itself / shipping and delivery / billing and subscription / support and refunds / "does not work". Give counts per theme and three short paraphrases per theme (no quote longer than 12 words).
- Store widgets that show almost no low reviews (first pass: Smooche 0.05%, GODA 0.1%) are curated: record the number, mark it ◇, and do not use it as a quality measure.

Output `leader_complaints.csv` and `LEADER_COMPLAINTS.md` (one short section per leader: what is fixable by a follower and what is not).

## E. What the leader's ads promise (M6)

For each leader in D: its 10 longest-running active ads. Per ad: start date, format, the hook (first line or first 3 seconds, paraphrased), every claim about the result, the offer, the landing page type (product page / advertorial / quiz). Mark each claim: cosmetic look claim / treatment or growth claim / testimonial or before-after / authority figure ("doctor", "dermatologist"). Do not judge legality; only classify. Output `leader_claims.csv`.

## F. Cost of goods and shipping for priority-1 products (M4)

- Supplier listings on Alibaba, Made-in-China and 1688 for the format the leader sells: price range at MOQ 500 and 5,000, MOQ, private-label option, lead time. At least 5 listings per product, with URLs. Listing prices are ◈, not quotes.
- Shipping one order to a US buyer: published rate cards of two US 3PLs or USPS Ground Advantage for the product's weight and size.
- Output `cogs.csv`.

## G. Optional, only if A-F are done: EU/UK library

The EU/UK Ad Library keeps stopped ads for about a year. For stores from A that also deliver ads in the UK or EU: stores whose first ad started 6-12 months ago, and the share of them that had any ad running 90+ days. This is the only survival rate that includes the dead. Output `eu_uk_cohort.csv`.

## Hand-in

`work/lensm/codex/`: the CSV files above; `METHOD_LOG.md` (every source tried, date, result, kept or dead end, including failures); `KEYWORD_CARDS.md` (K1, written before the pulls); the scripts. Start your report with three lists: what was not done and why; what could not be read; where you deviated from this task.

Acceptance: we take 10 random rows and open their source URLs. If a value cannot be found at its source, the file is not accepted.
