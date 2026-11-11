# One-time-purchase products: DeepResearch result + our check (2026-11-10)

Prompt: `work/prompts/DEEPRESEARCH_ONE_TIME.md`. The full report was pasted in chat (Russian) and is not stored here; this file keeps what matters and our check of it.
First run failed (the tool saw no question and wrote a generic agenda); the fix was the "ЭТО И ЕСТЬ МОЙ ЗАПРОС" line.

## Report's verdict

travel vacuum bags > CarPlay adapter (validate as steam cleaner's replacement) > 2-in-1 duffel > steam cleaner > microcurrent device.

## Facts we checked ourselves

| Claim | Check | Status |
|---|---|---|
| BISSELL recalled ~1.7M Steam Shot OmniReach/Omni, 206 reports, 161 burns | [CPSC recall, 2026-04-09](https://www.cpsc.gov/Recalls/2026/BISSELL-Recalls-Over-One-Million-Steam-Shot-OmniReach-Steam-Cleaners-Due-to-Risk-of-Serious-Burn-Hazard-from-Attachments) | ◆ confirmed |
| CPSC stop-use warning on Dovety TMSC-001 (sold on Amazon and TikTok), 52 reports, 48+ burns, no recall agreed | [CPSC warning, 2026-05-07](https://www.cpsc.gov/Warnings/2026/CPSC-Warns-Consumers-to-Stop-Using-Dovety-Steam-Cleaners-Immediately-Due-to-Risk-of-Serious-Burn-Injury) | ◆ confirmed |
| More steamer warnings exist: Uomeod mini (2025), PurSteam travel steamers (2026) | CPSC search results | ◆ seen, not read |
| Steam cleaner TikTok leader Phueut 371.5K sold | our `tiktok.py` had 371.3K on 2026-11-07 | ◆ matches |
| FastMoss Pro ~$89/mo monthly, 7-day trial | aggregators disagree ($63-109); official page not read | ◇ check fastmoss.com/pricing before paying |
| Vacuum bags on TikTok: 142.2K (Snofrid), 79.0K and several 6-8K listings | not re-checked; our `tiktok.py` had `vacuum_bags: None` | ◈ new, plausible |
| Luhxe traffic and duffel TikTok 87K | report could not confirm; these are our own earlier numbers | ◈ ours |

Note: Phueut on Amazon is listed as a "Pressurized Handheld" steamer (`work/blind/amazon.json`), the same build CPSC warns about for Dovety.

## Where the report is weak

1. **Its own vacuum-bag economics do not add up.** It asks for a first-order CAC of $15-25, but the prices it cites are $17.99-31.98 (Amazon leader Vacbird $29.99). Rough contribution at $28 AOV: landed kit ~$10, US fulfilment ~$6-8, payment ~$1, returns ~$1.5, so max CAC ≈ $8 and break-even ROAS ≈ 3.3. That is out of reach for Shopify + Meta at this price. It works only on TikTok Shop (affiliate commission instead of CAC) or Amazon, or with bundles taking AOV to $40+. This is the same reason our G3 rule (repeat or ≥$40) existed.
2. **Our main metric is missing.** No newcomer-survival reading (B1/B2) for any of the three. "13 Amazon listings at 1K+/mo" says nothing about who is new.
3. **Tools section adds little.** The GitHub finds are 2-3 star repos; the Shopify `/products.json` idea is one we already use. Kalodata and Tabcut prices are unverified.
4. **Return rates and complaints** were not measured (it says so); 1-3★ review mining is still to do.

## What is new and usable

- **Free TikTok tracker:** snapshot `sold` on 20-30 product pages daily; the metric is median daily Δsold, not lifetime sold. Our `tiktok.py` read keyword pages from a cache once; product pages read daily would give a trend.
- **Steam cleaner = product-liability risk**, confirmed by CPSC. Not a generic private-label SKU.
- **Microcurrent** stays out as a first product (FDA 510(k) route).
- **CarPlay adapter** deserves a short check (Amazon complaints, compatibility, sell-through) before it replaces the steam cleaner.
- Duty: exact rate needs a 10-digit HTS code per SKU (Section 301 China 7.5-100% by code); ask a customs broker before any PO.
