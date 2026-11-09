---
page: methods
title: "How we measured"
---

# How we measured

Method v2.1, frozen in `/RUNBOOK.md`. Rules were written before results were read; every change is a version bump with the reason logged.

## Amazon: who sells, and how new are they
- **What:** amazon.com search results, pages 1-5, for one query per category, delivery address set to New York 10001. Sponsored cards are skipped. 16 categories were read by our script; 4 (lash serum, hair serum, pre-wash oil, whitening powder) by hand by the owner's assistant after Amazon asked AI agents not to browse it.
- **Units:** the "bought in past month" badge. It is a **floor** ("1K+" = at least 1,000) and counts **buyers, not units**; the true number is higher. ◆ Amazon's own count.
- **Category:** a strict description of the product form (e.g. a neck cream must be sold *for the neck*), so other products don't leak in.
- **Brand age:** the oldest listing of a brand in the sample, dated from its Amazon product code (ASIN); codes are issued in order, error about ±1-2 months. ◈
- **New brand:** on Amazon less than 24 months, and not an established brand entering a new product (L'Oréal, Palmer's, RevitaLash…).
- **Unbranded seller:** a listing whose title does not start with a brand name. 22 of 72 top listings we checked by hand do have a registered brand that isn't in the title (LATORICE, NXPPYY…); they behave like unbranded sellers (price-led), and are counted as such.
- **Revenue floor:** units × listing price. Ignores discounts and multi-packs. ◈

## Meta ads: who keeps paying
- **What:** Meta Ad Library, United States, active ads containing the exact phrase (e.g. "tallow balm"). The counts are Meta's own (shown as "~N results"). ◆
- **Ad age:** the same search with "started before" today minus 30 / 90 / 180 days.
- **Shops:** a sample of ads drawn evenly from each age window, grouped by the shop they link to. Because the sample is drawn by age, almost every category shows some shop with a 90+ day ad; read the counts, not just "yes/no".
- **Brands:** counted on the brand's own Facebook Page, plus the share of ads mentioning the brand that link to its site (brands like GODA advertise mostly through creators' pages).
- **Limits:** the US library shows only ads running today; stopped ads vanish. A re-check in 30 days (`meta_recheck.py`) will show which of today's ads died. An old ad can also be a forgotten low-budget ad or brand advertising; we weigh small direct-to-consumer brands more than large ones.

## Google searches: is interest growing
- **What:** Google Trends, United States, 5 years, weekly. Growth = last 12 full weeks divided by the same weeks a year earlier.
- **Correction:** in April-June 2026 every term, including "shampoo" and "body lotion", spikes in the same weeks: a Google data artifact. Each term's growth is divided by the controls' growth (1.14 in pull 1).
- **Labels:** ≥1.2 growing, 0.8-1.2 flat, <0.8 falling (drop rule).
- **Noise:** Google returns a random sample each day; rare terms are noisy (we flag terms with many zero weeks). Three pulls on three days are averaged; pull 1 is in, 2-3 pending.

## Drop rules (decided before results)
A category is dropped if (a) searches fall below 0.8 of last year, or (b) new brands sell under 10,000 a month on Amazon **and** no shop keeps a Meta ad 90+ days.

## Not measured
Website traffic (estimators are unreliable for shops of this size: Similarweb itself shows nothing under 5,000 visits a month and is confident only above 100,000), review growth over time (pending), margins and product costs, TikTok Shop live sales.

## Data files
`work/dossier/dossier_data.json` (all layers), `digest/<id>.json` (per page), `chart_data.json` (charts), `verdict_v21.json` / `FINAL_V21.md` (verdict table). Scripts: `work/blind/graveyard_*.py`, `meta_*.py`, `trends_calc.py`, `work/dossier/build_dossier.py`, `digest.py`, `verdict_v21.py`.
