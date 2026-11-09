# Task: monthly review counts for 16 DTC stores (for a computer-use agent)

## Goal
For each store below, find how many customer reviews were posted **per calendar month from Nov 2025 to Oct 2026** on the store's own website. Growth of reviews over time is our proxy for growth of sales. We need real counts read from the page, not estimates.

## Hard rules
1. Never guess or fill a number you did not see. If something cannot be read, write `unknown` and say why.
2. Record the exact URL you used and the date/time you read it.
3. Use only the store's own website (not Amazon, not Trustpilot).
4. Do not log in, do not buy, do not submit forms. Only open pages, click "sort", "next page" and "load more".
5. If a page shows a robot check or CAPTCHA, stop for that store and write `blocked`.

## How to do it (per store)
1. Open the store, open its best-selling product (the first product on the home page, or the one named below).
2. Scroll to the reviews block. Note the widget brand (Loox, Judge.me, Okendo, Yotpo, Stamped, Junip) and the **total review count** it shows.
3. Switch the sort to **Newest / Most recent**. If there is no such sort, write `no date sort` and note the default order.
4. Page through the reviews and record each review's date until you pass **1 Nov 2025**.
   - If a month has more than ~300 reviews, it's too many to count all. Instead, write down the date of the review at every 50th position (position 1, 50, 100, ...) until you pass 1 Nov 2025. We will compute the monthly counts from these positions.
5. If the widget shows only relative dates ("3 weeks ago"), record them as they are shown.
6. If the store also has an "All reviews" page (often /pages/reviews), prefer it: it covers all products.

## Stores (category → store → widget we detected on the homepage)
| # | Category | Store | Widget |
|---|---|---|---|
| 1 | Color-changing foundation | luxe.com | Loox + Judge.me |
| 2 | Color-changing foundation | smooche.com | Loox |
| 3 | Color-changing foundation | primeprometics.com | Stamped |
| 4 | Body oil | goda.co (Silk Body Oil) | Loox (23,956 total) |
| 5 | Body oil | drmtlgy.com | several |
| 6 | Tallow balm | terralotus.shop | Judge.me |
| 7 | Tallow balm | try-forge.com | Judge.me |
| 8 | Tallow balm | ancestralcosmetics.com | Judge.me |
| 9 | Tallow balm | bare-ritual.com | Loox |
| 10 | Tallow balm | wildgoldtallow.com | Judge.me |
| 11 | Scent diffuser | scentifyhome.com | Judge.me |
| 12 | Scent diffuser | aurahouse.com | Okendo |
| 13 | Scent diffuser | aroma360.com | Okendo |
| 14 | Persimmon soap | try-kaori.com | not detected |
| 15 | Persimmon soap | miraiclinical.com | Yotpo |
| 16 | Shower filter | sproos.co | Junip |

## Output: one CSV file, `review_counts.csv`
Columns:
`store, product_url, widget, total_reviews_shown, sort_used, method, month, count, sample_positions, read_at, notes`
- `method` = `full` (every review in the month counted) or `positions` (dates at every 50th review)
- `month` = YYYY-MM, one row per month (Nov 2025 ... Oct 2026)
- `sample_positions` (for the `positions` method only) = `position:date; position:date; ...`
- `notes` = anything odd: reviews imported from Amazon, many reviews on one day, the same text repeated, no dates, blocked

Also save one screenshot per store showing the total review count and the sort setting.

## Red flags to note (do not fix, just report)
- Many reviews with the same date or the same text (bulk import).
- Reviews labelled "imported" or "from Amazon/AliExpress".
- Total count on the badge differs a lot from the number of reviews you can page through.
