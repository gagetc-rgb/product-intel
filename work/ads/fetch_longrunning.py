"""Pull long-running US Meta ads for each shortlisted brand (public, logged-off Ad Library).

Usage: python work/ads/fetch_longrunning.py [days=180]
Output: work/ads/longrunning.json + preview images in dashboard/ads_media/
Ads are sorted by Meta by total impressions; we keep what the library loads (top ~30-60 per query).
"""
import json, sys, time, hashlib, pathlib, datetime as dt
import requests
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[2]
MEDIA = ROOT / "dashboard" / "ads_media"
OUT = ROOT / "work" / "ads" / "longrunning.json"
MEDIA.mkdir(parents=True, exist_ok=True)

BRANDS = [  # product id (matches dashboard/data.json), landing domain, Shopify handle of the hero product, min ad age override
    ("turmeric", "earthlyderm.com", "turmeric-glow-soap", None),
    ("socks", "everstridesocks.com", "originals", None),
    ("persimmon", "try-kaori.com", "deodorizing-persimmon-soap", None),
    ("boxers", "menvault.com", "mens-all-day-protection-boxer-briefs-2-new", None),
    ("duffel", "luhxe.com", "luhxe-travel-bag-2-0", 60),  # Luhxe rotates ads fast: no ads live 180+ days
]
ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
# B5 (2026-11-08): --brands=<file> with lines 'id|domain|handle-or-/regex/|days' and --out=<json> (keeps longrunning.json intact)
_bf = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--brands=")), None)
if _bf:
    def _row(l):  # id|domain|handle-or-/regex/ (may contain '|')|days
        i, d, rest = l.split("|", 2); h, n = rest.rsplit("|", 1)
        return (i, d, h or None, int(n) if n.strip() else None)
    BRANDS = [_row(l) for l in pathlib.Path(_bf).read_text(encoding="utf-8").splitlines() if l.strip()]
    OUT = pathlib.Path(next(a.split("=", 1)[1] for a in sys.argv if a.startswith("--out=")))
LOGIN = "--login" in sys.argv  # use a saved, logged-in Facebook profile (loads far more than ~30 ads)
PROFILE = ROOT / "work" / "ads" / ".fb-profile"  # holds the session cookies; do not share
DAYS = int(ARGS[0]) if ARGS else 180
TODAY = dt.date.today()
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"

EXTRACT = r"""
() => {
  const spans=[...document.querySelectorAll('span')].filter(s=>/^Library ID: \d+$/.test(s.textContent.trim()));
  return spans.map(s=>{ let el=s; for(let i=0;i<8;i++) el=el.parentElement;
    const t=el.innerText, id=s.textContent.match(/\d+/)[0];
    const start=(t.match(/Started running on ([^\n]+)/)||[])[1]||'';
    const multi=(t.match(/(\d+) ads? use this creative and text/)||[])[1]||null;
    const imgs=[...el.querySelectorAll('img')];
    const avatar=imgs.find(i=>i.width<=60 && i.height<=60);
    const media=imgs.filter(i=>i!==avatar && (i.naturalWidth>100||i.width>100)).map(i=>i.src);
    const vids=[...el.querySelectorAll('video')];
    const lines=t.split('\n').map(x=>x.trim()).filter(x=>x && x!=='\u200b');
    const si=lines.indexOf('Sponsored');
    let land='';
    for(const a of el.querySelectorAll('a[href]')){ try{ const u=new URL(a.href);
      if(u.hostname==='l.facebook.com'){ land=u.searchParams.get('u')||''; break; }
      if(!u.hostname.endsWith('facebook.com')){ land=a.href; break; } }catch(e){} }
    const capIdx=lines.findIndex((x,i)=>i>si && /^[A-Z0-9.-]+\.[A-Z]{2,}$/.test(x));
    const body=lines.slice(si+1, capIdx>0?capIdx:lines.length).filter(x=>!/^\d+:\d+ \/ \d+:\d+$/.test(x)).join('\n');
    const after=capIdx>0?lines.slice(capIdx+1):[];
    return {id,start,multi,page:si>0?lines[si-1]:'',avatar:avatar?avatar.src:'',img:media[0]||'',
      poster:vids[0]?vids[0].poster:'',video:vids.length>0,carousel:media.length>1,land,
      headline:after.slice(0,-1).join(' · ').slice(0,160),cta:after[after.length-1]||'',body:body.slice(0,1500)};
  });
}"""


