"""Build the dossier site (2026-11-09): freezes every number into site/data.js from the raw outputs, renders the
category texts (content/*.md) to HTML, and copies a small set of resized images to site/media/.
Nothing typed by hand except the review readings below (taken from work/reviews/v2/RESULTS_V2.md) and short names.
Usage: python work/site/build_site.py  ->  site/index.html (template + data inline) and site/media/*.jpg"""
import json, re, html, pathlib, datetime as dt, sys
from PIL import Image

R = pathlib.Path(__file__).resolve().parents[2]
D = R / "work/dossier"; OUT = R / "site"; MED = OUT / "media"
OUT.mkdir(exist_ok=True); MED.mkdir(exist_ok=True)
sys.path.insert(0, str(R / "work/blind")); from trends_calc import TERM, CONTROLS, load
J = lambda p: json.load(open(p, encoding="utf-8"))

SHORT = {"color_foundation": "Color foundation", "body_oil": "Body oil", "scent_diffuser": "Scent diffuser", "tallow_balm": "Tallow balm",
         "persimmon_soap": "Persimmon soap", "shower_filter": "Shower filter", "lash_serum": "Lash serum", "hair_serum": "Hair serum",
         "prewash_oil": "Pre-wash oil", "hair_removal_cream": "Hair removal", "neck_cream": "Neck cream", "dog_fountain": "Pet fountain",
         "chin_wrap": "Chin wrap", "pore_patch": "Pore patch", "compression_socks": "Compression socks", "whitening_powder": "Whitening powder",
         "magnesium_spray": "Magnesium spray", "exfoliating_towel": "Exfoliating towel", "rosemary_oil": "Rosemary oil", "turmeric_soap": "Turmeric soap"}
# store photos that show the wrong product (checked on the photo sheet) are not used as the category photo
BAD_PHOTO = {"vibriance.com", "vueswiss.com", "boka.com", "sringe.com"}
# advertisers whose ads are not the category's product at all (2026-11-10: osanyinherbs.com is a herbal shop, it came in under chin wrap)
BAD_ADS = {"osanyinherbs.com"}
# per category: advertisers whose ads in our sample show another product (2026-11-11: Particle ran fragrance ads, Vibriance a face serum)
BAD_ADS_CAT = {"neck_cream": {"particleformen.com", "vibriance.com"},
               "dog_fountain": {"winkflo.com", "theflowzy.com"},      # grooming comb, leash, warehouse: not the fountain
               "hair_removal_cream": {"bumzzy.com"},                  # an electric body shaver
               "whitening_powder": {"boka.com"},                      # toothpaste
               "color_foundation": {"smooche.com"},                   # lip plumper ads
               "body_oil": {"goda.co"},                               # perfume-oil ads
               "rosemary_oil": {"hairqare.co"}}                       # a hair-care course, not the oil
# single ads that show another product of an otherwise right brand
BAD_IMG = {"media/4565047e8b095c7c.jpg"}                               # Prime Prometics eyeliner
# category photo chosen by hand from the category's own ads when the automatic pick shows another product (checked on a contact sheet 2026-11-11)
# chin wrap, rosemary oil, neck cream: the leader's own product photo from its store (tryskult.com, mielleorganics.com, medicube.us), fetched 2026-11-11
PHOTO_OVERRIDE = {"hair_serum": "media/prod_hair_bodywise.jpg", "pore_patch": "media/f7cf7a3c346a5b3b.jpg", "rosemary_oil": "media/prod_rosemary_mielle.jpg",
                  "chin_wrap": "media/prod_chin_skult.jpg", "neck_cream": "media/prod_neck_medicube.jpg",
                  "dog_fountain": "media/bd7400a7cd7fa20b.jpg", "body_oil": "media/766ef63a4d9c956b.jpg", "color_foundation": "media/9fae9b7bc570df28.jpg",
                  "whitening_powder": "media/85bccf6d73501792.jpg", "hair_removal_cream": "media/e690ff4f4bcf864e.jpg",
                  # lash serum: Hanae, the young copy the page is about, instead of the auto-picked Borboleta store photo (owner, 2026-11-11)
                  "lash_serum": "media/prod_lash_hanae.jpg"}

