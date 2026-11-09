# Full list: 22 products, public-data check for a US launch

Date: 2026-11-07. Scope: the top-20 from `top20_products.md` plus the two soaps (persimmon, turmeric).

Sources checked today:
- Google Trends API (US, last 12 months);
- Meta Ad Library (US, active ads, logged-off);
- competitor sites and price cards;
- Alibaba listings;
- US tariff tables;
- FDA/FTC/Meta policy pages;
- the full video transcripts.

Amazon blocks AI agents, so it was not crawled. Marks: ◆ seen directly or official source; ◈ likely or indirect; ◇ estimate.

## How to read the columns

- **Search** = Google searches for the product term as % of searches for "ski boots" (US, 12 months). ~0% means people do not look for it, so ads must create the demand. Year-over-year growth is not used: a Trends artifact makes many niche terms spike in Apr 2026.
- **Clone ads** = active US ads matching the category phrase. This is an upper bound: duplicates and loosely related ads are included. It measures how crowded the niche is on Meta.
- **Max CAC** = what one order leaves after goods, duty, freight, 3PL, shipping, payment fees and a returns allowance (◇ model). If ads cost more than this per order, we lose money. Duty = China rates as of Nov 2026: MFN + Section 301 + the 12.5% forced-labor layer.

## Summary table