def save_img(url, key):
    if not url:
        return ""
    name = hashlib.md5(key.encode()).hexdigest()[:16] + ".jpg"
    p = MEDIA / name
    if not p.exists():
        r = requests.get(url, headers={"User-Agent": UA}, timeout=30)
        if r.status_code != 200 or not r.content:
            return ""
        p.write_bytes(r.content)
    return "dashboard/ads_media/" + name


def product_photos(domain, handle, n=4):
    """First n photos of the hero product from the Shopify store (/products/<handle>.json)."""
    if handle and handle.startswith("/"):  # regex: pick the first store product whose title matches
        try:
            import re
            ps = requests.get(f"https://{domain}/products.json?limit=250", headers={"User-Agent": UA}, timeout=30).json()["products"]
            hit = next((x for x in ps if re.search(handle.strip("/"), x["title"], re.I)), None)
            if hit:
                return [i["src"] for i in hit["images"][:n]], hit["title"], f"https://{domain}/products/{hit['handle']}"
        except Exception:
            pass
        return [], "", f"https://{domain}"
    url = f"https://{domain}/products/{handle}"
    try:
        p = requests.get(url + ".json", headers={"User-Agent": UA}, timeout=30).json()["product"]
        return [i["src"] for i in p["images"][:n]], p["title"], url
    except Exception:
        return [], "", url


def parse_date(s):
    for fmt in ("%d %b %Y", "%b %d, %Y"):
        try:
            return dt.datetime.strptime(s.strip(), fmt).date()
        except ValueError:
            pass
    return None


def main():
    result = {"generated": TODAY.isoformat(), "minDays": DAYS, "brands": []}
    with sync_playwright() as pw:
        if LOGIN:
            br = pw.chromium.launch_persistent_context(str(PROFILE), headless=False, viewport={"width": 1280, "height": 900}, locale="en-US")
            page = br.pages[0] if br.pages else br.new_page()
            if not any(c["name"] == "c_user" for c in br.cookies("https://www.facebook.com")):
                page.goto("https://www.facebook.com/login")
                print("WAITING: log in to Facebook in the opened window (15 min max)", flush=True)
                for _ in range(180):
                    if any(c["name"] == "c_user" for c in br.cookies("https://www.facebook.com")):
                        break
                    page.wait_for_timeout(5000)
                else:
                    raise SystemExit("no login within 15 min")
            print("logged in", flush=True)
        else:
            br = pw.chromium.launch(headless=True)
            page = br.new_page(user_agent=UA, viewport={"width": 1280, "height": 900}, locale="en-US")
        for pid, domain, handle, days in BRANDS:
            cutoff = TODAY - dt.timedelta(days=days or DAYS)
            url = ("https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US"
                   f"&q={domain}&search_type=keyword_unordered&start_date[max]={cutoff.isoformat()}")
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(6000)
            total = page.evaluate(r"(document.body.innerText.match(/~?([\d,]+) results?/)||[])[1]||null")
            prev, same = -1, 0
            for _ in range(80 if LOGIN else 25):
                page.mouse.wheel(0, 20000)
                more = page.get_by_text("See more", exact=True)
                if more.count():
                    try:
                        more.last.click(timeout=3000)
                    except Exception:
                        pass
                page.wait_for_timeout(2500)
                n = page.locator("text=/^Library ID: \\d+$/").count()
                same = same + 1 if n == prev else 0
                prev = n
                if same >= 3:
                    break
            ads = page.evaluate(EXTRACT)
            seen, kept = set(), []
            for a in ads:
                if a["id"] in seen:
                    continue
                seen.add(a["id"])
                d = parse_date(a["start"])
                a["startISO"] = d.isoformat() if d else ""
                a["days"] = (TODAY - d).days if d else None
                a["imgLocal"] = save_img(a["img"] or a["poster"], a["id"])
                a["avatarLocal"] = save_img(a["avatar"], "avatar-" + a["page"])
                for k in ("img", "poster", "avatar"):
                    a.pop(k)
                kept.append(a)
            photos, title, purl = product_photos(domain, handle)
            result["brands"].append({"id": pid, "domain": domain, "minDays": days or DAYS, "total": total,
                                     "loaded": len(kept), "photos": [save_img(u, u.split("?")[0]) for u in photos],
                                     "productTitle": title, "productUrl": purl, "ads": kept})
            print(f"{domain}: total={total} loaded={len(kept)} photos={len(photos)}", flush=True)
        br.close()
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    print("saved", OUT)


if __name__ == "__main__":
    main()
