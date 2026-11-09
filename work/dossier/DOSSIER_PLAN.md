# Category dossier — plan (2026-11-08)

Goal: one page per category (20) that reads as a story — numbers are the arguments, not a list — plus an index with filters. Top 5 get a deeper "magnifying glass" pass later.
Order of work: **collect and verify all data → freeze → write texts → build HTML last.** No HTML until the data is frozen.

- All measured facts so far, per category: `dossier_data.json` (rebuilt by `build_dossier.py` from the raw outputs; nothing typed by hand).
- What each category is missing: `gaps.json`.
- Method and rules: `/RUNBOOK.md` (v2.0). Verdict table: `work/blind/FINAL_V2.md`.

## 1. Story template (every category page)

Each section answers one question. Every number in it carries a tier mark (◆ counted by a platform, ◈ estimate, ◇ disputed) and a link to the method/source, so that a suspicious number can be traced to the step that produced it.

| # | Section | Question it answers | Infographic | Data (source) |
|---|---|---|---|---|
| 0 | Header | What is it, verdict in one line | product photo, status badge, 4 key numbers | photo (B8), FINAL_V2 |
| 1 | The product and the buyer | What problem it solves, for whom, at what price | — | top listing titles, leader landing pages, price (B3) |
| 2 | How big, and where it is going | Is demand large, is it growing, is it seasonal | 5-year search curve with the Apr-Jun 2026 Google artifact marked; Amazon units/mo | Trends weekly series (B1), Amazon shelf units ◆ |
| 3 | Who holds the market | Old brands vs new brands vs generics | stacked bar: units by brand entry age (0-6 / 6-12 / 12-24 / 24+ months); top-brands table with photos | `amazon.units_by_brand_entry`, `units_by_kind`, `top_brands` |
| 4 | Can a newcomer get in | How many new brands reached 1K+/mo; is it a brand market or a price war | winners list with entry month; brands-vs-generics split | `amazon.win_brand`, `generic_units`, GRAVEYARD cohort |
| 5 | What happens in ads | How many ads run, how many live 1 / 3 / 6 months, who keeps ads alive | bars: active / 30d+ / 90d+ / 180d+; shops with long-lived ads | `meta_category` (+30d, B2), `meta_brands` (B4) |
| 6 | Do the winners keep growing | Are leaders' sales rising or fading | monthly reviews curve per leader | reviews (B6, owner via GPT) |
| 7 | What the winners say | Which angles and offers survive 90-180 days | 3-6 long-running creatives | `work/ads/longrunning.json` (B5) |
| 8 | Risks and open questions | What could make this wrong | — | data notes, compliance flag, trend label |
| 9 | Verdict and what would change it | Rank and the pre-registered kill rules | — | FINAL_V2, RUNBOOK rules 5-6 |
| 10 | Methods and sources | How each number was made; how to check it by hand in 5 minutes | — | RUNBOOK, script names, Ad Library / Amazon URLs |

Index page filters: status (top 5 / reserve / weak / dropped / not measured), best channel (Amazon / own store + Meta / both), trend (growing / flat / falling), price band, units taken by new brands, compliance flag.

## 2. What we have now (from `gaps.json`)

| # | Category | Status | Amazon | Meta category | Meta brands | Trend | Price | TikTok (cached) | Photos | Reviews/mo | Creatives |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Color-changing foundation | top 5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | — | — |
| 2 | Body oil (crepey skin) | top 5 | ✅ | ✅ | ✅ | ✅ | — | ✅ | — | — | — |
| 3 | Waterless scent diffuser | top 5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | — | — |
| 4 | Beef tallow balm | top 5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | — | — |
| 5 | Persimmon soap | top 5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | — | ✅ (Kaori) |
| 6 | Filtered shower head | reserve | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | — | — |
| 7 | Neck firming cream | data issue | ⚠️ filter leak | ✅ | — | ✅ | ✅ | ✅ | — | — | — |
| 8 | Rosemary hair oil | dropped | ✅ | ✅ | — | ✅ | ✅ | ✅ | — | — | — |
| 9 | Turmeric soap | dropped | ✅ | ✅ | — | ✅ | ✅ | ✅ | — | — | ✅ (Earthly Derm) |
| 10-17 | Fountain, chin wrap, pore patch, towel, magnesium, hair removal, socks, whitening | weak on Amazon | ✅ | — | — | — | partly | ✅ | — | — | socks ✅ |
| 18-20 | Lash serum, hair serum, pre-wash oil | not measured | — | — | — | — | partly | ✅ | — | — | — |

Ready to write now: sections 2-5 and 8-10 for categories 1-9 (except photos, the 30-day ad bar and the weekly trend curve, which need B1-B3).

## 3. Collection plan (phase B), in order

Order changed after the plan review (section 6): B7 definitions are frozen **before** the Amazon re-scan, so the new scan is read once under one version.

