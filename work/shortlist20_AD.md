# Devil's advocate + error check on shortlist20 (v1 → v2)

Date: 2026-11-07. The v1 files are kept as `shortlist20_v1.md` and `shortlist20_v1.py`. The current `shortlist20.md` is v2.

## Errors found and fixed

1. **Longevity metric was wrong.**
   - v1 used "oldest ad among the top 30 by impressions", so a single surviving old ad gave full credit.
   - v2 counts the leader's active US ads that started ≥6 months ago, using the Ad Library filter `start_date[max]=2026-05-07`.
   - Results: Lhanel back stretcher 0 (v1 implied 6 months), Blissal towel 1, Luhxe 0, Therapet 0, Good Origins 0, Swarva 0, North Alpine 1, Menvault 8, Sofyre 0 (13,000 ads, all new).
   - Truly long-running: Everstride 190, Skult 160, Purriq 130, Zevessa 94/94, SkiGuards 60, Moxielash 59, Kaori 53, Earthly Derm 44, Travlr 43, MLMT 26.
2. **16-head massager evidence was from unrelated advertisers.** The v1 query `"16 head" massager` matched neck massagers and vagus-nerve devices; `"16 head"` alone gives 0. Re-checked with `"16-head"`: 460 ads; real sellers are Zevessa (94 ads, all 6+ months old, pain angle), Alythera (180, holiday gift angle) and VitalHorse (a horse-massager niche).
3. **Guessed leader counts replaced with measured ones:** LED mask (Solawave 200, 0 aged), lash serum (Moxielash 310, 59 aged), hair-removal cream (Luuma 66, 37 aged).
4. **Seat-cushion price:** Travlr sells at NZ$181 (◈ ~US$105), not the $80 assumed from the YouTuber's clone. Economics stay strong.

Effect on the ranking:
- **Rose:** lash serum (#20 → #5), persimmon soap (#16 → #6).
- **Fell:** 16-head massager (#4 → #9), LED mask (#6 → #15), back stretcher (#9 → #13), exfoliating towel (#10 → #14), leak-proof boxers (#19 → #20).
- **Dropped out of the top 20:** pheromone perfume oil (#13 → #21), the only product to leave.
- **Entered the top 20:** tanning balm (#18; seasonal, launch in spring).

## Devil's advocate: what still does not hold up

1. **"Advertising" is not "profitable".** 13,000 Sofyre ads, all under 6 months old, look like aggressive testing, not proof. Even ads aged 6+ months only show the advertiser keeps paying; margin is unknown.
2. **Search % is noisy for broad terms.** "beef tallow" includes cooking tallow; "tennis bracelet" includes fine jewelry; "compression socks" includes medical and athletic socks; "body massager" is generic. S overstates demand for our specific product in those rows.
3. **The clone measure (C) is inconsistent across rows.** Some rows use exact phrases, others unordered keywords. Brand-dominated categories (LED masks: Solawave, Omnilux, CurrentBody) get C=5 because few domains appear, yet they are the hardest to beat.
4. **Max CAC is a model, not a benchmark.** It is never compared with real US Meta costs in Q4/Q1. Rows with CAC ≈ $22-28 (socks, silvervine, soaps, towel) need strong creatives and repeat purchases to work for a new brand with no pixel history.
5. **Weights are a choice.** Ranks 4-13 sit within ~9 points; a different weighting reorders them. Treat the list as tiers, not exact ranks.
6. **Seasonality is not scored.** The ski sleeve (Dec-Feb) and tanning balm (spring-summer) rank on evidence but have narrow windows.
7. **Selection bias remains.** Every product comes from one course seller's videos, and his viewers clone them (see persimmon soap).
8. **Capacity.** Owner + 1 employee + a small budget can test 2-3 products, not 20.

## What survives

- **Tier A (live and long-running leader, real search, sellable):**
  - compression socks;
  - lash serum (cosmetic peptide formula only);
  - tennis bracelet;
  - persimmon soap;
  - turmeric soap.
- **Tier B (strong leader, but weak search or narrow window):**
  - chin wrap;
  - silvervine cat sticks;
  - seat cushion;
  - ski sleeve (seasonal);
  - 16-head massager (gift angle, Alythera).
- **Tier C:** the rest; mostly no aged ads or regulatory weight.
