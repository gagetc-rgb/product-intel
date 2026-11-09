"""Public Judge.me store profile (judge.me/reviews/stores/<shop>.myshopify.com?format=json, no token):
total reviews, verified reviews, collecting since, country. Plus Wayback captures of the same profile page
for past review counts. Output cohort/judgeme.json (2026-11-07)."""
import json, re, ssl, pathlib, urllib.request
HERE = pathlib.Path(__file__).parent
facts = json.loads((HERE / "site_facts.json").read_text(encoding="utf-8"))
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36"}
def get(u, t=40):
    try: return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=t).read().decode("utf-8", "ignore")
    except Exception: return ""
out = {}
for k, f in facts.items():
    shop = f.get("myshopify")
    if not shop: continue
    b = get(f"https://judge.me/reviews/stores/{shop}.myshopify.com?format=json")
    try: s = json.loads(b)["shop_data"]
    except Exception: continue
    o = {"name": s.get("name"), "slug": s.get("shop_slug"), "reviews": s.get("number_of_reviews"), "verified": s.get("verified_published_reviews"),
         "since": (s.get("features") or {}).get("collected_reviews_since", "")[:10], "country": s.get("country"), "products": s.get("products_count")}
    # Wayback: past captures of the profile page -> review count then
    cdx = get(f"https://web.archive.org/cdx/search/cdx?url=judge.me/reviews/stores/{o['slug']}&fl=timestamp&filter=statuscode:200&collapse=timestamp:6", 60)
    pts = []
    for ts in cdx.split()[-12:]:
        h = get(f"https://web.archive.org/web/{ts}id_/https://judge.me/reviews/stores/{o['slug']}", 60)
        m = re.search(r"([\d,]+)\s+reviews", h)
        if m: pts.append((ts[:8], int(m.group(1).replace(",", ""))))
    o["wayback"] = pts
    out[k] = o
    print(k[:28].ljust(28), o["name"], o["reviews"], o["verified"], o["since"], o["country"], pts, flush=True)
(HERE / "judgeme.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