# ---------- tiny markdown -> html ----------
TIER = {"◆": ("t1", "counted by a platform"), "◈": ("t2", "estimate or our reading"), "◇": ("t3", "disputed")}
def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?!\w)", r"<em>\1</em>", s)
    for ch, (cls, t) in TIER.items():
        s = s.replace(ch, f'<span class="tier {cls}" title="{t}">{ch}</span>')
    return s
def md(text, drop_table=None):
    out, lines, i = [], text.split("\n"), 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip(): i += 1; continue
        if ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"): rows.append(lines[i]); i += 1
            cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
            if drop_table and drop_table(cells[0]): continue
            body = [c for c in cells[1:] if not all(re.fullmatch(r":?-+:?", x or "-") for x in c)]
            t = "<div class=tbl><table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in cells[0]) + "</tr></thead><tbody>"
            t += "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body) + "</tbody></table></div>"
            out.append(t); continue
        if re.match(r"\s*[-*] ", ln):
            items = []
            while i < len(lines) and re.match(r"\s*[-*] ", lines[i]): items.append(re.sub(r"^\s*[-*] ", "", lines[i])); i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>"); continue
        if re.match(r"\d+\. ", ln):
            items = []
            while i < len(lines) and re.match(r"\d+\. ", lines[i]): items.append(re.sub(r"^\d+\. ", "", lines[i])); i += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>"); continue
        if ln.startswith(">"):
            q = []
            while i < len(lines) and lines[i].startswith(">"): q.append(lines[i].lstrip("> ")); i += 1
            out.append(f"<blockquote>{inline(' '.join(q))}</blockquote>"); continue
        if ln.startswith("### "): out.append(f"<h4>{inline(ln[4:])}</h4>"); i += 1; continue
        p = []
        while i < len(lines) and lines[i].strip() and not re.match(r"(\||>|#|\s*[-*] |\d+\. )", lines[i]): p.append(lines[i]); i += 1
        if p: out.append(f"<p>{inline(' '.join(p))}</p>")
        else: i += 1
    return "".join(out)

def front(text):
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S); fm = {}
    for ln in m.group(1).split("\n"):
        mm = re.match(r"(\w+):\s*(.*)", ln)
        if not mm: continue
        k, v = mm.groups()
        try: fm[k] = json.loads(v)
        except Exception: fm[k] = v.strip().strip('"')
    return fm, m.group(2)

def section_kind(h):
    h = h.lower()
    if h.strip() == "ads": return "ads"
    for k, w in [("trend", "how big"), ("trend", "and trend"), ("shelf", "who holds"), ("entry", "newcomer"), ("ads", "in ads"), ("reviews", "keep growing"),
                 ("creatives", "winners say"), ("sources", "sources"), ("sources", "methods and")]:
        if w in h: return k
    return "text"
def drop_for(kind):
    if kind == "shelf": return lambda hdr: any(x in " ".join(hdr) for x in ("Share", "Units/mo"))
    if kind == "ads": return lambda hdr: "Active" in hdr[0] and "Brand" not in " ".join(hdr)
    return None
FIX = [(r"\(one pull of three; pulls 2-3 pending\)", "(pull 1 of 3; the chart shows pulls 1-2)"),
       (r"pull 1 is in, 2-3 pending", "pulls 1-2 are in (2026-11-08 and 11-09), pull 3 is due 2026-11-10")]

# ---------- images ----------
def img(src, maxw=560):
    p = R / src
    if not p.exists(): return None
    name = p.stem + ".jpg"; dst = MED / name
    if not dst.exists():
        im = Image.open(p).convert("RGB"); im.thumbnail((maxw, maxw * 2)); im.save(dst, "JPEG", quality=74, optimize=True)
    return "media/" + name

# ---------- trends ----------
TP = sorted((R / "work/blind/trends_pulls").glob("pull*_*.txt"))
pulls = {f.stem: load(f) for f in TP}
latest = pulls[TP[-1].stem]; first = pulls[TP[0].stem]
TS = J(R / "work/blind/trends_series_summary.json")
last_day = dt.date.fromisoformat(TP[-1].stem.split("_")[1])
def series(term):
    v = latest.get(term) or first.get(term)
    return v
