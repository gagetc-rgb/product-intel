# Task 2: finish the Amazon US data (follow-up to AMAZON_TASK.md)

Thank you for the first two files — they are clean and usable. Three things are still missing. Same rules as before: US delivery ZIP **10001** ("Deliver to New York 10001", prices in $), no login, no purchases, no guessing; if you see a robot check, CAPTCHA or "access restricted" page, stop and report it.

## 1. "Date First Available" for 120 products (most important)

In the first file every `date_first_available` cell is empty. This date is the main thing we need: it tells us how old each brand is on Amazon.

How to find it on a product page `https://www.amazon.com/dp/<ASIN>`:
1. Scroll down to the section called **"Product information"**, **"Item details"**, **"Product details"** or **"Additional details"**. On beauty products it is often a bullet list, not a table.
2. Press **Ctrl+F** and type `Date First Available`.
3. Copy the date exactly as shown, e.g. `March 3, 2025`.

**Pilot first:** do these 5 ASINs first: B0G1VDB22X, B0FFW9SQRW, B0DP37D91R, B082WZTJV5, B0DK6W7RPS. If none of the 5 pages shows a `Date First Available` line, stop item 1, send the 5 screenshots and tell us — we will switch to another method. If at least some show it, continue with all 120.

Please separate two cases, they mean different things:
- the page has no such line after Ctrl+F → write `not shown`
- you could not check (page did not load etc.) → leave empty and say why in `notes`

ASINs:
- the **72 ASINs from AMAZON_TASK.md, Part B** (color_foundation, body_oil, scent_diffuser, tallow_balm, persimmon_soap, shower_filter)
- plus **48 new ASINs** below (for these also fill `brand_line` and `brand_table` as in Part B):
  - **lash_serum:** B082WZTJV5, B0C8SQN7S6, B00325D0WK, B0FBT2D135, B0DZDBBNFT, B09SQPL2VS, B097R35Y3Q, B01ICGFKDU, B0DRDLJSVV, B07NDN3R9P, B0F1YB3MK5, B0HBZXGY4W
  - **hair_serum:** B0DK6W7RPS, B0CFYS7M4L, B0C6XJMSGP, B0GYYKQL9Z, B0DC6W8HL2, B000V8MTIC, B0GD1KRPT3, B0DK22L979, B0BSJ42G9M, B0DJS3X3C4, B09PLNNSYV, B0D2RSCZBD
  - **prewash_oil:** B07N7PK9QK, B01M5KZTAQ, B0048EZNR4, B0BCGZLKKM, B001AO0WCG, B0GHSXYY3Z, B07YFD3T2T, B09JKRHB15, B003JKFEL8, B0083H8ASG, B0DZDV2FLB, B0C2PPB5YZ
  - **whitening_powder:** B0CQPPDQM9, B0HJ1J16FC, B01M0DYTZ9, B0FH5LGLB2, B0763F6DD8, B0GSYYWQ7S, B0HH2T555J, B0H9RC61TQ, B07QHCP6LP, B07Y2BK5F5, B09HH8T8XD, B0HD7DYGRJ

**Screenshot for every ASIN (required).** After step 3, take one screenshot of the visible area that shows the highlighted `Date First Available` line together with the product title or ASIN on the same screen (if they don't fit on one screen, the date line plus the `ASIN` line from the same details section is enough). Save it as `<ASIN>.png`, e.g. `B0G1VDB22X.png`, into a folder `screens_dates/`. If the date is `not shown`, screenshot the details section where it is missing, same file name. These screenshots let us check each date by eye later, so do not skip them.

Output: **`amazon_dates_us.csv`**, 120 rows, columns:
`category_id, asin, brand_line, brand_table, date_first_available, collected_at, notes`
(for the first 72 ASINs `brand_line` / `brand_table` can be copied from your first file or left empty)

## 2. Re-collect page 1 of "pre wash hair oil"

Page 1 had only 37 cards (the note says it may have loaded partially; other pages had 48). Please search `pre wash hair oil` again, wait until the page has fully loaded (scroll to the bottom once), and record page 1 again in the same format as Part A.

Output: **`amazon_search_us_prewash_p1.csv`** (same columns as `amazon_search_us.csv`).

Screenshots: `prewash_p1_top.png` (top of the results with "Deliver to New York 10001" visible) and `prewash_p1_bottom.png` (bottom of page 1 with the pagination bar visible).

## 3. Time stamps

288 rows in `amazon_search_us.csv` have an empty `collected_at`. No need to re-collect them — just tell us the approximate time window in which those pages were collected (e.g. "2026-11-08, 19:30–19:55"), in your short note.

## Deliverables
1. `amazon_dates_us.csv` (120 rows)
2. `screens_dates/` — 120 screenshots named `<ASIN>.png`
3. `amazon_search_us_prewash_p1.csv` + `prewash_p1_top.png`, `prewash_p1_bottom.png`
4. `deliver_to.png` — one screenshot at the start showing "Deliver to New York 10001"
5. Short note: the time window for item 3, and anything that blocked you or looked wrong

Priority if time is short: item 1 in this order — lash_serum, hair_serum, color_foundation, body_oil, scent_diffuser, tallow_balm, persimmon_soap, prewash_oil, shower_filter, whitening_powder; then item 2.
