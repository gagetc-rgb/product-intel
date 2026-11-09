# Next task (set 2026-11-07, before context compaction)

Read `CONCLUSIONS.md` first, then this file. Data and scripts live in `work/` (`market_system.py` is the latest model).

## Owner's instructions for the next stage

1. **Re-check every brand we marked "small traffic"** (tennis bracelet/MLMT, chin wrap/Skult, seat cushion/Travlr, ski sleeve/SkiGuards, silvervine/Purriq, 16-head massager/Alythera+Zevessa, Kakiyu). Our traffic tools may undercount them (see "Why traffic tools fail").
2. **Lift the regulatory exclusions.** Move those products into a separate "needs compliance" group with the route and its cost. Excluded for good: products that are banned, or whose core promise is false. Supplements and ingestibles stay excluded until the owner returns to them.
3. **Seasonal products form their own group** (ski sleeve, tanning balm, dog car fan…), judged in season.
4. **Brand search is context, not a filter.** People may search little and still buy a lot.
5. **Primary signals:**
   - Is traffic growing?
   - How many ads, and how many have run for a long time (90+ / 180+ days)? Many long-running ads usually mean it works.
   - Can we verify sales another way?
6. **New question: which product ideas are the strongest in absolute terms?** Ignore competition and difficulty of entry; look at repeat-purchase potential and margin.

## Why traffic tools fail (to explain and to correct for)

- **SimilarWeb** estimates traffic from a panel (browser extensions, partner clickstream, ISP data) and only knows exact numbers for sites that connected Google Analytics. Below ~50-100K visits a month the panel sample is small, so numbers are noisy or missing. Example: Skult's "visitors" show up as Argentina/France while its ads target the US.
- **Meta-driven DTC traffic is mostly mobile, inside the Facebook/Instagram in-app browser,** which panels capture poorly (◈ likely). Ad-driven stores are therefore systematically undercounted.
- **Semrush** has two products. "Traffic Analytics" is clickstream-based like SimilarWeb, with the same weakness; it labels in-app traffic "Direct" (Earthly Derm ~90% direct). The "organic traffic" in its SEO cards is modelled from Google rankings × CTR and only covers Google organic search; for an ad-driven store it is near zero by design.
- **Multi-domain funnels.** Ads often land on advertorial or offer subdomains (try., offer., shop., order.), separate lander domains or checkout domains. The tools count per host, so the store's traffic is split.

## Better cross-checks to use

1. **Review velocity.** New reviews per month on Trustpilot, Judge.me/Okendo/Loox widgets on product pages, and Amazon listings, compared month to month. Only ~1-5% of buyers leave a review, so reviews × 20-100 gives an order range.
2. **All landing domains of a brand.** Collect every link host in its Ad Library ads and sum their traffic.
3. **Ad volume and age (Ad Library):** total, 30/90/180+ days, plus new ads per week (snapshot weekly). A growing pool of old ads means profitable scaling.
4. **Other channels:** TikTok Shop GMV (FastMoss/Kalodata/EchoTik free tiers), Amazon BSR (indexed pages, Keepa), Instagram/TikTok follower growth.
5. **Shopify store signals:** `/products.json` (catalogue, launch dates, price changes), the date the domain was registered, and the store's own "X sold" or "X customers" claims (treat as claims).

## History: how to look back in time (tested 2026-11-07)

### Reviews: rebuild the curve from review dates (works, no snapshots needed)
- Every review in Loox / Judge.me / Yotpo / Stamped / Trustpilot carries its date, so the past can be rebuilt today.
- **Loox (tested):**
  - client id: `https://loox.io/widget/loox.js?shop=<x>.myshopify.com` → `LOOX.clientId`. The myshopify domain is in the store's homepage HTML.
  - hash: `loox_global_hash` in the store HTML.
  - product id: `"id":<13 digits>` in the product page HTML.
  - pages: `https://loox.io/widget/<clientId>/reviews/<productId>?h=<hash>&page=N&sort=newest`, 15 reviews per page.
- **Judge.me (tested):** `https://judge.me/reviews/reviews_for_widget?url=<shop>&shop_domain=<shop>&platform=shopify&page=N&per_page=20&product_id=<id>&sort_by=created_at&sort_dir=desc` returns `total_count` and exact timestamps.
  - It stops at 1,000 reviews: deeper pages repeat, so de-duplicate by review id.
  - Tool: `work/review_fetch.py`.
- Some Loox widgets hide dates (Glo Melanin).
- **Method:** take every Nth page and record the date of its first review. `work/review_curve.py` turns the page→date pairs into reviews per month.
- **Caveats:**
  - Reviews lag orders by ~2-4 weeks, so the latest month reads low.
  - Review-request emails or incentives can change the review rate, which moves the curve without any change in sales.
  - Imported, deleted or merged products distort it.
  - Check for the "Verified" share.

