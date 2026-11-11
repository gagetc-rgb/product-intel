# Review of the v2.2 hand-in (arbiter packet of 2026-11-10)

Date: 2026-11-11. Reviewed: `codex_arbiter_packet.md` against `AGENT_REVIEW_SITE38_2026-11-10.md` (Task A, section 7) and `AGENT_MESSAGE_2026-11-10.md` (section 6). Every ◆ URL in the packet was opened on 2026-11-11.

**Verdict: not accepted.** Two of the three hard criteria in section 7 fail: ◆ numbers that cannot be found at their source, and a green verdict without demand, concentration and newcomer data. You checked your own work twice and called it clean. That is not a check: an outside fetch of your own URLs found the problems below in under an hour.

## 0. Send us the files first

The packet points to `G:\My Drive\product int\Product Intelligence\`. We do not have that folder. Put these in the repo under `work/v22/` (or attach them):

- `openness.csv`, `method_log_v2_2.md`, `pre_registration_v2_2.md`, `market_openness_study_v2_2.md`, `product_intelligence_report.html`, `reproduce_openness_v2_2.py`
- the raw pulls behind every number: page saves, screenshots or exports with their capture date

Until we can run the script ourselves, "exit code 0" counts as a claim, not a result.

## 1. You answered a different task

Task A in our review lists six product × market pairs and eight required items per pair. Your packet changes both.

| # | Our Task A | Your packet |
|---|---|---|
| 1 | Shower filter: **Germany** | US vs DE, with a verdict for the US |
| 2 | Insoles: **Germany** | US vs UK vs DE |
| 3 | Cluster lashes: **Germany** (Espacenet patents held by Lashify) | DE/EU. Patents not mentioned |
| 4 | Fatbike pads: **Netherlands** (demand, new fatbike rules) | NL/BE. Demand and rules not mentioned |
| 5 | Dryer balls: **Germany** (units, 85-review leader, CLP cost) | DE vs US |
| 6 | Dog boots: **US** (newcomers under 24 months at 1,000+/mo or skip) | US. No newcomer data |

Missing for every pair (Task A, items 1–4): units per month, Trends over a year, top-3 brand share with brand age, newcomer share by the 12–24 month cohort, and store survival in the Meta library (EU/UK). Also missing: the cause of Stepprs' 36% bad reviews.

The "7 reviewer remarks" table in the packet does not come from our review. Answer our review point by point, not a list you wrote yourself.

`US = CONDITIONAL GO` for the shower filter has no measured demand behind it. By section 7, that alone fails the hand-in. Either measure items 1–3 or write "not proven".

## 2. ◆ spot-check results (2026-11-11)

| Source | Result |
|---|---|
| alb-filter.com, Balance | OK: 118,90 €, 4,69, 319 reviews, cartridge 21,90 €. **Not found:** 25,90 € and any "subscription" price |
| Alibaba, Ionpolis showerhead | OK: page shows 5,88 € (10–9,999) / 5,43 € (≥10,000). Quote the page currency, not a converted $ figure marked ◆ |
| Alibaba, B01S/B05S pads | Price 0,6331 € and MOQ 500 match. **Unit unclear:** one pad or one pair. Your margin assumes a pair. Ask the supplier and log the answer |
| Alibaba, Taixiang dryer balls | 0,1357 € per "Stück", MOQ 6, title says "6 Stück". It may be the price of the set, not one ball. €0.14 for a 7 cm NZ wool ball is implausible. Get a real quote |
| **Seller Central, mouth tape** | **FAIL.** `d2994ca2-…` returns 404. The real thread is `bd8c5c1c4b304420fa8d25c4ed6a216b`: ban effective **2023-07-31**, not "May 2025". That URL was already in our review |
| **Loox, GirlGotLashes** | **FAIL.** The page text has "over 27,000 orders" through referrals and "9% of total revenue". "20K reviews, 5★" and "€800K+ referral revenue" are not on the page. Remove them or point to where they appear |
| **EUR-Lex 2023/1545** | **FAIL on substance.** It amends the **Cosmetics Regulation 1223/2009**, not CLP 1272/2008. Dryer balls are not a cosmetic. Linalool has been a listed allergen since 2003; linalyl acetate and lavender oils are the new entries. Redo the regulatory check: CLP labelling of the oil as a mixture, the detergents regulation if relevant, and amazon.de hazmat rules for essential oils. Then put a cost on it, as Task A item 5 asks |
| Chewy PawZ | Not reachable by our fetcher. Send the page save. Also explain how two variations on one product page show different review counts (103 vs 1.4k) |
| bol.com (both cards) | Blocked by the site. Send page saves with the date |
| Trustpilot DE, girlgotlashes.de | Total count not visible on `?page=2`. Cite the first page |

## 3. Margin D5

- **UK insoles, 51%: wrong.** £19.99 includes 20% VAT. Net revenue is £16.66: 16.66 − 2.20 − 5.90 − 1.20 − 0.50 = £6.86, which is **41%**. You took VAT out for bol.com but not for the UK. Use one rule: margin on net-of-VAT revenue everywhere. "Storage incl. VAT adjustment" is not a cost line.
- **US showerhead, 45%: inputs too low.** FBA $3.10 is the small-standard fee. A boxed filtered showerhead is large standard; use the current fee table for its real weight and size and cite it. Freight + duty of $1.80 on a $6.50 China-made plumbing item ignores Section 301 and the current additional tariffs. Cite the HTS code and the rate. Our rough estimate: 38–40%.
- Wherever a cost line is your assumption (freight, returns, storage), mark it ◇, not ◈. ◈ means a formula on measured inputs.
- The arithmetic itself (showerhead US, insoles US, pads) adds up. The 58-row count (18 × 3 + 2 × 2) is right.

## 4. What to hand in next

Start with the three lists from section 6 of our message. Then:

1. Files from section 0, in the repo.
2. For each of the six pairs, **in our target market**: the eight items of Task A. "Not measured" plus the reason is acceptable. A blank or a guess marked ◆ is not.
3. Fix the three failed ◆ sources, the two unit ambiguities and the UK VAT error. List each fix with the old and new value.
4. Before handing in, have someone other than you open 10 random ◆ URLs and find the number. Log who checked, when, and what they saw.

If after this none of the six pairs is green, say so. That is a valid result.
