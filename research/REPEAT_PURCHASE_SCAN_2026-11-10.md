# Repeat-purchase scan of the whole video corpus (2026-11-10)

Question (owner): did we miss products with a built-in repeat purchase, including "razor and blade" ones, now that most of the top 20 turned out not worth entering?

## What was read

- `work/videos_included.json`: briefs of all 138 videos (product, category, the author's reasoning). Full transcripts exist on this PC for 9 videos only; NotebookLM is not connected here.
- `work/blind/blind_rank.csv`: the category-level pass of 2026-11-07 over all 94 physical products of the corpus (Amazon "bought in past month" over the top 20 results, TikTok Shop lifetime sold, Meta ads by one phrase).

Limit that matters: the numbers below come from that early pass. It used one search phrase per product and the Meta counts by phrase, the two things we later found error-prone (`METRICS.md` section K). So this is a list of what to re-measure, not a set of verdicts. ◈ throughout.

## Result: nothing with repeat purchase was overlooked entirely, but five were set aside for reasons that no longer hold

Every repeat-purchase product of the corpus was measured on 2026-11-07. Five of them were dropped by rules we have since replaced, or were measured with a phrase that missed the product.

### A. Re-measure first

| Product | Repeat type | 2026-11-07 numbers | Why it was set aside | Why look again |
|---|---|---|---|---|
| Collagen overnight wrapping mask | Consumable: packs of 4-5, used weekly | Amazon 141K/mo, 9 listings at 1K+; TikTok 262K sold; Meta 2,500 ads, 210 aged 180+, 13 advertisers with 180+ day ads | Labelled "brand-owned" (K-beauty) without measuring newcomers; Meta phrase flagged noisy | Largest unexamined consumable in the corpus. Newcomer rate and follower stores were never computed |
| Work insoles | Semi-consumable: replaced every 3-6 months, several pairs per buyer | Amazon 93K/mo, 8 at 1K+; Meta 34 ads by the phrase "work insoles for construction workers" | "Dr. Scholl's owns it; no Meta ads" | The Meta phrase was too narrow. An outside study (the 38-product site) names two young stores, Stepprs and OrthoFlexx, with hundreds of long-running ads; unverified, but cheap to check by domain |
| Enzyme pet odor remover (fogger + enzyme refills) | Razor and blade: device plus refills | Amazon 15.7K/mo, 4 at 1K+; Meta 3,900 ads, 80 aged 180+, 8 advertisers with 180+ day ads | Small on Amazon, so it never reached the top 20 | For the "own store + ads" model the Meta signal is what counts, and it is strong here |
| Silvervine (matatabi) cat dental chew | Consumable | Amazon 2.3K/mo; TikTok 20.8K; Meta 690 ads, 52 aged 180+, 3 advertisers | Dropped on site traffic (~19K visits), a measure we later abandoned as unreliable for small stores | Sold through own stores, not Amazon; two videos; needs the by-domain check |
| Natural rodent repellent pouches | Consumable: replaced every 30-90 days | Amazon 21K/mo; TikTok 140K; Meta 9,300 ads, 1 aged 180+ | Every ad was young on 2026-11-07; needs pesticide registration (EPA exemption for essential oils exists, most states still require registration) | A category that was three months old then. Check whether its ads now pass 90 days. Compliance cost must be priced first |

### B. Second line

| Product | Repeat type | 2026-11-07 numbers | Note |
|---|---|---|---|
| Pet calming pheromone diffuser (device + monthly refill) | Razor and blade | Amazon 22K/mo; Meta 620 ads, 0 aged 180+ | Three videos, but weak ad evidence; old brands (Adaptil, Feliway) |
| Cat calming pheromone collar | Consumable: 30-60 days | Amazon 12.6K/mo, 7 at 1K+; Meta 1,100 ads, 7 aged 180+ | Same family as the diffuser; measure them together |
| Micro-infusion kit (stamp + serum refills) | Razor and blade | Amazon 6K/mo; Meta 6,500 ads, 130 aged 180+, 7 advertisers | Strong ad evidence; a microneedling device with skin claims is a regulated medical device. Price the compliance first |
| Hair-growth inhibitor serum (Cyperus oil) | Consumable | TikTok 597K sold; Amazon 0.4K; Meta 51 ads | A TikTok Shop product, not a Facebook one. Outside the investor's channel |

### C. Looked at and left out

| Product | Why |
|---|---|
| Collagen multi-balm stick (Amazon 195K, TikTok 1.2M) | Held by K-beauty brands (medicube, Dr.Melaxin) |
| Ceramide cleanser, body mousse-to-oil, wrinkle primer | Large on Amazon, almost no own-store advertisers: not the investor's game |
| Pheromone perfume oil (4 videos) | The core promise cannot be substantiated |
| Berberine patches, neuropathy cream, herbal "quit smoking" inhaler, acne kit | Drug or disease claims |
| No-rinse paw cleaner foam (3 videos) | Weak in every channel (Amazon 6K, Meta 60 ads) |
| Dissolving microneedle eye patches, pet calming stickers | Almost no demand |
| Leak-proof men's underwear | Checked earlier: FDA registration, small demand |

## Repeat purchase inside the current 20

- Razor and blade: shower filter (cartridges), pet fountain (filters), scent diffuser (oils).
- Plain consumables: tallow balm, both soaps, lash and hair serums, body oil, foundation, pore patches, whitening powder, magnesium spray, hair removal cream.
- Bought once or rarely: chin wrap, exfoliating towel, compression socks (several pairs, then slow).

## What to do with this

1. Add the five A products to the Codex pull (done: `work/prompts/CODEX_SCRAPE_LENS_M.md`, section "Additional products").
2. Repeat purchase itself is still not measured for any product (metric M5). The public traces are: subscription offered and pre-selected in the leader's store, refill SKUs, the share of the leader's ads and reviews that are about refills.
3. A product enters the report only after the same checks as the 20: keyword card, relevance of the phrase, followers by domain, money in an own store, what may be claimed.
