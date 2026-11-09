"""Market system: ads x traffic x brand search x customer economics (US), data as of 2026-11-07.
Sources:
- Meta Ad Library (US, active ads; age filters start_date[max]=2026-08-08 for 90+ days, 2026-05-07 for 180+ days);
- adlibraryspy.com store pages (SimilarWeb monthly visits Jun-Sep 2026, visitor countries);
- Google Trends API (US, 12 months, brand term as % of 'ski boots');
- competitor sites / video transcripts for prices.
Run: python market_system.py -> market_system.md
"""

CVR = (0.02, 0.03)  # assumed site conversion range (DTC rule of thumb, not measured)

# name, leader domain, ads_total, ads_90d+, ads_180d+, visits Jun,Jul,Aug,Sep (thousands), US visitor share %,
# brand search % of 'ski boots', category search %, AOV USD, AOV_is_estimate, repeat: (orders per year beyond first, reason), feasibility note
D = [
 ("Compression socks", "everstridesocks.com", 1423, 460, 190, (376, 387, 226, 330), 73, 5.0, 289, 50, True, (1.0, "socks wear out; multi-pair packs"), "Avoid medical (lymphedema) claims"),
 ("Turmeric glow soap (melanin-rich skin)", "earthlyderm.com", 468, 89, 44, (269, 219, 348, 913), 96, 2.2, 21, 45, False, (3.0, "1 bar ≈ 1 month; 3-5 bar bundles"), "Cosmetic claims only (no 'fades/blocks pigment')"),
 ("Persimmon soap (aging odor)", "try-kaori.com", 747, 200, 53, (49, 246, 653, 556), 34, 2.1, 13, 40, True, (3.0, "consumable; subscriptions"), "Flooded with clones; persona playbook"),
 ("Persimmon soap (aging odor) #2", "swarva.com", 354, 0, 0, (103, 79, 226, 155), 69, 2.9, 13, 40, False, (3.0, "consumable; subscription on by default"), "Same niche as Kaori"),
 ("2-in-1 carry-on duffel", "luhxe.com", 587, 26, 0, (936, 1500, 1800, 2300), 90, 12.9, 3, 129, False, (0.1, "durable, one-off"), "Bulky shipping; handbag duty ~55%"),
 ("Natural rodent repellent pouches", "sofyre.com", 11772, 0, 0, (310, 310, 778, 1200), 99, 8.7, 28, 40, True, (3.0, "pouches replaced every 1-3 months"), "EPA 25(b) minimum-risk rules + state registrations"),
 ("Men's compression tank", "north-alpine.com", 1627, 17, 1, (1200, 1900, 1800, 1100), 77, 13.9, 1, 60, True, (0.5, "apparel replacement"), "Sizes/returns; brand term ambiguous"),
 ("Back stretcher board", "lhanel.co", 388, 150, 0, (126, 127, 122, 114), 92, 2.2, 7, 50, True, (0.1, "durable"), "No disc/sciatica claims"),
 ("Red-light LED mask", "solawave.co", 54, 0, 0, (218, 252, 254, 250), 57, 19.3, 86, 200, True, (0.2, "durable device"), "Needs FDA-cleared OEM for wrinkle claims"),
 ("Magnetic lashes (not in corpus; found via lash check)", "moxielash.com", 302, 160, 59, (249, 289, 273, 301), 80, 2.2, 0, 50, True, (2.0, "lashes/clusters replaced"), "Cosmetic; crowded"),
 ("Exfoliating body towel", "blissal.com", 155, 1, 1, (339, 276, 223, 199), 56, 2.1, 5, 40, True, (0.5, "towel replaced yearly"), "Low ticket; fading traffic"),
 ("Men's leak-proof boxers", "menvault.com", 234, 20, 8, (11, 21, 60, 107), 100, 0.3, 3, 110, False, (1.0, "more pairs, replacement"), "FDA establishment fee ~$11.4K/yr if importing"),
 ("Non-tarnish tennis bracelet", "mylovemytreasure.com", 238, 110, 26, (14, 28, 52, 11), 96, 0.0, 140, 75, True, (0.3, "gifts, add-ons"), "Traffic tiny vs ads — evidence weak"),
 ("Collagen chin wrap", "tryskult.com", 870, 200, 160, (19, 24, 27, 16), 0, 0.6, 2, 50, False, (1.0, "wraps used up"), "Traffic data contradicts ads (visitors shown in AR/FR)"),
 ("Silvervine cat chew sticks", "purriq.com", 263, 150, 130, (23, 73, 52, 19), 52, 0.1, 7, 35, True, (2.0, "consumable chews"), "Low ticket; traffic falling"),
 ("Airplane seat cushion", "shoptravlr.com", 220, 120, 43, (29, 15, 18, 27), 68, 0.0, 3, 105, False, (0.1, "durable"), "Small traffic"),
 ("Gel ski shin sleeve", "skiguards.com", 107, 60, 60, (10, 13, 22, 18), 78, 0.0, 0, 55, False, (0.3, "seasonal re-buy"), "Off-season now; Dec-Feb window"),
 ("16-head massager (gift)", "alythera.com", 175, 22, 22, (None, None, None, 2), None, 0.0, 21, 120, True, (0.1, "durable"), "Tiny traffic; zevessa.com ~10K/mo"),
]

