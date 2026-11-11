# Acceptance of Codex step 1 (working checkpoint) — 2026-11-11

Input: `STEP1_STATUS_2026-11-11.md`, `meta_stores.csv` (39 rows, 31 counted on 2026-11-11), `follower_pages.csv` (383 cards, 19 domains), `store_facts.csv` (32 rows), `cogs.csv` (4 US soap rows), and the small notes beside them. Checked by Opus on 2026-11-11, same day as Codex's reads. Nothing here is on the site.

## 1. Spot-check against sources (9 checks, 15 values)

| # | Row | Codex | Our read, 2026-11-11 | Result |
|---|---|---|---|---|
| 1 | trykaoli.com, active 30+ | 0, "no ads match" | "No ads match your search criteria"; unfiltered: ~110 ads, all 28 visible started 29 Oct - 6 Nov | ✓ (total moved ~160 → ~110 the same day: churn) |
| 2 | thetallowedtruth.com, 90+ | ~300; newest visible 2026-06-18 | ~300; 30 cards, newest 2026-06-18 | ✓ |
| 3 | thetallowedtruth.com page names | 18 "Ben Corkery Founder at The Tallowed Truth", 11 brand, 1 "Non-Woke Daily" | 18 / 11 / 1 | ✓ (count); see §3 on the class |
| 4 | getmyto.com, 90+ | ~27; newest 2026-08-01; 27 brand | ~27; newest 2026-08-01; 27 × "Myto Oral Care" | ✓ |
| 5 | getxstance.com, 180+ | ~170 | ~170; newest visible 2026-05-12 (cutoff 05-15) | ✓ |
| 6 | Ad 1460137838991504 | 2026-04-11, "Foot Care Tips", lands on getxstance | same | ✓ |
| 7 | RDAP of 7 domains (getxstance, thexstance, bekyndbeauty, getmyto, trymooths, try-kaori, wildgoldtallow) | 2024-12-13, 2020-11-26, 2020-02-16, 2025-12-19, 2026-05-12, 2026-02-11, 2025-03-17 | identical (Verisign RDAP) | ✓ ×7 |
| 8 | Prices: MYTO $29.99 / $59.98 / $89.97; Wild Gold $45 | as stated | MYTO page in USD shows the same three; Wild Gold `products.json` $45.00 | ✓ |
| 9 | Oregon Soap Co. stamped bars | $3.10 a bar, 45-bar case, 5 cases minimum | same on the pricing page | ✓ |

Score: 9 of 9 checks, 15 of 15 values match. With the first pass (9 of 12, 1 wrong) the running total is 18 of 21 checks confirmed, 1 wrong, 2 not checkable. No invented number has been found in either pass.

## 2. What we accept

- **Meta age counts (section 2) for the 31 domains counted on 2026-11-11**: accepted, as domain-keyword floors. Rows marked noisy (cattle-creek.com, try-forge.com: own share of the first 20 cards 3/20 to "heavily contaminated") are not used as store counts.
- **Page types (section 4)**: counts accepted; class labels accepted with one reading change (§3).
- **Store facts**: accepted where Codex marks them read; every "US not confirmed" price stays provisional. Cause: the browser Codex uses is geolocated outside the US (pages show IDR and Indonesian shipping). `?currency=USD` fixes the currency, not the delivery country.
- **US soap makers (`cogs.csv`)**: accepted as listing prices for stock bars, not quotes for a persimmon formula.
- **Notes**: Beamach (no Meta ads on beamach.store; TikTok counters are lifetime), pre-wash personas (both land on bekyndbeauty.com, 2020), tooth-powder side checks, Babe 6/20 sample: accepted as written, with Codex's own limits.

Not accepted / not done: tooth-powder category leader; Hanae page types for all 90+ ads; Hanae low reviews; Mirai review-window endpoints (the 200 IDs were not saved, so they are lost for good).

## 3. One reading change: founder pages are not personas

The brief asked to classify by page name, and Codex did that correctly: "Ben Corkery Founder at The Tallowed Truth" is a human name, so `person`. But the reason for the field is to separate invented personas (a funnel we will not copy) from the brand speaking for itself. A page that names itself as the brand's founder is the brand speaking. For M2 we therefore read Tallowed Truth as **29 of 30 brand-affiliated**, not 11 of 30. All other `person` pages (Kaori's "Linda Doxey", "Margaret Whittaker" etc., Pure Good's 6, Neptune's 2) stay as possible personas. For step 2, add a class `founder` (page name states a role at the brand).

## 4. What the data says (◈ unless marked)

Counts are active / 90+ / 180+ ads on the domain keyword, US, 2026-11-11 ◆. "Brand share" = brand or founder pages among the visible 90+ cards.

