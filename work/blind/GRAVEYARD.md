# Amazon graveyard pilot: newcomer brand survival (2026-11-07)

Why: top-20 "listings with <500 reviews" measured newcomers with survivorship bias and mixed new ASINs of old brands with real new brands. Amazon keeps failed listings live, so failures are visible.

Method (`graveyard_amz.py`, `graveyard_stats.py`): Amazon US search pages 1-5 (click pagination; URL `&page=N` gets blocked), organic on-target listings, each listing opened for brand + "Date First Available". Health & Household pages hide the date, so it is estimated from the ASIN (B0 ASINs are issued in order; calibration on 52 dated listings, in-sample median error 0.1 mo, 80th pct 1.3 mo). Grouped by brand; brand entry = oldest listing. Success = a listing with "bought in past month" ≥100 (weak) or ≥1K (strong).

| Category | Brands seen | Entered 6-24 mo ago | ≥100/mo | ≥1K/mo | Units held by brands entered in last 24 mo |
|---|---|---|---|---|---|
| Exfoliating towel | 134 | 42 | 26 (62%) | 10 (24%) | 39% |
| Turmeric soap bar | 112 | 53 | 24 (45%) | 6 (11%) | 47% |
| Magnesium oil spray | 131 | 60 | 20 (33%) | 6 (10%) | 19% |

Reading:
- Towel is the most open: most newcomers reach sales and a quarter reach 1K+/mo.
- Magnesium spray reverses the top-20 reading (41% "newcomer share"): at brand level, brands older than 2 years hold 81% of units. The top-20 proxy counted new ASINs of old brands as newcomers.
- Turmeric soap reverses the other way: brands that entered 12-24 months ago hold 41% of units; the review-count proxy missed them because they gathered reviews fast.

Limits: pages 1-5 are relevance-ranked, so failures deeper than page 5 are missing → survival rates are upper bounds (comparable between categories, not absolute). Badge = floor of unique buyers. One snapshot. Amazon only; Meta survival needs an ad archive (BigSpy test pending).

## All badge bands, by brand entry cohort — INVALID, v1 data (off-target forms leaked in, brands title-guessed; see v2 below)

(added 2026-11-07, `scratchpad levels.py` logic: same brands as above)

Badge = Amazon "X+ bought in past month", per listing, brand = its best listing; "none" = under 50 or no badge. Monthly revenue at the category median price: magnesium $20 → 100/mo ≈ $2K, 1K/mo ≈ $20K; turmeric $12 → $1.2K / $12K; towel $18 → $1.8K / $18K.

| Category, cohort | Brands | none | 50-99 | 100-199 | 200-499 | 500-999 | 1K-1.9K | 2K+ | Median reviews |
|---|---|---|---|---|---|---|---|---|---|
| Towel 6-12 mo | 25 | 36% | 12% | 16% | 12% | 4% | 12% | 8% | 85 |
| Towel 12-24 mo | 17 | 18% | 6% | 6% | 24% | 18% | 6% | 24% | 1,000 |
| Towel 24+ mo | 85 | 16% | 12% | 8% | 20% | 8% | 11% | 25% | 1,100 |
| Magnesium 6-12 mo | 33 | 64% | 12% | 6% | 6% | 6% | 0% | 6% | 17 |
| Magnesium 12-24 mo | 27 | 52% | 4% | 19% | 7% | 4% | 4% | 11% | 108 |
| Magnesium 24+ mo | 63 | 35% | 17% | 8% | 10% | 5% | 8% | 17% | 850 |
| Turmeric 6-12 mo | 22 | 41% | 18% | 18% | 5% | 5% | 9% | 5% | 30 |
| Turmeric 12-24 mo | 31 | 45% | 6% | 10% | 23% | 6% | 0% | 10% | 205 |
| Turmeric 24+ mo | 47 | 21% | 30% | 13% | 11% | 6% | 6% | 13% | 599 |

Shape: bimodal. In magnesium and turmeric about half of the 12-24-month brands show no badge, ~10-15% sit at 1K+, few in between. Towel is the exception: most newcomers sell.

## Reading the weak brands (12-24 mo, under 100/mo) — superseded by the full-cohort check below (this 10-brand sample was hand-picked and over-represented brands with websites)

Weak brands: towel 4, magnesium 15, turmeric 16. Of these, 1, 4 and 8 have 100+ reviews, so they did sell at some point (reviews accumulate; the badge is the last month only).

