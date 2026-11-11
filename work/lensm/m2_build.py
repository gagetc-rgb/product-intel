"""Lens M step 3: merge raw fetches (raw/*.json) with hand classification (m2_data.py) -> m2_stores.csv"""
import json, csv, datetime as dt
from m2_fetch import CATS, RAW, R
from m2_data import Y, NO
cand = json.load(open(R / "m2_candidates.json", encoding="utf-8"))
CUT = dt.date(2024, 11, 10)
LEAD = {"persimmon_soap": ["miraiclinical.com"], "turmeric_soap": ["earthlyderm.com"], "body_oil": ["goda.co"], "color_foundation": ["luxe.com", "smooche.com", "primeprometics.com", "hestiacosmetics.com"],
        "tallow_balm": ["ancestralcosmetics.com", "terralotus.shop"], "lash_serum": ["borboleta.com", "babeoriginal.com"], "shower_filter": ["sproos.co"],
        "scent_diffuser": ["scentifyhome.com", "aroma360.com", "aurahouse.com"], "compression_socks": ["everstridesocks.com"], "chin_wrap": ["tryskult.com"]}
LEADER_Q = {"dog_fountain": "selenepets.com", "magnesium_spray": "ozcogoods.com", "exfoliating_towel": "goshi.com", "hair_serum": "hinu.co", "hair_removal_cream": "simplesnatched.com", "neck_cream": "", "rosemary_oil": ""}
EXTRA = {"color_foundation": ["luxe.com"], "tallow_balm": ["terralotus.shop"], "shower_filter": ["sproos.co"]}  # owner-listed leaders absent from the sample
def ds(s):
    try: return dt.date.fromisoformat(s)
    except Exception: return None
rows = []
for c in CATS:
    stores = [s for s in cand[c]["stores"] if s["max_age"] >= 90 or s["max_age"] < 30]
    for dom in EXTRA.get(c, []): stores.append({"domain": dom, "ads": "", "max_age": "not in sample", "hosts": [dom]})
    for s in stores:
        d = s["domain"]; o = json.load(open(RAW / f"{d}.json", encoding="utf-8"))
        sells, title, price, bundle, note = Y.get((c, d), ("no", "", "", "", ""))
        reason = NO.get(d, "") if sells == "no" else ""
        if sells == "no" and not reason: raise SystemExit(f"missing reason {c} {d}")
        sh = min((p["c"] for p in o["products"]), default="") if o.get("products") else ""
        rd = o.get("rdap_reg"); wb = o.get("wb_first")
        wbd = None if not wb or wb == "none" else dt.date(int(wb[:4]), int(wb[4:6]), int(wb[6:8]))
        wbs = wbd.isoformat() if wbd else ("none" if wb == "none" else "unknown")
        cs = [x for x in (ds(rd or ""), wbd, ds(sh)) if x]; flag = ""
        if not cs: age = "unknown"
        else:
            age = "young" if min(cs) >= CUT else "old"; r = ds(rd or "")
            if r and wbd and r >= CUT and wbd < r - dt.timedelta(days=180):
                if wbd < CUT: age = "unclear-old-domain"
                flag = f"first capture {wbs} precedes registration {rd}: earlier owner or re-registered domain"
            if r and wbd and r < dt.date(2023, 11, 10) and wbd >= dt.date(2025, 1, 1):
                age = "unclear-old-domain"; flag = f"registered {rd} but first capture only {wbs}: parked, bought or re-launched domain?"
        notes = [x for x in (note, flag) if x]
        if not rd: notes.append(f"RDAP gave no registration date (HTTP {o['rdap_status']})")
        if o["products"] is None: notes.append(f"products.json blocked or absent (HTTP {o['pj_status']})")
        if o["products"] is None and o.get("home_status") not in (200, None): notes.append(f"home HTTP {o.get('home_status')}")
        same = ""
        if d in ("trylumineskin.com", "hestiacosmetics.com"): same = "trylumineskin.com = hestiacosmetics.com (identical home page); count once"
        if d == "trykaoli.com": same = "possible, not proven: name one letter from try-kaori.com"
        if d == "try-kaori.com": same = "possible, not proven: name one letter from trykaoli.com"
        role = ""
        if sells == "yes": role = "leader" if d in LEAD.get(c, []) else ("leader?" if d == LEADER_Q.get(c) else "follower")
        elif d in LEAD.get(c, []): role = "leader (listed by owner)"
        if d == "trylumineskin.com" and c == "color_foundation": role = "leader (same shop as hestiacosmetics.com)"
        src = f"https://{d}/products.json?limit=250; https://{(s['hosts'] or [d])[0]}/; https://rdap.org/domain/{d}; http://web.archive.org/cdx/search/cdx?url={d}&limit=1&fl=timestamp"
        rows.append(dict(category=c, domain=d, max_age_days=s["max_age"], ads_in_sample=s["ads"], sells_product=sells, reason_if_no=reason, product_title=title,
                         price_usd=price or ("unknown" if sells == "yes" else ""), bundle=bundle,
                         shopify_created=sh or "unknown (products.json unreadable)", domain_created=rd or "unknown", wayback_first=wbs, age_class=age, role=role,
                         same_owner=same, source_urls=src, notes="; ".join(notes), checked_on="2026-11-10"))
with open("m2_stores.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(len(rows))
# summary
import collections
for c in CATS:
    rs = [r for r in rows if r["category"] == c]
    old = [r for r in rs if r["max_age_days"] != "not in sample" and r["max_age_days"] >= 90]
    new = [r for r in rs if r["max_age_days"] != "not in sample" and r["max_age_days"] < 30]
    yo = [r for r in old if r["sells_product"] == "yes"]
    print(f"== {c}: 90+={len(old)} yes={len(yo)} unclear={sum(r['sells_product']=='unclear' for r in old)} no={sum(r['sells_product']=='no' for r in old)} | <30: {len(new)} yes={sum(r['sells_product']=='yes' for r in new)} unclear={sum(r['sells_product']=='unclear' for r in new)}")
    for r in yo: print("   ", r["domain"], r["max_age_days"], r["role"], r["age_class"], r["domain_created"], r["wayback_first"], r["shopify_created"][:10])
    for r in new:
        if r["sells_product"] != "no": print("    NEW<30", r["domain"], r["sells_product"], r["age_class"])