n0 = len(series("shampoo")); week0 = last_day - dt.timedelta(weeks=n0 - 1)

# ---------- reviews ----------
V2 = R / "work/reviews/v2"
def jm(f):
    d = J(V2 / f); wf = (d.get("all_window_from") or "9999")[:7]; out = {}
    for ym, m in d["monthly"].items():
        if m.get("est") is None: continue
        out[ym] = [round(m["est"]), not (m.get("all_exact") is not None and ym >= wf)]
    return out
def plain(f, key="all"): return {ym: [m[key], False] for ym, m in J(V2 / f)["monthly"].items()}
def product(f, name): return {ym: [dict(m["top_products"]).get(name), False] for ym, m in J(V2 / f)["monthly"].items() if dict(m["top_products"]).get(name)}
def photo(f): return {ym: [v, True] for ym, v in J(V2 / f)["photo_reviews_monthly_est"].items()}
OLD = J(R / "work/reviews/curves.json")
def old(k): return {ym: [v, False] for ym, v in OLD[k]}
REV = {
 "color_foundation": [("Prime Prometics · foundation only", product("primeprometics_stamped.json", "Color Changing Foundation")),
                      ("Smooche · photo reviews (est.)", photo("smooche_loox_photo.json"))],
 "body_oil": [("GODA · photo reviews (est.)", photo("goda_loox_photo.json")), ("DRMTLGY · whole store", jm("drmtlgy_judgeme.json"))],
 "scent_diffuser": [("Scentify", jm("scentify_judgeme.json")), ("Aura House · whole store", plain("aurahouse_okendo.json")),
                    ("Aura House · diffuser only", product("aurahouse_okendo.json", "Aura Scent Diffuser")), ("Aroma360", plain("aroma360_okendo.json"))],
 "tallow_balm": [("Ancestral", jm("ancestral_judgeme.json")), ("Terra Lotus", jm("terralotus_judgeme.json")),
                 ("Forge", jm("forge_judgeme.json")), ("Wild Gold", jm("wildgold_judgeme.json"))],
 "persimmon_soap": [("Mirai Clinical", plain("mirai_yotpo.json"))],
 "shower_filter": [("Sproos", plain("sproos_junip.json"))],
 "lash_serum": [("Borboleta", jm("borboleta_judgeme.json"))],
 "turmeric_soap": [("Earthly Derm · Turmeric bar", old("earthlyderm_turmeric"))],
 "compression_socks": [("Everstride · main product", old("everstride_main"))],
}
REV_NOTE = {
 "color_foundation": "Store reviews do not show the growth that search shows. **Prime Prometics**, the second-largest store brand: its foundation got 687 reviews in Aug-Oct 2026 vs 690 a year earlier, and has drifted from about 330 a month in spring to 199 in October. ◆ **Smooche**: photo reviews ran at 1,000-2,650 a month in Apr-Aug 2026 and then almost stopped in Sep-Oct; more likely a change in how the store asks for reviews than a sales collapse. ◇ Luxe's store feed has months-long gaps and is not used.\n\nReading: the growth in search is going to Amazon and to new brands, not to the incumbent stores. ◈",
 "body_oil": "**GODA**, the newcomer that broke through, shows it in its own store too: photo reviews in Aug-Oct 2026 are about five times the same months of 2025, and October 2026 is its best month in the sample. ◈ (photo reviews only, read from a 20% sample)\n\n**DRMTLGY**'s store-wide reviews fell to about a quarter of last year, but body oil is a small part of what it sells, so this says little about the category. ◇",
 "scent_diffuser": "Three stores, all up. **Scentify**: 245 reviews in Aug-Oct 2026 vs 123 a year earlier, ×2.0; October 2026 is its best month on record. ◆ **Aura House**: ×2.7 store-wide; the diffuser itself went from 26 reviews in Oct 2025 to 139 in Oct 2026. ◆ Its Aug-Sep 2026 show only about 20 a month, which looks like paused review requests. ◇ **Aroma360**: ×1.4, but October is lifted by a free-diffuser promotion; August-September alone were below last year. ◈\n\nTogether with search (×2.0), this is the best-confirmed growth of all 20 categories. ◈",
 "tallow_balm": "The leaders move in different directions. **Terra Lotus**, a new brand, ramped from about 40 reviews a month in spring 2026 to about 1,350 in August, then fell to 488 in September and 336 in October; 43% of its September reviews are below five stars (26% all-time). ◈ **Ancestral**, the older store leader, is flat year on year at 300-600 a month. ◈ **Forge** started collecting in June 2026 (93 in Aug-Oct). ◆ **Wild Gold** peaked in late 2025 and faded (9 vs 53). ◆\n\nThis matches flat search (×1.04): new brands still get in, but the market as a whole is not growing. ◈",
 "persimmon_soap": "**Mirai Clinical**, the store leader: 947 reviews in Aug-Oct 2026 vs 471 a year earlier, ×2.0, climbing steadily since early 2025. ◆ Kaori, the other leader, has no review widget we can read. The store curve agrees with the search growth. ◈",
 "shower_filter": "**Sproos**: 329 reviews in Aug-Oct 2026 vs 344 a year earlier, flat. ◆ Its peak was Jan-Apr 2026 (180-295 a month); since then reviews have shifted to refill cartridges sold by subscription, which means fewer new devices. ◈ Matches flat search (×1.09).",
 "lash_serum": "**Borboleta**'s store has 1,286 reviews in total and single-digit months lately: too small to read. ◇",
 "turmeric_soap": "**A counter-signal.** Earthly Derm's Turmeric Fade & Glow Bar: 2,553 reviews in Aug-Oct 2026 vs 334 a year earlier, about ×7.6, rising almost every month of 2026. ◆ Search for \"turmeric soap\" is falling (×0.67), and that is what dropped the category. One brand growing fast while generic search falls points to a brand-driven product rather than a category trend. Worth a second look before writing it off. ◈",
 "compression_socks": "**Everstride**, the largest store brand: 5,809 reviews on its main product in Aug-Oct 2026 vs 4,248 a year earlier, ×1.4, though October 2026 (1,376) is below October 2025 (1,724). ◆ A strong single brand in a category where new brands sell little on Amazon. ◈",
}
def months(a="2024-07", b="2026-10"):
    y, m = map(int, a.split("-")); out = []
    while f"{y}-{m:02d}" <= b: out.append(f"{y}-{m:02d}"); m += 1; y, m = (y + 1, 1) if m > 12 else (y, m)
    return out