Web check of 10 weak brands (not a random sample: names that looked like brands; 2026-11-07, keenable search):

| Brand | What we found | Reading |
|---|---|---|
| Pixie Cup (magnesium, 50+/mo, 425 reviews) | Period-care DTC brand (pixiecup.shop), spray is a side SKU; two sizes on Amazon | Multi-channel; sales split across ASINs |
| No Crap In It (magnesium) | Texas handmade brand, "8 year history", own site + resellers | Old brand, new listing; Amazon is a side channel |
| Wink Well (magnesium) | Utah kids-sleep brand, own site; customer reviews mention finding it via Facebook ads | Sells via Meta + DTC |
| StelleVita (magnesium) | Amazon listing only, copies on resale sites | Amazon-native; looks like a real failure |
| Southern Natural (turmeric, 1,100 reviews, no badge) | Goat-milk soap business with own site and subscription, blog back to 2019 | Old multi-channel brand; Amazon sales faded or moved |
| AURAE (turmeric) | Amazon listing + INCI entry, no store found | Amazon-native; looks like a real failure |
| VALE (turmeric) | Own store riftvalleystore.com, "since 2023, 10,000 customers" (self-claim) | Multi-channel |
| Makari (turmeric) | Established brand, sold at Ulta and in Europe; the bar is one SKU | Big brand, Amazon secondary |
| Bare Botanics (towel) | Own site (barebotanics.co), local retail stores, Newegg | Multi-channel small brand |
| Cleanse Me With Hyssop (turmeric) | One-person handmade soap site | Hobby scale |

Takeaways:
- ◈ Only ~2 of 10 look like "launched on Amazon and failed". ~6 of 10 are older or multi-channel brands where Amazon is secondary.
- ◆ Cohort = age of the oldest listing in our search, not the brand's age. Old brands adding an Amazon listing get counted as newcomers, which makes newcomers look weaker than they are.
- ◈ No badge ≠ no sales: half the weak turmeric brands have 100+ reviews (a past sales history), and one brand can split sales across sizes.
- Fix before using survival as a decision input: tag every cohort brand as Amazon-native new / older or multi-channel (own site age, Ad Library, Wayback), and report survival for the Amazon-native group separately. Use the 1K+/mo bar (≈$12-20K revenue/mo here); 100+/mo is hobby scale.

## Full cohort check, v2 data (2026-11-07, `cohort/`)

Cohort: all 94 brand entities that entered Amazon 12-24 months ago in towel, turmeric soap and magnesium spray, on the v2 strict definitions (`graveyard_def.on_target`, brand keys as in `graveyard_stats2.py`; `cohort/cohort_brands.py` → `cohort/brands.json`). For each: own website (domain guessing with a name check + web search, `cohort/sites.json`), domain registration (RDAP) and first Wayback capture (`cohort/site_facts.json`), Judge.me public profile (`cohort/judgeme.json`). Classes (`cohort/classify.py`):
- A = no own store found (most have no brand on the listing): Amazon/marketplace-native.
- B = own store, first web evidence 2024 or later: young multi-channel brand.
- C = own store with web evidence before 2024: older brand that added an Amazon listing.

| Class | Brands | No badge (<50/mo) | 50-99 | 100-499 | 500-999 | 1K+ |
|---|---|---|---|---|---|---|
| A Amazon-native | 65 | 58% | 9% | 20% | 6% | 6% |
| B young, own site | 9 | 67% | 11% | 22% | 0% | 0% |
| C older brand | 20 | 45% | 5% | 25% | 10% | 15% |

