# What others use to judge product demand and entry timing (open sources review)

Date: 2026-11-08. Scope: research papers, platform documentation, practitioner articles and YouTube, compared with our method (`EVALUATION_METHOD.md`, `METHOD.md`).
Marks: ◆ confirmed (primary source or several independent ones) · ◈ likely (one decent source, or vendor docs) · ◇ disputed / vendor opinion / heuristic.

## 0. Our method in one paragraph (for comparison)

Three questions plus a gate: demand (units/month summed across Amazon + TikTok Shop + DTC), proof (someone with real data keeps paying: Meta ads alive 90/180+ days, review curves, traffic history), stage (life cycle A-E or fad, crowding, newcomer survival), and a fit gate (regulation, margin, logistics, creatives). SimilarWeb is kept as a Tier 2 signal (weak under ~50K visits), not discarded. All of it is **observational**: we read other people's results.

## 1. New free or cheap data sources we have not used

| # | Source | What it gives | Why it matters for us | Limits | Mark |
|---|---|---|---|---|---|
| 1 | **Amazon Product Opportunity Explorer** (Seller Central → Growth; needs a Professional seller account) | Per "niche" (cluster of search terms): search volume 90/360 days and its growth, **units sold** range, average price, top-5/top-20 click share, number of brands, average brand age, **# new products launched in past 180/360 days and # "successful launches" (> $50K annualized revenue)**, out-of-stock rate, Prime share, search-to-purchase conversion, trend views 7/30/90/360 days | Amazon's own first-party numbers. The "successful launches ÷ new launches" ratio is exactly our newcomer-survival metric (section 5a), already computed by Amazon. Replaces most of what Jungle Scout / Helium 10 estimate | Amazon only; niche grouping is Amazon's; account cost (Professional plan, ◈ ~$39.99/mo) | ◆ Amazon help page + user guide PDF |
| 2 | **Shop app "bought in past month" badge** (Shopify's consumer app) | Bucketed floor of orders in last 30 days for Shopify-store products: 25+, 75+, 300+, 500+ | The first platform-counted **DTC** sales signal. Fills our biggest gap (DTC volume was only traffic × assumed conversion) | Buckets coarse; shown only above a threshold; only for stores listed in Shop | ◈ merchant blog + Shopify locale string "{{value}}+ bought in past month" exists ◆ |
| 3 | **ImportYeti** (US customs bills of lading since 2015, free) | Per US importer: sea shipments over time, weight, containers, HS codes, overseas suppliers (factory names and addresses) | (a) A leader's **import volume curve** = real physical demand, independent of ads and reviews; (b) make-vs-buy: shows which factory makes the leader's product | Sea freight only (air and parcel missing, so small DTC brands shipping by air are invisible); companies can request confidentiality; paid tier for bulk/CSV | ◆ Bellingcat toolkit + ImportYeti docs |
| 4 | **Meta Ad Library, EU/UK transparency (DSA)** | For any ad delivered in the EU or UK: reach total and by country/age/gender, targeting, payer; **ads stay in the library 1 year after they stop**; API returns them | (a) Spend estimate = reach × frequency × CPM / 1000 (CPM = cost per 1,000 impressions); (b) **stopped ads stay visible**, which fixes our "dropouts disappear" denominator problem for any brand that also runs in the EU/UK | Covers only the EU/UK part of a US brand's campaign; spend is a modelled estimate (±2-5× per ad) | ◆ Meta API docs, cited by several independent guides |
| 5 | **Meta Ad Library "Sort by: Impressions high to low"** (since ~Jan 2026) | Ranks one advertiser's ads by delivery, no numbers | Shows which creative carries the budget; week-to-week rank movement = scaling | Claims that every commercial ad now shows an impression range bucket are **contradicted** by hands-on reviews; verify ourselves | ◈ sort exists; ◇ impression buckets |
| 6 | **FastMoss free tier** | TikTok Shop top products and shops, weekly units, week-over-week growth rate | TikTok trend direction (we only have lifetime "sold") | Estimates; free tier limited | ◈ |
| 7 | **Kickstarter / Indiegogo** | Backers and pledges for new physical products | Demand evidence for genuinely new products before they exist in retail | Backers ≠ mainstream buyers (see 3.6) | ◈ |
| 8 | **Competitor stock tracking** (cart "999" probe; `inventory_quantity` in some Shopify themes' page JSON) | Stock level over time → units sold per day | Practitioners say stock-based estimates beat BSR-based ones (BSR = Best Sellers Rank) | Grey zone: automated cart probing can breach site terms and looks like bot traffic. **Owner decision before any use** | ◈ method / ◇ legality |

## 2. Testing instead of observing (the main gap)

Practitioners and the lean-startup literature agree on one point we lack: **observed signals tell you a market exists; only a behavioural test tells you it will buy from you.**

- ◆ Method: fake-door / smoke test (Alberto Savoia, *Pretotype It*, 2011): a real-looking product page with a price, paid traffic, measure clicks → add-to-cart → checkout or pre-order. Set the pass/fail threshold before the test.
- ◈ Charge-later pre-orders on Shopify (card vaulted, charged at shipping, cancel = no fee): validates demand and sizes the first purchase order. YouTube: "How to Actually Validate Your Next Product (DTC Pre-order Strategy)" https://youtube.com/watch?v=XeaBwLkiAa4
- ◇ Case: Kettle & Fire founder says a $15 landing page selling bone broth at $29.99 converted ~30% before any product existed (founder's own claim). https://youtube.com/watch?v=-nvJIfQnidw
- ◈ Budget rule repeated across several practitioner guides: test each product with **3-4× break-even CPA** (CPA = cost per acquisition; break-even CPA = price − product − shipping − fees − refund reserve). Kill ladder: no add-to-cart at 1×, no checkout at 2×, ≤1 sale at 4×. If break-even ROAS (return on ad spend) > 3, paid ads cannot work at that margin.
- ◇ Disagreement: some guides say a real test needs ~50 purchases (Meta's learning-phase threshold), i.e. ~$650+ per product; others say dead products fail cheaply at the top of the funnel. Both agree a product needs 3-4+ distinct angles before it is declared dead.
- Ethics: never take money for something that will not ship; pre-orders must state the ship date and refund on request.

**Implication for us:** add a step 4 "Test" after the card: top 2-3 candidates get a smoke test or charge-later pre-order on Meta at a pre-written threshold. This also calibrates our own CPM and conversion, which feeds back into spend estimates (1.4) and DTC volume (our 2-3% conversion assumption).

## 3. What research says (peer-reviewed or primary)

1. ◆ **Pioneers often lose; early leaders win.** Golder & Tellis 1993 (J. Marketing Research, ~500 brands, 50 categories, survivors and failures both sampled): 47% of market pioneers failed; early leaders (share leaders during early growth) failed 8% and entered on average 13 years after pioneers. Durable-goods pioneers failed 67%, non-durables 28%. → Supports our rule "stage C (clone wave/growth) is the best window; stage A-B is risky". Caveat: old data, long product cycles; DTC cycles are months, not years.
2. ◆ **Takeoff is an elbow, not a smooth curve.** Golder & Tellis 1997 (Marketing Science): really new durables show a sudden sales jump of 400%+; post-war mean time to takeoff 6 years, price at takeoff 63% of launch price, penetration 1.7%. → For genuinely new categories, a price drop plus a sales elbow is the takeoff marker. Our products are mostly not "really new", so use with care.
3. ◆ **Google Trends predicts the present, not the future.** Choi & Varian (Google, 2009/2012): adding Trends to simple seasonal models improved nowcasts by a few % up to 18% (motor vehicles). → Trends is a current-state and seasonality signal, not a forecast. Matches our use.
4. ◈ **Review counts track sales.** arXiv 1704.02993 (1M+ Amazon products): Amazon-wide revenue from Verified Purchase review counts tracked revenue reported in SEC filings for several companies. One paper, so ◈. Chevalier & Mayzlin (NBER w10148): better reviews raise relative sales, and **1-star reviews move sales more than 5-star** ◆. → Supports our review curves; adds: watch the 1-star share, not the mean.
5. ◈ **Diffusion models + Trends.** Bass model (1969) splits buyers into innovators and imitators; papers combining Bass with Google Trends nowcast new-product sales better than either alone (iPhone/iPad case, Univ. Kent/Aberdeen 2019). Bass fits single-peak curves and predicts well near the peak. → Possible later tool: fit a Bass curve to a category's review or Trends series to estimate how far past the inflection point it is.
6. ◈ **Crowdfunding is evidence of launch, not of mainstream success.** Springer J. Academy of Marketing Science 2025: funded projects ~7× more likely to launch; larger crowds raise adoption but **lower** satisfaction; longer time-to-market worsens it. Sample mostly video games + 211 Kickstarter/Indiegogo products.
7. ◇ **Paid sales estimators are not ground truth.** Jungle Scout and Helium 10 each publish studies showing they are the most accurate (median error ~16% vs others); an independent seller test on 36 SKUs (Reddit, 2017) found errors up to ±60%. Vendor studies conflict, so ◇. → Paid estimators are Tier 2 at best; Opportunity Explorer (first-party) is preferable.

## 4. Practitioner heuristics worth adding (opinions, ◇)

- **Concentration:** HHI (Herfindahl-Hirschman Index = sum of squared market shares, used by the US DOJ/FTC for mergers) or simply top-3 / top-10 share. Vendor thresholds for Amazon niches: HHI < 1,500 open, 1,500-2,500 moderate, > 2,500 hard; top-10 brands > 80% of revenue = avoid unless sub-niche. Only the DOJ thresholds are official, and they are not made for Amazon. Compute **per brand, not per listing**.
- **Niche attributes** (Andrew Youderian, eCommerceFuel): can you add value (confusing/complex products, multi-component), price $50-200 (later $100-200), many accessories, consumable/repeat, hard to find locally, passionate or embarrassed buyers. Useful inputs for our fit gate.
- **Saturation signals** (several Amazon seller guides): rising seller count + falling price = price war; rising CPC (cost per click) = competition entering; top sellers' review counts as the social-proof barrier. Already partly in our stage table.
- **Fad filter** (Exploding Topics): accept a topic only after several months of compounding search growth; a 6-8 week spike = fad. Already in our method.
- **Make vs buy ladder** (supplement and DTC manufacturing guides, vendor opinion): dropship / print-on-demand to validate → private label (stock formula, own brand, MOQ = minimum order quantity typically 1,000-10,000; one lab quotes 2,000) once customer-acquisition cost is repeatable → custom product only for a proven hero SKU (SKU = stock keeping unit). Engineered products add EVT/DVT/PVT stages (engineering / design / production validation tests). ImportYeti finds the leader's factory to source samples.

## 5. YouTube found in this pass

| Video | Useful for | Mark |
|---|---|---|
| Amazon Product Opportunity Explorer best practices https://youtube.com/watch?v=_fH9xYwKAkE | Filters: growing search volume + few top-clicked products; high click share with low conversion = unmet need | ◈ |
| DTC pre-order strategy https://youtube.com/watch?v=XeaBwLkiAa4 | Charge-later pre-orders as demand test | ◈ |
| Kettle & Fire $50 validation https://youtube.com/watch?v=-nvJIfQnidw | Landing-page test before product exists | ◇ founder claim |
| "20 minutes to find winning products" https://youtube.com/watch?v=XVxz6_xfi0Q | Keyword Planner + Trends + Shop app sold badge | ◈ |
| SmartScout vs FastMoss vs Kalodata https://youtube.com/watch?v=5Bw9zTCbvHg | Which TikTok tool covers what (FastMoss free; Kalodata creators; SmartScout Amazon↔TikTok) | ◈ |
| FastMoss product research https://youtube.com/watch?v=AhpFkQP7tgM | GMV (gross merchandise value) + week-over-week growth as the two filters | ◈ |

## 6. Proposed changes to our method

1. Add **Opportunity Explorer** as Tier 1 for Amazon demand, trend and newcomer success (needs a Professional seller account: owner decision, ~$40/mo).
2. Add **Shop app badge** as Tier 1 DTC volume floor; test on Earthly Derm, Everstride, Kaori.
3. Add **ImportYeti** for leader import curves and factory lookup; test on Everstride and Earthly Derm (expect gaps if they ship by air).
4. Use **EU/UK Ad Library data** for (a) spend ranges of leaders that also run in the EU/UK and (b) a dropout-inclusive newcomer survival rate in EU/UK markets (also serves the cross-market scan).
5. Add stage **"Test"** (smoke test / charge-later pre-order, pre-written kill thresholds) before any inventory order; its results calibrate our CPM and conversion assumptions.
6. Add **1-star share** and **brand-level top-3 share / HHI** to the crowding block.
7. Do not buy Jungle Scout / Helium 10 for sales estimates until Opportunity Explorer is tried.