def seg(total, a90, a180, v):
    sep = v[3] or 0
    vals = [x for x in v if x]
    peak = max(vals) if vals else 0
    if sep < 40:
        return "SMALL (<40K visits) — ads don't translate into traffic"
    if a180 >= 25 or (a90 >= 100 and a180 >= 10):
        return "ESTABLISHED (old ads still live)"
    if sep >= 0.8 * peak and v[0] and sep >= 1.5 * v[0]:
        return "RISING (young ads, traffic growing fast)"
    if sep < 0.7 * peak:
        return "FADING (traffic down from peak, ads young)"
    return "STABLE-YOUNG (traffic steady, ads rotate)"

rows = []
for name, dom, tot, a90, a180, v, us, brand, cat, aov, aov_est, rep, feas in D:
    sep = v[3] or 0
    rev = (sep * 1000 * CVR[0] * aov, sep * 1000 * CVR[1] * aov)
    ltv = aov * (1 + rep[0] * 0.35)  # 35% of buyers act on the repeat cycle (assumption)
    passes = aov >= 50 or rep[0] >= 1.0
    rows.append(dict(name=name, dom=dom, tot=tot, a90=a90, a180=a180, v=v, us=us, brand=brand, cat=cat,
                     aov=aov, aov_est=aov_est, rep=rep, feas=feas, seg=seg(tot, a90, a180, v),
                     rev=rev, ltv=ltv, passes=passes, vpa=(sep * 1000 / tot) if tot else 0))

order = {"ESTABLISHED": 0, "RISING": 1, "STABLE-YOUNG": 2, "FADING": 3, "SMALL": 4}
rows.sort(key=lambda r: (order[r['seg'].split(' ')[0]], -(r['v'][3] or 0)))

def k(x):
    return "-" if x is None else (f"{x/1000:.1f}M" if x >= 1000 else f"{x:.0f}K")