| # | Product | Search | Clone ads (phrase) | Leader & its US ads | Leader price | Unit cost (Alibaba) | Duty CN | Max CAC ◇ | Main pitfall | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Turmeric "fade & glow" soap, melanin-rich skin** | 21% | 320 ("turmeric soap"); ~1,000 kojic+soap | Earthly Derm ~510 | $27 / 3 for $39 / 5 for $55 | $0.55-1.3 | 37.5% ◆ | ~$23 + repeat | "Fades dark spots" is a drug-style claim; race-targeted copy vs Meta policy | **Shortlist** |
| 2 | **Persimmon soap, aging body odor** | 13% (peak Oct 2026) | ~2,600 | Swarva ~410, Kaori ~750, Mirai | 2 for $29.99 / 3 for $39.99 / 6 for $59.99; Amazon 2-pack $34.99 | ~$0.5-1.6 | 37.5% ◆ | ~$22 + repeat | Most crowded niche on the list; fake-persona playbook everywhere | **Shortlist (as 2nd SKU of a soap brand)** |
| 3 | **Tennis bracelet (PVD steel, non-tarnish)** | 140% | ~2,700 (incl. big jewelers) | MLMT ~280 | from $69 | $1.5-3.5 (CZ) | 31-48% ◇ | ~$55 | Amazon floor $14.99; jewelry is the most crowded category | **Shortlist** |
| 4 | 16-head vibration massager (gift) | 21% ("body massager") | ~460 | several (VitalHorse, ReliefWave, Alythera…) | ~$142 (video) | ~$14-17 ◈ | ~37.5% ◇ | ~$86 | Electronics plus battery; competitors use pain claims; heavy item, returns | **Shortlist (gift test)** |
| 5 | Men's leak-proof boxers | 3% | ~560 ("bladder leak": Always, Everdries, Target…) | Menvault ~330 | 6 for $149.95 | $5.3-6.4 | 27.4% ◆ | ~$49 | FDA establishment fee $11,423/yr if we import; leader's claims fail in a real user test | Reserve (via US-registered supplier) |
| 6 | Inflatable airplane seat cushion | 3% | ~1,100 ("travel cushion") | Sondur, Travlr ~410 | ~$80 (video) | $1-8 | ~40% ◇ | ~$51 | Crowded; persona-page playbook | Reserve |
| 7 | 2-in-1 garment duffel | 3% | n/a (phrase too broad) | Luhxe ~490 | $129 | $18-20 | ~55% ◇ | ~$62 | Bulky (shipping); handbag duty high; fake-giveaway playbook | Reserve |
| 8 | Split-end trimmer | 3% | ~2,100 ("split ends", mostly hair care) | Luxmend | $59 | $3.5-7 | ~40% ◇ | ~$36 | Battery/FCC; incumbent Split-Ender; hair damage reviews | Reserve |
| 9 | Collagen chin/jaw wrap | 2% | ~610 ("face wrap") | Skult ~770 (top ad live 14 months) | $34.99 for 2, up to 6 for $64.99 | ~$1.7 ◈ | ~37.5% ◇ | ~$28 | Temporary effect leads to refunds; cosmetic claims | Reserve |
| 10 | Waterless scent diffuser | 49% | ~750 | Hotel Collection (big brand), Scentify | ~$60-100 ◇ | $7-8 | ~40% ◇ | ~$30 + refills | Big brand dominates; fragrance oil shipping; electronics | Drop |
| 11 | Men's compression tank | 1% | ~3,800 ("compression tank") | North Alpine; InShape, Selure… | ~$60/3 ◇ | $1.7-7.9 | 40-52% ◇ | ~$14 | Crowded, apparel sizes and returns, high synthetic-apparel duty, Meta body-attribute policy | Drop |
| 12 | Ratchet screwdriver set | 10% | ~99 | Toolsons | $42.99 (Walmart $26) | ~$7 ◇ | ~45% ◇ | ~$21 | Amazon and Walmart are cheaper; thin margin | Drop |
| 13 | Pillow speaker | 23% | ~160 | Radox (DreamWave) | $35 | $3.3-13.8 | ~42% ◇ | ~$15 | Low price; FCC plus battery; sound leakage complaints | Drop |
| 14 | Gel ski shin sleeve | ~0% | ~130 ("shin pain") | SkiGuards ~230 | $39.95 | $2.5-3.9 | ~30% ◇ | ~$40 | No search demand; skiers call it a band-aid; ski visits −15% last season | Drop (pre-order test only) |
| 15 | No-rinse paw cleaner | 3% | ~60 | small sellers; Dandylion on Amazon | ~$25-30 ◇ | ~$2 ◇ | ◇ | ~$15 | Low ticket; liquid shipping | Drop |
| 16 | Enzyme pet-urine spray + UV | 5% ("pet urine odor") | ~560 ("pet urine") | Rocco & Roxie, Zorbx, Petco… | ◇ | ◇ | ◇ | ◇ | Germ/bacteria claims need EPA registration; strong brands | Drop |
| 17 | Pet hair remover | 17% | ~14,000 ("pet hair", broad) | Uproot Clean dominates | $13-27 | <$1 | ◇ | low | Saturated, low price | Drop |
| 18 | Work insoles (concrete) | 16% | ~1,500 | Orthora, Stepprs, Xstance… | ~$40 ◇ | ~$2-4 ◇ | ◇ | ~$25 ◇ | Crowded; plantar-fasciitis claims | Drop |
| 19 | Body oil for crepey skin | 27% | ~9,900 | DRMTLGY, Beekman 1802… | ◇ | ◇ | ◇ | ◇ | Very crowded beauty niche | Drop |
| 20 | Reusable puppy pads | ~0% | ~12,000 ("puppy pad", incl. brand) | PuppyPad dominates | ◇ | ◇ | ◇ | ◇ | One brand owns the phrase | Drop |
| 21 | Facial epilator 40+ | 15% | ~4,200 ("facial hair") | many, incl. Alibaba | ◇ | ~$3-5 ◇ | ◇ | ◇ | Flawless incumbent; crowded | Drop |
| 22 | Lymphatic face brush | n/a (term too broad) | ~1,400 | Kojeva, Kitsch, Aeki | $24.99 | <$2 ◇ | ◇ | low | Low ticket, crowded | Drop |

## Deep dive: the two soaps

### Turmeric "Fade & Glow" bar for melanin-rich skin (Earthly Derm)

