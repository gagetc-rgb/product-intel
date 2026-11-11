# Review of the "38 repeat-purchase products" site, and the correction task

Review date: 2026-11-10. Site: https://product-intelligence-38.pages.dev/ (method v2.1).
Yardstick: our brief `AGENT_BRIEF_MARKET_OPENNESS.md` (with section 9) and `METRICS.md` (v2.2).
All 20 audit cards and the shortlist were read. The 18 dropped cards were not reviewed.

Marks as in the brief: ◆ confirmed · ◈ likely · ◇ disputed or an assumption.

## 1. Bottom line

The site shows well where **not** to enter. The red verdicts are mostly grounded.
The green verdicts are not proven. The shortlist of 6 cannot be used to decide on buying stock.

The main reason: openness is inferred from the **absence of US leaders** in a market. By the brief, a market is open when young brands (under 24 months) already hold a real share **in that market** and several reached winner volume. For 5 of the 6 favourites (Germany, the Netherlands) the site does not show this. An empty shelf can mean "too early" or "no demand", and the site does not tell them apart.

## 2. What is done well (keep)

- #15, adult diapers: "false newcomers" caught (new listings of Depend, Always Discreet and Amazon's own brand). This is the brief's rule "listing age ≠ brand age".
- #13, creatine: the market type "eats newcomers" is named from data (68.4% of units go to unbranded listings, 69,300 of 101,300).
- #16, PrintPod: the video case was checked and refuted (Trustpilot 1.4★, no ads older than 90 days).
- #19, cleaning paste: the leader's ad age was checked (0 of 219 ads older than 90 days).
- #20, foot-file rollers: a technology substitution was found (peeling sprays).
- #1, shower filter, US: the share of ads aged 90+ is given (60.7% of 4,198). That is the right metric. The US conclusion agrees with our v2.2 study, where the shower filter is also in the top five.

## 3. Method errors (by importance)

**3.1. Openness of the target market is not measured.** For Germany and the Netherlands there is no number from steps 1-3 of the brief: units per month on amazon.de, share of new brands, newcomers at winner volume, cohort survival. In their place: "the Americans do not advertise there".

**3.2. Meta survival in the EU and UK was not done.** The brief names it the top priority for these markets, because stopped ads stay visible there. The site has single stories (Peach Perfect, Wildpier), not the share of stores in a cohort that survived.

**3.3. Blended scores.** "Promise 90/100" and "Reality 88/100" are single numbers with no formula. The brief forbids blending demand, concentration and survival into one score. The "promise vs reality" chart is built on these scores, so it proves nothing.

