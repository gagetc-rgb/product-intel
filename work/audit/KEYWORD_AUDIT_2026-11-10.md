# Keyword audit of the v2.2 top 5 (METRICS.md section K), 2026-11-10

Owner's request after the CarPlay error. Nothing on the site was changed. The corrected filters below were written **after seeing results** (K8) and are proposals until the owner accepts them.

## Verdict per category

| Category | Search (A1) holds? | Amazon filter (K2) | Newcomer rate B1, was → corrected | Brand layer (K3/K4) | Reading |
|---|---|---|---|---|---|
| Pet water fountain | ◆ yes: 1.44-1.47 in 3 pulls; summed phrasings 1.44 ("cat fountain" is 44% of searches, "pet water fountain" only 11%) | 95% on-target; replacement filters slipped in ("Filter Replacement", "50 Pack … Filters") | 26.9% → **25.0%** (25 of 100) | Selene: 0% → 17% share of brand search in a year; also an Amazon newcomer at 1,000+/mo (5 months). Layers agree | Holds |
| Color-changing foundation | ◆ number holds (4.4-4.7; summed 4.5), but the phrase is navigational: related queries are Luxe, Smooche, Prime, "is luxe legit", "where to buy luxe" | 82% on-target | 27.1% → **22.2%**: Luxe, Smooche, Prime Prometics were counted as newcomers (their listings are 9-10 months old; the businesses date from 2020-2021) | 3 brands own the search; Luxe and Smooche went from ~0 in 2025 | The growth is these brands' ad campaigns, not an open market. Concentration HHI 2,403, top 3 = 65% |
| Lash serum | ◆ yes: 1.17 in 3 pulls; summed 1.12 | **Errors both ways**: Babe Lash (30K/mo, a leader) dropped by the stop word "extension" ("safe for Extensions"); castor oil and brow-only serums counted as lash serum | 16.4% → **8.0%** (4 of 50); HHI 775 → 1,119, top 3 35% → 49% | Babe 57% + Grande 40% of brand search; Hanae 0 → 3% | Weakest of the five after the fix |
| Tallow balm | ◆ "tallow balm" 1.04 in 3 pulls; "beef tallow for skin" 0.53; METRICS keeps the combined 0.78 | 90% on-target | 13.4% → **13.4%** | Based Supplies 82% (DTC), Terra Lotus 11% → 18% | Holds |
| Shower filter | ◆ 1.10-1.19 for every phrasing; summed 1.15 | 75% on-target (by design: inline filters such as Aquabliss are excluded) | 12.7% → **11.3%**: Magichome (sells since 2019) was a newcomer | Filter Baby 39% → 52%, Sproos 4% → 10% | Holds, but layers measure different things: the search phrase includes inline filters and generic "shower head" / "water filter"; Amazon counts only shower heads with a filter |

Spikes (K6): every category, and both control terms, jump in Mar-Apr 2026. That is the known Google Trends artifact (RUNBOOK v2.0 note), not demand.

## Problems the audit found in the method itself

1. **Listing age ≠ business age.** B1 takes the age of the Amazon listing. Old brands with new listings count as newcomers unless they are on the hand list `graveyard_table.EST`. It missed Luxe, Smooche, Prime Prometics and Magichome; other categories need the same check.
2. **Unbranded listings.** 34-106 of the entrants per category have no brand parsed, so every ASIN counts as a separate seller. One seller with several listings inflates both entrants and winners. This needs the brand or seller from the product page (Amazon task).
3. **Meta phrase for fountains is "water fountain".** That matches garden and decor fountains. B4 for this category was empty, so no number on the site depends on it, but it should be "cat water fountain" / "pet water fountain" or the leaders' domains.
4. **Category phrase = brand phrase.** For the foundation the category search is brand searches for three advertisers. Rule K5 (read it next to their ad volume) applies.

## If the corrections are accepted

Order by B1 among the five: fountain 25.0%, foundation 22.2%, tallow 13.4%, shower 11.3%, lash 8.0%. The reserve (hair serum, body oil, persimmon soap) and the other 12 categories have not been re-checked with K yet, so lash serum cannot simply be replaced; the whole table needs the same pass.

## Pass over all 20 (same day, owner's go-ahead)

Amazon recompute: `k_recompute.py` → `k_recompute.json`. Three variants: v22 = as on the site; filt = corrected title filters; full = filt + verified old brands removed + identical unbranded titles merged into one seller.

