# RUNBOOK — category evaluation, method v2.0 (frozen 2026-11-07)

Goal: anyone can rerun this and get the same ranking (numbers drift with live data; order should not jump).
Method changes only by a version bump (v2.1, v3.0...) with the reason written below. Results from different versions are never compared or mixed.

## What is measured (and what is not)

| Layer | Question | Source | Tier |
|---|---|---|---|
| A. Amazon shelf | How much demand, and how much of it went to NEW independent brands in the last 24 months? | Amazon search pages 1-5, search cards only | 1 (badge = platform count, floor) + ASIN dating |
| B. Meta ads | How many ads run, what share has lived 90+ / 180+ days, which shops keep ads alive? | Meta Ad Library, US, active, exact phrase | 1 (counts) + sample (who) |
| C. Traffic | Do the leaders get web traffic? | Similarweb (needs the owner's login) | 2 (modelled) — NOT DONE in v2.0 |

Not visible in v2.0: stopped Meta ads (US library shows active only → the "graveyard" of ads needs BigSpy or an own archive), TikTok Shop, trends over time (one snapshot).

## Frozen definitions

- Category = the product FORM we would sell: `work/blind/graveyard_def.py` (`STRICT`, title regex MUST + NOT). Written before the data was looked at.
- Amazon query per category: `work/blind/products.py` (5th field). Meta phrase: same file (4th field), exact-phrase search.
- Entry date of a listing: ASIN order, calibrated on dated listings (`graveyard_stats.py`, error about ±1-2 months).
- Brand: Amazon byline if known, else the first title word if it is not a generic product word (`GEN` in `graveyard_stats2.py`); else the listing is a stand-alone generic seller.
- NEW = brand entered < 24 months ago AND not an older brand entering a new category (`EST` list in `graveyard_table.py`).
- Winner = a listing with "bought in past month" ≥ 1,000.
- Meta store = registrable landing domain; persona pages pointing to the same shop count once (`meta_stats.py`).
- "Lives" = an active ad started ≥ 90 days ago.

## Steps

```
cd work/blind
python graveyard_search.py "pid=amazon query" ...     # writes graveyard/<pid>.json (slow pacing; stops on any robot check, no bypass)
python graveyard_table.py                              # Amazon layer table -> graveyard/table_v2.json
python meta_ages.py "pid=meta phrase" ...              # writes meta_ages/<pid>.json
python meta_stats.py                                   # Meta layer -> meta_ages/summary.json
```

## Reading rules (decided before results)

1. Demand = Amazon shelf units (floor) — Meta active ads are a signal of competition, not of demand.
2. Openness for us = units taken by NEW named brands + count of NEW brand winners. Units taken by generics = price war (good for a cheap Amazon seller, bad for a brand).
3. Strongest evidence = independent new winners on BOTH Amazon and Meta.
4. Meta 90d+ share: high = evergreen market where ads that work keep running; low = many short tests that fail.
5. Kill rules: a category drops if (a) demand is falling: Google Trends US, last 12 full weeks vs the same 12 weeks a year ago (YoY) < 0.8, or (b) new-brand units < 10,000/mo AND no shop with a 90d+ Meta ad.
6. Trend labels (Google Trends US, 5 years, weekly, partial last week dropped): YoY >= 1.2 growing; 0.8-1.2 flat; < 0.8 falling. Warning flag "post-spike" if the last 12 weeks are < 50% of the best 4-week average (a viral peak has passed). YoY is used instead of the last-3-months change because these products are seasonal and spiky (v2.0 amendment written after seeing only the tallow curve, before the other eight).

## How to check by hand (independent verification)

- Amazon: search the query, look at page 1: count listings with "bought in past month", note ASINs. An ASIN starting B0G/B0H is from 2026, B0F from 2025, B0D from 2024.
- Meta: open `facebook.com/ads/library`, country US, active ads, exact phrase "<phrase>"; the result count is at the top. Add "start date: before <today-90d>" — that count is the 90d+ number.

## Version log

- v2.1 addendum 2 (2026-11-08): accents are folded before brand matching ('L'Oréal' and 'L'Oreal' were two brands). Only color foundation's old-brand split moved (L'Oreal 6,000+3,000 merged); new-brand units unchanged.

- v2.1 addendum (2026-11-08): the 4 categories collected manually by the owner (US ZIP, AMAZON_TASK.md) use the same rules; GEN += their product words (lash, eyelash, brow, castor, biotin, rice, batana, scalp, shampoo, wash, pre, teeth...), EST += revitalash, olaplex, dralthea (long-established brands with recent ASINs). Done after a first look at their brand list, before final reading; disclosed.

- Data-collection rule (2026-11-08, owner decision): Amazon stays a primary layer; all Amazon data collected so far is kept. After amazon.com showed an 'unauthorized AI agent' notice, Claude no longer collects from Amazon automatically. New Amazon data (the 4 categories missing from the US-ZIP scan, re-scans) is gathered by the owner or an assistant, or a licensed tool, following a written task, and processed with the same v2.1 scripts.

- v2.1 (2026-11-08): (1) neck_cream form tightened to products sold for the neck (face creams that also mention the neck excluded; old rule kept as STRICT_V20_NECK); (2) GEN += retinol, retinal, pdrn, collagen, nad, peptide(s), hyaluronic, tighten(ing) — ingredient words were read as brands; (3) a leading 'The' is skipped when the brand is taken from the title ('The AirScent' -> airscent). Rules written before re-reading results. Output graveyard/table_v2.1.json; v2.0 kept as table_v2.0.json. Changes vs v2.0: diffuser new-brand units 8,300 -> 19,400 (winners 2 -> 3); neck cream shelf 210,750 -> 96,450, new-brand units 22,800 -> 7,500; body oil 29,650 -> 28,600; tallow, dog fountain, chin wrap +-1,000. All other categories unchanged.

- v1 (pilot, invalid): off-target forms leaked in; product pages failed and brands were title-guessed.
- v2.0 data note (2026-11-07): neck cream is NOT ranked — its STRICT filter lets face creams that mention the neck through, and the generic word 'retinol' was read as a brand. Fix needs v2.1 (tighter filter + GEN words). Diffuser: titles starting 'The AirScent' were counted as generic (brand known), so its new-brand units are understated.
- v2.0 trend note (2026-11-07): control terms 'shampoo' and 'body lotion' spike in Apr-Jun 2026 exactly like our terms, so that spike is a Google Trends artifact. The post-spike flag is void for 2026, and YoY is divided by the controls' mean YoY (1.14) before applying rule 6. Raw and adjusted values: work/blind/trends_v2.json.
- v2.0 (2026-11-07): strict forms; search-card data; new brands vs generics split; Meta 90/180-day counts + stratified sample grouped by shop domain.
