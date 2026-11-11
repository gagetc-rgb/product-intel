# M8 low-star reviews at the leaders, Lens M (collected 2026-11-10)

Marks: ◆ read directly from the review platform (counts, stars, text). ◈ my reading (theme sorting by keyword rules in `m8_themes.py`, then by eye on samples).

## Trustpilot: blocked for all 14 leaders
`https://www.trustpilot.com/review/<domain>` returned HTTP 403 with an empty body for every one of the 14 domains. I retried one domain once (try-kaori.com), got 403 again, and did not retry the others or try to get around it. So TrustScore is "blocked" for all. ◆
Next source used: the store's own review widget. Which one each store uses was read from the store's page source (Loox, Judge.me, Yotpo, Stamped, Junip). Scripts: `m8_loox.py`, `m8_judgeme2.py`, `m8_yotpo.py`, `m8_themes.py`. Raw: `raw_rev/`.

## Table

"Total" = reviews on the source named. 1-2★ share = (1★ + 2★) / total. Themes are counts of 1-3★ reviews that mention the theme (one review can count in several themes, and about a quarter of the texts matched none), out of the number of 1-3★ reviews read (all of them were read). The source row says what the reviews cover: a whole store, or only one product.

| Leader | Source and coverage | Total reviews (◆) | 1★ / 2★ / 3★ (◆) | 1-2★ share (◆) | Themes among 1-3★ reviews (◈): product / shipping / billing / support+refunds / does not work | fixable_by_follower (◈) |
|---|---|---|---|---|---|---|
| everstridesocks.com | Loox, whole store | 29,544 | 76 / 42 / 80 | 118 / 29,544 = 0.4% | of 197 with text: product 146 (fit, too tight or too small: 125), shipping 7, billing 2, support+refunds 45 (refund or return friction 27), does not work 20 | partly (fit and sizing need a different supplier spec); yes (US returns: several say a refund needs shipping back to China) |
| earthlyderm.com | Loox, whole store | 7,731 | 64 / 10 / 38 | 74 / 7,731 = 1.0% | of 112: product 28, shipping 10, billing 9, support+refunds 12, does not work 19; 54 matched no theme | yes (shipping, billing, support); no (the 19 "does not work") |
| goda.co | Loox, whole store | 23,966 | 4 / 22 / 338 | 26 / 23,966 = 0.1% | of 364: product 297 (scent fades or too weak: 291), shipping 23, billing 5, support+refunds 28, does not work 77 (claims not met: 47) | partly (scent longevity is formula); no (claims). Note below on templated text |
| smooche.com | Loox, whole store (all products) | 60,121 | 26 / 5 / 6 | 31 / 60,121 = 0.05% | of 37: product 7, shipping 4, billing 3, support+refunds 12 (refund friction 11), does not work 7; 15 matched none | yes (support and refunds) |
| miraiclinical.com | Yotpo, persimmon soap product page only (product id 4558891516036) | 2,137 | 49 / 26 / 67 | 75 / 2,137 = 3.5% | of 142: product 55 (scent: 39), shipping 8, billing 1, support+refunds 11, does not work 25; 60 matched none | partly (scent); no (no effect: 25) |
| terralotus.shop | Judge.me, store-level reviews (product_id 0) | 389 | 91 / 21 / 42 | 112 / 389 = 28.8% | of 154: product 55, shipping 33, billing and subscription 35, support+refunds 45, does not work 22 | **yes**: billing, delivery and support are about as many as the product items |
| terralotus.shop | Judge.me, one product (citrus-scented honey tallow balm, id 7695352398021) | 1,874 | 58 / 35 / 80 | 93 / 1,874 = 5.0% | of 173: product 68 (texture 34, scent 30), shipping 23, billing 10, support+refunds 32, does not work 15; 65 matched none | partly (texture and scent); yes (delivery, support) |
| ancestralcosmetics.com | Judge.me, one product (original tallow and honey balm, id 8046171816201) | 5,109 | 24 / 11 / 102 | 35 / 5,109 = 0.7% | of 137: product 57 (scent 36, texture 30), shipping 6, billing 0, support+refunds 6, does not work 11; 67 matched none | partly (scent, texture); small |
| luxe.com | Judge.me, one product (eyelash growth serum, id 7732108198146) | 64 | 0 / 0 / 0 (all 64 are 5★) | 0 / 64 = 0% | no low-star reviews to read | not readable |
| scentifyhome.com | Judge.me, store-level reviews only; the product id I used returned 0 | 341 (store-level) | 0 / 0 / 0 (34 are 4★, 307 are 5★) | 0 / 341 = 0% | no low-star reviews to read | not readable |
| primeprometics.com | Stamped public widget | 52,814 shop total reported | blocked: filters for 1-4★ return 0 reviews; the 5★ filter returns 50,001 | unknown | not readable | not readable |
| borboleta.com | Judge.me (0 reviews for the store and for the bundle product) and Yotpo (404 with the key found in the page) | unknown | unknown | unknown | not readable | not readable |
| sproos.co | Junip (page source only) | unknown | unknown | unknown | not read; no public endpoint found | not readable |
| try-kaori.com | no review app found in page source (Loox lookup returned nothing) | unknown | unknown | unknown | not readable | not readable |
| tryskult.com | Ali Reviews / Yotpo / Stamped scripts in page source; none fetched | unknown | unknown | unknown | not readable | not readable |