| Step | What | How (same method for all 20) | Time | Risk |
|---|---|---|---|---|
| B7 (first) | Freeze v2.1 definitions: neck-cream filter, GEN words (retinol, pdrn, collagen), "The AirScent" brand | edit `graveyard_def.py` / `graveyard_stats2.py`, bump RUNBOOK version, keep v2.0 copy | ~20 min | — |
| B1 | Full weekly Google Trends series for all 20 + 2 controls, **3 pulls on 3 different days** (Google re-samples at midnight UTC; same-day pulls are cached copies), averaged; report the spread of rel_yoy between pulls | in-app browser, read the chart's data table; save every pull to `trends_series.json` | ~30 min/day × 3 | Trends rate limit; niche terms (persimmon, waterless diffuser) are the noisiest |
| B2 | Meta category counts for the 11 missing + a new "30 days+" count for all 20 | `meta_ages.py` (add 30-day window) | ~25 min | none seen so far |
| B3 | Amazon re-scan with a **US delivery ZIP** (not "Indonesia"): price in USD, main image URL, rating; plus the 3 unmeasured categories. If units/ranking differ materially from the first scan, re-scan **all 20** and the US scan replaces v2.0 numbers | `graveyard_search.py` + ZIP setting; compare units with the first scan | ~60 min (all 20: ~3 h) | bot wall → stop, no bypass |
| B4 | Brand-level Meta for the top 3 brands of every category, **scoped to the brand's Page ID** (keyword search matches ad text and pulls in other advertisers); keep the phrase count only as a second column | `meta_brands.py` + page-id URL (`view_all_page_id=`) | ~40 min | brands with several Pages: sum them, list each |
| B5 | Long-running creatives (180d+) for top-5 leaders | `work/ads/fetch_longrunning.py` | ~20 min | — |
| B6 | Monthly reviews for 16 leader stores | owner, GPT computer use: `work/blind/REVIEW_TASK_GPT.md` | owner | dates may be relative or missing |
| B8 | Photos: top listing image per leading brand (from B3) + leader store product image | image URLs only, internal use | with B3 | — |
| B9 (new) | Ad survival re-check: save the Library IDs of the sampled ads now, re-open them in ~30 days and count which are still active. Meta keeps no history of stopped commercial ads in the US, so this is the only way to see failures | `meta_ages.py` sample IDs → re-check script | 1 h, in 30 days | none |

Not planned: Similarweb and Hypestat (see section 6 — evidence says they cannot measure stores of our size); TikTok Shop live data (captcha; cached lifetime "sold" counts stay ◈).

## 4. Known errata fixed or pending before publishing

- Fixed 2026-11-08: Forge (tallow) entered Amazon ~31 months ago — older entrant, not a new brand (FINAL_V2 corrected).
- Pending B7: neck cream numbers invalid; diffuser new-brand units understated (AirScent counted as generic).
- Pending B3: Amazon showed "Deliver to Indonesia" during all scans — ranking may differ from a US shopper's view; prices were in IDR.

## 6. Plan review against published evidence (2026-11-08)

What independent sources say about each signal, and what it changes for us.

