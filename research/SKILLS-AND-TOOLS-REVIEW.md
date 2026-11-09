# Skills & tools review: e-commerce product intel (checked 2026-11-07)

Legend: ◆ verified (opened repo/file) · ◈ likely · ◇ disputed / opinion

## 1. GitHub skills — verdicts

| Repo | Stars / last push | What it is | Verdict |
|---|---|---|---|
| apify/agent-skills → `apify-ultimate-scraper` | 2.5k / 2026-10-30 ◆ | Drives ~100 Apify Actors via CLI; workflow refs for competitive-intel, ads, reviews, trends, e-com price monitoring | **USE.** Fits our plan (Apify already chosen). Real data, not prose. |
| anthropics/knowledge-work-plugins (`marketing/competitive-brief`, `product-management/competitive-brief`, `synthesize-research`) | 35k / 2026-11-06 ◆ | Official structured templates for competitor briefs / research synthesis (331 lines) | **USE as output format**, feed it data from Apify. |
| coreyhaines31/marketingskills | 59k / 2026-11-04 ◆ | CRO, copy, launch, pricing, analytics. Some already installed locally (launch-strategy, email-sequence, lead-magnets) | Useful for post-research (landing, offer, launch). Not intel. |
| liangdabiao/amazon-sorftime-research-MCP-skill | 1.1k / 2026-10-28 ◆ | Amazon listing teardown, category, keyword, negative-review analysis; backed by Sorftime / SellerSprite / SIF MCPs | Methodology is good; **requires paid Chinese data MCPs**, docs in Chinese. Borrow the review-analysis / category-selection logic. |
| cosjef/keepa_MCP | 55 / 2026-02 ◆ | MCP for Keepa (Amazon price + BSR history) | Worth it if Amazon is a channel (Keepa ≈ €19/mo ◈). Low activity — test before relying. |
| Google Trends MCPs (andrewlwn77, trendsmcp-ai, HasData) | 5–34 ◆ | Interest over time / related queries | Optional; Apify skill already covers Google Trends. |
| buluslan/ecommerce-competitor-analyzer | 62 ◆ | Node scripts + Google Sheets + n8n | Small, single author; skip. |
| **nexscope-ai/eCommerce-Skills** | 1.3k ◆ | ~157 skills (Amazon/Shopify/TikTok/Etsy…) | **FLUFF.** Opened `dropshipping-product-research`: 63 lines, generic steps, "frameworks below" that don't exist, no data source, links to Nexscope (lead-gen for their SaaS). |
| alirezarezvani/claude-skills (410 skills), kostja94/marketing-skills (160+) | 29k / 1k ◆ | Mega-collections | Mostly prompt templates; skim for specific ones, don't install wholesale. |
| `r02-…-claude-skills-ecommerce`, `r08-…`, `r17-…` (random accounts) | ~50 each ◆ | Auto-generated "derived from" repos with near-identical star counts | **Suspicious / spam pattern** — do not install. |
| Meta Ad Library MCPs on `/ads_archive` | 0–1 ◆ | Official API wrappers | **Useless for US commercial ads**: API returns commercial ads only for EU/UK delivery (see APIS.md). |

Rule of thumb: a skill is worth installing only if it **pulls real data** (API/scraper/CLI) or encodes a **specific, tested procedure**. A SKILL.md that only says "analyse competitors and give actionable recommendations" adds nothing over a plain prompt.

## 2. Practitioners: what actually works vs hype

**Works (consensus across r/AmazonFBA, r/dropshipping, r/TikTokshop, agency blogs):**
- ◈ Meta Ad Library ad longevity + "N ads use this creative" (scaling) as a free spend proxy. Caveat repeated by pros: longevity = hypothesis, not proof of profit ◆ (gmsmediagroup, 2026-03).
- ◈ Stacking signals: early Meta scaling → TikTok Creative Center organic angles → Amazon reviews for a real recurring pain point (r/dropshipping, 2026-03).
- ◈ Capture daily: commercial ads disappear from the library when paused (only political ads are archived) ◆ (adplay.ai, 2026-10). → our own archive is the right call.
- ◈ Review mining (pain points, objections, customer language for copy) — the most cited real win of Claude-style skills.
- ◈ Claude Code as runtime (reads real exports, runs scripts, writes files) rather than chat "frameworks"; browser-driven competitor funnel/CRO audits.
- ◈ For Amazon: Helium 10 / Jungle Scout are useful as filters; Keepa / SellerSprite / DataDive cited as cheaper alternatives.

**Hype / overrated:**
- ◇ "Winning product" lists from trend/spy tools — called 2–3 weeks late; one user reports burning ~$1.2k on already-dead products (anecdote).
- ◇ "Tool = winning product": everyone sees the same data → same launches → price war; edge is positioning, product improvement, branding (r/AmazonFBA hot take, 2026-04).
- ◆ Sales-estimate accuracy claims are vendor marketing: Jungle Scout says it's 84% accurate, Helium 10 says it's 89% vs JS 60%, each from its own study; JS's 2019 study is outdated. BSR-based estimators share the same blind spot ◈. Treat as ±order-of-magnitude, not numbers.
- ◇ All-in-one "replace your stack" AI SaaS (Kaldon, EcomTools Pro bundles, etc.) — mostly self-promotional posts.
- ◆ Big prompt-only skill packs (Nexscope) — see above.
- Note: many "honest" Reddit comments contain affiliate links/coupon codes; discount them.

## 3. Recommendation for this project
1. Install `apify/agent-skills` (ultimate-scraper) once the Apify account exists.
2. Copy Anthropic `competitive-brief` + `synthesize-research` as the report template.
3. Build our own small skills (not install packs): `ad-longevity-tracker` (daily Meta library snapshot → longevity/scaling table), `review-miner` (Amazon/TikTok reviews → pains/objections/phrases), `product-scorecard` (signals stack → go/no-go).
4. Paid data only if Amazon is a channel: Keepa first (cheap), H10/JS only for validation.

Sources: GitHub API (repo stats, file contents), reddit.com/r/AmazonFBA, r/dropshipping, r/TikTokshop, gmsmediagroup.com, adplay.ai, klipio.io, helium10.com, junglescout.com, revenuegeeks.com, zentric.digital, dev.to.