| Rank v22 → filt → full | Category | B1 v22 → full | What changed |
|---|---|---|---|
| 1 → 1 → 1 | Pet water fountain | 26.9% → 24.1% | replacement filters out; merged look-alike listings |
| 2 → 2 → 2 | Hair growth serum | 27.8% → 28.6% | castor/eyelash/brow out. Overlaps rosemary oil (same rosemary sprays) |
| 3 → 3 → 3 | Color-changing foundation | 27.1% → 25.0% | Luxe, Smooche, Prime out of newcomers |
| 4 → 4 → 4 | Tallow balm | 13.4% → 16.5% | look-alike listings merged |
| 6 → 6 → 5 | Rosemary oil | 15.9% → 16.3% | |
| 11 → 8 → 6 | Persimmon soap | 10.4% → 12.0% | Kakiyu, Morovan old |
| 7 → 5 → 7 | Shower filter | 12.7% → 12.0% | Magichome old |
| 12 → 9 → 8 | Turmeric soap | 8.7% → 8.4% | |
| 8 → 7 → 9 | Compression socks | 20.0% → 12.0% | 177 of 238 listings were saved with the brand as title and dropped (165K units/mo); now counted |
| 5 → 12 → 12 | Lash serum | 16.4% → 8.7% | Babe back in; castor oil and brow serums out |
| 9 → 15 → 14 | Body oil | 12.8% → 7.1% | generic body oils (Palmer's, Neutrogena, Aveeno, vitamin E oil) out; firming/crepey only |
| 10 → 20 → 20 | Pre-wash hair oil | 13.8% → 0.0% | the filter's "hair oil" counted every hair oil (OGX, Moroccanoil, OUAI) |
| 16 → 16 → 16 | Hair removal cream | 8.7% → 6.5% | "Depilatory" matched the stop word "epilator"; men's No Hair Crew back in |
| others | chin wrap, whitening powder, exfoliating towel, magnesium spray, neck cream, scent diffuser, pore patches | small moves | |

Stable in every variant: fountain, hair serum, foundation, tallow are the top 4. Places 5-9 reshuffle (rosemary oil, persimmon soap, shower filter, turmeric soap, socks): their order is within noise.

The automatic brand-age check (`brand_age.py`) fell for homonyms: it took copper.com, gentle.com, living.com, california.com for sellers' sites. Old brands were therefore taken only from a hand-verified list (14 brands, in `k_recompute.py`).

Trends related queries for the 15 other A1 phrases (`trends_pulls/related_rest_2026-11-10.json`):

| A1 phrase | What people actually search | Use as A1? |
|---|---|---|
| double chin (chin wrap) | "get rid of double chin", surgery, Kybella, exercises | **no**: a body feature, not the product |
| crepey skin (body oil) | crepey-skin lotions and creams, DRMTLGY | **no**: the need, mostly creams |
| waterless diffuser | top = "oil diffuser", "essential oil diffuser" (ultrasonic) | weak: generic diffusers |
| magnesium spray | "magnesium glycinate" (a supplement) high and rising | weak: supplement noise |
| pore patches | "pimple patches", "eye patches", medicube | weak |
| pre wash hair oil | 2 related queries only | too rare |
| persimmon soap | brand names (Mirai, Swarva, Kaori breakout), "is persimmon soap a hoax" | brand-navigational; read with ads (K5) |
| rosemary oil for hair | dominated by Mielle | brand-led |
| turmeric soap | "kojic turmeric soap" on top | the market is kojic bars |
| hair growth serum, compression socks, exfoliating towel, hair removal cream, neck cream, teeth whitening powder | on-target; young brands rising (Cura, Lilyeve, Aparthy; Hushed, Hollow; Alorin) | yes |

## Which methods stay (owner, 2026-11-10: keep what is representative, drop the rest)

Keep:
- Amazon newcomer metrics (B1/B2/B3) with strict title filters, a manual read of the top listings per category, and brand age checked by hand.
- Trends A1 only for phrases whose related queries are mostly the product; phrasings summed in one request; mean of 3 pulls.
- Brand share of search (K4), brands in one request.
- Meta by the shop's landing domain.
- Store review curves only where reviews are organic (not imported batches).

Drop:
- Meta counts by category phrase (dealers, clinics, garden fountains).
- Trends on symptoms or body features as demand (double chin, crepey skin).
- Automatic brand age by guessed domain.
- A single TikTok keyword page as a sales figure.

## Files

- Trends: `work/blind/trends_pulls/pull3_2026-11-10.txt` (pull 3 exists), `sum_*_2026-11-10.txt` (phrasings in one request), `brands_*_2026-11-10.txt` (brands in one request), `related_top5_2026-11-10.json` (related queries; script `trends_related_pw.py`).
- Amazon recompute: inline in this session from `work/blind/graveyard_us/*.json`; corrected filters for lash serum and fountain are in the table above (not yet written into `graveyard_def.py`).
