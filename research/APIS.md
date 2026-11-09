# Competitor ad & traffic intel: APIs and prices

General reference (not only for tours). Section "US physical products" at the end covers the US e-commerce case.

Checked 2026-11-06. Prices are per 1,000 **results** (ads, posts, reviews) unless marked "per 1k requests". Marketplace prices change often; re-check before buying.

## Key limits (read first)

- No platform publishes competitors' conversions or spend for commercial ads. Proxies: ad run length, number of duplicates/variants, EU reach (Meta/TikTok, DSA), TikTok Creative Center CTR percentile + budget tier.
- Meta official API returns commercial ads **only if delivered to EU/UK** (past year). Elsewhere: political ads only. Source: https://www.facebook.com/ads/library/api
- TikTok official Commercial Content API: EU/EEA+UK/CH/TR data only, access for non-commercial researchers only.
- Google Ads Transparency Center: no official API. Free BigQuery public dataset covers EEA/Turkey ads (impression ranges, run dates, no creatives).

## Meta (Facebook + Instagram ads)

| Route | Price | Notes |
|---|---|---|
| Official Ad Library API (`ads_archive`) | Free | ID verification at facebook.com/ID (days), dev app, 60-day tokens. EU/UK commercial ads with `eu_total_reach`, targeting, age/gender breakdown |
| Apify `data_xplorer/facebook-ads-library` | $0.50 | flat, no start fee |
| Apify `aurelix/facebook-ad-library-scraper` | $0.70 free plan / $0.60 paid | + $0.20 per 1k for EU transparency data |
| Apify `automly/facebook-ad-library-scraper` | $0.70 → $0.55 | + $0.05/run |
| Apify official `apify/facebook-ads-scraper` | $5.80 → $3.40 | expensive |
| SearchAPI.io `meta_ad_library` | $40/mo = 10k requests; ~25 ads/request | per request, not per ad |
| ScrapeCreators | $47 = 25k credits ($1.88/1k req); $497 = 500k ($0.99/1k) | one key for Meta, TikTok, Google, LinkedIn, IG, YT; credits never expire |
| Metapi | free 3k records; $29/mo 25k | Meta only |

## TikTok

| Route | Price | Notes |
|---|---|---|
| Creative Center Top Ads (web) | Free | the only public source with performance-ish data: CTR percentile, budget tier, likes, 2s/6s view rate; Travel industry filter; ~20 ads per board, hundreds per country |
| Apify `azzouzana/tiktok-creative-center-top-ads-scraper` | $0.50 (+$0.50 details) | up to 3k ads/run |
| Apify `memo23/tiktok-creative-center-scraper` | $0.90 | |
| Apify `parsebird/tiktok-ads-scraper` | $1.79 → $1.19 | |
| TikTok Ads Library (library.tiktok.com) via ScrapeCreators | 1 credit/page | EU ads, reach, targeting |

## Google (Search, YouTube, Display)

| Route | Price | Notes |
|---|---|---|
| Ads Transparency Center (web) | Free | no metrics outside EEA |
| BigQuery public dataset | Free within 1 TB/mo queries | EEA/Turkey: impression ranges, dates, formats; link to ad, no creative |
| Apify Transparency Center actor | ~$0.90 | |
| SearchAPI.io / SerpApi | from $40/mo | separate calls for list and details |
| ScrapeCreators | 1 credit list, 25 credits with details | |
| DataForSEO Ads advertisers | from $0.002/call | |

## Instagram organic (posts, reels, engagement)

| Route | Price |
|---|---|
| Apify `sones/instagram-posts-scraper-lowcost` | $0.30 + $0.005/run |
| Apify `apidojo/instagram-scraper` | ~$0.50 |
| Apify official `apify/instagram-scraper` | $2.70 → $1.50 |

## Traffic / SEO (Similarweb, Semrush and cheaper)

| Route | Price | Notes |
|---|---|---|
| Similarweb API | No public price; sales only, no API trial. Third-party estimates $10k–60k/yr (unverified) | free web UI gives rough monthly visits, channels |
| Semrush API | Needs top plans (reported ~$549/mo Advanced, unverified) + API units; free plan 10 reports/day, no API | |
| DataForSEO Labs | pay-as-you-go, $50 minimum top-up, never expires; basic endpoints ~$0.01/task + $0.0001/item | Semrush-like data: competitors, ranked keywords, traffic estimate |
| AIsa reseller (Similarweb + Semrush per call) | Similarweb visits ~$0.075 per domain-month; channel mix ~$0.525 | single GitHub source, verify |