## Notes per leader
- **Everstride**: the 1-2★ share is tiny (0.4%), but 1-3★ complaints are dominated by fit: socks too tight at the calf or ankle, too long, or rolling down (125 of 197 mention a fit word; 8 say they roll down). Returns: about 27 mention refund, return or exchange friction; two say they were asked to return to China. Also a few reports of non-delivery. ◆◈
- **Earthly Derm**: complaints are spread thin: no effect, scent, delivery, subscription billing, each 7-19 of 112. ◈
- **Goda**: this is a perfume body oil ("Goda For Her", body butter, body wash), not a crepey-skin oil. 338 of 364 low reviews are 3★ and most say the scent fades. A large share of the 2-3★ texts reuse the same sentence frames with only the scent name swapped (for example "Not bad after a shower... scent is there, although I expected stronger projection"), so I cannot tell if these are all organic. ◆◈
- **Smooche**: only 37 reviews of 1-3★ among 60,121; the clearest theme is refunds (11). ◈
- **Mirai Clinical**: the soap product page alone has 3.5% 1-2★; main themes scent (39) and "no effect" (25), the claim itself. ◈
- **Terra Lotus**: the store-level Judge.me reviews are very different from the product reviews: 28.8% are 1-2★ and many describe unwanted recurring charges ("keep charging my account" kind of text), missing or late orders and slow refunds, e.g. "Does not do what it says" (6 words). Product-level 1-2★ is 5.0%. The store-level set is 389 of the 4,765 reviews Judge.me counts for the store, so the share is not a whole-store figure. ◆◈
- **Ancestral Cosmetics**: complaints are scent and texture (hard balm); delivery and support are rare. The store-level Judge.me set has only 86 reviews (82 five-star, 4 four-star). ◆
- **Luxe**: its page shows quoted Trustpilot reviews, but Trustpilot is blocked; the Judge.me product I read has 64 reviews, all 5★. ◆

## What was blocked or not read, and why
- Trustpilot: HTTP 403 for all 14 domains (one retry on one domain, also 403). ◆
- Stamped (PrimePrometics): rating filters return nothing below 5★; I did not try other parameter names beyond four guesses. ◈
- Yotpo (Borboleta): HTTP 404 for the key in the page; Judge.me returned 0 reviews for Borboleta's store and for its bundle product. I did not look up other products.
- Junip (Sproos): no store key found in plain text, no request made.
- try-kaori.com: no review widget identified in page source.
- tryskult.com: widget scripts found, no fetch made.
- Scentify: product id mismatch (0 reviews); only store-level reviews were read.
- Theme sorting is by keyword, so counts are approximate (±10%); 20-45% of reviews matched no theme (short texts such as "not for me").
- Shop-wide Loox counts include all products (Everstride includes wash bags; Smooche includes lip and lash products).
