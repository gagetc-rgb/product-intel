"""Step C fetcher. usage: rp_fetch.py <prod> '<product regex>' [--epa]  -> stepc_<prod>/<domain>.json, raw/<domain>*.html (new files only)"""
import sys, re, json, time, html, pathlib, requests, csv
from rp_lib import *
prod, KW = sys.argv[1], re.compile(sys.argv[2], re.I)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"
H = {"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9", "Accept": "text/html,application/xhtml+xml"}
OD = RP / f"stepc_{prod}"; OD.mkdir(exist_ok=True); RAW = RP / "raw"; RAW.mkdir(exist_ok=True)
SUB = re.compile(r"[^.<>]{0,60}\b(subscribe|subscription|refill|auto-?ship|every \d+ (?:days?|weeks?|months?))\b[^.<>]{0,60}", re.I)
EPA = re.compile(r"[^.<>]{0,60}(EPA|FIFRA|25\(b\)|registered)[^.<>]{0,60}")
PRICE = re.compile(r"(?:US\$|\$|USD|IDR|Rp\.?|€|£|CA\$|A\$)\s?[\d][\d,\.]*|[\d][\d,\.]*\s?(?:USD|IDR|EUR|GBP)")
BUN = re.compile(r"[^.<>]{0,50}\b(bundle|buy \d|\d[- ]pack|save \d+%|\d+ for \$)\b[^.<>]{0,50}", re.I)
def text(h):
    h = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", h)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h)))
def get(url, tag):
    try:
        r = requests.get(url, headers=H, timeout=25, allow_redirects=True)
    except Exception as e:
        return {"url": url, "status": "error: " + type(e).__name__}, ""
    d = {"url": url, "final": r.url, "status": r.status_code}
    if r.status_code in (403, 429): d["blocked"] = True; return d, ""
    (RAW / f"{tag}.html").write_text(r.text[:600000], encoding="utf-8") if not (RAW / f"{tag}.html").exists() else None
    return d, r.text
def extract(h):
    t = text(h); ti = re.search(r"(?is)<title[^>]*>(.*?)</title>", h)
    md = re.search(r'(?is)<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', h)
    hits = [t[max(0, m.start() - 60): m.end() + 80] for m in KW.finditer(t)][:4]
    cur = re.findall(r'(?i)(?:"currency"\s*:\s*"|priceCurrency"\s*:\s*"|og:price:currency" content=")([A-Z]{3})', h)[:3]
    return {"title": html.unescape(ti.group(1)).strip()[:150] if ti else "", "desc": html.unescape(md.group(1))[:250] if md else "",
            "kw_hits": hits, "kw_n": len(KW.findall(t)), "prices": PRICE.findall(t)[:8], "currency_meta": cur,
            "bundle": [m.group(0).strip() for m in BUN.finditer(t)][:3], "sub": [m.group(0).strip() for m in SUB.finditer(t)][:4],
            "epa": [m.group(0).strip() for m in EPA.finditer(t)][:4] if "--epa" in sys.argv else [], "len": len(t)}
def rdap(dom):
    try:
        r = requests.get(f"https://rdap.org/domain/{dom}", timeout=30, allow_redirects=True)
        if r.status_code != 200: return "unknown (http %s)" % r.status_code
        for e in r.json().get("events", []):
            if e.get("eventAction") == "registration": return e["eventDate"][:10]
        return "unknown (no registration event)"
    except Exception as e: return "unknown (" + type(e).__name__ + ")"
def wb(dom):
    try:
        r = requests.get(f"http://web.archive.org/cdx/search/cdx?url={dom}&limit=1&fl=timestamp", timeout=40)
        s = r.text.strip()
        return (s[:4] + "-" + s[4:6] + "-" + s[6:8]) if s else "none"
    except Exception as e: return "unknown (" + type(e).__name__ + ")"
def cls(rd, w):
    ds = [x for x in (rd, w) if re.match(r"\d{4}-", x)]
    if not ds: return "unknown"
    if re.match(r"\d{4}-", rd) and re.match(r"\d{4}-", w) and (int(w[:4]) * 372 + int(w[5:7]) * 31 - (int(rd[:4]) * 372 + int(rd[5:7]) * 31)) > 2 * 365 + 20 and rd < w:
        pass
    # domain date more than two years OLDER than first capture -> bought-domain flag
    if re.match(r"\d{4}-", rd) and re.match(r"\d{4}-", w):
        import datetime as dt
        if (dt.date.fromisoformat(w) - dt.date.fromisoformat(rd)).days > 730: return "unclear: possibly a bought domain"
    return "young" if min(ds) >= "2024-11-10" else "old"
if __name__ == "__main__":
    rows = list(csv.DictReader(open(RP / f"stores_{prod}.csv", encoding="utf-8")))
    sel = [r for r in rows if r["domain"] and r["age"] and (int(r["age"]) >= 90 or int(r["age"]) < 30)]
    sel = sel[:25]
    _, out = merged([f"rp_{prod}_{i}" for i in (1, 2, 3)])
    hosts = {}
    for a in out:
        if a["domain"] and isstore(a["domain"]): hosts.setdefault(reg(a["domain"]), a["domain"])
    only = [x for x in sys.argv[3:] if not x.startswith("--")]
    for r in sel:
        d = r["domain"]
        if only and d not in only: continue
        f = OD / f"{d}.json"
        if f.exists(): continue
        res = {"domain": d, "fetched": "2026-11-10", "oldest_ad": r["oldest"], "ads": r["ads"], "pages": []}
        g, h = get(f"https://{d}/?currency=USD", d); time.sleep(5)
        res["home"] = g
        if h: res["home"].update(extract(h))
        if not g.get("blocked") and h and res["home"]["kw_n"] == 0 and hosts.get(d) and hosts[d] != d:
            g2, h2 = get(f"https://{hosts[d]}/?currency=USD", d + "__landing"); time.sleep(5)
            res["landing"] = g2
            if h2: res["landing"].update(extract(h2))
        res["rdap"] = rdap(d); res["wayback"] = wb(d); res["age_class"] = cls(res["rdap"], res["wayback"])
        f.write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8"); print(d, res["home"].get("status"), res["home"].get("kw_n"), res["rdap"], res["wayback"], res["age_class"], flush=True)
        time.sleep(3)
