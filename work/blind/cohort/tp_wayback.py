"""Trustpilot review counts over time from Wayback snapshots (trustpilot.com itself returns 403 to scripts). 2026-11-07.
Per domain: CDX list of snapshots of trustpilot.com/review/<domain>, one per year-quarter, read 'N reviews' / reviewCount.
Run: python tp_wayback.py -> tp_wayback.json"""
import json, re, time, pathlib, urllib.request
HERE = pathlib.Path(__file__).parent
names = json.loads((HERE / "brand_names.json").read_text(encoding="utf-8"))
def get(u):
    for k in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read().decode("utf-8", "replace")
        except Exception: time.sleep(4)
    return ""
out = {}
for d in names:
    rows = []
    for host in (d, "www." + d):
        cdx = get(f"https://web.archive.org/cdx/search/cdx?url=trustpilot.com/review/{host}&output=json&filter=statuscode:200&collapse=timestamp:6&fl=timestamp")
        try: rows += [r[0] for r in json.loads(cdx)[1:]]
        except Exception: pass
    pts = {}
    for ts in sorted(set(rows)):
        q = ts[:4] + "Q" + str((int(ts[4:6]) - 1) // 3 + 1)
        if q in pts: continue
        h = get(f"https://web.archive.org/web/{ts}id_/https://www.trustpilot.com/review/{d}")
        m = re.search(r'"reviewCount"\s*:\s*"?(\d+)', h) or re.search(r'"numberOfReviews"\s*:\s*\{?"?(?:total"?:)?\s*(\d+)', h) or re.search(r"([\d,]+)\s+(?:total\s+)?reviews", h)
        if m: pts[q] = (ts[:8], int(m.group(1).replace(",", "")))
        time.sleep(0.5)
    out[d] = pts
    print(d, len(rows), pts, flush=True)
(HERE / "tp_wayback.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
