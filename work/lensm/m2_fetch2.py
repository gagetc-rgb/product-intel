"""Second page per store: /collections/all (Shopify HTML) -> product link slugs, first prices. One extra request per store."""
import json, re, glob, concurrent.futures as cf, pathlib
from m2_fetch import get, RAW
NOISE = {"sephora.com","google.com","whatsapp.com","magnolia.com","bombas.com","valspar.com","trendhunter.com","drteals.com","hiyahealth.com","petkit.com","pacas.com","irestorelaser.com","everymarket.com","alltimeairconditioning.com","propondandlakes.com"}
def run(f):
    o = json.load(open(f, encoding="utf-8"))
    if o["products"] is not None or o.get("home_status") != 200 or o["domain"] in NOISE or "c2" in o: return
    host = next((h for h in o["hosts"] if not h.startswith(("www.", "offer.", "quiz.", "lp.", "redir.", "analytics.", "promotion.", "get.", "try.", "api."))), o["domain"])
    s, u, h = get(f"https://{host}/collections/all")
    c2 = {"status": s}
    if s == 200:
        slugs = list(dict.fromkeys(re.findall(r'/products/([a-z0-9][a-z0-9\-_%]+)', h)))[:25]
        c2["slugs"] = slugs; c2["prices"] = list(dict.fromkeys(re.findall(r"\$\s?\d+(?:\.\d\d)?", h)))[:10]
        c2["captcha"] = bool(re.search(r"captcha|cf-chl|Just a moment", h, re.I)) and len(h) < 20000
    o["c2"] = c2; open(f, "w", encoding="utf-8").write(json.dumps(o, ensure_ascii=False))
fs = glob.glob(str(RAW / "*.json"))
with cf.ThreadPoolExecutor(6) as ex: list(ex.map(run, fs))
print("done")
