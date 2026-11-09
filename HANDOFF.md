# Product Intel — handoff

Started 2026-11-06 in the 1000 Islands session, moved here. Team: owner + 1 employee + a little money + AI tools.

## Goal

Launch physical products on the US market, using competitor ad and sales data to choose products and creatives.

## Decisions so far

- **Do NOT build an ad-spy SaaS.** The market is saturated: dozens of tools at $19–69/mo, many launched in 2025–26, competing mainly through SEO comparison content. Barrier to entry is low; moat is distribution.
- **Chosen direction: own launch + ad archive.** Use the intel ourselves; start archiving US ads now (non-EU ads disappear from Meta Ad Library once stopped, so history cannot be bought later).
- Maybe later: "intel + AI-made creatives" done-for-you service, once our own launch proves the pipeline. Price hypothesis $500–1,500/mo per client is unvalidated.
- Side options noted: publish our scrapers as Apify Actors (Apify keeps 20%); Russian-language niche for RU-speaking US sellers (unverified); Indonesia sourcing angle (tariffs/logistics unverified).

## Key facts (see research/APIS.md for prices and sources)

- No tool shows real spend/targeting/conversions of a US commercial ad. Signals: days live, number of variants, engagement; TikTok Creative Center gives CTR percentile + budget tier.
- Meta official Ad Library API returns commercial ads only if delivered to EU/UK. For US: scrape the public web library ($0.50–0.70 per 1k ads on Apify).
- The real "what sells" signal is marketplace sales data: Keepa (Amazon BSR history), FastMoss/Kalodata/EchoTik (TikTok Shop GMV estimates).
- Logged-off scraping of public Meta data: Meta v. Bright Data (N.D. Cal., Jan 2024) ruled Meta's ToS do not bar it. Logged-in scraping not covered.

## Plan

0. **Frame (owner decides):** channel (Amazon FBA / TikTok Shop / Shopify + Meta ads), budget for first batch and ad test, product filters (~$25–80, light, not fragile, avoid regulated: food, supplements, cosmetics, kids, electronics).
1. **Archive (day 1, runs forever):** weekly pull of Meta Ad Library US (category keywords + competitor pages) and TikTok Creative Center US Top Ads (all industries). SQLite keyed by ad ID with first_seen/last_seen; download media only for ads live >14 days. Cron via GitHub Actions or Apify schedules. ~$10–20/mo.
2. **Product discovery (weeks 1–3):** growth signals from TikTok Shop (EchoTik free / FastMoss 7-day trial), Amazon Best Sellers / Movers & Shakers, Google Trends → shortlist 10–20 → Keepa Pro (€29/mo) BSR check → competitor reviews: look for ~3.8–4.2 rating with fixable complaints → winners' ads from the archive.
3. **Demand test before buying stock (weeks 3–5):** 10–20 AI creatives modelled on long-running competitor ads, landing page with pre-order/waitlist, Meta test $200–500; pass threshold computed from margin in advance.
4. **Sourcing:** Alibaba or Indonesia (check US tariffs + logistics first).

## METHOD (2026-11-07, latest): `EVALUATION_METHOD.md` + `evaluation-method.html` define how products are judged (demand summed across channels, proof, life-cycle stage, fit gate). Re-read CONCLUSIONS and BLIND_PASS through it.


## START HERE — v2.1 (2026-11-08, latest)
- Verdict: `work/dossier/FINAL_V21.md` (supersedes work/blind/FINAL_V2.md). Top 5 unchanged: color foundation, body oil, waterless diffuser, tallow balm, persimmon soap; challengers (compliance): lash serum, hair serum; reserve: shower filter.
- Board texts ready (no HTML yet): `work/dossier/content/00_index.md`, `01..20_*.md`, `99_methods.md`; chart data `work/dossier/chart_data.json`; numbers checked by `check_numbers.py`.
- Pending: Trends pulls 2-3 (2026-11-09, 11-10), Meta 30-day ad re-check (`meta_recheck.py`, on/after 2026-12-08), review curves (owner), Amazon dates (not available without login).
- Amazon: no automated access by Claude (owner decision recorded in RUNBOOK); new Amazon data via written tasks (`work/blind/AMAZON_TASK*.md`).

