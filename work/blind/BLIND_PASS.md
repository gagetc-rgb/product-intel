# Blind pass over every product in the corpus (2026-11-07)

Why: the owner suspected model bias. The earlier "take" list (turmeric soap, persimmon soap) matched products the owner had named, so this pass re-ranks **every** physical product in the corpus with fixed, mechanical rules and no input from earlier verdicts.

Files: `products.py` (universe + keywords), `amz_scan.py`, `meta_scan*.py`, `tiktok.py`, `amz_filter.py`, `score.py` → `blind_rank.md` / `blind_rank.csv` (full tables).

## Universe

- 173 analysed videos + 7 excluded by title → **94 non-ingestible products** (MAIN) and **30 supplements** (SUPP), incl. products from mixed videos that were excluded earlier (rosemary roll-on, mouth tape, inflatable tent, flea spray…) and the 7 supplement videos that had no analysis (identified from live transcripts: magnesium glycinate gummies, Ceylon cinnamon + MCT, parasite cleanse, NAC, dog probiotics, Hormone Harmony, Beyond Alpha).
- Left out: digital products, courses, methodology-only videos. Excluded for good: infant sleep positioner (banned), red-light "hearing restoration" (false core claim).

## Signals (category level, not one brand)

| Channel | What | Source | Why it matters |
|---|---|---|---|
| AMZ | Sum of "bought in past month" badges across top-20 organic results, on-target titles only | Amazon US search (headless) | Amazon's own monthly unit floor; sees sellers that never run Meta ads |
| AMZ 1K+ | Listings each selling 1K+/month | same | Number of clones that actually sell |
| TT | Highest lifetime "sold" of an on-target product | TikTok Shop US keyword pages `shop.tiktok.com/us/k/<kw>` (keenable cache) | TikTok-native sellers |
| META 180+ | Active US ads started 180+ days ago, exact category phrase | Meta Ad Library (headless) | Advertisers keep paying → profitable |

Scoring: each channel 0–5 on a log scale (cuts fixed before reading the data). **POP = mean of AMZ and TT** (real sales). **CONF = channels scoring 3+** (max 3).

### What went wrong during the pass (and was fixed)

1. Amazon search drifts off-target (Nutrafol supplement for "hair growth serum", Depend diapers for "men's incontinence underwear", Olaplex for "split end trimmer"). Fix: title regex per product (`amz_filter.py`), duplicates removed.
2. Meta "exact phrase" matches med-spas, nail salons, clinics and car dealers ("chin", "collagen mask", "seat cushion", "CarPlay"). Fix: Meta dropped from POP; used only in CONF, and not at all for 13 phrases whose top aged advertisers were off-target (`META_NOISY`).
3. A regex escape bug zeroed two supplements (NAC, caffeine gum) in the first run; fixed.

## Result: main block (top 15 by evidence)

| # | Product | AMZ units/mo | TT k sold | META 180+ | CONF | Comment |
|---|---|---|---|---|---|---|
| 1 | Collagen multi-balm stick | 195K | 1,200 | 25 | 3 | Mega-hit, but owned by K-beauty brands (medicube, Dr.Melaxin) |
| 2 | Handheld steam cleaner | 31K | 371 | 72 | 3 | Generic appliance |
| 3 | Eyelash growth serum (cosmetic) | 87K | 344 | 90 | 3 | Needs prostaglandin-free formula |
| 4 | Color-changing foundation stick | 267K | 68 | 120 | 3 | |
| 5 | Beef tallow balm | 50K | 663 | 52 | 3 | Consumable |
| 6 | **Compression socks** | 110K | 71 | 610 | 3 | Most aged ads of all; 16 Amazon clones selling 1K+/mo |
| 7 | Hair-growth scalp serum | 133K | 112 | 62 | 3 | Overlaps rosemary roll-ons |
| 8 | Neck firming cream | 70K | 653 | 83 | 3 | GoPure 653K on TikTok |
| 9 | Rosemary hair oil roll-on | 46K | 598 | 60 | 3 | Bodywise roll-on 598K (the clone from an excluded video) |
| 10 | Men's body hair removal cream | 64K | 135 | 54 | 3 | |
| 11 | Topical magnesium oil spray | 25K | 105 | 53 | 3 | |
| 12 | Filtered shower head + cartridges | 46K | 15 | 42 | 3 | Refill model |
| 13 | Stainless-steel pet water fountain | 62K | 35 | 22 | 3 | Filters = refills |
| 14 | Waterless scent diffuser + oils | 29K | 87 | 17 | 3 | Refill model |
| 15 | LED face/neck mask | 16K | 28 | 70 | 3 | Needs FDA-cleared OEM |

