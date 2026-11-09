# Brief: is this market open to a new brand? (20 products, US / EU / UK / AU)

Written 2026-11-09 from a finished study of 17 US categories (method v2.1). Everything below is what that study proved works, what failed, and what cannot be seen from public data. Follow it; where you deviate, write down why.

Confidence marks used everywhere, including your output: ◆ confirmed (platform's own count, or several independent sources) · ◈ likely (one decent source, or vendor docs) · ◇ disputed / heuristic / assumption. Never invent a number. If a number is unknown, write "unknown" and the reason.

---

## 1. The idea

We are not asking "is there demand?" (that is easy to see) but **"can a newcomer win a share of it?"**

A market can be:

| Type | What it looks like | Verdict for a new brand |
|---|---|---|
| **Captured** | 1-3 old brands hold most units; newcomers that entered in the last 2 years sell almost nothing | Skip, unless a clearly different sub-segment exists |
| **Price war** | Volume is spread, but it goes to unbranded / generic listings at low prices | Bad for a brand (good only for a cheap marketplace seller) |
| **Eats newcomers** | Many brands enter, very few survive (low survival rate) | Skip or treat as high-risk |
| **Open** | Named brands younger than 24 months already hold a real share AND several of them reach "winner" volume | Main target |
| **Too early / fad** | Category is a few months old, everything is young, search spikes and crashes | Watch only |

The core trap we fell into and fixed: **looking only at today's winners is survivorship bias.** You must also count the brands that tried and failed. "Openness" = units taken by new named brands + how many new brands reached winner volume + what share of an entry cohort survived.

Demand, concentration and newcomer survival are **three separate answers**. Never blend them into one score; the contradictions between them are the information.

---

## 2. What is visible and what is not (public, logged-off data)

| Visible ◆ | Not visible ◆ |
|---|---|
| Amazon "X+ bought in past month" badge (floor of unique buyers, 30 days) | Real ad spend, targeting, conversions, profit, refunds of any brand |
| Listing age via ASIN | Amazon sales or review **history** (logged-off; Keepa public graph shows price only) |
| Meta Ad Library: active ads, start dates, landing domains, Meta's own "~N results" count | **Stopped** ads outside the EU/UK (US, AU libraries show active commercial ads only) |
| Meta Ad Library EU/UK: also stopped ads (kept ~1 year) + reach by country/age/gender ◆ (Meta API docs) | TikTok Shop trend over time without a paid tool (only lifetime "sold") |
| Google Trends by country (relative index, 5 years) | DTC store sales (only proxies: traffic, reviews, Shop app badge) |
| Store review widgets with dates (Loox works without auth) | Small-store traffic: estimators are unreliable under ~50K visits/mo |
| Domain registration (RDAP), first Wayback capture | Anything behind a login, captcha or bot check — do not bypass |

Consequence: in the **EU/UK you can measure newcomer survival on Meta properly** (dropouts stay visible). In the US/AU you can only measure it on Amazon (by ASIN cohort) or by building your own archive forward.

---

## 3. Per-market source map (verify each cell on day 1 and record the result)

| Market | Amazon site | Badge present? | TikTok Shop live? | Meta library | Trends geo |
|---|---|---|---|---|---|
| US | amazon.com | ◆ yes | ◆ yes | active only | US |
| UK | amazon.co.uk | ◈ yes (verify) | ◆ yes | **EU/UK DSA: stopped ads + reach** | GB |
| DE / FR / IT / ES | amazon.de / .fr / .it / .es | ◈ yes in local language (verify) | ◈ launched 2024-25 (verify per country) | **EU DSA: stopped ads + reach** | DE, FR, IT, ES |
| AU | amazon.com.au | ◇ unknown, check | ◇ likely not live, check | active only | AU |

Set the delivery address to a real postcode of the market (we used New York 10001) before reading Amazon; prices and badges depend on it.

If a platform shows an "unauthorized AI agent" / robot notice, **stop collecting from that platform automatically**, keep what you have, and write a manual collection task (exact queries, pages, fields) for a human. We hit this on amazon.com; that is now a standing rule.

---

## 4. Method, step by step

### Step 0. Pre-register (before looking at any data)

For each product write down, and save to a file with a date:
1. **Product form** as a strict rule: title MUST contain X, MUST NOT contain Y (e.g. "neck cream" = sold for the neck; face creams that mention the neck are out). This stops neighbouring products leaking in. We had to re-run once because they did.
2. **Search query** per market (local language for DE/FR/IT/ES).
3. **Exact phrase** for Meta Ad Library per market (local language).
4. **Thresholds** (section 6). Rules written after seeing data must be disclosed as such.
5. **Market priority**: which market is primary for this product. Screen every product in its primary market first; expand to other markets only for products that pass.

### Step 1. Amazon shelf (demand + who holds it)

- Read search result pages 1-5 for the query. Skip sponsored cards. Keep only listings that pass the form rule.
- Per listing record: ASIN, title, brand (byline), price, rating, review count, badge bucket.
- **Units** = badge bucket floor (1K+ → 1,000). It counts unique buyers, so it is a floor ◆. Revenue floor = units × price ◈.
- **Listing entry date from the ASIN**: ASINs are issued in order. B0D… ≈ 2024, B0F… ≈ 2025, B0G/B0H… ≈ 2026. Calibrate on a few listings with "Date First Available" visible; error ±1-2 months ◈. ASINs are usually global across Amazon sites ◈ (verify on a few).
- **Brand** = byline if present; else the first title word if it is not a generic product word; else "unbranded". Fold accents ("L'Oréal" = "L'Oreal"), drop a leading "The", keep a list of generic/ingredient words (retinol, collagen, peptide, beef, color…) that must never be read as brands. We got fake brands from all three mistakes.
- **Brand age** = oldest listing of that brand in your sample.
- **NEW brand** = entered < 24 months ago AND not an established company entering a new product (L'Oréal, Palmer's etc.). Keep this "established" list explicit and in a file.
- Split units into three buckets: **old brands · new named brands · unbranded/generic**.

### Step 2. Concentration

Compute **per brand, not per listing** (one brand with 5 sizes is one player):
- Top-1 and top-3 brand share of shelf units.
- HHI = sum of squared brand shares × 10,000. Vendor rule of thumb ◇: < 1,500 open, 1,500-2,500 moderate, > 2,500 hard.
- Read concentration **together with who the top-3 are and how old they are**: a high top-3 share held by brands that entered last year means the market is moving and newcomers can win; the same share held by long-established brands means it is captured. In our data, color-changing foundation had top-3 = 74% yet 80% of units went to brands under 24 months old, while men's hair-removal cream had top-3 = 93% and only 6% to new brands. Concentration alone would have called both "closed".

### Step 3. Newcomer survival (the survivorship-free part)

**On Amazon (all markets):**
- Cohort = brands whose first listing entered 12-24 months ago.
- For each cohort brand: badge bucket today. Report the distribution (none / 50-99 / 100-499 / 500-999 / 1K+), not one number.
- Classify each cohort brand: **A** no own store found (marketplace-native) · **B** own store, first web evidence (RDAP / first Wayback capture) 2024 or later · **C** own store with evidence before 2024 = older brand that just added Amazon. Report survival for A, B, C separately. ◆ Lesson: without this split, old brands entering Amazon look like "newcomers" and distort the result; and a hand-picked sample of brands with websites hid that most marketplace-native newcomers fail (58% under 50/mo after 1-2 years in our data).
- "No badge" ≠ dead brand: some live off Amazon (one brand had no badge but ~250 reviews/mo on its own store). Check classes B/C on their own channel before calling them failures.

**On Meta, EU/UK markets (do this — it is the cleanest survival number available):**
- Pull all ads for the category phrase including inactive ones (EU/UK keep them ~1 year).
- Unit = **store**, not page: group by registrable landing domain, merge persona/creator/advertorial pages that land on the same shop. Exclude marketplace landings (amazon, tiktok).
- Cohort = stores whose first ad started 6-12 months ago. Success = the store has at least one ad that ran 90+ days.
- Survival rate = successful stores ÷ all stores in the cohort. Also record reach for the leaders (spend estimate = reach × frequency × CPM / 1000, error ±2-5× per ad ◈).

**On Meta, US/AU (active only):**
- Count from Meta's "~N results" (US, active, exact phrase), then the same search with start date before today−30 / −90 / −180 days.
- Share of ads aged 90+ / 180+: high = evergreen market where working ads keep running; low = many short tests that die.
- Sample ads evenly across the age windows, group by store domain, list which stores keep ads alive 90+ / 180+ days and how old those stores are.
- Stopped ads are invisible, so this is **not** a survival rate. If the product matters, re-check the same searches after 30 days to see which of today's ads died.

### Step 4. Trend and stage

- Google Trends, market geo, 5 years, weekly, drop the partial last week. Growth = last 12 full weeks ÷ same 12 weeks a year ago (YoY, robust to seasonality).
- Always pull 2 control terms (we used "shampoo", "body lotion") and divide by their YoY: in Apr-Jun 2026 every term spiked together in the US — a Google artifact, not demand. Check whether it appears in your geos too.
- Pull on 3 different days and average; rare terms are noisy (flag terms with many zero weeks).
- Labels: YoY ≥ 1.2 growing · 0.8-1.2 flat · < 0.8 falling. "Post-spike" flag if the last 12 weeks < 50% of the best 4-week average.
- Assign a life-cycle stage, category and leader separately (they often differ):
  A test (one advertiser, ads < 30 days) · B breakout (leader's ads multiply, all young) · C clone wave (many advertisers, leader's first ads pass 90 days, 1K+ listings appear; **best window** if an angle is open) · D maturity (few survivors with 180+ day ads, prices falling) · E decline (falling YoY, aged ads stop) · Fad (6-8 week spike, then gone).
- ◆ Research backing (Golder & Tellis 1993): pioneers failed 47% of the time, early growth-stage leaders 8% — so entering at C beats entering at A/B.

### Step 5. Channel cross-check

- TikTok Shop where live: lifetime "sold" per product (lifetime ÷ months listed, rough). Direct access hits a captcha; cached pages may work; do not bypass. Trend needs FastMoss/Kalodata (paid, owner decides).
- Absence from a channel counts **against** a product only if: (a) it has sold visibly for 6+ months somewhere, (b) the channel suits the product (TikTok = 5-second visual demo + impulse price; Amazon = searched by problem/name, replenishment; Meta → own store = needs a story, higher AOV), (c) the channel allows the category. Otherwise record "not yet" or "not suited".
- Meta-only screening misses TikTok-native hits (we found one with 597K sold and zero aged Meta ads). Amazon-only screening misses DTC brands (our fastest-growing soap brand was invisible on Amazon). Read every channel on its own.

### Step 6 (only for finalists). Leader proof

- Two independent signals must agree before you call a leader "proven" ◆ (our strongest evidence was a review curve that rose in step with traffic).
- Review curve: Loox public widget works without auth (`loox.io/widget/<clientId>/reviews/<productId>?limit=40&page=N`; order is "featured", so pull the full set). Use the curve's **shape**, not its level. Curves break when a store switches review apps or imports reviews — always pair with a second signal.
- Trustpilot logged-off: only the latest ~200 reviews → good for 1-2★ share (quality red flag: 9.5% was our worst, 2% our best), not for history.
- Wayback snapshots of store/Trustpilot pages: cheap historical point checks.
- Untested but promising (try, report the result): Shop app "bought in past month" badge (first platform-counted DTC volume floor); ImportYeti (US sea imports curve + the leader's factory; US only, air freight invisible); Amazon Product Opportunity Explorer (needs a seller account; gives Amazon's own "new launches vs successful launches" ratio = exactly our survival metric).

---

## 5. Mistakes we made — do not repeat

1. **"Fewer than 500 reviews = new" is wrong.** Fast winners collect 10,000 reviews in 10 months. The proxy called our most open category 3% new; dated by ASIN it was 80%. Date by ASIN.
2. **Ad count ≠ success.** 870 active ads with ~16K site visits. Ad **age** is the signal, count is testing intensity.
3. **"Oldest ad in the top 30"** is not longevity. Use Meta's counts with start-date filters. Logged-off, the library loads only ~30 top ads per query; read the "~N results" number (wait ~4 s for it).
4. **Generic phrases on Meta are noisy** (salons, clinics, car dealers match). Use specific product phrases and check a sample by hand.
5. **Count stores, not pages.** Persona pages of one company count once.
6. **Guru / YouTube / case-study revenue is not data** — ran 2× to 400× above our sanity band. Use only as leads.
7. **Prices from the real leader's store**, not from clones.
8. **Listing age ≠ brand age.** Old brands adding a new product look new.
9. **Brand success ≠ category openness.** One DTC brand grew fast while its category ranked ~60 of 94. Report both levels.
10. **Free traffic sources disagree on country split by up to 2×** (34% vs 71% US for one store). Any country-level conclusion needs two sources.
11. **Free sources rate-limit fast** (Shopify bot check after ~20 requests, Trustpilot 403, Trends "Oops", Cloudflare blocks). Pace requests, keep several routes, never bypass.
12. **Never mix method versions.** If you change a rule, bump the version, re-run all products, log the reason.

---

## 6. Thresholds (◇ calibrated on the US only — adapt and disclose)

| Item | US value we used | Other markets |
|---|---|---|
| Winner listing | badge ≥ 1,000/mo (≈ $12-20K revenue/mo) | Use a revenue bar (≈ $15K/mo floor = units × price) rather than a unit bar, since UK/DE/AU shelves are smaller ◇ |
| New brand | entered < 24 months, not an established company | same |
| Ad "lives" | started ≥ 90 days ago; 180+ = very strong | same |
| Ad rarity reference | ◈ ~2% of US ads reach 90 days (one vendor study, 4,634 ads); another study of DTC brands says 26% — compare within a category, not to these numbers | — |
| Kill: falling | Trends YoY (control-adjusted) < 0.8 | same |
| Kill: closed | new-brand units < 10,000/mo AND no store with a 90+ day Meta ad | scale the 10,000 by market size, state the number used |
| Small demand | category < ~5-10K units/mo across channels | scale, state |

---

## 7. Output

### 7.1 One CSV row per product × market (`openness.csv`)

```
product, market, method_version, date_collected,
shelf_units_mo, shelf_revenue_floor_mo, median_price,
listings_on_target, brands_count,
top1_share, top3_share, hhi, top3_brands_with_age,
units_old_brands, units_new_named, units_generic, new_named_share,
new_named_winners, generic_winners,
cohort_12_24_n, cohort_A_n, cohort_A_pct_winner, cohort_B_n, cohort_C_n, cohort_pct_no_badge,
meta_active_ads, meta_90d_plus, meta_180d_plus, meta_aged_share_90,
meta_stores_with_90d_ad, meta_cohort_survival_rate (EU/UK only, else blank),
tiktok_sold_top (if live), trends_yoy_adj, trends_label, post_spike_flag,
stage_category, stage_leader, market_type (captured/price_war/eats_newcomers/open/too_early),
confidence, notes
```

### 7.2 One card per product (markdown)

```
Product:
  Markets checked: __ (primary: __)
  Demand        : ~N units/mo floor per market, revenue floor $__      [◆◈◇]
  Concentration : top-3 __% (who, how old) · HHI __
  Newcomers     : new named brands hold __% · winners __ · cohort survival __ (A/B/C split)
  Meta          : aged share __ · stores alive 90d+ __ · EU/UK survival rate __
  Trend / stage : YoY __ (__) · category stage _ / leader stage _
  Market type   : captured / price war / eats newcomers / open / too early
  Best market   : __ and why
  Verdict       : enter / test / watch / skip — and the ONE fact that would change it
  Unknowns      : what could not be measured and why
```

### 7.3 Summary table

All 20 products ranked by **units taken by new named brands per month** in their best market, with market type and verdict next to it. Show the full distribution, not just the top.

### 7.4 Method log

A table of every source you tried: date, source, used for, result, verdict (keep / unreliable / dead end), including failures. Plus a short list of new method insights with ◆◈◇ marks. This is as valuable as the verdicts.

---

## 8. Order of work

1. Day 1: verify the per-market source map (section 3) on 1-2 products; write the pre-registration file (step 0) for all 20.
2. Screen all 20 in their primary market: steps 1-4. Apply kill rules.
3. For survivors: run the same in their other markets (EU/UK Meta survival is the priority there).
4. Finalists (top ~5): step 5-6 and the cards.
5. Before reporting, attack your own result: for each top verdict, list the strongest reason it might be wrong (wrong form filter, generic phrase noise, one-snapshot spike, a dominant brand hidden under several names) and check it.

What you hand back: `openness.csv`, the cards, the summary table, the method log, the pre-registration file, and the scripts — so anyone can re-run and get the same ranking.
