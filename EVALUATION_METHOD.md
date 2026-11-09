# Evaluation method: reading a product's demand and life stage from public signals

Version 1, 2026-11-07. This file defines **how we judge a product**. `METHOD.md` stays the log of sources and insights; `CONCLUSIONS.md` and `work/blind/BLIND_PASS.md` hold verdicts, which should be re-read through this method.

Marks: ◆ confirmed by several independent sources or our own data · ◈ likely (one decent source, or vendor data) · ◇ disputed / heuristic / our assumption.

## Why we need it

Our two rankings disagree because they answered different questions with different signals:

| Ranking | Unit | Signals | Example result |
|---|---|---|---|
| `CONCLUSIONS.md` | the leader brand | Meta ad age, site traffic, reviews of one store | Turmeric soap #1 (Earthly Derm grew fast) |
| `BLIND_PASS.md` | the category | Amazon badges, TikTok sold, Meta 180+ by phrase | Turmeric soap ~60/94 |

Both are correct about what they measured. The method below keeps the two levels apart and then combines them on purpose.

## Core: three questions and one gate, never one blended score

1. **Demand. How many units move per month, across all channels?** Measured at **category** level.
2. **Proof. Do people with real data keep paying and buying over months?** Measured mostly on the **leaders**.
3. **Stage. Where is the product on its life cycle, and how crowded is it relative to demand?** Category plus leaders.
4. **Gate: Fit. Can we sell it?** Regulation, unit economics (margin, AOV = average order value, LTV = lifetime value), logistics, ability to make creatives. Pass/fail, not a score.

The verdict comes from the combination (section 8), not from an average. An average hides exactly the contradictions we need to see.

## 1. One currency: estimated units per month, with an error band

Every volume signal is converted to orders per month before comparison. Each conversion has an error band; we keep the band visible.

| Signal | Conversion | Quality | Notes |
|---|---|---|---|
| Amazon "X+ bought in past month" | floor of **unique customers** in the last 30 days; sum over on-target top-20 listings | Tier 1 | ◈ Badge counts unique customers, needs 50+ customers, ASIN listed 30+ days, 3-4 day lag (Amazon Seller Support reply, Seller Central forum 2026). ◈ Within one bucket of real 30-day sales >90% of the time (PMG study). Coarse buckets: "2K+" = 2,000-9,999 |
| TikTok Shop "sold" counter | lifetime units ÷ months listed (rough); 28-day units from FastMoss/Kalodata (paid) | Tier 1 counter / Tier 2 if estimated | Lifetime counter hides the trend; ◈ FastMoss estimates GMV from changes in the sold count (FastMoss docs) |
| DTC site traffic (SimilarWeb) | visits × 2-3% conversion | Tier 2 | ◇ 2-3% is our assumption; ◆ weak under ~50K visits (our log) |
| Reviews per month | Amazon: × 50-100 (1-2% of buyers review) · DTC store with review-request emails: × 10-30 | Tier 1 count, Tier 3 multiplier | ◈ Amazon 1-2% review rate repeated across several seller sources; 5-15% with automated requests (Ridge). ◇ DTC multiplier is our assumption. **Use the curve shape, not the level** |
| Google Trends | no conversion; relative index | Tier 2 | Shape and seasonality only |
| Meta ads | no conversion | Tier 1 dates | Proof and stage, never volume |
| Guru / case-study revenue | do not convert | Tier 3 | ◆ ran 2× to 400× above our sanity band (`METHOD.md`) |

**Category demand = sum of channels** (Amazon + TikTok Shop + DTC), on a log scale. Not the mean. `BLIND_PASS.md` used POP = mean(AMZ, TT), which halves a product that sells only on one channel; that is the bias the owner suspected.

## 2. Channel presence: when does "not on TikTok" mean "weaker"?

Owner's hypothesis: a real hit gets cloned, and clones spread to the free channels (Facebook taken → TikTok → Amazon). Evidence:

- ◈ Across 37 brands, ~65% saw Amazon search rise **in the same month** as their TikTok Shop GMV grew; the link fades ~3 months after the spike (The Bluebird Group, Dec 2025).
- ◈ Shoppers who discover on social often buy on Amazon: 48.8% prefer Amazon vs 9.5% TikTok Shop (Envision Horizons survey, via Modern Retail). One survey, so ◇ on the exact numbers.
- ◈ Saturation guides treat "the same item on Amazon with Prime" as a marker of the late, commoditised stage (several dropshipping tool blogs; vendor opinion).

So spreading is the normal path of a real hit, but the order of channels is not fixed (some products start on Amazon or TikTok). Rule:

```
Missing on channel X counts AGAINST the product only if all three hold:
  (a) it has been visibly selling for 6+ months somewhere (time for clones to arrive),
  (b) channel X fits the product (see below),
  (c) channel X allows the category (TikTok Shop and Amazon restrict some health/medical items).
Otherwise absence is neutral: record it as "not yet" or "not suited".
```

