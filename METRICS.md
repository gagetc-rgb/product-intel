# Dossier metrics v2.2 (fixed 2026-11-09) + v2.3 (frozen 2026-11-10, section "v2.3" below)

The site still shows v2.2. v2.3 is the method for the next pass; where they differ, v2.3 wins for new work.

The site is built only from these metrics. A metric that is not measured is shown as "not measured", never guessed.
A label such as "price war" is used only when the metric behind it shows it (D2 below); never as an inference.
Every metric names the accepted practice it follows. Where we adapted a practice ourselves, it says so.
Tiers: ◆ counted by a platform · ◈ our estimate or reading · ◇ disputed. Weights between groups: not decided yet (owner).

## Two lenses (site switch)

- **Default: "Can a newcomer follow the leader?"** Group B first, A as a floor.
- **Switch: "Whole market".** Group A: size and growth, big players included.

## A. Demand

| # | Metric | Definition | Channel | Practice it follows | Status |
|---|---|---|---|---|---|
| A1 | Search growth | Google Trends US, all product phrasings pulled together and summed; last 12 full weeks vs the same weeks a year ago; divided by the growth of 5 broad personal-care terms. Context only: Google computes it from a search sample that changes daily, so the sign and the order of magnitude matter, not the exact percent. Shown as a plain number, no colour (owner, 2026-11-10, after seeing results). One pull per update; no repeated daily pulls | Google | "search trends" input of Jungle Scout's Opportunity Finder; Trends is a sample ([Eichenauer et al. 2022](https://onlinelibrary.wiley.com/doi/full/10.1111/ecin.13049)) | ◈ current value = arithmetic mean of the 3 pulls already made (2026-11-08, -09, -10; tallow and turmeric: 2 samples, `work/blind/trends_combined.py`); they differed by 0-3% for 13 of 18 products. Next update: one pull, with the Meta re-check (2026-12-08) |
| A2 | Amazon volume | Sum of "bought in past month" badges, search pages 1-5, US address; a floor | Amazon | "Units sold" = the demand input of Jungle Scout's Opportunity Score ([support](https://support.junglescout.com/hc/en-us/articles/360015964774-Understanding-the-Opportunity-Score-in-the-Extension)); badge meaning per Amazon | ◆ one snapshot |
| A3 | TikTok Shop volume | Units/revenue of top products | TikTok | FastMoss / Kalodata shop GMV | not measured (paid tool) |

## B. Can a newcomer follow (default lens)

