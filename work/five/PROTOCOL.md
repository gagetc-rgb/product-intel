# Method proof on five products (started 2026-11-10)

Owner's rule: prove each metric on these five until there is no doubt, keep what is representative, drop the rest; only then roll out to other categories.
Products = the site's current top 5: pet water fountain, color-changing foundation, lash serum, tallow balm, shower filter.

For each metric: what it claims → how we test that it measures that → pass condition → status.

| Metric | Claims | Test on the five | Pass if | Status |
|---|---|---|---|---|
| Category definition (K1) | the product form we would sell | one card per product: form, price band, in/out examples | owner agrees with each card | to do |
| A1 search growth | demand for the product is rising | related queries, phrasings summed in one request, 3 pulls, controls | related queries mostly the product; spread across phrasings and pulls small | done 2026-11-10: fountain, lash, tallow, shower pass; foundation = brand search (read with ads, K5) |
| A2 Amazon volume | units/month of the product | read the top 25 included and top 5 excluded listings by hand | ≥80% of units are the product; no big product left out | done: lash filter fixed (Babe in, castor out), fountain (refill filters out) |
| B1/B2 newcomer success | share of new sellers that reach 1,000+/mo | read every entrant at 300+/mo by hand (`work/audit/five_winners.txt`) | each entrant is a real new seller of the product | **fails on identity**: fountain and foundation entrants are almost all unbranded; one seller may hold several listings and old sellers can relist. Title-based merging over-merges (24 different foundation listings merged into one). Needs seller ID / brand from the product page (Keepa or an Amazon task) |
| Brand age | the entrant is a young business | published sources: brand site, USPTO trademark filing date, first reviews | two sources agree | automatic version dropped (homonyms); by hand: Luxe, Smooche, Prime, Magichome old. To do for named entrants (tallow has many) |
| B7 growing newcomers | steady growth at any level | monthly-sold or sales-rank history per entrant | curves readable for ≥80% of entrants | needs Keepa |
| B8 growth that pays | same creative alive 90+ days | Meta by entrant's landing domain | domain found for named entrants | to do |
| B9 graveyard | who entered and disappeared | Keepa listed-since + history; Wayback best-seller pages a year ago | a dated list of dead entrants per category | needs Keepa |
| K4 share of search | young brands gaining attention | brands in one Trends request | the brand names are not homonyms (related queries) | done: Selene (fountain), Terra Lotus (tallow), Filter Baby / Sproos (shower), Hanae (lash) |

Method version: METRICS.md v2.3 (frozen 2026-11-10). New rows from v2.3: branded vs unbranded B1, brand premium B10, revenue bar, groups with intervals, absolute floor, D6 compliance (first reading done: `research/ENTRY_REQUIREMENTS_US_2026-11-10.md`), control categories, back-test, money test with legal claims.

Next steps, in order:
1. Category cards (K1) for the five, owner approves.
2. Seller identity for entrants: Keepa (brand, sellerIds, listed-since, monthly-sold history) once the owner buys it; until then do not quote B1 as more than an upper bound.
3. Brand age of named entrants from published sources (brand site, USPTO, first reviews), with subagents and Keenable (added to `~/.claude.json` 2026-11-10; available from the next session).
4. B8 for named entrants by landing domain.
5. Control categories (3-5, not from the source channel) through the same steps.
6. Back-test on November 2025 once Keepa is in.
7. Contractor quotes for D6 (shower flow test and California listing, cosmetic label review, insurance).
