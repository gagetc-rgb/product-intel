# Dossier metrics v2.2 (fixed 2026-11-09)

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
| A1 | Search growth | Google Trends US, all product phrasings pulled together and summed; last 12 full weeks vs the same weeks a year ago; divided by the growth of 5 broad personal-care terms; mean of daily pulls | Google | Trends as a demand index with repeated samples ([Eichenauer et al. 2022](https://onlinelibrary.wiley.com/doi/full/10.1111/ecin.13049)); "search trends" input of Jungle Scout's Opportunity Finder | ◆ pulls 1-2; pull 3 on 2026-11-10 |
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
| D5 | Margin | Price vs landed cost and ad cost per order; under 20-25% net is a red flag | common Amazon research checklists ◈ | not measured: deep pass for the top 5 |

## Decision rule (default lens)

1. Demand floor: out only if A1 and C1 both point down.
2. Rank the rest by B1 and B2 together, then B3 (lower is better), then B4/B6.
3. D2 and D5, once measured, can remove a category (price war shown by D2; margin under 20%).
Changes to this file are versioned; a change made after seeing results is marked as such.
