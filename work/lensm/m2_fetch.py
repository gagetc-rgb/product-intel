"""Lens M step 2: fetch public facts per candidate domain (products.json or home page, RDAP, Wayback CDX). Paced per host >=2s."""
import json, re, time, threading, urllib.request, urllib.error, pathlib, sys, concurrent.futures as cf
R = pathlib.Path(__file__).parent; RAW = R / "raw"
cand = json.load(open(R / "m2_candidates.json", encoding="utf-8"))
CATS = "persimmon_soap turmeric_soap body_oil color_foundation tallow_balm lash_serum shower_filter scent_diffuser hair_serum compression_socks chin_wrap dog_fountain hair_removal_cream neck_cream rosemary_oil magnesium_spray exfoliating_towel".split()
UA = "Mozilla/5.0 (research; public pages only)"
lk = threading.Lock(); last = {}
def get(url, timeout=25):
    host = re.sub(r"^https?://([^/]+).*", r"\1", url)
    with lk:
        w = max(0, last.get(host, 0) + 2.1 - time.time()); last[host] = time.time() + w
    time.sleep(w)
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US"}), timeout=timeout)
        return r.status, r.geturl(), r.read(3_000_000).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, url, ""
    except Exception as e:
        return -1, url, str(e)[:100]
def one(dom, hosts):
    out = {"domain": dom, "hosts": hosts}
    s, u, b = get(f"https://{dom}/products.json?limit=250")
    out["pj_status"] = s; out["pj_final"] = u
    try:
        j = json.loads(b); ps = j["products"]
        out["products"] = [{"t": p["title"], "pr": (p["variants"][0]["price"] if p.get("variants") else None), "c": p.get("created_at", "")[:10], "type": p.get("product_type", "")} for p in ps]
    except Exception:
        out["products"] = None
        host = next((h for h in hosts if not h.startswith("www.")), hosts[0]) if hosts else dom
        s2, u2, h = get(f"https://{host}/")
        out["home_status"] = s2; out["home_final"] = u2
        t = re.search(r"<title[^>]*>(.*?)</title>", h, re.S | re.I)
        out["home_title"] = re.sub(r"\s+", " ", t.group(1)).strip()[:200] if t else None
        d = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)', h, re.I)
        out["home_desc"] = d.group(1)[:300] if d else None
        txt = re.sub(r"<script.*?</script>|<style.*?</style>", " ", h, flags=re.S | re.I); txt = re.sub(r"<[^>]+>", " ", txt)
        out["home_text"] = re.sub(r"\s+", " ", txt)[:700]
        out["home_prices"] = list(dict.fromkeys(re.findall(r"\$\s?\d+(?:\.\d\d)?", h)))[:8]
        out["captcha"] = bool(re.search(r"captcha|cf-chl|Just a moment|Attention Required", h, re.I)) and len(h) < 20000
    s3, u3, b3 = get(f"https://rdap.org/domain/{dom}")
    out["rdap_status"] = s3
    try:
        ev = json.loads(b3).get("events", []); out["rdap_reg"] = next((e["eventDate"][:10] for e in ev if e["eventAction"] == "registration"), None)
    except Exception: out["rdap_reg"] = None
    s4, u4, b4 = get(f"http://web.archive.org/cdx/search/cdx?url={dom}&limit=1&fl=timestamp")
    out["wb_status"] = s4; out["wb_first"] = (b4.strip()[:8] or "none") if s4 == 200 else None
    return out
if __name__ == "__main__":
    jobs = {}
    for c in CATS:
        for s in cand[c]["stores"]:
            if s["max_age"] >= 90 or s["max_age"] < 30: jobs[s["domain"]] = s["hosts"]
    print(len(jobs), "domains"); res = {}
    def run(k):
        f = RAW / f"{k}.json"
        if f.exists(): return json.load(open(f, encoding="utf-8"))
        o = one(k, jobs[k]); f.write_text(json.dumps(o, ensure_ascii=False), encoding="utf-8"); return o
    with cf.ThreadPoolExecutor(6) as ex:
        for k, o in zip(jobs, ex.map(run, jobs)): print(k, o["pj_status"], o["rdap_reg"], o["wb_first"], flush=True)