| Product | Young follower (domain reg.) | Ads | Brand share of 90+ | Reading |
|---|---|---|---|---|
| Persimmon soap | try-kaori.com (2026-02) | 750 / 210 / 67 | 11 of 30; 19 persona-style ("Linda Doxey", "Margaret Whittaker", "Grandma's Glow", "Grandma's Care Journal" …) | Holds, but mostly through persona pages. Evidence for the funnel, weak evidence that a lawful copy holds. |
| Persimmon soap | beamach.store (TikTok leader) | 0 | — | Sells on TikTok Shop only (12.5K sold lifetime ◆); no Meta proof. |
| Tallow balm | wildgoldtallow.com (2025-03) | 35 / 35 / 24 | 29 of 29 | The cleanest lawful follower in the set: small, every ad from the brand, 24 past 180 days. $45 a jar, subscription preselected at $31.50. |
| Tallow balm | bare-ritual.com (2025-08) | 2,200 / 180 / 27 | 20 of 20 | Holds at scale, brand pages only. US price still unconfirmed (page showed Indonesian shipping). |
| Turmeric soap | glomelanin.com (old, 2022) | 180 / 30 / 5 | 28 of 28 | Not a young follower. |
| Turmeric soap | trykaoli.com (2026-05) | 110-160 / 0 / 0 | — | Nothing older than 30 days: no evidence yet. Baseline for 2026-12-08. |
| Work insoles | getxstance.com (2024-12) | 550 / 280 / 170 | 27 of 29 | **Not young after all**: the site links to thexstance.com (2020) and uses its e-mail domain. |
| Work insoles | movaracare.com (2026-02) | 200 / 19 / 8 | 19 of 19 | Its 90+ ads sell **work boots**, not insoles. |
| Silvervine sticks | purriq.com (2025-08) | 190 / 67 / 46 | 21 of 27 (+4 "expert" pages) | Holds. |
| Silvervine sticks | heycomfora, clawval, tryarleo, nylatails, kittykazoom | 0-8 at 90+ | — | Four of five newer entrants have nothing past 90 days. Baseline for the death rate on 2026-12-08. |
| Tooth powder | getmyto.com (2025-12) | 150 / 27 / 0 | 27 of 27 | Young, brand-only, $29.99 with automatic refills offered. Leader unknown. |
| Tooth powder | trymooths.com (2026-05) | 55 / 7 / 0 | 6 of 7 | Young, thin. |

Consequences for the plan:

1. **Insoles lose their "two young followers"** (HANDOFF, NEXT_FOR_OPUS): one is tied to a 2020 business, the other advertises boots. Insoles now have no confirmed young follower holding 90+ days on insoles.
2. **Tallow balm is the only product with two young, brand-only followers holding 90+ and 180+ days** (Wild Gold, Bare Ritual). It is also the most crowded (M2 result: 11 sellers with 90+ ads).
3. **Persimmon soap's only young follower depends on persona pages**: 19 of 30 visible 90+ cards. A lawful copy has no proof here yet.
4. **Tooth powder** is a real new candidate on M2 (MYTO), pending the leader and MYTO's 180-day mark (domain is 11 months old; its oldest ads date from 2026-06-30).
5. **US-made soap**: stock bars list at $2.40-3.70 (Oregon Soap Co., Wholesale Tallow Soap USA, Made Natural) to $7.25 (Bath Promotions, engraved), minimums 100-500 bars. That is before a custom persimmon formula, which none of them prices publicly. Against a China bar plus 37.5% duty it has to be compared on a real quote.

## 5. Assessment of Codex as a source (two passes)

- **Accuracy: high.** 18 of 21 checks confirmed, 1 date-range error (Mirai, pass 1), 0 invented values. Counts we took independently (Sonnet subagent, 2026-11-10) agree within Meta's rounding: getxstance 470/280/170 vs 550/280/170, purriq 180/67/46 vs 190/67/46, stepprs 910/35/31 vs 910/38/34.
- **Honesty: high.** Unknowns are written as unknown with the reason; it flags its own non-random samples and noisy searches unprompted (Cattle Creek, Forge, Movara boots, the GetXstance–thexstance link). The GetXstance finding is one we had missed.
- **Literalness: a weakness.** It applies the brief's rule exactly even where the purpose says otherwise (founder page as `person`), and copies one classification note across all rows of a domain (Superfeet rows mention Fleet Feet). It does not synthesise; that stays our job.
- **Completeness and speed: the main weakness.** Step 1 is still a checkpoint after two working days: tooth-powder leader, Hanae page types and reviews are open; 8 legacy rows have no age counts; it lost raw data once (Mirai IDs). It also could not get a US delivery view, so many prices stay provisional.
- **Prose: over-hedged.** Every line carries caveats; the status file is hard to read. Harmless for data, costly for review time.

Verdict: trust Codex's numbers as raw data without re-checking every row (keep a 5-10 row spot-check per hand-in); do not use its text as conclusions; give it narrow, closed tasks with a fixed output schema and a deadline.

## 6. Asks for the rest of step 1 (and step 2)

1. Tooth powder: the leader (product-filtered 90+ ads; start with Banyan Botanicals and Essential Oxygen), then section 2/4/5 for it.
2. Hanae: page type for every 90+ card, split lash vs concealer by landing URL; Babe and Hanae low reviews on a defined sample (all 1-3★ of the last 90 days, or the first N by date, not "most relevant").
3. Add `founder` to page types.
4. Save raw IDs and dates for every review sample.
5. If a US delivery view cannot be had, say so once in the status file and stop retrying prices.