## (superseded 2026-11-08 by v2.1) START HERE — GRAVEYARD v2 (2026-11-07, latest)
Method frozen as v2.0: /RUNBOOK.md. VERDICT (Amazon + Meta + Google Trends): work/blind/FINAL_V2.md — #1 color-changing foundation; then body oil, waterless diffuser, tallow balm, persimmon soap; rosemary oil and turmeric soap dropped (falling trend). Amazon x Meta overlay: work/blind/OVERLAY_V2.md. Traffic (Similarweb) needs the owner's login.
Openness now measured one way for 17 categories: work/blind/GRAVEYARD.md, section 'v2 across 17 categories'. Leader by proven openness: beef tallow balm (11 indie brands reached 1K+/mo in 2 years). Biggest pie: color-changing foundation (young, fad risk). Earlier openness lists (reviews<500 proxy, v1 pilot) are superseded.

## NEXT: `NEXT_TASK.md` (owner's instructions after compaction: re-check "small traffic" brands, compliance group instead of exclusions, seasonal group, strongest ideas by LTV/margin).

## BLIND PASS (2026-11-07, later): `work/blind/BLIND_PASS.md` re-ranks all 94 non-ingestible products + 30 supplements by category sales signals (Amazon bought/mo, TikTok sold, Meta 180+). After the devil's-advocate fix (bad TikTok page), tier A = 14 products incl. socks, turmeric and persimmon soap; leak-proof boxers out. Supersedes the "take" list in CONCLUSIONS.md until the owner decides.

## (superseded 2026-11-08 by GRAVEYARD v2 / FINAL_V2.md above) `CONCLUSIONS.md` → section "Shortlist v3": favourites socks, turmeric soap (+ persimmon SKU 2), magnesium spray, scent diffuser, tallow balm; supplements shilajit, pumpkin seed oil, moringa. Boxers and duffel are out. Dashboard `product-intel-dashboard.html` shows v3. The older take list in CONCLUSIONS and the log below are history.

## 2026-11-06: product shortlist from Daily Ecommerce channel

