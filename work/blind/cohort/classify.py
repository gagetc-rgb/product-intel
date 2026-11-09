"""Classify the 12-24-month Amazon cohort by channel and real brand age (2026-11-07).
A = no own store found (no brand on the listing, or brand without a site): Amazon/marketplace-native.
B = own store, first web evidence (domain registration or first Wayback capture) in 2024 or later: young multi-channel.
C = own store with web evidence before 2024: older brand that added an Amazon listing.
Then badge distribution ("bought in past month") per class."""
import json, pathlib, collections
HERE = pathlib.Path(__file__).parent
rows = json.loads((HERE / "brands.json").read_text(encoding="utf-8"))
sites = json.loads((HERE / "sites.json").read_text(encoding="utf-8"))
facts = json.loads((HERE / "site_facts.json").read_text(encoding="utf-8"))
jm = json.loads((HERE / "judgeme.json").read_text(encoding="utf-8"))
def first_evidence(f):
    c = [d.replace("-", "")[:8] for d in (f.get("registered"), f.get("wayback_first")) if d]
    return min(c) if c else None
BANDS = [("none", 0, 50), ("50-99", 50, 100), ("100-499", 100, 500), ("500-999", 500, 1000), ("1K+", 1000, 10**9)]
out = []
for r in rows:
    k = f"{r['cat']}|{r['key']}"
    dom = sites.get(k)
    f = facts.get(k, {})
    fe = first_evidence(f) if dom else None
    cls = "A" if not dom else ("B" if (fe or "99999999") >= "20240101" else "C")
    out.append(dict(cat=r["cat"], brand=r["byline"] or r["key"], cls=cls, site=dom, first_web=fe, badge=r["b"], reviews=r["r"],
                    judgeme=jm.get(k, {}).get("reviews")))
(HERE / "classified.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("class  n  " + "  ".join(b for b, _, _ in BANDS) + "  | med Amazon reviews")
for cls in "ABC":
    c = [x for x in out if x["cls"] == cls]
    cnt = [sum(lo <= x["badge"] < hi for x in c) for _, lo, hi in BANDS]
    rv = sorted(x["reviews"] for x in c)
    print(cls, len(c), "  ".join(f"{n}({n/len(c):.0%})" for n in cnt), "|", rv[len(rv)//2])
print()
for cat in sorted({x["cat"] for x in out}):
    print(cat, collections.Counter(x["cls"] for x in out if x["cat"] == cat))
print()
for x in sorted(out, key=lambda x: (x["cls"], -x["badge"])):
    if x["cls"] != "A" or x["badge"] >= 500:
        print(x["cls"], x["cat"][:9], str(x["brand"])[:20].encode("ascii","replace").decode().ljust(20), (x["site"] or "-").ljust(24), x["first_web"], x["badge"], x["reviews"], x["judgeme"])