- **Video** [zRMForJwsy8](https://www.youtube.com/watch?v=zRMForJwsy8). Author: $7-14M/mo; traffic 30-40K/mo, then 900K in Sep 2026; 537 active ads. Unverified.
- ◆ Live US check: earthlyderm.com ~510 active ads, plus creator pages ("Product Queen Vicki", "cb.the.trainer"). The top-impression ad has run since 19 Feb 2026. Other turmeric-soap advertisers: Kaoli (trykaoli.com, ~96 ads, launched 28 Oct 2026, so clones are just arriving), Stem & Soul, Herb'N Eden, GloMelanin, Honey Glow.
- **Offer:**
  - 1 bar $27, 3 for $39, 5 for $55, shown as a price per day;
  - 60-day money-back guarantee;
  - "counterfeit warning" (sold only on their site);
  - buy 2 get 1.
  - Current site extends to a "Bump Bar" for razor bumps and ingrown hairs on coarse, curly hair.
- **Creatives:**
  - Cold ad: ~3 min with an AI "licensed esthetician who specializes in melanin-rich skin". It runs problem → agitation → why surface products fail → a centuries-old remedy from Kerala, India → mechanism → 30/60-day results → offer.
  - Retargeting: a "60% off, don't use code X" reverse-psychology ad, and a "copycats on Amazon burn your skin" ad.
- **Page:**
  - benefit-named product ("Fade & Glow");
  - results timeline (first use, 2-3 weeks, 60 and 90 days), which pushes the 3-5 bar bundles;
  - testimonials that look believable;
  - ingredient explainer and FAQ.
- **Economics:** bar cost $0.55-1.3 ◈; soap duty from China 37.5% ◆ (MFN free + 301 List 3 25% + 12.5%). About $23 left per $39 order before ads, and customers rebuy every 1-3 months.
- **Search demand:** "turmeric soap" 21% of "ski boots", "kojic acid soap" 13%. Real, steady demand exists beyond ads.
- **Pitfalls:**
  1. ◆ Claims. FDA treats skin lightening and "pigment-blocking" products as drugs; it sent warning letters over OTC skin-lighteners in 2022. Copy must stay cosmetic: brightens, evens the look of tone. No "blocks the enzyme that makes pigment".
  2. ◆ Meta's personal-attributes policy bans ads that assert the viewer's race or medical condition. "Made for melanin-rich skin" as a product statement is fine; "your Black skin…" is not.
  3. ◈ Turmeric and kojic soaps can irritate. The leader's own ads attack "copycats that burn"; we need a gentle, tested formula.
  4. MoCRA cosmetic duties (facility registration, product listing, adverse-event reporting); small businesses are partly exempt ◇.
- **Verdict:** best new candidate. There is real search demand on top of the ads, the clones are only now arriving, unit cost is tiny and customers rebuy. Main work: a compliant claim set and a gentle formula.

### Persimmon deodorizing soap (Swarva)

- ◆ Search interest is rising ("persimmon soap" peaked in Oct 2026; "old people smell" 9%).
- ◆ But ~2,600 active US ads mention it. Swarva ~410, Kaori ~750, plus Mirai Clinical, Kakiyu, Grandma's Glow, many from fake persona pages. Competitors already run "we tested every persimmon soap" comparison ads.
- ◈ Customer feedback: "it works but too expensive", subscription cancellations, "bars are small".
- **Economics:** same as the turmeric bar (soap duty 37.5%, bar cost ~$0.5-1.6).
- **Verdict:** not as a standalone first launch. As a **second SKU of one soap brand** it makes sense: same supplier type, same funnel (long AI story ad, then advertorial, then bundles plus subscription), same compliance work. Possible angle: unscented or larger bars, honest price per wash.

## Proposed shortlist (for discussion)

1. **Soap brand: turmeric glow bar first, persimmon bar second.** Real search demand, tiny cost, repeat purchase, and one funnel for both.
2. **Tennis bracelet** for Valentine's Day 2027 (image-first test).
3. **16-head massager** as a gift test (high price leaves room for ad costs; check clone claims and product quality).
4. Reserve: **men's leak-proof boxers** via a US-registered supplier.

Not done yet: sample orders, supplier quotes with landed cost, a regulatory opinion on soap claims and boxers, Amazon sales data (blocked).
