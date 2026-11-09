# Indonesia shortlist: devil's advocate on the METHOD (2026-11-08)

Scope: how the repeat-purchase shortlist in `ID_CREATOR_PLAN.md` section 7 was built, not the products themselves.
Markers: ◆ confirmed · ◈ likely / judgment · ◇ disputed or unchecked.

## A. What the current list actually rests on

| Claim in the list | What was really checked | Gap |
|---|---|---|
| 10 device+refill candidates | My own idea from the razor-and-blades pattern and US TikTok hits | Zero Indonesian sales numbers per product. One Tokopedia search for "refill pewangi otomatis": Stella Matic listings at 70+ and 250+ sold; most counts not captured |
| Refill cycles | Guessed | Not taken from reviews or seller data |
| Category growth | Snippets of secondary posts (FastMoss via dami.co.id, Cube via Smartkarma, Compas via Shopdora) | Primary reports not read; FastMoss and Magpie disagree on beauty |
| Shower filter market | IndexBox pages | IndexBox reports are model-made estimates (◇) |
| PKRT / BPOM tiers | Permit-consultant websites + one news explainer | Consultants sell the permit, so they lean to "everything needs one". Primary Permenkes 5/2026 PKRT list not read |
| "No permit" for filters, liners, mop pads | Not checked at all | SNI-mandatory list, import rules (Lartas), import licence not checked |
| Smoking accessories on TikTok Shop | Tokopedia guideline page fetched; the text had nothing on it | Unknown (◇) |
| Fit to our 98 creators | Nothing | Audience age/gender/city unknown |

## B. Attacks

1. ◆ **The device+refill prior has no Indonesian evidence.** Involve Asia's top-30 by real affiliate conversions (their ID publisher dashboard, ranked by quantity) has no device+refill item. It's cheap consumables bought again:
   hair tonic (4 rows incl. variants), men's face wash, whitening toothpaste, body lotion, bar soap, stain-remover powder (2),
   herbal toothache oil/drops (3), collagen drink, spicy snack (2), throat gel, nasal inhaler, perfume.
   ◆ FastMoss free top-10 (period not shown): gluta soap, false lashes, skin tint, two perfumes, lip cream, sheet mask, wall hook, hijab.
   ◈ In Indonesia "repeat" looks like re-buying the same cheap consumable (sachet economy), not refills for a device.
   Counter: Involve Asia covers only its own network and ranks by units (favours cheap items); FastMoss top-10 has no period.
   So the refill idea is unproven, not disproven.
2. ◆ **"BPOM" is a selling point, not just a cost.** Top sellers put "BPOM" in the product title. A no-permit product loses that trust signal.
   And the truly permit-free zone is small: anything with scent or chemistry is PKRT, anything on the body is BPOM.
3. ◇ **The repeat proxy (refill vs device "terjual") is untested.** Confounders: refills bought for other brands' devices, multipacks,
   lifetime counters, inflated "terjual" from fake orders (◈ common). Validate on 3-5 known brands before trusting it.
4. ◈ **Affiliate test confounds.** Orders per 1,000 views depend on price, commission, video quality, creator effort, posting time.
   Need a crossed design: same product across several creators, same creator across several products, one fixed brief.
5. ◆ **US lessons not applied** (see `METHOD.md` insights 12-14): brand success ≠ category demand; openness by brand cohort
   (do brands that entered in the last 12-24 months take share?); top-3 concentration; life-cycle stage; seasonality
   (12.12 now, Ramadan ~Feb-Mar 2027).
6. ◈ **Unit economics unchecked.** Many top items sell at IDR 18-60K (~$1-4). After ~25-30% platform + affiliate take,
   shipping promos and returns, little is left unless COGS is tiny. Cheap Chinese-made rivals push prices down.
7. ◇ **Own-product route unchecked:** local contract maker vs import (import licence, Lartas, SNI), lead times, MOQ.
8. ◇ **Creatives:** whether Meta winners carry over to TikTok is not checked. TikTok-native data exists:
   FastMoss/Kalodata show estimated units and revenue per video (◆ per their tutorials; the numbers are estimates ◇,
   Viralaris says TikTok does not publish per-video sales).

## C. Free data routes tested today
- ◆ FastMoss `saleslist?region=ID` without login: top 10 only, no period, no filters.
- ◆ FastMoss keyword search without login: no rows.
- ◆ Viralaris category pages: 5 names, no sold counts in the free view. Paid IDR 19K / 7 days (~$1.2).
- ◆ Tokopedia search via fetch: works but sold counts mostly missing. In-app browser navigation to tokopedia.com failed (denied).
- Conclusion: a real pass needs a FastMoss or Kalodata login (the owner registers; trial).

## D. Method v1 for the Indonesia shortlist (proposal, not yet run)
1. **Discover from data:** top ~500 products, last 30 days, TikTok Shop ID, by category (FastMoss/Kalodata), plus "refill" / "isi ulang" searches.
2. **Repeat filter:** the product is used up, plus evidence of re-buying: multipack/bundle listings selling; share of reviews saying
   "repeat order / beli lagi / order lagi / langganan" (◈ common phrasing, untested as a metric).
3. **Openness:** share of category revenue held by brands that started selling in the last 12 months; top-3 share.
4. **Life cycle:** 3-6 month revenue trend of the category and of the leaders; seasonality.
5. **Permit tier and time to our own SKU:** none / PKRT / BPOM / food.
6. **Economics at the real price point** (fees, affiliate commission, shipping, returns, COGS quote).
7. **Fit to our creators** once audience screenshots arrive.
8. **Affiliate test** with the crossed design; repeat proxy validated first.
Run steps 1-6 as a mechanical script so the list is reproducible (lesson from the US list that took five passes).