| # | Metric | Definition | Channel | Practice it follows | Status |
|---|---|---|---|---|---|
| B1 | Entrant success rate | Of sellers whose first listing in this product is 3-24 months old (established brands excluded), the share selling 1,000+/mo. Upper bound (sellers who left pages 1-5 are invisible) | Amazon | Entry and survival analysis of firms (industrial organisation; e.g. business survival rates); the Amazon adaptation is ours ◈ | ◈ measured |
| B2 | Survivors | Number of those entrants at 1,000+/mo and 300+/mo | Amazon | "number of sellers" competition input (Jungle Scout) | ◆ measured |
| B3 | Concentration | Herfindahl-Hirschman Index (HHI) of seller shares of A2, plus top-3 share. Above 1,800 = highly concentrated | Amazon | US DOJ/FTC [2023 Merger Guidelines](https://www.justice.gov/d9/2023-12/2023%20Merger%20Guidelines.pdf) | ◆ measured |
| B4 | Shops that keep ads alive | Distinct shops (by their own domain) with ads running 90+ days | Meta | Ad run time as the free proxy for a profitable ad, with known limits (see `work/dossier/DOSSIER_PLAN.md` §6) | ◆ leader shops measured |
| B5 | Ad death rate | Share of today's sampled ads gone after 30 days | Meta | same; the US library keeps no stopped ads, so a re-check is the only way | pending 2026-12-08 |
| B6 | Verified young winners | Businesses under 3 years old (site, reviews, company facts; not Amazon age) with a large share in any channel | all | ours ◈; checked by hand, sources listed per brand | ◆ leaders of 9 categories |

## C. Are the leaders still growing

| # | Metric | Definition | Channel | Practice it follows | Status |
|---|---|---|---|---|---|
| C1 | Leader store reviews | Reviews per month in each leader's own store; Aug-Oct vs a year ago and the last 3 months' direction | own store | review count as a share of orders ([Judge.me benchmark](https://judge.me/blog/benchmarking-review-collection-rate)); growth within one store only | ◆/◈ 13 stores |
| C2 | Leader ad volume over time | Domain ad count repeated monthly | Meta | same as B4 | first point 2026-11-09 |

## D. Context next to the score

| # | Metric | Definition | Practice it follows | Status |
|---|---|---|---|---|
| D1 | Unbranded among survivors | Share of B2 survivors with no brand name. Says copies survive; says nothing about prices | Jungle Scout "listing quality" input (weak listings = room) | ◆ measured |
| D2 | Price trend (the only basis for "price war") | For the top 10 listings: Buy Box price over 12 months from Keepa. "Price pressure" = most top listings sit below their own 12-month average for 90+ days; "price war / dumping" = that, plus prices still falling and new entrants coming in below the leaders | reading Keepa charts: compare current Buy Box with the 90-day and 12-month averages, look at a full year ([Kozan](https://kozan.ai/blog/keepa-tutorial), [Mezvic](https://mezvic.com/blog/how-to-read-keepa-charts)) ◈ practitioner sources | ◈ read by eye from Keepa charts for 9 categories + camelcamelcamel table (current vs all-time average, 27 usable listings; see AUDIT §10), 2026-11-09: no war, no pressure shown; exact 12-month series need Keepa's paid data |
| D3 | Quality gap | Leaders' star ratings | Jungle Scout "listing quality" | ◆ measured |
| D4 | Regulatory flag | Claims that need drug/medical status or extra filings | FDA cosmetic vs drug rules ◈ | ◈ |
| D5 | Margin | Price vs landed cost and ad cost per order; under 20-25% net is a red flag | common Amazon research checklists ◈ | ◈ measured 2026-11-10 for all 20, Amazon FBA, before ads (`work/margin/margin.py`): price − Amazon fees (2027 card) − supplier price × (1 + duty) − freight − returns − storage. Verdict on the middle of the range: 40%+ of price = good, 25-40% = tight, under 25% = bad (ads take the rest). The 25% cut-off was set after seeing the results |

## Decision rule (default lens, v2.2; v2.3 replaces steps 2-3 with groups and the absolute floor, see "v2.3")

1. Demand floor: out only if A1 and C1 both point down.
2. Rank the rest by B1 and B2 together, then B3 (lower is better), then B4/B6.
3. D2 and D5, once measured, can remove a category (price war shown by D2; margin under 20%). Applied 2026-11-10: pet water fountain (−9…16% of price before ads) moved from the top to "watch"; the 5th slot is the owner's call.
Changes to this file are versioned; a change made after seeing results is marked as such.

## v2.3 (frozen 2026-11-10)

Written after seeing v2.2 results: the owner's additions (B7-B9) and an external review (Fable 5.2) checked on our data the same day (`work/audit/KEYWORD_AUDIT_2026-11-10.md`). Frozen before any new data: Keepa, control categories, the back-test. Any change after that is v2.4, with its reason.
Thresholds marked "default" were set by us without outside calibration; the owner may change them only before the next data pull.

### What changed against v2.2

1. **Two entry games, measured apart.** B1/B2 are computed separately for branded entrants and unbranded ones. A brand counts only from the Amazon brand field or seller data (Keepa), never from a guess on the title. We plan to enter as a brand, so the branded figure decides; the unbranded one is context (it shows the price floor).
2. **New metric B10, brand premium.** For all sellers of the category: the brands' share of units and their units-weighted median price against the unbranded one. A brand earns its keep where brands hold ≥50% of units at ≥1.3× the unbranded price (default). Seen on 2026-11-10: lash serum 87% at 2.1×, tallow 71% at 1.7×, persimmon soap 47% at 2.0×, fountain 49% at 1.4×, foundation 72% at 1.0× (no premium).
3. **Who the unbranded are is measured, not assumed.** Factory, trading company or one-batch reseller: read from the seller profile (Amazon shows the business name and address), not inferred.
4. **Success in money, not units.** Winner = entrant with revenue ≥ $20,000/mo (units × its price; default, ≈1,000 units at $20); "mid" = ≥ $6,000/mo. When D5 is measured, the bar becomes profit before ads (revenue × our margin).
5. **Groups, not places.** Each category's B1 is shown with its 95% interval (Wilson). Group "clearly above" = lower bound above the pooled rate of all categories; "clearly below" = upper bound under it; the rest "middle". No numbered ranking inside a group.
6. **Absolute floor: "none passes" is a valid answer.** A category reaches "test it" only if all hold:
   - at least 2 verified young brands (B6) among branded winners;
   - branded B1 lower bound ≥ 5% (default);
   - brand premium met (item 2);
   - demand floor of v2.2 (not both A1 and C1 down);
   - no price war (D2);
   - when measured: landed cost ≤ 25% of price (default; D5) and compliance cost known (D6).
7. **Entry cost and expected value.** Per category: first batch + compliance (D6) + launch test budget = entry cost. Expected value = P(success) × 12-month profit − (1 − P) × entry cost, with P = branded B1 (lower bound as the cautious case). Ad cost is unknown from public data; the money test (item 10) supplies it.
8. **Control categories.** 3-5 categories not from the source channel, picked at random from Amazon Movers & Shakers in the same departments, run through the same pipeline. Without them we cannot say whether 27% is high.
9. **Back-test.** With Keepa history, rebuild each category as of November 2025 and check whether the entrants and groups the method would have picked then are alive now. The method is trusted only if its 2025 "clearly above" group holds up.
10. **Money test is the last gate.** A $200-500 demand test (Meta or TikTok) with the pass bar written before it starts, computed from margin. Public data only gives a probability. The test uses **only the claims we may legally make** (D6): measured demand often rests on claims a lawful seller cannot repeat ("grows lashes", "stops hair loss", "heals eczema"), so a test with them would measure demand we cannot sell to. If it takes money, the FTC mail-order rule applies (ship on time or within 30 days, else refund); a no-payment waitlist avoids it.
11. **New metric D6, compliance cost.** Per category: registrations (MoCRA for cosmetics), product liability insurance, Amazon category approval, and what the claims may say. Example: an eyelash-growth claim makes the product a drug under FDA's intended-use rule (warning letters to eyelash-serum firms in 2011); a cosmetic may only promise a look ("longer-looking lashes"). First reading for the four "go" products: `research/ENTRY_REQUIREMENTS_US_2026-11-10.md` (foundation low, tallow low-medium, shower filter medium-high: 2.5 gpm federal cap, California certification and listing before sale, no health or "kills bacteria" claims; lash serum high). Prices of tests and certifications are not public: ask contractors.
12. **Measurement windows.** One November snapshot is not enough for season, deaths or multi-listing sellers; B7/B9 and seasonality come from Keepa history.

Kept from v2.2 unchanged: search as colourless context (A1), keyword rules (K), concentration (B3), Meta by the shop's landing domain (B4), "price war" only from price history (D2).

### Newcomer growth and the graveyard (owner, 2026-11-10)

Why: B1 counts only entrants already at 1,000+/mo and sees only survivors on pages 1-5. The owner wants (a) newcomers that grow steadily at any level, (b) a check that their ads pay back, (c) who entered in the past and disappeared.

| # | Metric | Definition | Source | Status |
|---|---|---|---|---|
| B7 | Growing newcomers | Entrants (first listing 3-24 months old, established brands excluded) whose monthly units rose in at least 3 of the last 4 months, from a floor of 100/mo (e.g. 100 → 200 → 500) | Amazon: Keepa monthly-sold and sales-rank history; TikTok: our tracker (Δsold), FastMoss/EchoTik history | needs Keepa |
| B8 | Growth that pays | A B7 newcomer whose same creative has run 90+ days on Meta (searched by its landing domain). Owner's rule: an advertiser keeps paying for a creative only if it pays back | Meta Ad Library by domain, field "N ads use this creative" | free, ready |
| B9 | Graveyard | Of listings that entered 12-36 months ago, the share now under 50/mo or delisted; names and dates of the ones that died | Keepa (listed-since filter + history); free fallback: Wayback captures of Amazon best-seller and search pages a year ago | needs Keepa |

Limits: a long-running creative is the best free signal of payback, not proof (big brands run brand ads at a loss, some ads are simply forgotten). B9 is the honest denominator for B1, which today is an upper bound.

## v2.4 (2026-11-10): the entry model is "copy a working store and scale it with ads"

Reason for the change: the owner stated the model on 2026-11-10, after v2.3 was frozen and after seeing its results. The investor's way is to take a store that already sells through Facebook/Instagram ads, build the same landing page and funnel, buy the same traffic and take a share. v2.3 item 1 assumed "we enter as a brand" and judged by the Amazon shelf; that measures a different game. No new data was looked at between v2.3 and v2.4.

What changes:

1. **Two lenses, the first one decides.** Lens M ("own store + ads") is the main one for the report. Lens A (the Amazon metrics of v2.2/v2.3) stays as market size, the price a buyer can compare against, and a second channel.
2. **A "copy" here is a store, not an unbranded Amazon listing.** Unbranded Amazon winners are mostly factories competing on price; their survival says nothing about a copied funnel. Do not use them as evidence for lens M.
3. **The test of the investor's logic is the follower, not the leader.** A leader's ad that runs 180 days shows that the leader's ad pays. A copy enters later, with no reviews and no ad history, into a dearer auction. The evidence that a copy can take a share is: stores other than the leader, younger than 24 months, that keep ads alive 90+ days.

Lens M metrics (all by landing domain, never by category phrase, rule K3):

| # | Metric | Definition | Source | Status |
|---|---|---|---|---|
| M1 | Leader proof | The leader store's ads alive 90+ and 180+ days; its store reviews per month against a year ago | Meta Ad Library US by domain; store review widgets | measured for the leaders of 9 categories (AUDIT §5, C1) |
| M2 | Followers that hold | Number of distinct stores selling the same product, other than the leader, with an ad alive 90+ days; how many of them are under 24 months old (domain date, first reviews) | Meta Ad Library US: product phrasings → sample → group by domain → check each domain by hand | not measured (only leaders so far) |
| M3 | Follower death rate | Of the follower stores advertising today, the share with no live ad after 30 days | re-check of the same domains (first re-check 2026-12-08); EU/UK library keeps stopped ads | pending |
| M4 | Own-store money | Order value in the leader's store (price × usual bundle) − product landed − shipping to the buyer − payment fee − returns = what is left to pay for an order. That is the highest ad cost per order that still breaks even on the first purchase | leader's store prices; supplier listings; carrier rates | not measured (soaps only, `work/full_list_analysis.md`) |
| M5 | Repeat | Subscription or refill offered by the leader; share of its ads and reviews that are for refills | leader's store; review text | not measured |
| M6 | What may be said | The claims the leader's ads rest on, and which of them a lawful seller may repeat (D6). If demand rests on a claim we cannot make, lens M fails | leader's ads and pages; FDA / FTC / Meta rules | first reading for 4 products (`research/ENTRY_REQUIREMENTS_US_2026-11-10.md`) |
| M7 | How crowded | Stores advertising the product whose oldest live ad is under 30 days (fresh copies), against stores with 90+ day ads | same sample as M2 | not measured |
| M8 | What to fix in the leader (owner, 2026-11-10: the copy is the market leader's store, improved where its buyers complain) | The leader's 1-3★ reviews, dated, sorted into: the product itself / shipping and delivery / billing and subscription / support. Report the share of low reviews, the top two complaints with their share, and whether each is fixable by a follower (faster US shipping: yes; formula or build: needs a supplier change; "does not work": not fixable, it is the claim) | leader's store review widget (Loox, Judge.me), Trustpilot (latest ~200), Amazon reviews of the leader's listing | not measured as a metric; single readings exist (Terra Lotus: 43% of September reviews under 5★; Menvault: 9.5% at 1-2★) |

Reading:
- "Test it" under lens M needs: M1 proven by two signals; **at least 2 follower stores under 24 months old holding ads 90+ days** (default); M4 leaves room for ads (default: at least 50% of the order value before ads); M6 passes. "None passes" stays a valid answer.
- M8 picks the model to copy and the angle: a leader with strong M1 and one dominant fixable complaint is the best target. A leader whose main complaint is "it does not work" is a warning about the product, not an opening.
- Ad count is never evidence (Skult: 870 ads, about 1,000 Amazon units a month, revenue in the video derived from the ad count). Ad age is.
- The US library shows only live ads, so M2 sees survivors only; M3 is the correction and needs the re-check.
- Ad cost per order cannot be seen in public data. M4 gives the ceiling; only the money test (v2.3 item 10) gives the real number.
- The products come from a public YouTube channel whose viewers copy the same stores: M7 is expected to be high. Report it.
- Copy the model (offer, funnel structure, angle), not the page: the leader's texts, photos and invented "doctors" or "customers" are a legal risk (copyright, FTC rule on fake reviews and testimonials, 16 CFR 465).

Seen in data we already hold (leaders only, AUDIT §5): persimmon soap is the one case that already shows item 3: the old leader is Mirai (since 2014), and Kaori, a store from February 2026, holds 210 ads alive 90+ days. Turmeric soap (Earthly Derm, site since 2024: 86 ads at 90+), body oil (GODA: 580), color foundation (Smooche 1,500, Prime Prometics 380) show strong leaders; their followers are not counted yet.

The site still shows v2.3. Lens M goes on the site only after M2 and M4 are measured.

## K. Keyword rules (added 2026-11-10 at the owner's request, after the CarPlay error; applies to every search phrase in every channel)

Why: our answers have moved more with the phrase than with the product. From our own data:
- Meta "carplay": 560 ads aged 180+, but they were car dealers; the exact product phrase "wireless carplay adapter": 5 of 180 ads aged 90+.
- Meta phrase vs shop domain: Earthly Derm 12 aged ads by phrase, 44 by its domain.
- Trends: tallow 1.04 for "tallow balm" vs 0.54 for "beef tallow for skin"; body oil is measured by a symptom ("crepey skin") and the chin wrap by a body feature ("double chin"), not by the product.
- Amazon: "hair growth serum" returned Nutrafol supplements, "men's incontinence underwear" returned Depend, "handheld steam cleaner" top 20 included BISSELL carpet cleaners.
- TikTok: turmeric soap 0.9K sold on one keyword page, 819K on another.

Rules:
- **K1. Keyword card first.** Before any pull, write per phrase: what it must capture, the buyer's intent, likely false matches (services, dealers, clinics, B2B, neighbouring products, homonyms), and the synonyms buyers use. Written before seeing numbers.
- **K2. Relevance check, recorded.** Open what the phrase returns (Amazon top 20, TikTok top 20, the Meta sample, Google results and Trends "related queries") and count the on-target share. Under 80%: filter by title or domain, or change the phrase. Store the share and the date next to the number.
- **K3. Three layers, never one phrase.**
  - Category: all common phrasings, pulled together and summed (the tallow rule). Symptoms and body features only as a separately labelled "need" signal.
  - Brand: each leader's brand name, domain and hero product name. Disambiguate homonyms (Luxe, Kaori): brand + category word, the Trends "Topic" entity where Google has one, a check of related queries.
  - Identity instead of words wherever a channel allows: Meta by landing domain, reviews by store, Amazon by ASIN and brand, TikTok by product ID.
  - A verdict needs the layers to agree. Disagreement is reported, not averaged away.
- **K4. Share of search.** Compare leaders' brand searches in one Trends request (shared scale) and track each brand's share over time ("share of search", a practice from brand measurement). A young brand gaining share supports B6.
- **K5. Read the buyer's path.** Category search → brand search → visit to the brand's site. Read brand search next to the brand's ad volume (C2): brand search rising with flat ads = organic demand; both rising = mostly ad-driven; category search rising too = a market trend (news, TV, a viral video).
- **K6. Explain every spike.** A jump of 2× or more within 8 weeks needs a cause before the number is used: news, TV or a viral video in that week (Google News, YouTube/TikTok search, Trends "rising" queries); a Trends artifact (the control terms jump too, as in Apr-Jun 2026); or the season. Unexplained = ◇.
- **K7. Real volume.** Trends is relative. Over 20% zero weeks in 2 years = too rare. Where available, add an absolute check: Google Keyword Planner range, Amazon Brand Analytics search frequency rank, or a tool's volume.
- **K8. Repeat and freeze.** Trends samples: use the mean of 3+ pulls on different days. Phrase lists are frozen per method version; a phrase changed after seeing results is marked as such.
- 2026-11-10 (owner, after seeing results): A1 is context, not a scored signal on the site: plain number without colour, one pull per update instead of a mean of daily pulls. A1 still feeds rule 1 (both A1 and C1 down) and the video check "товар хорошо продаётся" (A1 below ×0.8, well outside the 0-3% day-to-day spread).
