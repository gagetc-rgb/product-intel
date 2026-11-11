"""Run B (2026-11-11): active US ads with the exact product phrase that started 2026-08-13..2026-10-12 (alive 30-90 days). Groups by landing domain."""
import json, collections, datetime as dt, re, pathlib, urllib.parse
P = pathlib.Path(__file__).parent; T = dt.date(2026, 11, 11)
X = json.load(open(P / "runB_2026-11-11.json", encoding="utf-8")); PH = json.load(open(P / "runB_phrases.json"))
inv = {v: k for k, v in PH.items()}
def phrase(x): return urllib.parse.unquote(re.search(r"q=([^&]+)", x["url"]).group(1)).strip('"')
def host(x):
    u = x["snapshot"].get("link_url") or ""; h = urllib.parse.urlparse(u).netloc.lower().removeprefix("www.")
    return h or (x["snapshot"].get("caption") or "").lower() or "(none)"
SKIP = re.compile(r"amazon\.|walmart\.|tiktok\.|facebook\.|instagram\.|fb\.me|bit\.ly|linktr|etsy\.|ebay\.|target\.com|shopmy|ltk\.|youtube")
out = {}
for ph in PH.values():
    L = [x for x in X if phrase(x) == ph]; by = collections.defaultdict(list)
    for x in L: by[host(x)].append(x)
    rows = sorted(({"domain": h, "ads": len(v), "oldest_days": max((T - dt.date.fromtimestamp(x["start_date"])).days for x in v),
                    "pages": [p for p, _ in collections.Counter(x["page_name"] for x in v).most_common(3)]} for h, v in by.items()), key=lambda r: -r["ads"])
    out[inv[ph]] = {"phrase": ph, "ads": len(L), "meta_total": L[0].get("total") if L else 0, "domains": rows}
    print(f"\n=== {inv[ph]} \"{ph}\": {len(L)} ads read (Meta total {out[inv[ph]]['meta_total']}), {len(rows)} landing domains")
    for r in rows[:14]: print("  ", r["ads"], r["oldest_days"], r["domain"], "|", "; ".join(r["pages"])[:70], "SKIP" if SKIP.search(r["domain"]) else "")
json.dump(out, open(P / "runB_domains.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
