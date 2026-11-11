# Category verdict, method v2.0 (2026-11-07)

**Superseded** by v2.1 (`work/dossier/FINAL_V21.md`, 2026-11-08), then v2.2 (`work/audit/AUDIT_2026-11-09.md` §11, 2026-11-09). Kept as history.

All layers measured the same way for every category (see /RUNBOOK.md). Sources: `graveyard_table.py` (Amazon), `meta_stats.py` (Meta), `trends_v2.json` (Google Trends).

| Category | Amazon: to NEW brands /mo | NEW brand winners ≥1K | Amazon: to generics /mo | Meta active ads | Meta ads alive 90d+ | Trend (YoY vs controls) | Price $ | Verdict |
|---|---|---|---|---|---|---|---|---|
| Color-changing foundation | 212,600 | 3 (+19 generic) | 75,850 | 12,000 | 10% | ×4.0 growing | 30-40 | **#1 — every layer positive** |
| Body oil (crepey skin) | 29,650 | 4 | 2,350 | 11,000* | 10% | ×1.0 flat | 39-49 DTC | #2 — GODA shows a new brand can win big on both channels |
| Waterless scent diffuser | 8,300 (◇ AirScent counted as generic) | 2 (+4 generic) | 30,650 | 690 | 16% | ×2.1 growing | 80 | #3 — Meta/own-store play; Amazon is a generic price war |
| Beef tallow balm | 47,950 | 10 | 25,100 | 2,500 | 9% | ×1.06 flat | 20 (DTC 50) | #4 — most proven newcomer wins, but growth has stopped |
| Persimmon soap | 5,900 | 3 (+3 generic) | 14,850 | 2,700 | 5% | ×4.9 growing | 15 | #5 — fastest growth, small pie, low price, Meta ads die fast |
| Filtered shower head | 7,300 | 1 (+7 generic) | 21,000 | 1,200 | 20% | ×1.1 flat | 50 | reserve |
| Neck firming cream | ◇ invalid | — | — | 4,200 | 10% | ×1.2 | 98 | not ranked: category leaked face creams, "retinol" counted as a brand |
| Rosemary hair oil | 25,450 | 5 | 3,750 | 4,300 | 6% | ×0.76 falling | 15 | **dropped** (kill rule a) |
| Turmeric soap | 13,900 | 3 | 9,350 | 330 | 7% | ×0.68 falling | 12 | **dropped** (kill rule a) |

\* Meta phrase "crepey skin" also covers creams.

Who wins on both channels (new brands): color foundation — Luxe, Smooche, Prime Prometics; body oil — GODA; tallow — 10 new Amazon brands (Terra Lotus, Richgrand, Elbbub...) and Meta-long-lived Ancestral Cosmetics, Bare Ritual, byminus (correction 2026-11-08: Forge is on both channels but entered Amazon ~31 months ago, so it is an older entrant, not a new brand); persimmon — Kaori, Kakiyu (both 2-5 months old); diffuser — Meta: Scentify, Aura House, Hotel Collection, Aroma360.

Traffic: not used. Similarweb needs a login (owner's sign-in not finished). Hypestat gave estimates dated Feb 2025 – Apr 2026 from mixed sources (one was Semrush), not comparable across brands. Context only (◇): GODA ~2.2M visits/mo (Oct 2025), Forge ~162K (Feb 2025), Ancestral ~138K, Smooche ~105K (Jul 2025), Lumine Skin ~100K (Apr 2026), Aura House ~92K, Scentify ~25K.

Not covered: TikTok Shop, stopped Meta ads (BigSpy), margin/COGS, review curves for small shops.

## Brand-level ad longevity (Meta, US, active; `meta_brands.py` → `meta_brands.json`)

Exact-phrase search on the brand name; the pages/domains columns in the json show the phrase hits the brand's own ads.

| Category | Brand | Active ads | Alive 90d+ | Alive 180d+ | Reading |
|---|---|---|---|---|---|
| Color foundation | Prime Prometics | 3,800 | 730 (19%) | 350 | large, sustained spend → ads pay back |
| Color foundation | Smooche | 12,000 ◈ | 2,500 (21%) | 790 | same; count may include other "smooche" ads |
| Color foundation | Luxe ("Luxe Color") | 1,200 | 42 | 0 | ◇ phrase mixes advertorial pages |
| Body oil | GODA ("Goda Silk") | 930 | 100 (11%) | 0 | runs through creator pages; fast creative turnover |
| Body oil | DRMTLGY | 1,300 | 300 (23%) | 38 | |
| Tallow | Ancestral Cosmetics | 150 | 77 (51%) | 55 | evergreen winners |
| Tallow | Bare Ritual | 84 | 44 (52%) | 21 | evergreen winners |
| Tallow | Terra Lotus | 170 | 0 | 0 | Amazon winner, only now testing Meta |
| Tallow | Forge Men | 150 | 0 | 0 | rotates creatives |
| Diffuser | Scentify | 330 | 100 (30%) | 89 | evergreen |
| Diffuser | Aroma360 | 370 | 78 (21%) | 0 | |
| Diffuser | Aura House | 280 | 27 (10%) | 4 | |
| Diffuser | AirScent | 4 | 0 | 0 | not a Meta advertiser (Amazon-only) |
| Persimmon | Kaori | 850 | 210 (25%) | 58 | |
| Persimmon | Mirai Clinical | 130 | 20 (15%) | 18 | |
| Persimmon | Kakiyu | 760 | 0 | 0 | 2-month-old brand testing hard |
| Shower filter | sproos | 130 | 110 (85%) | 94 | very evergreen |
| Shower filter | Filterbaby | 630 | 100 (16%) | 7 | |

Reading: brand-level longevity confirms the ranking. Color foundation leaders run thousands of ads with hundreds alive 180d+ (money keeps flowing into ads that work). Tallow, diffuser and shower filter have small but very evergreen DTC advertisers.

Review growth: not obtained this pass. The Loox widget no longer shows review dates in its HTML (our earlier `loox_shop.py` parser finds none), and the Judge.me widget API now needs a store token (401). Totals only, e.g. GODA has 23,956 Loox reviews (◆, widget header).