Channel fit cues (◇ practitioner heuristics, to be validated on our data):
- **TikTok Shop**: visual demo in 5 seconds, impulse price, novelty.
- **Amazon**: people search by problem or product name; commodity; replenishment.
- **Meta → own store**: needs a story or explanation, higher AOV, bundles, subscription.

Reading: a product old enough and suited to a channel, yet absent there, is **narrower** (◈ demand depends on one brand's ads or one creator wave). Channel count is therefore a **stage** indicator (section 4) more than a demand indicator.

## 3. Proof: persistence by someone who sees the real numbers

| Signal | Threshold | How rare | Source |
|---|---|---|---|
| Meta ad still running | 90+ days strong, 180+ very strong | ◈ 6.5% of US ads alive at 30 days, 2.1% at 90 (Adligator, 4,634 ads, Aug 2026). ◇ Another study of DTC brand ads: 26% pass 90 days (Funnelens 2026). Rarity depends on the sample: compare within one category | vendor studies |
| Ad relaunches / seasonal comebacks | same creative returns | strong; invisible in Ad Library (each flight gets a new start date) | ◈ Adligator |
| Many variants of one ad | 4+ variants | ◈ 4-9 variants ≈ 3× the estimated spend of single ads (Ad-Radar board, 2,443 ads) | vendor data |
| Review curve | rising or stable for 6+ months | ◆ our Earthly Derm and Everstride curves matched their traffic | our data |
| Traffic / BSR history | 3-6+ months without a cliff | ◈ Keepa practice: read the direction over months, not one snapshot | seller guides |
| Search shape | compounding growth over months, not a 6-8 week spike | ◈ Exploding Topics method | |

Failure modes: brand-awareness and retargeting ads run long without strong direct response (◈); review counts can be gated, imported or incentivised (◆ our log).

Proof needs **two independent Tier 1-2 signals that agree** (◆ our insight 8: reviews and traffic agreed for Earthly Derm).

## 4. Stage: the life-cycle fingerprint

The classic product life cycle (introduction, growth, maturity, decline) is standard marketing theory; e-commerce guides add a test phase and a "commodity" end. What matters for us is the **observable fingerprint** of each stage in our channels.

| Stage | Typical age | Meta Ad Library | TikTok Shop | Amazon | Search (Trends) | Reviews / traffic | Clones | Our move |
|---|---|---|---|---|---|---|---|---|
| **A. Test** | 0-1 mo | 1 advertiser, ads < 30 days | none | none | none | none | 0 | Nothing proven; ignore |
| **B. Breakout** | 1-3 mo | Leader's ads multiply, many variants, all young | first sellers, sold count jumping | maybe 1 listing | brand search appears | steep rise | 0-3 | Early. Fad risk. Only a fast, cheap test |
| **C. Clone wave (growth)** | 3-9 mo | Many advertisers, most ads young; leader's first ads pass 90 days | many shops and creators | several listings with badges, 1K+ appear | category search rising year on year | still rising | many, multiplying | **Best window** if an angle is open |
| **D. Maturity** | 9+ mo | Few survivors with 180+ day ads; creatives look alike | high but flat | many 1K+ listings, prices falling, seller count high | high and flat (seasonal pattern repeats) | flat | saturated | Enter only with a different angle, segment or offer |
| **E. Decline** | — | Aged ads stop; few new advertisers | sold flat or falling | sellers leave, price war | falling year on year (not seasonal) | falling 3+ months | leaving | Skip |
| **Fad** (branch from B) | weeks | spike of young ads, then gone | one viral wave | never builds | 6-8 week spike, then crash | spike, then cliff | rush then exit | Skip unless in and out within weeks |

Sources for the stage signals: ◈ saturation stages and markers (Pyratrend, AS Tools, DropshipSeek, Koala blogs: vendor opinions that agree with each other); ◈ "rising seller count + falling price = price war" (Keepa reading guides); ◈ fad vs trend by curve shape (Exploding Topics); ◆ classic PLC.

Stage is read at **both** levels. A brand can be in B while its category is in D (Earthly Derm vs turmeric/kojic bars).

## 5. Crowding relative to demand

◇ All practitioner heuristics, but they agree: saturation is **sellers relative to demand, plus how fast new sellers arrive**, not seller count alone.

- **Demand per seller**: Amazon badge units ÷ listings selling 1K+; TikTok revenue per shop and top-3 shop share (Kalodata uses both).
- **Entry velocity**: share of a category's advertisers whose ads are all under 30 days; week-to-week growth in advertisers or listings.
- **Creative sameness**: the same hook across many advertisers = the obvious angle is burned.
- **Open angles**: aged share by angle (◈ our insight 9: wide calf and nurses proven, men and pregnancy tried but rarely survive).
- Concentration: if the top 3 sellers hold most of the volume, entry is hard; if volume is spread, entry is easier.

### 5a. Newcomer survival on Meta (owner's addition, 2026-11-07)

The survivorship-free openness metric: **of the stores that tried to sell this category with ads, what share reached success?**

- Unit = **store**, not ad account or page. Group ads by landing domain, then merge domains of one company (same Shopify shop / checkout domain, redirects to the same store, advertorial or persona pages pointing to one brand). Creator and partner pages count under the brand they link to. Marketplace landings (amazon.com, tiktok.com) are excluded.
- Cohort = stores whose first ad in the category started in a fixed window (e.g. 6-12 months ago).
- Success = the store has an ad that ran 90+ days. Survival rate = successful stores ÷ all stores in the cohort.
- Read together: leader + N survivors + M dropouts. High survival with many entrants = open; low survival = the category eats newcomers.
- Data problem: ◆ the US Ad Library shows only **active** commercial ads, so dropouts disappear. Denominator sources: (1) a paid ad archive with stopped ads and first/last-seen dates (BigSpy-type tools; verify it keeps stopped US ads before paying); (2) our own weekly archive (forward only, needs ~3 months); (3) a "store graveyard" check: stores found via search/Wayback that sold the product, and whether they still sell and advertise it (rough).

## 6. Evidence tiers

| Tier | What | Use |
|---|---|---|
| 1. Counted by the platform | Amazon badges, TikTok sold counter, Ad Library start dates, dated reviews, Wayback snapshots | Evidence |
| 2. Modelled estimates | SimilarWeb traffic, FastMoss/Kalodata GMV, Helium 10 / Jungle Scout sales, Trends index | Evidence with a band; cross-check with a second source |
| 3. Claims | Guru videos, case studies, vendor blogs | Leads and heuristics only |

## 7. The product card (output of the method)

```
Product / category:
  Demand     : ~N units/mo (range), by channel: AMZ __ · TT __ · DTC __   [tiers]
  Proof      : leader persistence __ months; agreeing signals: __ + __
  Stage      : category _ / leader _  (A-E or Fad), confidence ◆◈◇
  Channels   : present __ · absent __ (neutral / against, why)
  Crowding   : demand per seller __ · entry velocity __ · open angles __
  Fit gate   : regulation __ · margin/LTV __ · logistics __ · creatives __  → pass/fail
  Verdict    : take / test / watch / skip, and the one fact that would change it
```

## 8. Decision rules

1. Fit gate fails → skip, whatever the signals say.
2. Demand small (category under ~5-10K units/mo across channels) → skip, unless the leader shows a brand-execution story we can repeat. ◇ threshold to calibrate.
3. Stage A or Fad → watch only.
4. Stage B with strong proof on two signals → small, fast test.
5. Stage C → main target; enter on an angle that is not yet crowded.
6. Stage D → enter only with a named, evidenced open angle (segment, bundle, offer).
7. Stage E → skip.
8. Category and leader disagree → say which bet we are making: **category bet** (ride demand) or **execution bet** (copy what the leader does better). Execution bets need more creative and brand work.

## 9. Our current contradictions, read through the method

Data from `CONCLUSIONS.md` and `BLIND_PASS.md`; readings are judgments.

| Product | Category demand | Leader proof | Stage (category / leader) | Reading |
|---|---|---|---|---|
| Compression socks | High in all 3 channels (AMZ 110K/mo, TT 71K sold, 610 Meta 180+) | Everstride: 190 aged ads, reviews since 2024 | D / D | Category bet with an angle (wide calf, nurses). Consistent in both rankings |
| Turmeric soap | Medium; Amazon volume is mostly kojic + turmeric dark-spot bars; TikTok weak | Earthly Derm: traffic 269K→913K, reviews 209→957/mo | D (kojic bars) / B→C | **Execution bet**, not a category wave. Rankings differ because they measured different levels |
| Persimmon soap | Amazon solid (11 listings 1K+), TikTok and Meta weak | Kaori: 53 aged ads; only 34-71% US traffic | D / C-D | Narrow; second SKU only |
| Men's leak-proof boxers | Low as measured (the query hit women's period underwear and disposables) | Menvault: traffic 11K→107K, but 8 of 234 ads aged 180+ | ? / B | Unproven. Category measurement itself is unreliable; needs a better category query |
| Carry-on duffel | TikTok-only (87K sold), Amazon ~2.2K/mo | Luhxe 2.3M visits, ads rotate fast | C on TikTok / C | If the TikTok wave is 6+ months old, the Amazon gap counts against it (rule in section 2) |

## 10. Known gaps of this method

- Free Amazon and TikTok data are snapshots; trend direction needs Keepa (Amazon history) or FastMoss/Kalodata (TikTok history), both paid. ◆
- Meta Ad Library does not show spend, and logged-off it loads only ~30 top ads per query. ◆
- Conversion factors (site conversion 2-3%, DTC review rate) are assumptions until calibrated on one store where we know real sales. ◇
- Thresholds in sections 5 and 8 come from vendor blogs, not research. ◇
