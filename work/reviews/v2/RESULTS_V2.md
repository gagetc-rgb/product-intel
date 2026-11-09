# Review curves v2 (2026-11-09)

Store-wide reviews per month for leader stores, read from the stores' public review widgets. Growth of reviews = proxy for growth of orders (shape only; review rates differ 3-5x between stores, so levels are not comparable across stores).

## How (two new routes)

1. **Judge.me** (`jm_curve.py`): public storefront feed `api.judge.me/reviews/all_reviews_js_based` (newest first, exact timestamps). It stops at page 40 = the latest 1,000 reviews. Older months: the same feed filtered to 1-4 stars goes years deeper (rarer reviews), and is scaled by the store's all-time ratio total / non-5-star (assumes a stable star mix, ◈). Months marked `~` are such estimates; the rest are exact counts.
2. **Loox with hidden dates** (`loox_photo.py`): the widget shows no dates, but each photo review's image URL contains its upload date (`images.loox.io/uploads/YYYY/M/D/`). Shop-wide feed paged with limit=100 gives a ~20% systematic sample. Result = curve of **photo reviews** only (◈ shape; ◇ if the store changes how it asks for photos).

3. **Okendo / Stamped / Yotpo / Junip** (owner allowed access on 2026-11-09): public storefront feeds, newest first, paged back to Jul 2024 → **exact** monthly counts.
   - `okendo_curve.py` — `api.okendo.io/v1/stores/{subscriberId}/reviews` (subscriberId read from the store page; the id found earlier by `detect.py` was wrong).
   - `paged_curve.py` — Stamped `stamped.io/api/widget/reviews` (storeUrl + public key) and Yotpo `api-cdn.yotpo.com/v1/widget/{appKey}/reviews.json`.
   - `junip_curve.py` — `api.juniphq.com/v1/product_reviews` with the public store key from the page.
   - DRMTLGY turned out to run Judge.me (not Okendo); Borboleta's Judge.me shop is `borboleta-consumer.myshopify.com` (the earlier domain was wrong).

Kaori has no review widget (Trustpilot only, see `../RESULTS.md`).

## Results, Aug-Oct 2026 vs Aug-Oct 2025

| Category | Store | Reviews total | Aug-Oct 2026 | Aug-Oct 2025 | Reading |
|---|---|---|---|---|---|
| Waterless diffuser | scentifyhome.com (Judge.me) | 2,104 | 245 (exact) | 123 (exact) | ◆ ×2.0 a year; Oct 2026 = 104, the best month on record |
| Beef tallow balm | terralotus.shop (Judge.me) | 4,358 | 2,171 (Aug ~1,347 est; Sep 488, Oct 336 exact) | ~130 est | ◈ explosive ramp Jun-Aug 2026, then falling Sep → Oct. ◇ quality flag: 43% of Sep reviews are below 5 stars (vs ~26% all-time) |
| Beef tallow balm | ancestralcosmetics.com (Judge.me) | 10,013 | Sep 345, Oct 488 exact | non-5★ basis: 82 vs 77 | ◈ flat year on year (~300-600/mo), mature |
| Beef tallow balm | try-forge.com (Judge.me) | 499 | 93 | 0 | ◆ small brand that started collecting in Jun 2026 |
| Beef tallow balm | wildgoldtallow.com (Judge.me) | 145 | 9 | 53 | ◆ faded after a 2025 peak |
| Body oil | goda.co (Loox photo reviews) | 19,819 | ~465 photo | ~90 photo | ◈ ×5; Oct 2026 the highest month in the sample (~270 photo reviews) |
| Color foundation | smooche.com (Loox photo reviews) | 47,519 | ~1,235 photo (almost all in Aug) | ~30 photo | ◇ photo reviews ~1,000-2,650/mo Apr-Aug 2026, then ~0 in Sep-Oct. A drop that abrupt is more likely a change in review collection than a sales collapse; unresolved |
| Waterless diffuser | aurahouse.com (Okendo) | 5,243 | 669 exact | 244 exact | ◆ ×2.7 store-wide; the diffuser product alone: Oct 2026 139 vs Oct 2025 26 (×5). ◇ Aug-Sep 2026 only ~20/mo (review requests apparently paused), then Oct 630 |
| Waterless diffuser | aroma360.com (Okendo) | 50,970 | 1,221 exact | 878 exact | ◈ ×1.4, but Oct 2026 (837) is driven by "free diffuser" promo offers; Aug-Sep alone flat (384 vs 645 → lower) |
| Persimmon soap | miraiclinical.com (Yotpo) | 7,216 | 947 exact | 471 exact | ◆ ×2.0; steady climb since early 2025 (Jan 2025 69 → Sep 2026 341). 16% below 5 stars |
| Shower filter | sproos.co (Junip) | 2,427 counted | 329 exact | 344 exact | ◆ flat ×0.96. Peak Jan-Apr 2026 (180-295/mo), now ~100/mo; reviews shifting to refill cartridges (subscription), i.e. fewer new devices |
| Body oil (store-wide, mostly other skincare) | drmtlgy.com (Judge.me) | 61,466 | ~908 (Sep-Oct exact) | ~3,376 est | ◈ ×0.27 falling store-wide; body oil is a small part of the range, so this says little about the category ◇ |
| Color foundation | primeprometics.com (Stamped) | 50,001+ | 4,912 exact | 4,662 exact | ◆ store flat ×1.05. The foundation product itself: Aug-Oct 2026 687 vs 690 (flat); monthly ~330 in Feb-May 2026 → 199 in Oct, drifting down. ◇ the public feed shows no reviews below 5 stars, so it is filtered |
| Lash serum | borboleta.com (Judge.me) | 1,286 | ~12 | ~1 | ◇ too small to read (single-digit months) |
| Color foundation | luxe.com (Judge.me) | 11,984 | 332 (Oct only) | ~1,022 est | ◇ gaps of several months with zero reviews; the store also runs Loox; Luxe sells mainly on Amazon. Not usable |

## What this changes

- Diffuser (#3): three stores now — Scentify ×2.0, Aura House ×2.7 (diffuser product ×5 Oct/Oct), Aroma360 ×1.4 (promo-driven). Agrees with search (Trends ×2.0). Strongest store-level confirmation of any category.
- Persimmon (#5): Mirai ×2.0, steady climb — consistent with search (×4.7).
- Color foundation (#1): the 2nd-largest store brand (Prime Prometics) is flat on the foundation product and drifting down since spring, while search is ×4.5. Growth is on Amazon / new brands rather than in the incumbent DTC stores ◈.
- Shower filter: Sproos flat and shifting to refill cartridges — matches the flat search (×1.09).
- Body oil (#2): GODA's growth is visible in its own store, consistent with 20,000/mo on Amazon.
- Tallow (#4): the category is mixed: one new brand (Terra Lotus) ramped hard this summer and is now cooling with weaker ratings; the older DTC leader (Ancestral) is flat; a 2025 entrant (Wild Gold) faded. Matches the flat search trend (×1.04).
- Color foundation, other stores: Smooche anomaly (photo reviews stop after Aug), Luxe unusable.
- Kaori (persimmon): no widget, still no data.
