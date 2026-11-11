# Steam cleaner and CarPlay adapter: v2.2 metrics we could collect (2026-11-10)

Separate study, not on the site. Method: `METRICS.md` v2.2. Amazon metrics (B1-B3, D1-D3) are not here: Claude has no automated Amazon access (owner decision 2026-11-08); they are asked of ChatGPT in `work/prompts/GPT_WORK_ONE_TIME.md`.
Tiers: ◆ counted by a platform · ◈ our estimate or reading · ◇ disputed.

## Summary

| Metric | Handheld steam cleaner | Wireless CarPlay adapter | Top 5 of v2.2, for scale |
|---|---|---|---|
| A1 search growth (YoY of last 12 weeks ÷ controls; 1 pull) | ◆ 0.77-0.85 (all 4 phrasings) | ◆ 0.73-0.86 (3 phrasings) | 0.78 (tallow) … 4.52 (foundation) |
| A2 Amazon, top-20 badges (2026-11-07) | ◆ ~31K/mo on-target; BISSELL/Shark carpet and mop listings excluded | ◆ ~42K/mo; mostly unbranded $28-30 listings, Ottocast the only brand | not comparable: top 5 use pages 1-5 |
| TikTok Shop leader (lifetime sold) | ◆ Phueut 371K | ◆ 16K | |
| B4 Meta shops with ads alive 90+ days (exact phrase) | ◆ 64 of 160 active ads are 90+ days old, but in the sample nearly all belong to one store (Magoloft / m.moonycozy.com, 51 of 54 aged ads); DTC newcomers (EcoSteam Pro, EcoPure, Sakerplus) run ads under 30 days | ◆ 5 of 180 active ads are 90+ days old; 0-2 shops (homniva, ottocast.store, drivefix) | |
| B6 young winners | ◈ none: leader Phueut sells since 2021 (first store product 2021-07-31) | ◈ none: Ottocast is an established brand (store products since 2023, a wide line) | |
| C1 leader store reviews | ◈ not usable: Phueut's own store has ~600 reviews, mostly an imported batch (Aug-Sep 2024), ~1/month since | ◈ not usable: Ottocast's 554 + 303 reviews are an imported batch (Oct-Nov 2025, "collected from another provider"), ~5/month since | |
| D4 regulatory | ◆ CPSC: BISSELL recall ~1.7M (Apr 2026), Dovety stop-use warning (May 2026), CasaClean, Uomeod, PurSteam; all pressurized steamers. Phueut's best seller is "Pressurized" too | ◈ FCC authorization (Wi-Fi/Bluetooth radio) and Apple's "CarPlay" trademark: not checked yet (in the ChatGPT task) | |

## What this says

1. **The "560 aged CarPlay ads" was noise.** The phrase "carplay" matched car dealers (Ancira Nissan, BMW of Devon) and installers. On the exact product phrase almost no ad lives 90 days. CarPlay adapters sell on Amazon and TikTok, not through Meta.
2. **Steam cleaner ads on Meta look strong only because of one store.** No sign yet that a new DTC brand keeps Meta ads alive in this category.
3. **Both leaders' own stores are not where they sell.** Their reviews are imported; the sales channel is the marketplace. For us this means Amazon / TikTok Shop launch economics, not Shopify + Meta.
4. **Search is slightly behind the general trend in both** (A1 under 1). By our rule a category is out only if A1 and C1 both point down; C1 cannot be measured here, so A1 alone does not remove them.
5. **CarPlay has a higher-AOV path.** Ottocast moved from $42-49 adapters to "AI boxes" and screens at $99-229 plus mounts and accessories: a one-time product with an accessory line.

## Gaps

- Amazon B1/B2/B3 (newcomer success, survivors, concentration), ratings and complaint themes: ChatGPT task.
- Trends: one pull; the method asks for a mean of several.
- Meta sample: logged-off, ~30 ads per age window, Meta's order.

## Files

- Trends: `work/blind/trends_pulls/onetime_2026-11-10.txt` (terms + controls shampoo, body lotion).
- Meta: `work/blind/meta_ages/steam_cleaner.json`, `carplay.json` (exact phrases "handheld steam cleaner", "wireless carplay adapter").
- Reviews: `work/reviews/onetime/phueut_judgeme.tsv`, `ottocast_judgeme.tsv`. `work/review_fetch.py` now reads Judge.me's new JSON format (the old widget HTML returns nothing since at least 2026-11-10).
- Amazon snapshot: `work/blind/amazon.json` keys `steam_cleaner`, `carplay`.
