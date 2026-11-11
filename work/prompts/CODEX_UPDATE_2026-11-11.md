# Update for Codex, 2026-11-11 (adds to `CODEX_FOLLOWUP_2026-11-11.md`)

Read `CODEX_FOLLOWUP_2026-11-11.md` first; its rules and hand-in stay. This file adds five items. Same rules: public pages only, no logins or bypasses, never press cart, buy, subscribe or checkout controls, unknown = "unknown" plus the reason.

## 1. Add a 60-day cutoff

In every `meta_stores.csv` row add `active_60_plus` (`start_date[max]` = run date minus 60 days), with the same filter check as the other cutoffs. The owner wants 30+ and 60+ as the baseline for the 2026-12-08 re-check.

## 2. Tooth whitening powder joins step 1 (sixth product)

Found on 2026-11-11 (`work/lensm/M2_EXTRA_2026-11-11.md`): two young stores hold Meta ads 90+ days, getmyto.com (MYTO, registered 2025-12-19) and offers.trymooths.com (MOOTHS, trymooths.com registered 2026-05-12).

- Find the category leader: the store with the most 90+ day US ads for tooth powder (phrases "teeth whitening powder", "tooth powder", "remineralizing tooth powder"; write the keyword card first).
- For MYTO, MOOTHS and the leader: all of section 2 (counts and the oldest ad's start date), section 4 (page types) and section 5 (store facts) of the follow-up task.
- Also check trydeos.com, bronzepalms.com, essentialoxygen.com: do they sell tooth powder? (They came up in the same search; not read yet.)

## 3. Persimmon soap: the TikTok Shop leader

EchoTik shows the US TikTok Shop leader for persimmon soap is the shop "Beamach Oral Care" (listing "Persimmon Soap for Old People Smell, Japanese Persimmon & Green Tea", $15.99-30.59), not Mirai or Kaori. Find whether it has its own store domain and Meta ads; if yes, give it the section 2 counts and section 4 page types. Record whether Mirai and Kaori sell on TikTok Shop at all (search their names on tiktok.com/shop logged off; if blocked, say so).

## 4. Soap made in the US: price check for comparison

The owner asks why soap would come from China when it can be made in the US (Chinese soap pays about 37.5% duty). Collect 3-5 US private-label or contract soap makers that publish prices or minimums: bar size, unit price at 500 and 5,000 bars, minimum order, lead time, whether custom scent or additive (e.g. persimmon extract) is possible. Listing prices only, no quotes requested, no contact with sellers. Output rows in `cogs.csv` with `country = US`.

## 5. Pre-wash oil: one check

The 90+ day advertisers for "pre shampoo hair oil" were ekmiveda.com, bekyndbeauty.com, peteandpedro.com, us.phyto.com, plus pages "Dawna Wilson" and "Kristin McAllister" with no domain read. Open one ad of each persona page and record its landing domain and registration date. Nothing else for this product.

## 6. Lash serum is back, as a main candidate

Reversed on 2026-11-11 after a domain-level count (`work/lensm/LASH_CHECK_2026-11-11.md`): hanaekorea.com holds ~250 ads alive 90+ days and ~12 alive 180+. Add lash serum to step 1 with these tasks only:
- section 4 (page types) for every Hanae ad aged 90+; open the page "Trending In Korea": what it claims, whether it presents a person or expert, where it lands;
- section 5 (store facts) for hanaekorea.com;
- the 1-3★ reviews of Hanae (store widget or Amazon listing B0HBZXGY4W) and of Babe Original: count how many say "did not work" or "no growth".

## Hand-in

Add items 1-5 to the step 1 hand-in (`STEP1_STATUS_<date>.md` says what is done for each). If step 1 is already handed in, send these as `STEP1_ADDENDUM_<date>.md` with the updated CSV files.
