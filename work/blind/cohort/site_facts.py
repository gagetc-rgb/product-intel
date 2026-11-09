"""For each brand site: domain registration date (RDAP), first Wayback capture, store platform,
review widgets on the homepage, Trustpilot page. Output cohort/site_facts.json (2026-11-07)."""
import json, re, ssl, pathlib, urllib.request, concurrent.futures as cf
HERE = pathlib.Path(__file__).parent
sites = {k: v for k, v in json.loads((HERE / "sites.json").read_text(encoding="utf-8")).items() if not k.startswith("_") and v}
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36"}
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
def get(url, n=600000, t=25):
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=t, context=ctx)
        return r.status, r.read(n).decode("utf-8", "ignore")
    except urllib.error.HTTPError as e: return e.code, ""
    except Exception as e: return None, str(e)[:80]
def facts(dom):
    o = {"domain": dom}
    s, b = get(f"https://rdap.org/domain/{dom}")
    if s == 200:
        ev = {e.get("eventAction"): e.get("eventDate", "")[:10] for e in json.loads(b).get("events", [])}
        o["registered"] = ev.get("registration")
    s, b = get(f"https://web.archive.org/cdx/search/cdx?url={dom}&limit=1&fl=timestamp&filter=statuscode:200", t=40)
    o["wayback_first"] = b.strip()[:8] if s == 200 and b.strip() else None
    s, h = get(f"https://{dom}")
    hl = h.lower()
    o["home_status"] = s
    o["platform"] = "shopify" if "cdn.shopify.com" in hl or "shopify" in hl[:200000] and "myshopify" in hl else ("woocommerce" if "woocommerce" in hl else "")
    o["widgets"] = [w for w in ["loox", "judge.me", "okendo", "yotpo", "stamped", "junip", "reviews.io", "trustpilot", "opinew", "fera"] if w in hl]
    o["myshopify"] = (re.search(r"([a-z0-9-]+)\.myshopify\.com", hl) or [None, None])[1]
    s, b = get(f"https://www.trustpilot.com/review/{dom}", n=300000)
    m = re.search(r'"numberOfReviews"\s*:\s*\{?[^0-9]*(\d+)', b) or re.search(r"([\d,]+)\s+(?:total\s+)?reviews", b)
    o["trustpilot"] = {"status": s, "reviews": m.group(1) if m else None}
    return o
with cf.ThreadPoolExecutor(8) as ex:
    res = dict(zip(sites, ex.map(facts, sites.values())))
(HERE / "site_facts.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
for k, o in res.items():
    print(k[:28].ljust(28), o["domain"][:24].ljust(24), o.get("registered"), o["wayback_first"], o["home_status"], o["platform"], o["widgets"], o["myshopify"], o["trustpilot"])