out = ["# Market system: ads × traffic × brand search × customer economics (US)", "",
       "Date: 2026-11-07. Purpose: separate products whose demand is proven and holding from those that only just took off or are fading, and keep only those where one customer is worth enough (price ≥$50 or repeat purchases).",
       "",
       "## Layers",
       "",
       "1. **Ads (Meta Ad Library, US, active):** the leader's total ads, how many started 90+ days ago, how many 180+ days ago. Old ads still running mean the advertiser keeps paying for them.",
       "2. **Traffic (SimilarWeb via adlibraryspy, Jun-Sep 2026):** whether ads turn into visits, and whether traffic grows or fades. Visits per active ad flags spam-like ad volume.",
       "3. **Brand search (Google Trends, US, 12 months):** people typing the brand name themselves, as % of 'ski boots'. This shows organic pull and returning buyers. Category search % is shown for scale.",
       "4. **Customer economics:** AOV and a repeat cycle. Rough LTV = AOV × (1 + repeats/yr × 35%); the 35% is an assumption. Pass rule (owner's): AOV ≥$50 **or** at least one repeat order a year.",
       "",
       f"Revenue band = Sep visits × {CVR[0]:.0%}-{CVR[1]:.0%} conversion × AOV. This is a sanity check against the YouTuber's claims, not a measurement.",
       "",
       "## Segments",
       "",
       "- **ESTABLISHED:** ≥25 ads aged 180+ days, or ≥100 aged 90+ days and ≥10 aged 180+ days.",
       "- **RISING:** young ads, Sep traffic ≥1.5× June and near its peak.",
       "- **FADING:** Sep traffic below 70% of the peak.",
       "- **SMALL:** under 40K visits a month despite the ads.",
       "",
       "## Table",
       "",
       "| Segment | Product | Leader | Ads total / 90d+ / 180d+ | Visits Jun→Sep | US % | Visits per ad | Brand search % | Category search % | AOV | Repeats/yr | LTV ◇ | Rev/mo band ◇ | Pass $50-or-repeat | Main issue |",
       "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    v = " → ".join(k(x) for x in r['v'])
    out.append(f"| {r['seg'].split(' (')[0]} | {r['name']} | {r['dom']} | {r['tot']:,} / {r['a90']} / {r['a180']} | {v} | {r['us'] if r['us'] is not None else '-'} | {r['vpa']:.0f} | {r['brand']} | {r['cat']} | ${r['aov']}{' ◇' if r['aov_est'] else ''} | {r['rep'][0]} ({r['rep'][1]}) | ${r['ltv']:.0f} | ${r['rev'][0]/1e3:,.0f}K-{r['rev'][1]/1e3:,.0f}K | {'yes' if r['passes'] else 'NO'} | {r['feas']} |")
out += ["", "## Reading the table", "",
 "- **The YouTuber's revenue claims are inflated about 2× to 400× against the sanity band.** Luhxe ~2× and Menvault ~2× are the closest; Everstride ~7×, North Alpine ~8× and Earthly Derm ~11× are well above; Skult ($8.2M claimed vs ~$20K) is wildly off.",
 "- **Ad count alone misleads.** Skult (870 ads, ~16K visits), MLMT (238 ads, 11K visits), Kakiyu (830 ads, 13K visits) and Alythera (175 ads, 2K visits) run many ads with little traffic.",
 "- **Rising with no ad history:** Sofyre (11,772 ads, all <90 days; 0.3M → 1.2M visits) is a hot, risky trend; Luhxe (0.9M → 2.3M visits; strong brand search) has ads that rotate fast.",
 "- **Established and fed by both ads and brand demand:** Everstride (190 ads aged 180+ days; 330K visits; brand 5%), Earthly Derm (44 aged; 913K visits), Kaori (53 aged; 556K, but only 34% US).",
 "", "## Shortlist under this system", "",
 "**A. Established: proven and holding.** All pass the $50-or-repeat rule.",
 "1. Turmeric glow soap (Earthly Derm): 44 ads aged 180+ days; traffic 269K → 913K; consumable, LTV ~$90. Risk: cosmetic-only claims.",
 "2. Compression socks (Everstride): the most aged ads (190); 330K visits; brand search 5%; LTV ~$70. Risk: crowded category, no medical claims.",
 "3. Persimmon soap (Kaori): 53 aged ads; 556K visits, but only 34% of visitors are in the US; consumable. Risk: clone flood.",
 "4. Magnetic lashes (Moxie): found while checking the lash-serum row; not in the corpus. 59 aged ads; 301K visits. Would need its own look.",
 "",
 "**B. Rising: bigger upside, less proof.**",
 "5. 2-in-1 carry-on duffel (Luhxe): 0.9M → 2.3M visits; brand search 12.9%; AOV $129 passes despite no repeats. Ads rotate fast. Risk: bulky product, high duty.",
 "6. Men's leak-proof boxers (Menvault): 11K → 107K visits, 100% US; AOV $110 plus repeats. Risk: FDA establishment fee if we import.",
 "7. Rodent repellent pouches (Sofyre): 0.3M → 1.2M visits; consumable. Risk: EPA/state registration; every ad is younger than 90 days.",
 "",
 "**C. Stable but young ads:** LED mask (Solawave; strong brand search, needs an FDA-cleared OEM) and back stretcher (Lhanel; one-off ~$50).",
 "",
 "**Dropped by this system:**",
 "- small traffic despite ads: tennis bracelet, chin wrap, seat cushion, ski sleeve, silvervine sticks, 16-head massager;",
 "- fading: compression tank, exfoliating towel, Swarva.",
 "",
 "Data limits: SimilarWeb is weak for sites under ~50K visits a month. Brand terms like 'north alpine' and 'lhanel' may include unrelated searches. AOV marked ◇ is estimated. Conversion rate and the repeat share are assumptions.",
]
open("market_system.md", "w", encoding="utf-8").write("\n".join(out))
for r in rows:
    print(f"{r['seg'][:12]:12} | {r['name'][:40]:40} | sep {k(r['v'][3]):>6} | ads {r['tot']:>5}/{r['a90']:>3}/{r['a180']:>3} | brand {r['brand']:>5} | AOV {r['aov']:>4} | rep {r['rep'][0]} | LTV {r['ltv']:.0f} | rev {r['rev'][0]/1e3:.0f}-{r['rev'][1]/1e3:.0f}K | pass {r['passes']}")