## Reviews (instead of Amazon: tours are reviewed on Tripadvisor, Google Maps, GetYourGuide, Viator, Klook)

| Route | Price |
|---|---|
| Apify `compass/google-maps-reviews-scraper` | from $0.30 |
| Apify `santhej/tripadvisor-scraper-pro` | $0.30 + $0.005/run |
| Google Places API (official) | ~$17 per 1k, 5 reviews/request |

## Proposed pipeline

1. Competitor list (20–50): Bali/Indonesia tour operators, upper-middle segment. Seed from Google SERP + Meta Ad Library keyword search + TikTok Travel top ads.
2. Weekly pull: Meta ads (scraper for all countries + official API for EU reach), Google ads, TikTok library; TikTok Creative Center Travel top ads monthly.
3. Store snapshots (SQLite/Sheets), key by ad ID; never overwrite, so run length is measured.
4. Score each creative: days live, duplicates/variants, EU reach, TikTok CTR tier/budget.
5. LLM tags each top creative: hook, format (UGC/drone/talking head), offer, CTA, landing page.
6. Join with site traffic (DataForSEO / Similarweb free UI) and reviews (what clients praise/complain about).
7. Output: monthly "winning creatives" report with previews.

Rough running cost for 30 competitors, weekly: ~$15–30/mo + $50 one-time DataForSEO top-up. Apify gives $5 free credit/mo.

## US physical products (e-commerce case)

For US-only advertisers the Meta official API returns nothing (EU/UK only), and no tool shows real spend/targeting of a US ad. Ad data = creatives + days live + variants + engagement. **Sales data is the real "what converts" signal** and it exists for marketplaces:

| Source | What it gives | Price |
|---|---|---|
| Keepa API (Amazon) | BSR, price, review-count history per ASIN; 1 token per ASIN | €49/mo = 20 tokens/min (~893k tokens/mo); Keepa Pro €29/mo includes 1 token/min |
| Jungle Scout | Amazon sales estimates, keyword volume | $49–149/mo; API only on Cobalt (custom) |
| Helium 10 | same + reverse-ASIN keywords | Platinum $129/mo ($99 yearly), Diamond $359 ($279 yearly); MCP on Diamond |
| FastMoss (TikTok Shop) | estimated GMV, units sold, top products/creators/videos; API + MCP | $49/mo (first month $29); API ~$0.01/call |
| Kalodata (TikTok Shop) | same | ~$50–60/mo Starter; API ~0.1 credit/call (~$0.01) |
| EchoTik (TikTok Shop) | same, 30-day history on entry | $13.9/mo or free plan |
| Apify Amazon Product Scraper (junglee) | listings, price, rating, BSR | $5 free / $4 Starter per 1k |
| Apify Amazon Reviews | review text | $0.70–5 per 1k depending on actor |

Ad spy tools (US ads, with engagement):

| Tool | Platforms | Price | API |
|---|---|---|---|
| PiPiAds | TikTok, Facebook; days-running sort, likes/comments/shares, cost estimate | $49–900/mo (credits) | higher tiers, contact sales |
| Minea | Meta (+ influencer placements), Shopify stores | $49–199/mo | no |
| Foreplay | Meta, TikTok, LinkedIn, YT Shorts; swipe files | $59–459/mo | MCP/API from $175 |
| AdSpy | FB/IG, 210M+ ads, comment search | $149/mo | no |
| BigSpy | many networks | ~$69/mo | enterprise |

US pipeline: (1) product discovery from sales data (FastMoss/Kalodata, Keepa/Jungle Scout BSR trends); (2) for winning products, pull their ads (Meta library scraper, TikTok Creative Center US top ads, PiPiAds); (3) score creatives by days live + variants + engagement; (4) mine 1–3 star reviews for pain points to fix and 5-star for angles; (5) Shopify store traffic via DataForSEO / Similarweb free UI.