MONTHS = months()
def growth(s):
    a = sum((s.get(f"2026-{m}") or [0])[0] or 0 for m in ("08", "09", "10")); b = sum((s.get(f"2025-{m}") or [0])[0] or 0 for m in ("08", "09", "10"))
    return round(a / b, 2) if b >= 30 else None  # under 30 reviews a year earlier: too small to compare (Borboleta)

# ---------- creatives ----------
ADS = {}
for f in ["work/ads/longrunning_v2.json", "work/ads/longrunning_v3a.json", "work/ads/longrunning_v3b.json"]:
    for b in J(R / f)["brands"]: ADS.setdefault(b["id"], []).append(b)
CFIX = J(R / "work/site/creatives_fix.json")
def creatives(pid):
    out, photo_ = [], None
    for b in ADS.get(pid, []):
        if b["domain"] in BAD_ADS or b["domain"] in BAD_ADS_CAT.get(pid, ()): continue
        stem = b["domain"].split(".")[0]
        if not photo_ and b["domain"] not in BAD_PHOTO and b.get("photos"): photo_ = img(b["photos"][0], 640)
        seen, n = set(), 0
        for a in sorted(b.get("ads", []), key=lambda a: -(a.get("days") or 0)):
            if stem not in (a.get("land") or "") or not a.get("imgLocal"): continue
            key = (a.get("body") or "")[:70] + (a.get("headline") or "")[:30]
            if key in seen: continue
            seen.add(key); src = img(a["imgLocal"])
            if not src or src in BAD_IMG: continue
            out.append({"img": src, "days": a.get("days"), "start": a.get("startISO"), "page": a.get("page"), "domain": b["domain"],
                        "head": (a.get("headline") or "").split(" · ")[0][:90], "body": re.sub(r"\s+", " ", a.get("body") or "")[:180],
                        "video": bool(a.get("video")), "lib": f"https://www.facebook.com/ads/library/?id={a['id']}"})
            n += 1
            if n >= 3: break
    # 2026-11-11: drop shown ads that Meta no longer runs, add replacements (work/site/creatives_fix.json, checked through Apify)
    out = [c for c in out if c["lib"].split("id=")[-1] not in CFIX["dead_ids"]] + CFIX["add"].get(pid, [])
    out.sort(key=lambda c: -(c["days"] or 0))
    return out[:6], photo_

