"""Writes the 12 shorter category pages (weak / dropped). Numbers in the front matter and the facts table come from
digest/<pid>.json and verdict_v21.json; the prose is hand-written per category and only cites numbers from those files."""
import json, pathlib
H = pathlib.Path(__file__).parent
V = {r["pid"]: r for r in json.load(open(H / "verdict_v21.json", encoding="utf-8"))}
TERMS = {"prewash_oil": "pre wash hair oil", "hair_removal_cream": "hair removal cream", "neck_cream": "neck cream", "dog_fountain": "pet water fountain",
         "chin_wrap": "double chin", "pore_patch": "pore patches", "compression_socks": "compression socks", "whitening_powder": "teeth whitening powder",
         "magnesium_spray": "magnesium spray", "exfoliating_towel": "exfoliating towel", "rosemary_oil": "rosemary oil for hair", "turmeric_soap": "turmeric soap"}
PAGES = [  # (order, pid, title, status, verdict line, body markdown)
 (9, "prewash_oil", "Pre-wash hair oil", "weak",
  "Looks big but isn't ours: a $200K-a-month shelf held 89% by old hair-oil brands, with a search term too rare to read and a Meta phrase that measures laundry ads.",
  """The Amazon query `pre wash hair oil` returns general hair oils: Mielle (52,350/mo), Moroccanoil (25,000), L'Oréal (24,000), OUAI, OGX. Old brands hold **89%** of the 203,900 units a month; brands under 24 months hold 6%. ◆

**Trend is unreadable**: 71% of the last two years' weeks are zero in Google Trends, so the ×3.4 is noise, not growth. ◆
**Meta is unreadable**: the exact phrase "pre wash" mostly finds laundry and car-detailing ads (sockcatcher.com, a laundromat page). ◆

Reading: there is no distinct "pre-wash oil" market yet; it is the general hair-oil shelf, which belongs to big brands. ◈"""),
 (10, "hair_removal_cream", "Men's body hair removal cream", "weak",
  "Two giants (Veet, Nair) hold 85% of the shelf; one young brand (Phofay) gets through. Strong Meta survival, flat demand.",
  """Veet (37,350/mo) and Nair (35,400) together take **85%** of 85,550 units a month. The young brand Phofay sells 7,150/mo at $22.99 (~15 months), about twice the giants' price ($10.47-11.99). ◆ units/price, ◈ age.
Meta ("hair removal cream"): 2,600 active, **24% alive 90+ days**, one of the highest shares; 15 of 23 shops keep a 90+ day ad (shopluuma.com 500 days, bumzzy.com 414). ◆ Search ×0.96: flat. ◆

Reading: a premium niche next to two cheap giants. Phofay shows it can work, but there is room for perhaps one more brand. The ID scan gave new brands only 3,800/mo versus 9,700 in the US scan: the newcomer number is unstable. ◈"""),
 (11, "neck_cream", "Neck firming cream", "weak",
  "After the v2.1 fix (only creams sold for the neck), new brands take 8% of the shelf; old skincare brands hold the rest.",
  """v2.0 counted face creams that also mention the neck; v2.1 keeps only creams sold for the neck. Result: 103,400 units a month, **86% to old brands** (medicube 30,000, Gold Bond 20,000, goPure 10,300), 8% to brands under 24 months. ◆
Meta ("neck cream"): 4,200 active, 10% alive 90+ days; 10 of 11 shops keep a 90+ day ad (sreemed.com 722 days, vibriance.com 225). ◆ Search ×1.19: on the border between flat and growing. ◆

Reading: demand exists and ads survive, but the Amazon shelf is a skincare-brand shelf. A newcomer would compete with medicube and Gold Bond on trust. ◈"""),
 (12, "dog_fountain", "Stainless-steel pet water fountain", "weak",
  "Big and growing, but a price war: unbranded sellers take half the units, old brands most of the rest, new brands 4%.",
  """220,150 units a month; **51% to unbranded sellers**, 45% to old brands (Veken 56,900/mo, PETLIBRO 13,950), 4% to brands under 24 months. 26 unbranded listings sell 1,000+ a month. Median price $39.99. ◆
Search "pet water fountain" ×1.44: growing. ◆ Meta's phrase "water fountain" mostly finds pond and garden fountains (propondandlakes.com, 1,494 days), so the ad layer does not describe this product. ◆

Reading: demand is real and rising, but it is an Amazon commodity. Good for a cheap private-label seller, not for a brand. ◈"""),
 (13, "chin_wrap", "Collagen chin / V-line wrap", "weak",
  "A small Amazon shelf held by old brands; the big Meta numbers belong to med-spas and surgery, not to chin wraps.",
  """42,450 units a month; 72% to old brands (Marée 9,500/mo, STYLIA 8,600), 14% to brands under 24 months, 14% unbranded. Median price $12.99. ◆
Meta's phrase "double chin" (7,600 active) is dominated by clinics: thestudiomd.com (778 days), med-spa and AirSculpt pages. It measures the worry, not the product. ◆ Search for "double chin" ×0.84: flat, close to falling. ◆

Reading: low price, small shelf, old leaders, and the ad market belongs to clinics. ◈"""),
 (14, "pore_patch", "Hydrocolloid nose pore patches", "weak",
  "Bioré holds the shelf; no Meta market (one ad found); the search term is too rare to read.",
  """50,900 units a month; **88% to old brands** (Bioré 26,000/mo, Mighty Patch 9,000, Peach Slices 6,000). One young brand (Vue, ~5,000/mo, ~10 months). ◆
Meta: the exact phrase "pore patches" finds **one** active ad (vueswiss.com). ◆ Trends: ×0.81 with 30% zero weeks: unreliable. ◆

Reading: a mature drugstore item with no visible direct-to-consumer ad market. This is the only category that nearly failed kill rule (b). ◈"""),
 (15, "compression_socks", "Compression socks", "weak",
  "Huge Meta activity, but on Amazon three-quarters of units go to unbranded sellers and no young brand reaches 1,000 a month.",
  """66,850 units a month in the US scan (172,000 in the earlier Indonesia-address scan: the shelf shown depends on the address; overlap only 29%). **73% unbranded**, 21% old brands (Copper Compression 11,900/mo), 6% brands under 24 months; no young brand at 1,000+. ◆
Meta ("compression socks"): **15,000 active**, 15% alive 90+ days, 610 alive 180+; everstridesocks.com keeps an ad 789 days. ◆ Search ×0.98: flat. ◆

Reading: a big ad market of store brands (EverStride and others) next to an Amazon commodity. The opportunity, if any, is a store brand; Amazon shows no sign that a new brand can win there. ◈"""),
 (16, "whitening_powder", "Teeth whitening powder", "weak",
  "The smallest shelf of all 20 and almost no lasting ads: 2 of 150 active ads have run 90+ days.",
  """16,100 units a month (collected by hand, US), the smallest shelf measured. 52% old brands (Boka 5,000/mo, Viva 2,600), 20% young brands, 29% unbranded. Median price $17.99. ◆
Meta ("whitening powder"): 150 active, **2 alive 90+ days, 0 alive 180+**: ads do not survive. ◆ Search for "teeth whitening powder" ×1.11: flat. ◆

Reading: a niche with high TikTok sales in our cached data (292,500 sold for the top item, ◈) but little Amazon demand and no lasting Meta advertiser. ◈"""),
 (17, "magnesium_spray", "Topical magnesium oil spray", "weak",
  "Old wellness brands hold two-thirds; young brands almost absent; a long-lived but small ad market.",
  """60,250 units a month; 68% old brands (Dr Teal's 13,000/mo, Seven Minerals 10,300, Ancient Minerals 5,400), 30% unbranded, 2% young brands. ◆
Note: the earlier scan used Amazon bylines for this category and found 4,550/mo to young brands; with title-only brand reading (the rule for all 20) it is 1,250. Some young brands may be hidden in the unbranded share. ◆/◈
Meta ("magnesium spray"): 510 active, 14% alive 90+, **10% alive 180+**; 5 of 13 shops keep a 90+ day ad (ozcogoods.com 443 days). ◆ Search ×0.97: flat. ◆

Reading: a small evergreen niche for a few store brands; nothing on Amazon says a newcomer can grow there. ◈"""),
 (18, "exfoliating_towel", "Exfoliating shower towel", "weak",
  "Growing search interest, but Goshi and unbranded sellers hold the shelf; young brands take 2%.",
  """53,700 units a month; 53% old brands (Goshi 13,000/mo, Salux 3,650), 45% unbranded, 2% young brands. ◆ Same caveat as magnesium: with Amazon bylines (earlier scan) young brands were 5,100/mo, with title-only reading 900. ◆/◈
Search for "exfoliating towel" **×1.63: growing**. ◆ Meta: 460 active, 28% alive 90+, 14% alive 180+ (high survival); goshi.com keeps an ad 294 days. ◆

Reading: demand is rising and ads that work keep running, but Goshi owns the brand position and unbranded towels own the price. Worth a second look only if a clear product difference exists. ◈"""),
 (19, "rosemary_oil", "Rosemary hair oil", "dropped",
  "Dropped by the pre-registered rule: search interest is falling (×0.76 a year).",
  """Kill rule (a): searches for "rosemary oil for hair" are at **0.76** of last year (control-corrected). The yearly index peaked in 2023-24 (39.9) and has not grown since. ◆
The shelf is large (200,700 units/mo) and still has young winners (6 brands at 1,000+, e.g. Aveya 10,000/mo), but 80% belongs to old brands (Mielle 56,100/mo, BASK & LATHER 28,000, Botanic Hearth 21,800). ◆
Meta: 4,300 active, 6% alive 90+; exotichairdoctor.com keeps an ad 2,860 days. ◆

Why it matters elsewhere: hair-growth serum (#8) overlaps this shelf. ◈"""),
 (20, "turmeric_soap", "Turmeric soap", "dropped",
  "Dropped by the pre-registered rule: search interest is falling (×0.67 a year).",
  """Kill rule (a): searches for "turmeric soap" are at **0.67** of last year (control-corrected); the yearly index peaked in 2023-24 (39.8). ◆
The shelf: 109,800 units/mo, Valitic alone 49,850 (~59 months on Amazon), unbranded sellers 30%. Median price $9.99, the cheapest on the list. ◆
Meta: 330 active; glomelanin.com (337 days) and earthlyderm.com (253) keep long-running ads, and our earlier creative study saved Earthly Derm's. ◆

Reading: a cheap, falling, crowded soap market. ◈"""),
]
for order, pid, title, status, verdict, body in PAGES:
    d = json.load(open(H / "digest" / f"{pid}.json", encoding="utf-8")); v = V[pid]; a = d["amazon_us"]; m = d["meta_category"]
    fm = {"id": pid, "title": title, "status": status, "rank": order, "verdict": verdict,
          "trend_label": None if v["trend"] is None else ("growing" if v["trend"] >= 1.2 else "flat" if v["trend"] >= 0.8 else "falling"),
          "trend_x": v["trend"], "price_median_usd": v["price"], "price_p25_p75_usd": d["price_us"]["price_usd_p25_p75"],
          "shelf_units_mo": v["shelf"], "new_brand_units_mo": v["nb"], "new_brand_winners": v["winB"], "generic_units_mo": v["gen"],
          "meta_phrase": m["phrase"], "meta_active": m["active"], "meta_aged30": m["aged30"], "meta_aged90": m["aged90"], "meta_aged180": m["aged180"],
          "compliance_flag": v["flag"] or "", "data": f"digest/{pid}.json",
          "charts": [{"id": "shelf_by_kind", "type": "donut", "source": "digest.amazon_us.units_by_kind"},
                     {"id": "meta_ages", "type": "bar", "source": "digest.meta_category"}]}
    lines = ["---"] + [f"{k}: {json.dumps(x, ensure_ascii=False)}" for k, x in fm.items()] + ["---", "", f"# {title}", "",
             f"**Verdict: {status}.** {verdict}", "", body.strip(), "",
             "## Sources",
             f"Amazon (US, ZIP 10001) → `work/blind/graveyard_us/{pid}.json`. "
             f"Meta [exact phrase \"{m['phrase']}\"](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=%22{m['phrase'].replace(' ', '%20')}%22&search_type=keyword_exact_phrase&media_type=all). "
             f"Trends [\"{TERMS[pid]}\"](https://trends.google.com/trends/explore?date=today%205-y&geo=US&q={TERMS[pid].replace(' ', '%20')}). Method: `/RUNBOOK.md` v2.1.", ""]
    (H / "content" / f"{order:02d}_{pid}.md").write_text("\n".join(lines), encoding="utf-8")
    print("wrote", f"{order:02d}_{pid}.md")
