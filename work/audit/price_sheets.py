"""Price history sheets (2026-11-09): for each category, the 10 best-selling on-target listings from our saved Amazon scan;
Keepa's public price-history chart (graph.keepa.com, 365 days, Buy Box + new) per listing, tiled into one sheet.
No Amazon access: ASINs come from our saved scan, charts from Keepa."""
import json, sys, io, time, urllib.request
from PIL import Image, ImageDraw
sys.path.insert(0, "."); import graveyard_stats2 as g
UA = {"User-Agent": "Mozilla/5.0"}
for pid in sys.argv[1:]:
    L = {a: x for a, x in json.load(open(f"graveyard_us/{pid}.json", encoding="utf-8"))["listings"].items() if g.on_target(pid, x["title"])}
    top = sorted(L.items(), key=lambda kv: -kv[1]["b"])[:10]
    sheet = Image.new("RGB", (1000, 5 * 230), "white"); d = ImageDraw.Draw(sheet); meta = []
    for i, (a, x) in enumerate(top):
        try:
            png = urllib.request.urlopen(urllib.request.Request(f"https://graph.keepa.com/pricehistory.png?asin={a}&domain=com&range=365&used=0&bb=1", headers=UA), timeout=30).read()
            im = Image.open(io.BytesIO(png)).convert("RGB")
        except Exception as e:
            im = Image.new("RGB", (500, 200), "#eee")
        X, Y = (i % 2) * 500, (i // 2) * 230
        k = g.norm(x["brand"]) or g.title_brand(x["title"]) or "(no brand)"
        d.text((X + 4, Y + 2), f"#{i+1} {k[:18]} | {x['b']:,}/mo | scan {x['price']} | ASIN age {g.age_m(a, x):.0f} mo", fill="black")
        sheet.paste(im, (X, Y + 16)); meta.append({"asin": a, "brand": k, "units": x["b"], "price_scan": x["price"], "asin_age_m": round(g.age_m(a, x))})
        time.sleep(0.5)
    sheet.save(f"../audit/prices/{pid}.png"); json.dump(meta, open(f"../audit/prices/{pid}.json", "w"), indent=1)
    print(pid, "ok")
