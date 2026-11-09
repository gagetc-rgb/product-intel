# Review of your report (product-intelligence-38.pages.dev) — what to fix

Date: 2026-11-09. Reviewer checked the live site against `AGENT_BRIEF_MARKET_OPENNESS.md` and spot-checked facts online.

The presentation is strong and some findings are genuinely valuable (Amazon mouth-tape ban, Intake Breathing's patent enforcement, Jude's capsule pivot, the foot-file rollers losing to peeling sprays, "false newcomers" in incontinence pads). But as delivered it does not follow the brief, and several headline facts are wrong. The report is meant for an investor decision, so it must be redone, not polished.

Confidence marks: ◆ confirmed · ◈ likely · ◇ disputed.

---

## 1. Factual errors (fix first)

1. ◆ **Afina (your #1 pick's main proof) was founded in October 2024, not August 2025** (Wikipedia, DIYRated, Flip). As of Nov 2026 it is ~25 months old, past the 24-month "new brand" line. Its founder, Ramon van Meer, is a serial entrepreneur whose brands did $200M+ revenue — not a comparable newcomer for a 2-person team. Afina also says it is **#1 on Amazon**, which contradicts your claim that young brands win only via their own sites, away from the Amazon price war. Re-check every "young brand" with the business age (site / Wayback / RDAP / reviews history), not the launch date of one product or ad.
2. ◆ **Pickleball: Franklin X-40 is already a seamless, one-piece rotationally molded ball** (Pickleball Central, Pickleball Science, Pickleball Union). "Seamless" cannot be the differentiation against the leader. Rewrite card #11.
3. ◆ **Mouth tape "scheme" breaks Amazon policy instead of getting around it.** The Seller Central policy explicitly bans "products shaped like mouth tapes or otherwise visually similar", tapes listed as "athletic / skin / medical tape", and says Amazon may use outside marketing to classify. Renaming to "sleep strips" is a suspension risk. Keep the scheme, but describe it accurately: quote the policy wording and state the risk (listing removal / account suspension) next to it.
4. ◈ **Shoalvex is Intake Breathing's own enforcement platform** (their job posting), not a hired agency. The patent win is real (preliminary injunction, D.D.C., May 2026) — cite it.
5. ◆ **Channel count**: cards cite 15 channels (Satddu, Millionaire Anderson, Swirlback, Jasper Leeuw, ZIK Analytics, Alex Robinson, Sébastien Villa, Conquer AMZ, Travis Marziani, Hammersley Brothers, Davie Fogarty, Buppan NAVI, Masanobu Terada, Daisuke Sato, vSprint); the header says 12. Also "38 products" counts the 5 Polish items as one card while the text says "5 Polish positions".
6. ◆ **Arithmetic**: insoles "1 yuan/pc ($0.45–1.20)" — 1 CNY ≈ $0.14; "markup 15–20×" does not match $0.45–1.20 cost vs $25–39 price. Dryer balls: "+€5 net per box" in one place, €6.80 vs €2.64 (= +€4.16) in another. Pick one calculation and show it.

## 2. Brief violations (method)

1. **Single 0–100 "openness" score and a "hype" score.** The brief says: demand, concentration and newcomer survival are three separate answers, never blend them. Remove both scores and the chart built on them, or show the formula and the three components separately.
2. **No newcomer survival — the core of the method is missing.** Required: Amazon cohort (brands entered 12–24 mo ago) with badge distribution and A/B/C split; EU/UK Meta cohort survival rate (stores whose first ad started 6–12 mo ago, share with a 90+ day ad). "5 young brands grew" is survivorship bias — exactly the trap section 1 warns about.
3. **"Leaders spend 99–100% of budget in the US" is not measurable.** Spend of commercial ads is not public. The EU DSA library gives reach only inside the EU, so a US share cannot come from it. If a third-party tool gave the number, name the tool, the field, the date, and mark ◇. Same for "US leaders absent in Germany ⇒ empty shelf": absence of US brands ≠ empty shelf — list the German shelf leaders and their age.
4. **Summed reach shown as people** ("101.3M people reached"). Reach of separate ads overlaps; it cannot be added. Report per-ad reach or drop it.
5. **Ad counts used as proof of success** ("1,243 active ads"). Brief §5.2: count = testing intensity, age is the signal. Use Meta's "~N results" with start-date filters (total / 90+ / 180+) and aged share.
6. **No confidence marks and no sources** except video links. Every number needs ◆/◈/◇ and a source (Ad Library URL with query, ASIN + date, Trustpilot URL, tool export). Never invent; write "unknown" + reason.
7. **Country conclusions from one source.** Brief §5.10: any country-level conclusion needs two sources.
8. **Deliverables missing**: `openness.csv` (one row per product × market), cards in the §7.2 format, summary ranked by new-brand units per month, method log (every source tried, incl. failures), pre-registration file, scripts. Hand these over.
9. **No self-attack** (§8.5): for each top verdict list the strongest reason it might be wrong and check it.

## 3. Risks the report ignores (add per card)

- ◆ **Entering Germany/EU costs paperwork**: packaging registration LUCID (Amazon.de requires the number), EU responsible person under GPSR (EU General Product Safety Regulation), VAT registration, German-language listings and support. Add these to every EU recommendation.
- ◈ **Shower filter "against hair loss from hard water"**: KDF / vitamin-C shower filters barely reduce hardness; hair-loss wording is a health claim (German unfair-competition / health-advertising law). Rewrite the positioning or source the claim.
- ◈ **Fatbike brake pads**: safety-critical part (product liability, GPSR); sintered pads are not compatible with all rotors; the Dutch fatbike market faces tightening regulation — check whether demand is about to shrink.
- ◈ **Lavender oil in dryer-ball kits**: EU CLP labelling, safety data sheet, "Bio" needs organic certification. Not just "€0.30 bottle".
- ◈ **Insoles sold as "orthopaedic"** in the EU can fall under medical-device rules. Use comfort wording or flag it.
- Remove second-person notes to the owner ("as you said", "by your decision") from the investor version.

## 4. Keep and expand (good work)

- Platform-rule check per product (Amazon bans, patents, medical-device class) — make it a standard step for all 20.
- "Technology moved on" finding (rollers → peeling sprays): keep as a separate market type.
- Offer tactics (consumable in the box, fix the leader's top complaint, honest fill vs shrinkflation, measuring scoop on the main photo): move to a separate "tactics" section, not mixed into verdicts.

## 5. What to send back

1. Corrected site with sources + ◆◈◇ on every number, scores removed or decomposed.
2. `openness.csv`, cards (§7.2), summary table (§7.3), method log (§7.4), pre-registration file, scripts.
3. Re-run survival (Amazon cohorts + EU/UK Meta survival) for the current top 6 before keeping any of them in the shortlist.
4. A short changelog: what changed vs this version and why.
