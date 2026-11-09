"""Metrics v2.2 (METRICS.md) for all 20 categories, computed from saved data only (2026-11-09).
Amazon metrics (A2, B1, B2, B3, D1) are recomputed here from the saved search scan (work/blind/graveyard_us),
with the same rules as AUDIT_2026-11-09 sections 8-9, so the site never carries a hand-typed Amazon number.
A1 = mean of Trends pulls (trends_series_summary.json); for tallow and turmeric the combined-phrasing value from AUDIT section 7.
B4 = shops by own domain (meta_by_domain.json). D2 = price reading from AUDIT sections 9-10 (text, ◈).
Usage (from work/blind): python ../audit/metrics_v22.py  ->  ../audit/metrics_v22.json"""
import json, sys, pathlib
sys.path.insert(0, "."); import graveyard_stats2 as g, graveyard_table as t
A = pathlib.Path(__file__).parent
J = lambda p: json.load(open(p, encoding="utf-8"))
TS = J("trends_series_summary.json")
TT = J(A / "trends_terms.json")["categories"]

# A1 override: all phrasings pulled together and summed, divided by the sector controls (AUDIT section 7)
A1_COMBINED = {"tallow_balm": (0.78, "tallow balm + beef tallow for skin + tallow skincare + tallow moisturizer, summed"),
               "turmeric_soap": (0.72, "turmeric soap + kojic acid soap + turmeric bar, summed")}
# D2: price reading over 12 months (Keepa charts read by eye + camelcamelcamel table), AUDIT sections 9-10
D2 = {"color_foundation": ("stable", "Luxe cut to ~$13-17 Jul-Oct, back to $28-30; temporary"),
      "dog_fountain": ("stable", "flat all year, regular discount cycles"),
      "lash_serum": ("stable", "flat, discount cycles"),
      "tallow_balm": ("stable", "nearly flat; Terra Lotus $19.99 all year"),
      "persimmon_soap": ("mild", "cheap multipacks down ~20%; Mirai $23 to $18-20"),
      "scent_diffuser": ("stable", "promo dips; new models launch at $130 and settle at $80-90"),
      "shower_filter": ("mild", "mixed; some models drift down $30 to $22"),
      "body_oil": ("stable", "flat; GODA $47 to $33-35 in Jan, flat since"),
      "turmeric_soap": ("mild", "cheap 5-packs drift $10 to $7; Valitic flat")}
# B6: verified young businesses (under 3 years) with a large share in a channel, AUDIT sections 1 and 9 (checked by hand)
B6 = {"persimmon_soap": "Kaori (domain Feb 2026; 750 Meta ads)", "tallow_balm": "Terra Lotus (domain Mar 2024; Amazon #1)",
      "lash_serum": "Hanae (domain Nov 2025; 5,500/mo on Amazon)", "turmeric_soap": "Earthly Derm (site since Jan 2024; store reviews x7.6)"}
B6_NONE = {"color_foundation": "Luxe 2021, Smooche ~2021, Prime Prometics 2020", "body_oil": "GODA: reviews since Dec 2023, founding year not found",
           "scent_diffuser": "AirScent 1946, Scentify ~2020", "shower_filter": "Magichome sells since 2019"}

DOM = {"smooche.com": "color_foundation", "primeprometics.com": "color_foundation", "luxe.com": "color_foundation",
       "goda.co": "body_oil", "drmtlgy.com": "body_oil", "try-kaori.com": "persimmon_soap", "miraiclinical.com": "persimmon_soap",
       "earthlyderm.com": "turmeric_soap", "aroma360.com": "scent_diffuser", "scentifyhome.com": "scent_diffuser", "aurahouse.com": "scent_diffuser",
       "bare-ritual.com": "tallow_balm", "byminus.com": "tallow_balm", "ancestralcosmetics.com": "tallow_balm", "terralotus.shop": "tallow_balm",
       "try-forge.com": "tallow_balm", "wildgoldtallow.com": "tallow_balm", "sproos.co": "shower_filter", "borboleta.com": "lash_serum"}
MD = {r["domain"]: dict(r, pid=DOM.get(r["domain"])) for r in J(A / "meta_by_domain.json")}
print("domains without category:", sorted(d for d in MD if d not in DOM))
out = {}
for f in sorted(pathlib.Path("graveyard_us").glob("*.json")):
    pid = f.stem
    if pid not in TT: continue
    L = {a: x for a, x in J(f)["listings"].items() if g.on_target(pid, x["title"])}
    ent, bu = {}, {}
    for a, x in L.items():
        k = g.norm(x["brand"]) or g.title_brand(x["title"]) or "solo:" + a
        ent[k] = max(ent.get(k, 0), g.age_m(a, x)); bu[k] = bu.get(k, 0) + x["b"]
    U = sum(bu.values()) or 1
    E = {k for k in ent if 3 <= ent[k] < 24 and k not in t.EST}
    win = {k for k in E if bu[k] >= 1000}; mid = {k for k in E if bu[k] >= 300}
    ts = TS.get(pid, {})
    a1, a1src = (A1_COMBINED[pid][0], A1_COMBINED[pid][1]) if pid in A1_COMBINED else (ts.get("rel_yoy_mean"), TT[pid]["current"][0])
    shops = [{"domain": d, "active": v.get("active"), "aged90": v.get("aged90")} for d, v in MD.items() if v.get("pid") == pid] if isinstance(MD, dict) else []
    out[pid] = {
        "A1": a1, "A1_terms": a1src, "A1_pulls": len(ts.get("pulls", {})),
        "A1_zero_share": max([v.get("zero_share_2y") or 0 for v in ts.get("pulls", {}).values()] or [None]),
        "A2": U, "A2_source": J(f).get("source") or "automated scan",
        "flags": [x for x, ok in [("small sample: under 20 entrants", len(E) < 20),
                                  ("search term too rare (>20% zero weeks)", (max([v.get("zero_share_2y") or 0 for v in ts.get("pulls", {}).values()] or [0])) > 0.2),
                                  ("Amazon data collected by hand, not re-verified", "manual" in (J(f).get("source") or "")),
                                  ("hair serum, pre-wash oil and rosemary oil overlap: partly one market", pid in ("hair_serum", "prewash_oil", "rosemary_oil")),
                                  ("shelf = all body oils, not only firming/crepey", pid == "body_oil"),
                                  ("brand-only titles: shelf undercounted by ~43K/mo", pid == "compression_socks")] if ok],
        "B1": round(len(win) / len(E), 3) if E else None, "B1_n": len(E), "B2_1k": len(win), "B2_300": len(mid),
        "B3_hhi": round(sum((100 * v / U) ** 2 for v in bu.values())), "B3_top3": round(sum(sorted(bu.values(), reverse=True)[:3]) / U, 2),
        "D1_unbranded_1k": sum(k.startswith("solo:") for k in win),
        "B4_shops": shops, "B6": B6.get(pid), "B6_none": B6_NONE.get(pid),
        "D2": D2.get(pid, (None, "not measured"))[0], "D2_note": D2.get(pid, (None, "not measured"))[1],
    }
    r = out[pid]
    print(f"{pid:18} A1 {r['A1']} A2 {U:>7,} | B1 {r['B1_n']:>3} -> {r['B2_1k']:>2} ({(r['B1'] or 0):.0%}) 300+ {r['B2_300']:>2} | HHI {r['B3_hhi']:>5} top3 {r['B3_top3']:.0%} | unbr {r['D1_unbranded_1k']} | shops {len(shops)}")
json.dump(out, open(A / "metrics_v22.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