**3.4. Numbers from videos are used as facts in the shortlist.** Brief, mistake 6: guru revenue and calculations are leads only. The shortlist itself contains: dryer-ball cost €1.01 (Jasper's calculation), insoles $0.45 (Anderson), "a seller with 2 reviews makes €3,500/mo" (Jasper). In card #16 the agent cites this very rule.

**3.5. Kill rules are not applied to every product.**
- #6, dog boots: 62.1% held by a brand from 2008. By the brief this is a "captured" market, yet the verdict is green.
- #10, mouth tape: 86.1% of units in three listings, yet the verdict is "the scheme works".

**3.6. The maximum age of one ad is presented as proof.** "Up to 556 days", "up to 508 days", "up to 740 days" is mistake 3 of the brief. What is needed: the share of ads aged 90+ and 180+ and the number of stores that have them. The ad count ("1,243 ads") is mistake 2: it shows testing intensity, not success.

**3.7. No margin.** Everywhere: "cost X, price Y, a 15-20× markup". Our metric D5: price − platform fees − goods with duty − freight − returns − storage, before ads. Under 25% of price is bad. None of the 6 favourites has this calculation. For own-store sales there is no ad cost per order.

**3.8. The fit check comes after the verdict, not before.** In our method a product that cannot be sold legally is dropped at once. The site presents ways around the rules as a finding ("golden fund"):
- #10: sell a banned product under another name. Amazon removes such listings even without the word "mouth" (see section 4). The risk is an account suspension.
- #9: change the description and the shape to get past a patent and medical-device status.
- #14: NMN as a "reagent not for human consumption" that everyone eats.
- #15: bladder capsules are a health claim. The UK ad regulator (ASA) bans such wording without an authorised claim.
- #1: "a clinical beauty gadget against hair loss, dandruff and acne" are treatment claims. In Germany competitors send legal warning letters (Abmahnung) for these.

**3.9. EU seller duties are ignored.** Germany needs: VAT, the LUCID packaging register, an EU responsible person (GPSR). Per product:
- #5: lavender oil is a hazardous mixture under CLP. It needs labelling, a child-resistant cap and a poison-centre notification. "A €0.30 bottle" does not cover this.
- #3: lash glue and remover are cosmetics. They need a responsible person, a safety report, CPNP notification.
- #2: the word "orthopaedic" makes insoles a medical device.
- #4: brake pads are a safety-critical part. Liability sits with the seller.

**3.10. Claims the data cannot support.**
- "Jolie and Afina spend 99-100% of the budget in the US", "88% of Stepprs ads go to the US, UK and Ireland", "Intake spends 95% in the US", "Hostage Tape sends 13% to amazon.co.uk". The Meta library shows no spend and no US reach. Reach exists only for the EU and UK. If a figure comes from a third-party tool (AdManage, Sprites.ai), it is an estimate ◇ and must be labelled so.
- "0% of sales in Germany", "90% of all traffic belongs to Wildpier", "62.1% of the US market": it is not stated what was counted and where.

**3.11. The hand-in files from section 7 of the brief are missing.** No `openness.csv`, no method log, no pre-registration file, no scripts. The site has 20 links, all to YouTube. The check numbers have no source, no date (a pull date is given only in #10 and #13), no ◆◈◇ mark, no "could not be measured" list, no "one fact that would change the verdict".

## 4. What we re-checked ourselves

| Claim on the site | Result | Source |
|---|---|---|
| Amazon US banned mouth tape from 2023-07-31 | ◆ True | [Seller Central forum](https://sellercentral.amazon.com/seller-forums/discussions/t/bd8c5c1c4b304420fa8d25c4ed6a216b) |
| Renaming saves the listing from the ban | ◆ False as a rule: Amazon moderators say a product is restricted if it can be used to cover the mouth, whatever it is called | [Seller Central forum](https://sellercentral.amazon.com/seller-forums/discussions/t/fef14a98-9e61-4ca6-95bc-188664705858) |
| The German shelf for beauty shower filters is "completely empty" | ◆ False: Stone Stream and MineralStream sell hard-water shower filters "for hair" in German from their own German sites; eBay.de and Kaufland.de carry dozens of offers | [Stone Stream DE](https://de.stone-stream.com/products/hartwasser-filter-universelle), [MineralStream DE](https://de.mineralstream.co/products/vitality-pro-festsitzender-duschkopf-fur-haut-und-haare) |
| PawZ on Chewy: 3.4★ on 1,400 reviews | ◈ The rating is close (3.1-3.4★ across listings), the count did not match: the largest listing has 636 ratings | [Chewy](https://www.chewy.com/pawz-waterproof-dog-boots-black/dp/56710) |
| The agency Shoalvex takes down Intake clones | ◇ No mention found anywhere. A source is needed | — |
| Lashify carries no patent risk in Europe | ◇ Not verified. The US lawsuits are confirmed; nothing found for Europe. No lawsuits does not mean no patents | [Lashify complaint, US](https://ai-lab.exparte.com/case/dct/txwd/6:22-cv-00777/doc/analysis/1) |
| Fatbikes in the Netherlands are a growing market with no risks | ◈ A risk is not mentioned: the government is bringing in a separate vehicle category, a minimum age and helmets for minors; Amsterdam banned them in parts of the city from February 2026 | [Rijksoverheid](https://www.rijksoverheid.nl/actueel/nieuws/2025/08/28/minister-tieman-neemt-maatregelen-tegen-gevaarlijke-situaties-met-fatbikes-en-andere-e-bikes), [DutchNews](https://www.dutchnews.nl/2026/04/government-to-bring-in-minimum-age-helmets-for-fatbike-users/) |

The other numbers on the site were not re-checked.

## 5. What does not add up on the site itself

- Header: "12 with a scheme". The schemes section has 6. The ★ mark is on 11 of the 20 cards.
- Summary: "5 Polish + 13 niche + 8 overheated" = 26, plus 6 favourites = 32. There are 38 products. The six yellow ones vanish without explanation.
- "58 country cuts". The "markets checked" lines in the cards add up to 63.
- #4: "7 new sellers", 5 are named.
- #2: cost "1 yuan apiece" (about $0.28 a pair) next to "$0.45-1.20 a pair". Retail is $29-39 in the card and $25-39 in the shortlist.
- #6: cost $2.87 in the video, $1.40-2.80 in the card, $1.40 in the shortlist.
- #5: HHI 1,695 is called "low". On the brief's scale 1,500-2,500 is moderate.
- #5, #20, #11: the text still addresses the owner directly ("at your request", "by your rule", "you set the task").

## 6. The task

Do not redo all 20. Do three things.

### A. Re-check the 6 favourites in their target market (the main part)

For each product + market pair run steps 0-4 of the brief and fill the card from section 7.2:

| # | Product | Market | What exactly to prove |
|---|---|---|---|
| 1 | Shower filter | Germany | Units per month on amazon.de for "Duschfilter" and synonyms. Who already sells (Stone Stream, MineralStream and others), how old they are, how many of their ads live 90+ days. Trends DE over a year |
| 2 | Insoles | Germany | Whether Germany has stores with ads aged 90+ days. Stepprs' share of bad reviews (36%): is the cause shipping or the product |
| 3 | Cluster lashes | Germany | The amazon.de shelf for "Wimpern Cluster": who, how many units, how old. Whether Lashify holds European patents (Espacenet), not "there are no lawsuits" |
| 4 | Fatbike brake pads | Netherlands | Demand in units, or at least Trends NL. bol.com shows no sales: state what you used in its place. How the new rules affect the fatbike fleet |
| 5 | Dryer balls + oil | Germany | Units per month on amazon.de. 85 reviews at the leader: a free market or small demand. CLP requirements for the bottle and what they cost |
| 6 | Dog boots | US | By the brief the market is captured (62% with an old brand). Show newcomers under 24 months at 1,000+/mo, or the verdict is "skip". The spreader tool is a hypothesis, mark it ◇ |

Required for each pair:
1. Demand: units per month (floor from Amazon badges) and search growth over a year for the country.
2. Concentration: top-3 share by brand, who they are and how old.
3. Newcomers: share of units held by new named brands, number of winners, the 12-24 month cohort with the A/B/C split.
4. Meta, EU/UK: store cohort survival (first ad 6-12 months ago; success = an ad that ran 90+ days).
5. Margin before ads by formula D5 (brief, section 9.3). Your own supplier prices, not the video's.
6. Fit: which registrations and labels are needed, which claims are not allowed.
7. Market type from the brief (captured / price war / eats newcomers / open / too early) and the verdict.
8. What could not be measured, and the one fact that would change the verdict.

No data = write "not measured" and the reason. Do not write "enter" without items 1-3: write "not proven".

### B. Fix the presentation on the site

1. Remove the "promise" and "reality" scores and the chart built on them. Show three separate answers: demand, concentration, newcomers.
2. Every check number gets a source (a link or the name of the pull), a date and a ◆◈◇ mark.
3. Numbers from videos appear only in the "what was claimed" block and nowhere else.
4. Remove the "golden fund of schemes" section. Describe ways around platform rules and laws as a risk inside the card, not as a recommendation. #10 and #9: the US verdict is "closed".
5. Remove the claims from 3.10 or replace them with what was really measured ("no ads in the EU library").
6. Fix the mismatches from section 5. Remove the direct address to the owner and the hype wording.
7. Explain where the 6 yellow products went and how 38 is made up.

### C. Hand in the files

`openness.csv` (one row per product × market), the method log with every source and every failure, the pre-registration file, the scripts. Link to them from the site. All working files in English; only the site is in Russian.

## 7. How we will check the result

- We take 10 random numbers from the site. Each has a source and a date, and the number can be found at the source.
- Every green verdict has items 1-3 of task A measured for the target market.
- The site has no single score and no advice to get around platform rules.
- The count adds up: 38 = the sum of the groups.
- The CSV, the log and the pre-registration file are attached.

If any of the first three fails, the work is not accepted.