- Corpus: 138 long 2026 videos of youtube.com/@daily-ecommerce, briefs in `C:\Users\Kirill\Documents\Codex-Research\Daily-Ecommerce-2026` (made by Codex). Codex's own top-3 (microscope, pillow speaker, ski sleeve) is an outside opinion, not the owner's.
- Our scoring: `work/score.py` -> `work/top20_products.md`, `work/scores.csv`. 7 weighted criteria (US demand 20, competition 15, regulation 20, ops 10, economics 15, AI-creative 15, timing 5); scores are judgment.
- Deep dive of the top 8 done (`work/deep_dive_top8.md`): full transcripts read (local copies in `work/transcripts/`, same text as NotebookLM) + live US Meta Ad Library check (public, logged-off, works in the in-app browser).
- Current shortlist (after AD pass 1): men's leak-proof boxers (menvault.com), gel ski shin sleeve (conditional on stock by ~10 Dec), moissanite tennis bracelet (aim at Valentine's). Reserve: compression tank. Dropped: persimmon soap.
- Do not copy competitors' fake persona pages / fake scarcity (FTC 16 CFR 465 risk).
- NotebookLM MCP here is not authenticated (Codex used another client); local transcripts are enough unless audio overviews are wanted.
- Public-data market check done (`work/market_check.md`: Google Trends API, NSAA, reviews, FDA, tariffs, Alibaba, unit-economics model). Verdict: tennis bracelet GO to test for Valentine's (samples now); leak-proof boxers GO only via a cheaper route (own-brand import likely triggers FDA establishment fee $11,423/yr, FY2026); ski sleeve NO-GO for stock this season (optional pre-order ad test).
- Sources: YouTube videos have only auto-captions (no manual subs), so names/numbers in transcripts may be garbled. Amazon blocks AI agents; use indexed pages only.
- 2026-11-07: full public-data pass on all 22 (top-20 + persimmon & turmeric soaps): `work/full_list_analysis.md` (Trends share, Ad Library clone counts, leader prices, Alibaba costs, China duty, max CAC, pitfalls). New proposed shortlist: soap brand (turmeric glow bar for melanin-rich skin first, persimmon second), tennis bracelet (Valentine's), 16-head massager gift test; reserve men's leak-proof boxers. Soap duty from China 37.5%; soap claims must stay cosmetic (no "fades/blocks pigment").
- 2026-11-07 (later): owner asked for a serious re-check of the whole corpus. Rebuilt from all 138 videos: 31 sellable candidates, checked live US Ad Library by landing domain (persona pages of one company count once), Trends, clone pressure, feasibility, max CAC. Mechanical scoring in `work/shortlist20.py` -> `work/shortlist20.md`. Top of the list: tennis bracelet, seat cushion, compression socks (Everstride ads live since Sep 2024), 16-head massager, ski sleeve (seasonal), LED mask via cleared OEM.
- AD + error check done (`work/shortlist20_AD.md`). The longevity metric is now L6 = leader's active US ads started 6+ months ago (Ad Library `start_date[max]`). v1 kept as shortlist20_v1.*. Tier A: compression socks, lash serum (cosmetic), tennis bracelet, persimmon soap, turmeric soap.
- 2026-11-07: built `work/market_system.py` → `market_system.md`: ads by age (total / 90d+ / 180d+), traffic Jun–Sep (SimilarWeb via adlibraryspy.com/store/<domain>; Similarweb itself has an anonymous limit of ~3 sites), brand search (Trends), AOV + repeat → LTV, segments ESTABLISHED / RISING / FADING / SMALL. Result: tennis bracelet, chin wrap, seat cushion, ski sleeve, silvervine, massager have small traffic → dropped. Established: turmeric soap, compression socks, persimmon soap (Kaori), magnetic lashes (Moxie, not in corpus). Rising: Luhxe duffel, Menvault, Sofyre. The YouTuber's revenue claims run ~2–400× above a visits×CVR×AOV sanity band.
- Correction: moxielash.com sells magnetic lashes, not lash serum, so the "lash serum" row in shortlist20 v2 used the wrong leader.
- Method note: count clones by landing domain, not by page name. With the browser pane hidden, Ad Library loads only the top ~30 ads.
- Next: owner picks; then samples + supplier quotes, claims review, AI creative tests.
- Context: US de minimis is suspended for all countries since 2025-08-29 (statutory repeal 2027-07-01) — imports pay duty, prefer US-warehouse stock.

## 2026-11-07: long-running ads page + dashboard cleanup

- `long-running-ads.html`: Ad-Library-style cards of each leader's oldest active US ads (180+ days; Luhxe 60+ since it rotates fast), filters by format / brand vs creator pages, every card opens the ad in Ad Library in a new tab.
- Refresh: `python work/ads/fetch_longrunning.py` (headless Playwright, logged-off; saves previews to `dashboard/ads_media/` because fbcdn links expire in ~4 days), then `python dashboard/build.py`. Logged-off Ad Library loads only ~30 ads per query (top by impressions).
- Dashboard: product photos (Shopify `/products/<handle>.json`), 3 KPIs + "More numbers", ad preview strip, secondary blocks collapsed. View via `.claude/launch.json` → `dashboard` (python http.server :8765); file:// in the app pane shows no images.

## Waiting on the owner

- Apify account (owner registers; token goes into `.env`, never into chat).
- Stage 0 answers: channel, budget.
- Categories in mind, or search from scratch.