- **First results** (samples and curves in `work/reviews/`):
  - **Earthly Derm, turmeric bar, 6.9K reviews:**
    - reviews per month: ~75-95 in Oct 2025-Feb 2026, ~290 in Apr 2026, ~570 in Jul, ~900 in Sep, ~850 in Oct;
    - this matches the SimilarWeb traffic rise (269K → 913K) and implies a review rate of ~3-5% of orders (◈).
  - **Everstride, bamboo socks, 29K reviews, all on one product page:**
    - ~3,800-4,200 reviews per month in Jul-Sep 2026, almost all "Verified";
    - against SimilarWeb's 330K visits × 2-3% ≈ 7-10K orders, that would be a 40-60% review rate, which is implausible;
    - so SimilarWeb probably undercounts Everstride several times over (◈), and the YouTuber's revenue claim (~7× our band) may be closer to the truth than our band.
  - Earthly Derm's Sep-Oct reviews do not fall, so the September traffic spike is not just one viral moment (◈).

### Snapshots of pages (Wayback Machine)
- CDX API: `https://web.archive.org/cdx/search/cdx?url=<page>&output=json&collapse=timestamp:6`.
- For our DTC stores it is sparse (Everstride product page: 1 snapshot; Earthly Derm: 2). Use it only to read a review count or price at one past date.

### Meta Ad Library history
- US commercial ads vanish from the library when they stop. Meta keeps no archive of them, and the API does not return them.
- History exists only:
  1. **EU/UK loophole:** if the brand's ads were also delivered in the EU or UK, they stay searchable for 1 year after the last impression, with reach. Set country to an EU country or GB and status to inactive/all.
     - Tested: GB with "persimmon soap" shows both active and inactive ads (kakiyucare.com, swarva.com, clones), with start dates.
  2. **Paid spy tools,** which keep copies they captured while the ads were live: Foreplay Spyder (tracks brands you add, from that day on; Workflow plan ~$175/mo), BigSpy (deepest archive; $69/mo, free 5 searches/day), AdSpy ($149/mo). Their coverage of a given small brand is unknown until checked.
  3. **Our own weekly archive,** from now on (see HANDOFF plan step 1).
  4. **Survivor curve:** today's active ads by start month. It shows only the ads that survived, not the ones that were stopped.

## The "needs compliance" group (no longer excluded)

| Product | Route | Main cost/risk |
|---|---|---|
| LED / red-light mask | Private-label a device whose OEM already holds a 510(k) for wrinkles or acne; label "manufactured for" | Brand-dominated; OEM quality; claims must match the K-number |
| EMS neck massager | OEM with 510(k) for OTC TENS/EMS pain relief | Same as above |
| Leak-proof incontinence boxers | FDA establishment registration (~$11.4K/yr) or buy from a registered US supplier | Fee; real absorbency must match claims |
| Rodent repellent pouches | EPA 25(b) minimum-risk formula + state registrations | Paperwork and money for each state |
| Lash serum | Cosmetic peptide formula, no prostaglandin analogs, appearance claims only | Claims discipline |
| Hair-growth serum | OTC minoxidil under the FDA monograph (drug facts label, registered drug establishment), or a cosmetic "thicker-looking hair" formula | Drug registration if minoxidil |
| Neuropathy / nerve-pain cream | OTC topical analgesic monograph (menthol, lidocaine…) with a compliant label | Drug registration; no disease claims |
| Turmeric / dark-spot soap | Cosmetic wording only ("evens the look of tone") | Claims discipline |
| Enzyme pet-odor spray | No antimicrobial claims, or EPA registration | Claims or registration |
| Kids products (microscope, BT headband) | CPSIA third-party testing + Children's Product Certificate; FCC for Bluetooth | Testing cost per SKU |

Still excluded:
- infant sleep positioner (CPSC/federal ban);
- red-light "hearing restoration" (false core claim);
- berberine "Ozempic" patches and smoking-cessation inhalers (drug claims with no realistic route; revisit with supplements);
- microneedling devices (medical device, high risk).

## Seasonal group

Ski shin sleeve (Dec-Feb), tanning balm (Apr-Aug), dog car fan (Jun-Aug). Judge each with last season's data: Ad Library ads started in that window, last season's traffic peak, and Trends seasonality.

## "Strongest ideas in absolute terms" (to evaluate next)

The best economics come from:
- **refill / razor-and-blade models**: device + consumable;
- **daily-use consumables** with tiny cost of goods;
- **high-AOV products** with huge markup.

Candidates from the corpus:
- refill models: scent diffuser + fragrance oils; filtered shower head + cartridges; pet calming diffuser + refills; rodent pouches;
- daily consumables: soaps (turmeric, persimmon); balms, oils and serums (tallow, body oil, lash serum, collagen stick); teeth-whitening powder; hair-removal cream; nose patches; cat chews; puppy pads and paw cleaner; compression socks and leak-proof underwear (replacement cycle);
- high AOV: LED mask ($150-400, cost $20-40); 16-head massager (~$140, cost ~$15); carry-on duffel ($129, cost ~$19).

Rank them by gross margin %, repeat cycle (days), and 12-month LTV/CAC potential. Then cross with the evidence (ads by age, traffic trend, review velocity).
