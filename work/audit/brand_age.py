"""Business age of every brand counted as NEW on Amazon (2026-11-09).
For each brand: find its own site (known domain, else guessed names verified by the brand name on the homepage),
then the earliest Wayback Machine capture whose page title/text contains the brand name (domain age alone can belong to
a previous owner), plus the domain registration date (RDAP). Output brand_age.json."""
import json, re, sys, time, urllib.request, concurrent.futures as cf
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/131.0"}
KNOWN = {"luxe": "luxe.com", "smooche": "smooche.com", "prime": "primeprometics.com", "goda": "goda.co", "terra": "terralotus.shop",
         "kaori": "try-kaori.com", "earthly": "earthlyderm.com", "vuehydrocolloi": "vueswiss.com", "airscent": "airscent.com",
         "maree": "maree.com", "eight": "eightsaints.com", "pelican": "pelican-soap.co.jp", "gisou": "gisou.com", "ogxprogrowth": "ogxbeauty.com",
         "aussie": "aussie.com", "foltene": "foltene.com", "cliganic": "cliganic.com", "lilyeve": "lilyeve.com", "nuna": None}
def get(u, n=60000):
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=25)
        return r.status, r.read(n).decode("utf-8", "ignore")
    except Exception as e: return 0, ""
def words(row):
    t = row["title"].split("|", 1)[-1].strip()
    w = re.findall(r"[A-Za-z0-9&']+", t)[:3]
    return w
def names(row):
    k = row["key"]; w = [x.lower().replace("'", "") for x in words(row)]
    c = {k}
    if len(w) >= 2: c |= {w[0] + w[1], w[0] + "-" + w[1], w[0] + w[1].replace("&", "and")}
    if len(w) >= 3 and w[1] in ("&", "and"): c |= {w[0] + "and" + w[2], w[0] + w[2]}
    return [x for x in c if x and len(x) >= 3]
def has_brand(html, row):
    k = row["key"][:6].lower(); w0 = words(row)[0].lower() if words(row) else k
    t = html.lower()
    return (k in t) or (len(w0) >= 4 and w0 in t)
def find_site(row):
    k = row["key"]
    if k in KNOWN: return KNOWN[k]
    for n in names(row):
        for d in (f"{n}.com", f"{n}.co", f"try{n}.com", f"shop{n}.com", f"get{n}.com", f"{n}skin.com", f"{n}beauty.com", f"the{n}.com", f"{n}.shop", f"{n}store.com"):
            s, h = get("https://" + d, 30000)
            if s == 200 and has_brand(re.sub(r"(?s)<script.*?</script>", "", h)[:30000], row):
                tl = re.search(r"(?is)<title>(.*?)</title>", h)
                if tl and has_brand(tl.group(1), row): return d
    return None
def rdap(d):
    tld = d.rsplit(".", 1)[-1]
    url = {"com": f"https://rdap.verisign.com/com/v1/domain/{d}", "co": f"https://rdap.nic.co/domain/{d}"}.get(tld, f"https://rdap.org/domain/{d}")
    s, h = get(url, 200000)
    try:
        for e in json.loads(h).get("events", []):
            if e.get("eventAction") == "registration": return e["eventDate"][:10]
    except Exception: pass
    return None
def wayback(d, row):
    s, h = get(f"https://web.archive.org/cdx/search/cdx?url={d}&output=json&fl=timestamp&filter=statuscode:200&collapse=timestamp:6&limit=400", 400000)
    try: ts = [x[0] for x in json.loads(h)[1:]]
    except Exception: return None, None
    if not ts: return None, None
    first = ts[0]
    # walk forward one capture per year until the brand name appears in the archived page
    seen_years = []
    for t in ts:
        if t[:4] in seen_years: continue
        seen_years.append(t[:4])
        s, page = get(f"https://web.archive.org/web/{t}id_/http://{d}/", 60000)
        if page and has_brand(page, row): return first[:8], t[:8]
        if len(seen_years) >= 8: break
        time.sleep(1)
    return first[:8], None
def work(row):
    d = find_site(row); out = dict(row, site=d)
    if d:
        out["domain_registered"] = rdap(d)
        out["wayback_first"], out["wayback_brand_first"] = wayback(d, row)
    return out
rows = json.load(open("new_brands.json", encoding="utf-8"))
with cf.ThreadPoolExecutor(6) as ex: res = list(ex.map(work, rows))
json.dump(res, open("brand_age.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
for r in res: print(f"{r['pid'][:12]:12} {r['key'][:12]:12} {r['units']:>7,} amz {r['amz_months']:>4.0f}m | {r.get('site') or '-':26} reg {r.get('domain_registered') or '-':10} wb {r.get('wayback_first') or '-':8} brand {r.get('wayback_brand_first') or '-'}")