Next tier (CONF 2): retinol firming cream, collagen overnight mask, nose pore patches, lymphatic contour brush, mini projector, teeth-whitening powder, vacuum travel bags, V-line chin mask, **persimmon soap (#24)**, rodent pouches, CarPlay adapter, pre-wash hair oil, mouth tape.

## Where the earlier picks land (94 main products)

| Earlier verdict | Blind rank | AMZ / TT / META 180+ | Reading |
|---|---|---|---|
| Compression socks (take) | **6** | 110K / 71K / 610 | Confirmed in all three channels |
| Persimmon soap (take, 2nd SKU) | 24 | 60K / 12K / 11 | Strong on Amazon (11 clones selling 1K+/mo), weak on TikTok and Meta |
| Turmeric soap (take #1) | **60** | 58K / 0.9K / 12 | Amazon demand is mostly "kojic + turmeric dark-spot" bars (VALITIC); TikTok and Meta weak. Earthly Derm's own growth is a **brand** signal, not a category one |
| Men's leak-proof boxers (take) | **88** | 2.5K / n/a / noisy | Weak: the category is women's period underwear and disposables |
| Carry-on duffel (optional) | 58 | 2.2K / 87K / 1 | TikTok-only hit (Lefame) |
| Tennis bracelet (dropped) | 43 | ~0 / 65K / 52 | TikTok hit (PAVOI); our Amazon query found none with badges |

**Verdict on the bias question:** partly justified. Turmeric soap was ranked #1 from one brand's traffic and review curve; at category level it is mid-pack. Persimmon soap is real but not top. Compression socks hold up independently. Leak-proof boxers do not hold up at category level.

## Hidden products: little or no Meta, strong elsewhere

These are the cases the owner asked about: sold through TikTok Shop or Amazon, nearly invisible in the Ad Library.

| Product | AMZ units/mo | TT k sold | META 180+ | Main channel |
|---|---|---|---|---|
| Hair-growth inhibitor (Cyperus oil) | 0.4K | **597** (Caramela) | 0 | TikTok |
| Teeth-whitening powder | 17K | **293** | 0 | TikTok |
| Nose pore patches/strips | 42K | **209** | 0 | TikTok + Amazon |
| Lymphatic contour brush (corpus: Geta) | **93K** | **195** | 3 | TikTok + Amazon |
| Creatine for women (SUPP) | **176K** | **162** | 1 | Amazon + TikTok |
| Caffeine gum (SUPP, corpus: Neuro) | 31K | 111 | 0 | TikTok |
| Rodent repellent pouches | 21K | 140 (Reliant) | 1 | TikTok |
| Work insoles | 93K | 2 | 0 | Amazon (Dr. Scholl's) |
| Ceramide face cleanser | 173K | n/a | 0 | Amazon (CeraVe-type brands) |

## Supplements block

| # | Product | AMZ units/mo | TT k sold | META 180+ | CONF |
|---|---|---|---|---|---|
| 1 | Menopause / hormone-balance | 48K | 99 | 85 | 3 |
| 2 | Shilajit gummies | 16K | 411 | 210 | 3 |
| 3 | Moringa capsules (corpus: Rosabella 171K on TikTok) | 33K | 184 | 83 | 3 |
| 4 | Pumpkin seed oil softgels | 82K | 184 | 32 | 3 |
| 5 | Beef liver capsules | 55K | 48 | 32 | 3 |
| 6 | Cayenne / capsaicin softgels | 17K | 27 | 45 | 3 |
| 7 | Colostrum | 15K | 16 | 93 | 3 |
| 8 | Creatine for women | 176K | 162 | 1 | 2 |
| 9 | Parasite cleanse | 91K | n/a | 53 | 2 |
| 10 | Caffeine / nootropic gum | 31K | 111 | 0 | 2 |
| 11 | Magnesium glycinate gummies | 226K | 9 | 140 | 2 |

Weak: fertility tea, sleep patches, dog probiotics, acne gummies, vitamin patches.

## Limits

- Popularity is not attractiveness: big numbers often mean brand-owned (medicube, CeraVe, Dr. Scholl's) or crowded categories. Margin, repeat and entry difficulty are a separate step.
- TikTok "sold" is lifetime, from a cached keyword page (date unknown, up to a few months); ~25% of pages missing → n/a, not zero.
- Amazon badges are floors ("10K+") on top-20 results only; keyword choice moves the number (e.g. "moissanite tennis bracelet" had no badges).
- Meta exact-phrase counts are noisy even after the filter.
- One snapshot (2026-11-07); no trend.

## Devil's-advocate pass and final shortlist (same day, later) — supersedes the ranks above

What broke: TikTok readings from one keyword page can be badly low (turmeric soap 0.9K → 819K sold, Honey Glow lemon-turmeric-kojic bar; exfoliating towel 0.17K → 79.5K, GOSHI). Amazon re-run hours later: 10 of 12 products in the same strength band (drift −32%…+45%). Alternative Amazon keywords: turmeric 119–131K/mo, persimmon 66K, men's leak-proof boxers 3.6K. Meta phrase search undercounts DTC brands (Earthly Derm 44 aged ads by domain vs 12 by phrase).

New rules (`shortlist.py`): demand proven by the STRONGEST sales channel (G1), ≥5 Amazon sellers at 1K+/mo (G2), repeat or ≥$40 (G3), legal (G4); Meta = max(phrase, leader domain where measured); big-brand-owned categories set aside. Trust = witnesses agreeing (0–3).

Tier A (all three witnesses, open market, no compliance step), by total score: compression socks, color-changing foundation stick, beef tallow balm, neck firming cream, rosemary hair roll-on (start set by rule), men's body hair removal cream, exfoliating towel, turmeric soap, V-line chin wrap, magnesium oil spray, persimmon soap, filtered shower head, pet water fountain, waterless scent diffuser. Order inside tier A is within noise. Tier A supplements: shilajit gummies, menopause/hormone balance, moringa, pumpkin seed oil, beef liver.
Out: men's leak-proof boxers (small demand, two sources), duffel and tennis bracelet (few Amazon sellers, one-off purchase). Brand-owned: multi-balm, retinol, collagen night mask, ceramide cleanser, work insoles.
Visual explainer: https://claude.ai/artifact/MgeYjaz6roHD5VVBB8Hxvg (source `product_evidence_map.html`).
