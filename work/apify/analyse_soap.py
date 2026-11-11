"""Soaps (2026-11-11): every active US ad alive 90+ days that contains a soap phrase; group by landing domain; RDAP domain age."""
import json, re, datetime as dt, urllib.parse, urllib.request, collections, time, pathlib
P = pathlib.Path(__file__).parent; T = dt.date(2026, 11, 11)
X = json.load(open(P / "runSoap_2026-11-11.json", encoding="utf-8")); PH = json.load(open(P / "runSoap_phrases.json"))
ph = lambda x: urllib.parse.unquote(re.search(r"q=([^&]+)", x["url"]).group(1)).strip('"')
def host(x):
    u = x["snapshot"].get("link_url") or ""; h = urllib.parse.urlparse(u).netloc.lower().removeprefix("www.")
    return h or (x["snapshot"].get("caption") or "").lower() or "(none)"
def root(h): p = h.split("."); return ".".join(p[-3:]) if len(p) > 2 and p[-2] in ("co", "com") and len(p[-1]) == 2 else ".".join(p[-2:])
RD = {}
def rdap(d):
    if d in RD: return RD[d]
    try:
        with urllib.request.urlopen(urllib.request.Request(f"https://rdap.org/domain/{d}", headers={"User-Agent": "research-script"}), timeout=20) as r:
            j = json.loads(r.read()); RD[d] = next((e["eventDate"][:10] for e in j.get("events", []) if e.get("eventAction") == "registration"), "?")
    except Exception as e: RD[d] = "unknown"
    time.sleep(0.3); return RD[d]
seen = set(); by = collections.defaultdict(lambda: collections.defaultdict(list))
for x in X:
    if not x.get("ad_archive_id") or x["ad_archive_id"] in seen: continue
    seen.add(x["ad_archive_id"]); by[PH[ph(x)]][root(host(x))].append(x)
for x in [X[0]]: pass
for x in X:
    if x.get("ad_archive_id") is None and x.get("url"): print("empty source:", ph(x))
out = {}
for pid, D in by.items():
    print(f"\n=== {pid}: {sum(len(v) for v in D.values())} unique 90+ ads, {len(D)} domains")
    rows = []
    for d, L in sorted(D.items(), key=lambda kv: -len(kv[1])):
        age = [(T - dt.date.fromtimestamp(x["start_date"])).days for x in L]
        reg = rdap(d) if d not in ("(none)", "facebook.com", "instagram.com", "amazon.com") else "-"
        young = reg[:4].isdigit() and (T - dt.date.fromisoformat(reg)).days < 730
        r = {"domain": d, "ads90": len(L), "oldest": max(age), "registered": reg, "young": young,
             "pages": [p for p, _ in collections.Counter(x["page_name"] for x in L).most_common(3)],
             "links": [l for l, _ in collections.Counter(re.sub(r"\?.*", "", x["snapshot"].get("link_url") or "")[-50:] for x in L).most_common(2)]}
        rows.append(r)
        print(f"  {r['ads90']:3} oldest {r['oldest']:3}  {d:28} reg {reg:10} {'YOUNG' if young else ''}  | {'; '.join(r['pages'])[:55]} | {r['links'][0]}")
    out[pid] = rows
json.dump(out, open(P / "soap_holders_2026-11-11.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
