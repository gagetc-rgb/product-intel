"""Newcomer share of a category, v2 (2026-11-07). Search-card data only (no product pages needed).

Why v2: the v1 pilot mixed in other product forms (oral magnesium, net sponges, disposable face towels)
and grouped brands by the first two title words because most product pages had failed to load.

Per category (pre-registered form in graveyard_def.STRICT):
  listing entry date = Date First Available if known, else estimated from the ASIN (graveyard_stats calibration)
  brand = byline if known, else the first title word if it is not a generic product word, else unknown
  brand entry = its oldest on-target listing in the sample; unknown-brand listings stand alone
  NEW = brand (or stand-alone listing) entered < 24 months ago
Outputs: shelf units, share of units held by NEW, count of NEW winners (>=1K/mo) and NEW with >=100/mo,
and survival among listings that entered 6-24 months ago (window = the 5 visible pages, so an upper bound).
"""
import json, re, sys, io, contextlib, pathlib
from graveyard_def import on_target
HERE = pathlib.Path(__file__).parent
src = (HERE / "graveyard_stats.py").read_text(encoding="utf-8").split("out = {}")[0]
with contextlib.redirect_stdout(io.StringIO()):
    exec(src)  # gives est(), age_m(), TODAY, D

GEN = set("""a an the and & for with of to in on by new natural organic pure premium original authentic best extra deep
magnesium oil spray topical turmeric kojic acid soap bar bars face body exfoliating exfoliate exfoliation exfoliator japanese korean
asian african towel towels washcloth washcloths wash cloth cloths shower bath scrub scrubber nylon long back handmade
lemon honey dark spot spots remover brightening skin care set kit pack pcs piece pieces count ct pc x xl large
ultra super deluxe luxury dual textured beauty men women unisex usp grade highly concentrated zechstein dead sea salt
beef tallow grass fed whipped balm cream color colour changing foundation stick waterless diffuser cold air scent filtered filter
handheld high pressure rainfall persimmon odor hair growth rosemary oils serum stainless steel large small mini dog cat pet water
cordless wireless automatic smart old people aging firming anti silk glow crepey neck chin v line double lifting mask strap
nose pore patches patch hydrocolloid teeth tooth whitening powder compression socks sock hotel home room essential""".split())
# v2.1 (2026-11-08): ingredient words that were read as brands
GEN |= set("retinol retinal pdrn collagen nad peptide peptides hyaluronic tighten tightening".split())
# v2.1 (2026-11-08, before reading the 4 manually collected categories in full): their product words
GEN |= set("lash lashes eyelash eyelashes eyebrow eyebrows brow brows castor biotin rice batana scalp shampoo wash pre prewash teeth tooth".split())

import unicodedata
def _fold(t):  # v2.1: 'L'Oréal' -> 'l'oreal' (accents split brand names into fake brands)
    return ''.join(c for c in unicodedata.normalize('NFKD', t) if not unicodedata.combining(c))

def _key(w):  # 'dr teal's' -> 'drteal', 'valitic' -> 'valitic'
    w = [x for x in w if x]
    if not w: return None
    return (w[0] + w[1]) if len(w[0]) <= 3 and len(w) > 1 else w[0]

def title_brand(t):
    w = re.findall(r"[a-z0-9]+", _fold(t).lower().replace("'s", ""))
    if w and w[0] == "the": w = w[1:]  # v2.1: 'The AirScent ...' -> airscent
    if not w or w[0] in GEN or re.fullmatch(r"[\d.]+[a-z]*", w[0]): return None
    return _key(w)

def norm(b):
    if not b or b.strip().lower() in ("generic", "unbranded"): return None
    return _key(re.findall(r"[a-z0-9]+", _fold(b).lower().replace("'s", "")))

def analyse(pid, L):
    L = {a: x for a, x in L.items() if on_target(pid, x["title"])}
    ent = {}
    for a, x in L.items():
        k = norm(x["brand"]) or title_brand(x["title"]) or ("solo:" + a)
        x["_k"] = k; x["_age"] = age_m(a, x)
        ent[k] = max(ent.get(k, 0), x["_age"])
    units = sum(x["b"] for x in L.values()) or 1
    new = [x for x in L.values() if ent[x["_k"]] < 24]
    newk = {x["_k"] for x in new}
    win = {x["_k"] for x in new if x["b"] >= 1000}
    w100 = {x["_k"] for x in new if x["b"] >= 100}
    coh = [x for x in L.values() if 6 <= x["_age"] < 24 and ent[x["_k"]] < 24]
    return dict(listings=len(L), units=units, entities=len(ent),
                new_entities=len(newk), new_share=round(sum(x["b"] for x in new) / units, 3),
                new_win1k=len(win), new_win100=len(w100),
                coh=len(coh), coh_s100=sum(x["b"] >= 100 for x in coh), coh_s1k=sum(x["b"] >= 1000 for x in coh),
                known_brand=round(sum(1 for x in L.values() if not x["_k"].startswith("solo:")) / max(1, len(L)), 2),
                top_new=sorted(((x["b"], x["_k"], round(x["_age"])) for x in new), reverse=True)[:5])

if __name__ == "__main__":
    pids = sys.argv[1:] or [f.stem for f in sorted(D.glob("*.json")) if f.stem not in ("survival", "survival2")]
    out = {}
    for pid in pids:
        f = D / f"{pid}.json"
        if not f.exists(): continue
        r = analyse(pid, json.loads(f.read_text(encoding="utf-8"))["listings"]); out[pid] = r
        print(f"{pid:20} lst {r['listings']:>3} units {r['units']:>7,} ent {r['entities']:>3} | NEW: ent {r['new_entities']:>3} "
              f"share {r['new_share']:>5.0%} win1K {r['new_win1k']:>2} win100 {r['new_win100']:>3} | 6-24mo lst {r['coh']:>3} "
              f">=100 {r['coh_s100']:>3} >=1K {r['coh_s1k']:>2} | brand known {r['known_brand']:.0%}")
        print("    top NEW:", r["top_new"])
    (D / "survival2.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