# ---------- categories ----------
M22 = J(R / "work/audit/metrics_v23.json")
cats = []
for f in [p for p in sorted((D / "content").glob("[0-2][0-9]_*.md")) if not p.name.startswith("00")]:
    fm, body = front(f.read_text(encoding="utf-8"))
    for a, b in FIX: body = re.sub(a, b, body)
    pid = fm["id"]; d = J(D / "digest" / f"{pid}.json"); a = d.get("amazon_us", {}); m = d.get("meta_category", {})
    body = re.sub(r"^# .*\n", "", body.strip() + "\n", count=1)
    parts = re.split(r"^## (.+)$", body, flags=re.M)
    lead, secs = parts[0], []
    for h, t in zip(parts[1::2], parts[2::2]):
        k = section_kind(h)
        if k == "reviews" and pid in REV_NOTE: t = REV_NOTE[pid]
        secs.append({"h": re.sub(r"^\d+\.\s*", "", h).strip(), "kind": k, "html": md(t, drop_for(k))})
    ts = TS.get(pid, {}); term = TERM.get(pid)
    tr = {"term": term, "values": series(term), "mean": ts.get("rel_yoy_mean") or fm.get("trend_x"),
          "pulls": {k.split("_")[0]: v.get("rel_yoy") for k, v in ts.get("pulls", {}).items()}, "label": ts.get("label") or fm.get("trend_label"),
          "zeros": (list(ts.get("pulls", {}).values()) or [{}])[-1].get("zero_share_2y")}
    leaders = []
    for b in a.get("top_brands", [])[:8]:
        x = b.get("best", {})
        pr = float(re.sub(r"[^\d.]", "", x.get("price") or "") or 0) or None
        leaders.append({"name": x.get("amazon_brand") or b["key"], "units": b["units"], "listings": b.get("listings"), "status": b.get("status"),
                        "months": b.get("entry_months"), "price": pr, "stars": x.get("stars"), "asin": x.get("asin"), "title": x.get("title")})
    bp = []
    for name, v in (d.get("meta_brand_pages") or {}).items():
        s = {k: sum((p.get(k) or 0) for p in v.get("own", {}).values()) for k in ("active", "aged30", "aged90", "aged180")}
        bp.append({"name": name, **s, "pages": len(v.get("own", {})), "sample": v.get("phrase_sample"), "own_domain": v.get("own_domain")})
    cr, ph = creatives(pid)
    if pid in PHOTO_OVERRIDE: ph = PHOTO_OVERRIDE[pid] or ""
    rv = None
    if pid in REV:
        rv = {"series": [{"name": n, "pts": [[ym, *(s.get(ym) or [None, False])] for ym in MONTHS], "growth": growth(s)} for n, s in REV[pid]]}
    vr = d.get("verdict_row", {})
    cats.append({
        "pid": pid, "slug": pid.replace("_", "-"), "rank": fm.get("rank"), "status": fm.get("status"), "title": fm.get("title"), "short": SHORT[pid],
        "verdict": fm.get("verdict"), "channel": fm.get("best_channel"), "compliance": fm.get("compliance_flag") or vr.get("flag") or "",
        "price": fm.get("price_median_usd"), "p25p75": fm.get("price_p25_p75_usd"),
        "shelf": a.get("shelf_units") or fm.get("shelf_units_mo"), "nb": vr.get("nb", fm.get("new_brand_units_mo")), "gen": vr.get("gen"),
        "winB": vr.get("winB"), "winG": vr.get("winG"), "stores": vr.get("stores"), "stores90": vr.get("stores90"),
        "meta": {k: m.get(k) for k in ("phrase", "active", "aged30", "aged90", "aged180", "date")} if m else None,
        "kind": a.get("units_by_kind"), "age": a.get("units_by_brand_age"), "leaders": leaders, "brandPages": bp,
        "storesTop": d.get("meta_stores_top") or [], "trend": tr, "reviews": rv, "creatives": cr, "photo": (ph or None) if pid in PHOTO_OVERRIDE else (ph or (cr[0]["img"] if cr else None)),
        "lead": md(lead), "sections": secs, "m": M22.get(pid), "kill": vr.get("kill"), "note": vr.get("note"),
    })
    print(pid, "secs", [s["kind"] for s in secs], "cr", len(cr), "photo", bool(ph), "rev", bool(rv))