By category (brands; 500+/mo; 1K+/mo):
- Towel: A 5 (0; 0), B 2 (0; 0), C 3 (2; 1: MainBasics, Blissal).
- Magnesium spray: A 14 (0; 0), B 3 (0; 0), C 11 (3; 2: Dr Teal's, plusOne — both retail brands).
- Turmeric soap: A 46 (8; 4: QOOQ, Treeroot and two unbranded kojic-turmeric bars), B 4 (0; 0), C 6 (0; 0).

Reading:
- ◆ Most of the cohort (65 of 94) is Amazon-native, and most of those (58%) sell under 50/mo after 1-2 years: these are real Amazon failures, not brands living elsewhere. The earlier 10-brand sample ("only 2 of 10 failed") was biased toward brands with websites.
- ◆ Magnesium spray: no Amazon-native or young brand reached 500/mo; every 500+ newcomer is an older brand (Dr Teal's, plusOne, iMatchMe). On Amazon this category is closed to newcomers.
- ◆ Turmeric soap on Amazon is won by cheap kojic-turmeric generics (QOOQ, Treeroot ~4K/mo), not by brands. Earthly Derm-type DTC brands win on Meta, not on Amazon: Amazon is the wrong yardstick for our soap plan.
- ◈ "No badge" can still be a healthy brand off Amazon: Wink Well (magnesium for kids) has no Amazon badge but 10,938 Judge.me reviews since 2022-04 (~250/mo, US store); Southern Natural 1,138 since 2018 (~13/mo, small).
- ◈ Young brands with their own site (B, n=9) did not break through on Amazon either; n is too small to say more.
- Limits: "no site found" can be a miss (brand unknown on 40+ unbranded listings); Wayback/RDAP dates can belong to a previous domain owner; Amazon badge only, other channels not measured for class A; Meta Ad Library by domain not yet checked.

## v2 across 17 categories — newcomer share of the Amazon shelf (2026-11-07, `graveyard_search.py` + `graveyard_stats2.py`)

Same ruler for every category: Amazon search pages 1-5 (search cards only; product pages hit a bot wall and are not bypassed), category = pre-registered product form (`graveyard_def.STRICT`, written before the scrape), entry date from the ASIN, brand = byline or non-generic first title word. "Indie" = brand entered < 24 months ago and is not a known older brand (Dr Teal's, plusOne, medicube, abib, Cetaphil, Vedix, Dr.Melaxin, MainBasics, Blissal, Luminess, Bissell, Momcozy... — partly from the cohort site/domain check above, partly general knowledge ◈).

| Category | Shelf units/mo | Top-3 brands | Indie share | Units to indies/mo | Indie brand winners ≥1K | Generic winners ≥1K | Price $ |
|---|---|---|---|---|---|---|---|
| Color-changing foundation | 309,250 | 0.74 | 80% | 247,400 | 3 | 10 | 30 |
| Beef tallow balm | 102,200 | 0.55 | 52% | 53,100 | 11 | 0 | 20 |
| Body oil (crepey skin) | 178,850 | 0.54 | 18% | 32,200 | 4 | 0 | ? |
| Pet water fountain | 156,600 | 0.58 | 18% | 28,200 | 3 | 5 | 43 |
| Rosemary hair oil | 181,100 | 0.58 | 15% | 27,200 | 5 | 0 | 15 |
| Turmeric soap | 98,550 | 0.62 | 24% | 23,700 | 3 | 3 | 12 |
| Neck firming cream | 210,750 | 0.50 | 11% (+22% older brands) | 23,200 | 5 | 0 | 98 |
| Waterless scent diffuser | 50,500 | 0.67 | 41% | 20,700 | 2 | 2 | 80 |
| Persimmon soap | 57,500 | 0.72 | 36% | 20,700 | 4 | 2 | 15 |
| Filtered shower head | 77,400 | 0.47 | 21% | 16,300 | 2 | 1 | 50 |
| Nose pore patches | 82,700 | 0.69 | 9% | 7,400 | 1 | 0 | ? |
| V-line chin wrap | 40,850 | 0.54 | 17% | 6,900 | 2 | 0 | 15 |
| Exfoliating towel | 67,950 | 0.51 | 8% | 5,400 | 2 | 0 | 18 |
| Compression socks | 172,000 | 0.29 | 3% | 5,200 | 1 | 0 | 16 |
| Magnesium oil spray | 44,000 | 0.58 | 11% (+34% older brands) | 4,800 | 1 | 0 | 20 |
| Men's hair removal cream | 76,250 | 0.93 | 6% | 4,600 | 1 | 0 | 19 |
| Teeth whitening powder | 13,500 | 0.61 | 24% | 3,200 | 1 | 0 | ? |

Not scraped (Amazon returned empty pages repeatedly): lash serum, hair-growth serum (both compliance-flagged), pre-wash oil.

Why the earlier "openness" lists flipped: the top-20 proxy called a listing "new" if it had < 500 reviews. Fast winners break that: Luxe color-changing foundation is ~10 months old with 10,300 reviews; Terra Lotus tallow balm ~18 months with 6,700. The proxy scored color foundation 3% new and tallow 2% new; dated by ASIN they are 80% and 52%. The v1 graveyard pilot was invalid for other reasons (off-target forms, failed page loads), see above.

Limits: Amazon only; badge floors; one snapshot (no trend, so fad risk is not measured here — color foundation is a ~10-month-old category); visible 5 pages only; brand unknown on generic titles (counted as stand-alone sellers); rosemary filter let one "hair growth spray" in (AVEYA, 10K).

Note (same day, later): the table above used a short generic-word list, so unbranded titles starting with "Beef...", "Color...", "Waterless..." were merged into fake old brands. Frozen v2.0 numbers (generic list expanded, NEW split into named brands vs generics) are produced by `graveyard_table.py` and summarised in `OVERLAY_V2.md`; use those.

## Cohort brands outside Amazon: Meta ads and review curves (2026-11-07, `cohort/meta_brands.py`, `cohort/meta_join.py`, `work/reviews/loox_shop.py`)

Question: the 29 cohort brands that have their own store (classes B/C above) — do they live on Meta, and for how long, and do their review counts grow?

Meta Ad Library, US, active ads, searched by domain and by brand name; an ad counts as the brand's only if the page or landing domain is the brand's (namesakes such as people, a sushi bar, a clinic and a safari operator were removed by hand).

| | brands |
|---|---|
| own store | 29 |
| running own Meta ads now | 10 (Pixie Cup's ads are for period cups, not magnesium, so not counted) |
| any own ad alive 180+ days | 4: Pacifica (since 2020, ~10 aged ads), Vigority (13 of 17 ads aged 180+), Pura D'or (3), Wink Well (2; 8 ads, all 90+) |
| no Meta ads at all | 19, incl. MainBasics (2K/mo on Amazon), iMatchMe (500), LivaClean (300), Southern Natural (1,100 Judge.me reviews) |

By category:
- Turmeric soap: nobody in the cohort has a long-running Meta ad. Ecloura/BacneOut (class B, 200/mo on Amazon) is in a fresh push: ~400 active ads, the oldest from 2026-09-16. Its outcome is unknown; re-check in Feb 2027 (do the ads survive 90/180 days?).
- Magnesium spray: the four brands with 180+ day ads are all old (class C) and sell only 0-300/mo on Amazon, so for them Meta/DTC is the main channel, not Amazon. plusOne (1K/mo Amazon) and Dr Teal's (8K) run only young ads, partly sending traffic to Amazon/Walmart.
- Towel: Blissal (900/mo Amazon) runs ~190 ads that rotate fast (1 of ~30 sampled is 90+ days old) — matches its falling site traffic in `market_system.md`.

Review curves (Loox shop-wide widget, all products; ~20% systematic sample, scaled):
- Monier (turmeric, class B, 277 reviews): rose Aug 2024 - May 2025 (peak ~40/mo), then faded to 2-6/mo through 2026. A brand that peaked and stalled; Amazon still 200/mo.
- LivaClean (class C, 41,976 reviews): ~0-100/mo until Dec 2024, ~3,000/mo Feb 2025 - Jan 2026, then ~20/mo since Mar 2026. The jump and the stop are both abrupt; the site now also carries Okendo and Yotpo code, so the likeliest reading is a change of review app or review import, not a sales collapse. ◇ not a demand signal.
- Judge.me (Southern Natural, Wink Well): public pages are JS-rendered and returned 429 in the browser; no curve.
- Trustpilot via Wayback: 2 snapshots for 29 domains, no counts. Dead end for small brands.

Reading:
1. Amazon-native newcomers (class A) are invisible on Meta by definition (no site); the B/C brands split into "Meta-first" (Pacifica, Vigority, Wink Well, Pura D'or: steady old ads, weak Amazon) and "Amazon-first" (MainBasics, iMatchMe, LivaClean: no Meta at all). So a weak Amazon badge does not mean a weak brand, and vice versa; each channel must be read on its own.
2. Long-running Meta ads (the signal we used for the leaders) are rare among newcomers: 4 of 29 site brands, all old. A new turmeric or magnesium DTC brand that reaches 180-day ads would be unusual in this cohort.
3. Review widgets are fragile as a time series: an app switch or import breaks the curve. Use them only with a second signal (traffic or ad age).

Limits: traffic (Jun-Sep visits) could not be added: adlibraryspy.com blocked our IP via Cloudflare after one headless request and hypestat shows a bot check; we did not try to bypass either. Meta library shows active ads only (stopped campaigns are invisible). Brand-name search misses ads that name neither brand nor domain in the text.