**Traffic estimators (Similarweb, Hypestat) — dropped.**
- Similarweb itself: shows nothing below 5,000 visits/month and is "more confident" only above 100,000 ([support: vs direct measurement](https://support.similarweb.com/hc/en-us/articles/360002329778-Similarweb-vs-Direct-Measurement), [data accuracy](https://support.similarweb.com/hc/en-us/articles/360002219177-Similarweb-s-Data-Accuracy)).
- Omniconvert, 1,787 e-commerce sites vs Google Analytics: sessions over-reported ~94%; 10K-100K sessions "unreliable", under 10K worst ([source](https://omniconvert.com/blog/we-analyzed-1787-ecommerce-websites-similarweb-google-analytics-thats-we-learned)).
- PLOS ONE, 86 large sites (median 7.8M visits): visits 19% low, but site ranking correlates well ([Jansen et al. 2022](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0268212)). Error direction flips between studies; typical error ~50% (Ahrefs 2022, Promodo 2024, summarised [here](https://launchranked.com/blog/how-accurate-is-similarweb)).
- Hypestat re-displays Semrush/Similarweb numbers next to its own model ([example page](https://hypestat.com/info/google.com)); one owner's check found its figures at 31-71% of actual ([forum](https://forum.entropiauniverse.com/t/interesting-info-about-this-forum/250902)).
- Our leader stores are mostly 25K-160K visits/month (Hypestat ◇), i.e. inside the band where these tools are least reliable. Only GODA (~2M) is in the reliable band, and its size is already proven by 23,956 reviews. Verdict: no decision depends on traffic; not collected.

**Meta ad longevity — keep, with three corrections.**
- Practitioners agree run time is the best free proxy, and also list why it fails: forgotten low-budget ads, retargeting/catalog ads, big-brand awareness ads; a relaunched ad gets a new ID and date ([Mockingbird](https://mockingbird.digital/blog/how-long-has-a-facebook-ad-been-running), [Showfolk](https://showfolk.ai/blog/which-competitor-ads-are-working), [Phil Graham](https://philgrahamdigital.com/podcasting/ep-477-the-facebook-ad-library-trap-why-competitor-research-can-mislead-you)). → Weight long runs from small direct-response brands more than from big brands; read the CTA.
- Keyword search matches ad text, not the advertiser; a page-scoped search is exact ([Hitmyalgo test](https://hitmyalgo.com/insights/meta-ad-library-page-id-method)). → B4 moves to Page ID.
- The count is ad objects: one creative duplicated across ad sets counts many times ([Klipio](https://klipio.io/blog/is-the-meta-ad-library-accurate)). → Report distinct creatives from the sample next to raw counts.
- Benchmark (vendor sample, ◈): of 4,634 US ads, 6.5% were still running at 30 days and 2.1% at 90 days ([Showfolk citing Adligator](https://showfolk.ai/blog/which-competitor-ads-are-working)). Our "90d+ share" divides by ads active today, not by ads launched, so it is not comparable to that 2.1% — say so on every page.

**Amazon "bought in past month" — keep, read as a floor.**
- It counts unique customers, not units; needs 50+; buckets are floors (1K+ = 1,000-1,999; 2K+ may cover up to 9,999 depending on steps seen); 3-4 day lag ([Amazon support reply in Seller Forums](https://sellercentral.amazon.com/seller-forums/discussions/t/0e83887a-e6f2-4584-85ce-0d8f8143eeaa), [Arbitrage Hero, ~900K badges](https://arbitragehero.com/blog/amazon-sales-estimate-accuracy)). → Our unit sums are lower bounds; the dossier shows floor-to-next-step ranges. Category ranking is unaffected (same bias everywhere).

**Reviews as a sales proxy — keep, growth only.**
- Judge.me: median store turns 3.7% of requested orders into a review, top 10% reach 10%+, and the rate differs by store size ([Judge.me benchmark](https://judge.me/blog/benchmarking-review-collection-rate)). → Absolute review counts can't be compared across stores (3-5× spread); month-over-month growth within one store can.

**Google Trends — keep, pull several times.**
- Each pull is a random sample; noise is largest for low-volume terms; studies average 12-30 pulls ([Eichenauer et al. 2022](https://onlinelibrary.wiley.com/doi/full/10.1111/ecin.13049), [Gummer & Oehrlein 2025](https://journals.sagepub.com/doi/10.1177/08944393241279421)); results are cached for 24 h, new sample after midnight UTC ([arXiv 2504.07032](https://arxiv.org/pdf/2504.07032)). → B1 takes 3 pulls on different days. No public note found on the Apr-Jun 2026 spike; the control-term correction stays.

## 5. Writing rules for the texts

- Each page opens with the answer, then the story: product → demand → who holds it → can we get in → ads → growth → risks → verdict.
- A number appears only to support a sentence; tables and charts carry the rest.
- Every claim gets ◆/◈/◇ and a source link; no number without a file behind it.
- Plain words; acronyms explained once per page.
- What is unknown is said as unknown.

## 7. Phase B status (2026-11-08)

| Step | Status | Output |
|---|---|---|
| B7 v2.1 | done | `graveyard_table.py` → `graveyard/table_v2.1.json` (v2.0 kept as `table_v2.0.json`); RUNBOOK version log |
| B1 Trends | pull 1 of 3 done (all 20 + 2 controls) | `trends_pulls/pull1_2026-11-08.txt`, `trends_calc.py` → `trends_series_summary.json`; pulls 2-3 on 2026-11-09 and 11-10 |
| B2 Meta categories | done, all 20, with 30d+ window | `meta_ages/<pid>.json` |
| B4 Meta brands | done, 22 brands, own Page ID + phrase-sample domain share | `meta_pages.json` |
| B5 creatives | running | `work/ads/longrunning_v2.json` |
| B3 Amazon US ZIP | **stopped at 17/20** — amazon.com showed "Access restricted: continued access by an unauthorized AI agent violates Amazon's Conditions of Use". Not clicked; Claude's automated Amazon access stopped. Owner decision: Amazon stays a primary layer, collected data is kept; missing 4 categories to be gathered by the owner/assistant | `graveyard_us/` (17 categories, collected before the notice) |
| B8 photos | partial: image URLs for 17 categories in `graveyard_us/` | — |
| B9 survival re-check | script ready, run on/after 2026-12-08 | `meta_recheck.py` |

Findings so far:
- Indonesia vs US delivery: new-brand units in the top categories move within ±10% (color foundation 212,600 → 211,800; tallow 48,150 → 45,550; body oil 28,600 → 26,600; diffuser 19,400 → 21,200). Generic units and weak categories move more (compression socks shelf 172K → 67K, 29% listing overlap). Ranking of the top 5 unchanged.
- Method inconsistency found in v2.0: magnesium, towel and turmeric files carry bylines from product pages (pilot), the other 14 use title-only brand detection. Title-only reclassifies some branded listings as generic (magnesium new-brand units 4,550 → 1,650 when bylines are removed; towel 5,100 → 900). So in title-only categories "generic" may include brands whose titles start with a product word; new-brand units are a lower bound there.