cats.sort(key=lambda c: c["rank"])
ifm, ibody = front((D / "content/00_index.md").read_text(encoding="utf-8"))
mfm, mbody = front((D / "content/99_methods.md").read_text(encoding="utf-8"))
for a_, b_ in FIX: mbody = re.sub(a_, b_, mbody)
mbody += """
## Store reviews: are the winners still growing
- **What:** each leader store's public review feed (Judge.me, Okendo, Yotpo, Stamped, Junip, Loox), counted per month back to mid-2024. A review is a share of orders, so growth in reviews tracks growth in orders. ◈
- **Exact or estimated:** Okendo, Yotpo, Stamped and Junip give every review with its date: exact. Judge.me gives the latest 1,000 exactly; older months are estimated from the 1-4 star reviews, which go further back, times the store's overall star mix (dashed on the charts). Loox hides dates; photo reviews carry their date in the image address, so for Loox stores we count photo reviews only, from a 20% sample (dashed).
- **Limits:** stores turn 3-10% of orders into reviews, so review counts can't be compared between stores, only month to month within one store. A store that changes how it asks for reviews breaks its own curve (Smooche, Aura House in Aug-Sep 2026). Some feeds hide low ratings (Stamped).
"""
msecs = [{"h": h.strip(), "html": md(t)} for h, t in zip(re.split(r"^## (.+)$", mbody, flags=re.M)[1::2], re.split(r"^## (.+)$", mbody, flags=re.M)[2::2])]
mlead = md(re.sub(r"^# .*\n", "", re.split(r"^## ", mbody, flags=re.M)[0].strip() + "\n"))
ilead = re.split(r"\*\*The answer:\*\*", re.sub(r"^# .*\n", "", ibody.strip()))[0]

ctl = {c: latest.get(c) or first.get(c) for c in CONTROLS}
DATA = {"built": dt.date.today().isoformat(), "week0": week0.isoformat(), "controls": ctl,
        "pulls": [f.stem for f in TP], "months": MONTHS, "cats": cats, "intro": md(ilead), "methods": {"lead": mlead, "secs": msecs}}
js = json.dumps(DATA, ensure_ascii=False, separators=(",", ":"))
tpl = (R / "work/site/template.html").read_text(encoding="utf-8")
(OUT / "v21_en.html").write_text(tpl.replace("/*__DATA__*/null", js), encoding="utf-8")  # previous English site, kept for reference
DATA["ru"] = J(R / "work/site/ru.json")
DATA["credraw"] = J(R / "work/audit/cred_check.json")  # numbers for "Насколько верить видео"
DATA["margin"] = J(R / "work/margin/margin.json")["cases"]  # money left per sale before ads (work/margin/margin.py)
DATA["groups"] = J(R / "work/site/groups_ru.json")  # go / watch / no, one-line reasons, young followers
DATA["story"] = J(R / "work/site/story_ru.json")  # home-page story blocks (make_story.py, site plan v2.5)
DATA["grave"] = J(R / "work/site/graveyard_ru.json")  # stopped advertisers per product, from BigSpy US tables (work/graveyard/make_graveyard.py)
js = json.dumps(DATA, ensure_ascii=False, separators=(",", ":"))
tpl = (R / "work/site/template_ru.html").read_text(encoding="utf-8")
(OUT / "index.html").write_text(tpl.replace("/*__DATA__*/null", js), encoding="utf-8")
print("site/index.html", round(len(js) / 1024), "KB data;", len(list(MED.glob("*.jpg"))), "images",
      round(sum(p.stat().st_size for p in MED.glob("*.jpg")) / 1e6, 1), "MB")
