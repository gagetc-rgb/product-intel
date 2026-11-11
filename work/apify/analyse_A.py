"""Run A (2026-11-11): active US ads of the 8 young copies that started on or before 2026-08-13 (alive 90+ days)."""
import json, collections, datetime as dt, re, sys, pathlib
P = pathlib.Path(__file__).parent; T = dt.date(2026, 11, 11)
X = json.load(open(P / "runA_2026-11-11.json", encoding="utf-8"))
dom = lambda x: re.search(r"q=([^&]+)", x["url"]).group(1)
def prod(x):
    u = (x["snapshot"].get("link_url") or "").lower()
    m = re.search(r"/products?/([^/?#]+)", u) or re.search(r"/(?:pages|collections)/([^/?#]+)", u)
    return (m.group(1)[:38] if m else (re.sub(r"https?://(www\.)?", "", u).split("?")[0][:38] or "(no link)"))
by = collections.defaultdict(list)
for x in X: by[dom(x)].append(x)
for d, L in by.items():
    age = [(T - dt.date.fromtimestamp(x["start_date"])).days for x in L]
    print(f"\n=== {d}: {len(L)} ads 90+ (Meta total {L[0].get('total')}), 180+: {sum(a>=180 for a in age)}, oldest {max(age)} d, creatives {len({x['collation_id'] for x in L})}")
    print("  products:", collections.Counter(prod(x) for x in L).most_common(6))
    print("  pages:", collections.Counter(x["page_name"] for x in L).most_common(8))
    print("  formats:", collections.Counter(x["snapshot"].get("display_format") for x in L).most_common(3))
