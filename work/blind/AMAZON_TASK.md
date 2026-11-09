# Task: Amazon US search data for 4 categories + brand names for 72 top listings

You are collecting data from amazon.com as a normal shopper would see it in the United States. We need exact values read from the page, not estimates.

## Hard rules
1. Never guess. If a value is not shown, leave the cell empty. If something looks odd, write it in `notes`.
2. Do not log in, do not buy, do not add to cart, do not submit any forms.
3. If Amazon shows a robot check, a CAPTCHA or an "access restricted" page, stop and report it. Do not try to get around it.
4. Record the date and time you collected each part.

## Step 0. Set the delivery location to the US
1. Open https://www.amazon.com
2. Click "Deliver to" (top left), enter ZIP code **10001**, click Apply.
3. Check that the top left now says **"Deliver to New York 10001"** and that prices are in **$**.
   If it still shows another country or another currency, stop and report it.

## Part A. Search results for 4 categories

For each search query below:
1. Type the query into the Amazon search box exactly as written and press Enter. Do not change the sorting or add filters (keep "Featured").
2. Go through **result pages 1 to 5** using the "Next" button at the bottom.
3. On every page, record **every product card** in the results, **except** cards marked "Sponsored". Skip the "Related brands", "Top rated", "Editorial" and video carousels as well; take only the main grid or list of results.

| # | category_id | Search query |
|---|---|---|
| 1 | whitening_powder | `teeth whitening powder` |
| 2 | lash_serum | `eyelash growth serum` |
| 3 | hair_serum | `hair growth serum` |
| 4 | prewash_oil | `pre wash hair oil` |

For each card, record the following:

| Column | What to write | Example |
|---|---|---|
| `category_id` | from the table above | `lash_serum` |
| `page` | result page number, 1-5 | `2` |
| `position` | position on that page, counting only non-sponsored cards, from 1 | `7` |
| `asin` | the 10-character product code. It is in the product link after `/dp/`; hover the title or open the card's link to see it | `B0DP37D91R` |
| `title` | full product title as shown on the card | |
| `bought_past_month` | the text "X bought in past month" exactly as shown, e.g. `1K+`, `500+`; empty if the card doesn't show it | `2K+` |
| `price` | the main price shown (not the crossed-out one) | `$19.99` |
| `rating` | stars, e.g. `4.4`; empty if not shown | `4.4` |
| `review_count` | number of ratings shown next to the stars, e.g. `12,345` or `(1.2K)` as shown | `1,204` |
| `image_url` | the card image URL: right-click the image, then "Copy image address" | `https://m.media-amazon.com/images/I/...jpg` |
| `collected_at` | date and time | `2026-11-09 14:20` |
| `notes` | anything odd | |

Save the results as **`amazon_search_us.csv`**, one row per product card.

## Part B. Brand name for top listings in 6 categories

For each ASIN below, open `https://www.amazon.com/dp/<ASIN>` (with the delivery location still set to 10001) and record:

| Column | What to write |
|---|---|
| `category_id` | from the list below |
| `asin` | the ASIN |
| `brand_line` | the small link right under or above the title, exactly as shown, e.g. `Visit the Terra Lotus Store` or `Brand: Terra Lotus` |
| `brand_table` | the "Brand" value in the product details table, if there is one |
| `date_first_available` | the value of "Date First Available" in the product details section (scroll down), e.g. `March 3, 2025`; empty if not shown |
| `bought_past_month` | as shown on the product page, if shown |
| `price` | main price |
| `collected_at` | date and time |
| `notes` | e.g. "page not available", "different product than expected" |

ASINs (12 per category):

- **color_foundation:** B0G1VDB22X, B0G1VBDXYF, B0GN8JW57H, B0G1T61T7X, B0GZP4FL6N, B0H6S4DVKC, B0HDHZ35FT, B0G1VT7GMP, B00L2SNFPQ, B0HHFB3DGK, B0H73V4FN4, B0HGKKW25X
- **body_oil:** B0FG8K9QYK, B0FB9LWGY5, B004L17FKC, B08D43LHYP, B0CSTCYSF7, B07SWJ5PVH, B000056W74, B0FB9LRL1V, B00008BK7H, B001B0ZZFS, B0D1QYBNNQ, B001KYU1H2
- **scent_diffuser:** B0DXHGTMQL, B0GGQ6ZPT9, B0FSQYDJ91, B0F99KD5K2, B0CRTPVD1D, B0DXHSDLVD, B0DHBZ2TX9, B0GKGH1R5X, B0DP2B5WZN, B0GKSGZCMV, B0DCJPK87K, B0GCYW7VRV
- **tallow_balm:** B0FFW9SQRW, B0BJMSH4JX, B0D1NGHSZ8, B0DTQ8FGQX, B0FFPMJKVC, B0BRTQYJZL, B0DWMZR8WD, B0GS9KCQD5, B0FFWL5YVN, B0FFWY7L61, B0D2DVJVS9, B0G38DHXH5
- **persimmon_soap:** B0DP37D91R, B0D4LX75GN, B0GFMMW31V, B0GJ6N1VYS, B0FJ2S57DQ, B0GXVQ4C5Y, B0FT31T6FL, B0H3K8VN7Z, B087VQG6L5, B0DWMRPCYG, B0HDQXZWWW, B0FKGD1TWW
- **shower_filter:** B07Q4MYZNC, B0F6BPJZLW, B0CL4SVJQ3, B0H392GY5R, B0CCTNWYDH, B0FNWXG9Q7, B0BJDPJNN3, B0G6DYFPB2, B0H7WSS741, B0BNPMJDB6, B0DDCBZ8W9, B0FXZMJKRS

Save the results as **`amazon_brands_us.csv`**, one row per ASIN.

## Deliverables
1. `amazon_search_us.csv` (Part A, about 4 × 5 pages × ~48 cards)
2. `amazon_brands_us.csv` (Part B, 72 rows)
3. One screenshot showing "Deliver to New York 10001" at the start of the session
4. A short note: anything that blocked you or looked wrong

## Priority if time is short
Part A first (4 categories, all 5 pages). Then Part B in this order: color_foundation, body_oil, scent_diffuser, tallow_balm, persimmon_soap, shower_filter.
