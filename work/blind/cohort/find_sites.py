"""Guess each named cohort brand's own website (2026-11-07).
Candidates: <name>.com/.co/.shop, get/shop/try<name>.com, <name>skincare/naturals/beauty/wellness.com.
Accept if the homepage loads and its HTML mentions the brand name. Output cohort/sites_guess.json."""
import json, re, pathlib, concurrent.futures as cf, urllib.request, ssl
HERE = pathlib.Path(__file__).parent
rows = json.loads((HERE / "brands.json").read_text(encoding="utf-8"))
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36"}
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
def base(r):
    n = (r["byline"] or "" if not r["key"].startswith("solo:") else "")
    n = re.sub(r"[^a-z0-9 ]", "", n.lower()).strip()
    if not n and not r["key"].startswith("solo:"): n = r["key"]
    return n
def cands(n):
    j = n.replace(" ", ""); out = []
    for d in [j, "get" + j, "shop" + j, "try" + j, j + "skincare", j + "naturals", j + "beauty", j + "wellness", j + "shop", j + "store"]:
        out += [d + ".com"]
    out += [j + ".co", j + ".shop", j + ".us"]
    return out
def check(dom, n):
    try:
        req = urllib.request.Request("https://" + dom, headers=UA)
        h = urllib.request.urlopen(req, timeout=12, context=ctx).read(400000).decode("utf-8", "ignore").lower()
        first = n.split()[0]
        if first in h and not re.search(r"domain (is )?for sale|buy this domain|parked|godaddy|hugedomains|dan\.com", h):
            shop = "shopify" if "cdn.shopify.com" in h else ("woocommerce" if "woocommerce" in h else "")
            widgets = [w for w in ["loox", "judge.me", "okendo", "yotpo", "stamped", "junip", "reviews.io", "trustpilot"] if w in h]
            title = (re.search(r"<title[^>]*>(.*?)</title>", h, re.S) or [None, ""])[1].strip()[:80]
            return {"domain": dom, "platform": shop, "widgets": widgets, "title": title}
    except Exception:
        return None
res = {}
jobs = {}
with cf.ThreadPoolExecutor(24) as ex:
    for r in rows:
        n = base(r)
        if not n or len(n) < 3 or n in ("generic",): continue
        for d in cands(n): jobs[ex.submit(check, d, n)] = (r["cat"], r["key"], d)
    for f in cf.as_completed(jobs):
        k = jobs[f][:2]; v = f.result()
        if v: res.setdefault("|".join(k), []).append(v)
(HERE / "sites_guess.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
named = [r for r in rows if base(r) and base(r) != "generic"]
print("named brands:", len(named), "with a guessed site:", len(res))
for k, v in sorted(res.items()): print(k.encode("ascii","replace").decode(), [(x["domain"], x["platform"], x["widgets"], x["title"][:40].encode("ascii","replace").decode()) for x in v])
