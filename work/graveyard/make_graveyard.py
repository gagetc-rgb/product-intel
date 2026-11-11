"""Graveyard ("Кладбище копий") per product, from data already collected (owner 2026-11-11: no new reconnaissance).
Inputs: BigSpy US advertiser tables of 2026-11-11 (one longest ad per advertiser, sorted by running days),
known full domains from our store lists (m2_stores.csv, codex/meta_stores.csv, codex/store_facts.csv, rp/stores_*_full.csv).
A masked BigSpy domain (e.g. 'sap***com') is unmasked only when exactly one known domain fits the visible start and end.
Stopped = last seen on or before 2026-10-28 (two weeks before the pull). Output: work/site/graveyard_ru.json."""
import csv, json, pathlib, re, glob
R = pathlib.Path(__file__).resolve().parents[2]
CUT = "2026-10-28"
SRC = {"persimmon_soap": "persimmon_soap_us_advertisers_2026-11-11.tsv", "lash_serum": "lash_serum_us_advertisers_2026-11-11.tsv",
       "whitening_powder": "whitening_powder_us_advertisers_2026-11-11.tsv"}
CAT = {"persimmon_soap": {"persimmon_soap"}, "lash_serum": {"lash_serum"}, "whitening_powder": {"whitening_powder", "tooth_whitening_powder"}}
known, live, reg = {}, {}, {}   # known[category] = set of full domains; reg[domain] = registration date we saved
def norm(d):
    d = (d or "").strip().lower().replace("https://", "").replace("http://", "").split("/")[0]
    return d[4:] if d.startswith("www.") else d
def add(cat, d, date=""):
    d = norm(d)
    if "." not in d: return d
    known.setdefault(cat, set()).add(d)
    if date and date[:4].isdigit(): reg.setdefault(d, date[:10])
    return d
role = {}
for r in csv.DictReader(open(R / "work/lensm/m2_stores.csv", encoding="utf-8-sig")):
    d = add(r["category"], r["domain"], r.get("domain_created", ""))
    role[d] = "лидер" if r.get("role") == "leader" else ("не этот товар: " + r["reason_if_no"]) if r.get("sells_product") == "no" else ""
for r in csv.DictReader(open(R / "work/lensm/codex/store_facts.csv", encoding="utf-8-sig")): add(r["category"], r["domain"], r.get("domain_registration", ""))
for r in csv.DictReader(open(R / "work/lensm/codex/meta_stores.csv", encoding="utf-8-sig")):
    d = add(r["category"], r["domain"]); live[d] = (r.get("active_results") or "").strip()
# identified by hand on 2026-11-11 (work/bigspy/BIGSPY_2026-11-11.md), RDAP dates read that day
for cat, d, dt in [("persimmon_soap", "kakibody.com", "2026-05-05"), ("lash_serum", "lashtherapyaustralia.com", "2026-06-21"),
                   ("lash_serum", "facelove-cosmetics.com", "2025-12-28"), ("lash_serum", "hanaekorea.com", "2025-11-02"),
                   ("lash_serum", "diablocosmetics.com", "2018-09-18"), ("whitening_powder", "ecobrightsmile.com", "2025-07-22")]: add(cat, d, dt)
# unmasked by hand in Meta Ad Library on 2026-11-11: work/graveyard/unmasked_2026-11-11.csv (same product only)
UNM = {}
for r in csv.DictReader(open(R / "work/graveyard/unmasked_2026-11-11.csv", encoding="utf-8-sig")):
    UNM[(r["product"], r["mask"], r["page"])] = (add(r["product"], r["domain"], r["registered"][:10]), r["tier"])
    m = re.search(r"Meta says ~([\d,]+)", r["active_ads_us"])   # Meta's own count beats the visible-card lower bound
    n = "~" + m.group(1) if m else r["active_ads_us"].split(" ")[0]
    if n != "0": live[norm(r["domain"])] = n   # visible active US cards, lower bound ("30+"); "0" = none
HAND = {("try***.com", "Grand***ournal"): "try-kaori.com", ("try***.com", "Ai***ori"): "try-kaori.com"}  # Kaori pages, BIGSPY_2026-11-11.md
def unmask(pid, m, page):
    if (pid, m, page) in UNM: return UNM[(pid, m, page)]
    if (m, page) in HAND: return HAND[(m, page)], "◈"
    if "***" not in m: return norm(m), "◆"
    a, b = m.split("***", 1); a = a[4:] if a.startswith("www.") else a
    if len(a) < 4: return "", ""   # "try***.com" fits too many stores
    pool = set().union(*(known.get(c, set()) for c in CAT[pid]))
    hit = [d for d in pool if d.startswith(a) and d.endswith(b) and len(d) >= len(a) + len(b)]
    return (hit[0], "◈") if len(hit) == 1 else ("", "")
out = {}
for pid, f in SRC.items():
    rows = list(csv.DictReader(open(R / "work/bigspy" / f, encoding="utf-8"), delimiter="\t"))
    gap = [r for r in rows if r["last_seen"] == "2026-08-01"]   # BigSpy crawl gap: 9 lash rows end on this exact day
    dead = [r for r in rows if r["last_seen"] <= CUT and r not in gap]
    alive = [r for r in rows if r["last_seen"] > CUT]
    L = []
    for r in sorted(dead, key=lambda r: -int(r["span_days"])):
        d, t = unmask(pid, r["domain"], r["page"])
        L.append({"page": "" if r["page"] == "Special Creative" else r["page"], "mask": r["domain"], "domain": d, "tier": t,
                  "from": r["first_seen"], "to": r["last_seen"], "days": int(r["span_days"]),
                  "head": "" if r["headline"] == "Special Creative" else r["headline"],
                  "now": live.get(d, "") if d else "", "reg": reg.get(d, "") if d else "",
                  "fbpage": r["domain"].startswith("faceboo") or r["domain"][:4].isdigit(), "role": role.get(d, "") if d else ""})
    out[pid] = {"source": f, "read": len(rows), "dead": L, "alive": len(alive), "gap": len(gap)}
json.dump(out, open(R / "work/site/graveyard_ru.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for pid, v in out.items():
    print(pid, "read", v["read"], "dead", len(v["dead"]), "alive", v["alive"], "unmasked", sum(1 for x in v["dead"] if x["domain"]))
    for x in v["dead"]:
        if x["days"] >= 30 or x["domain"]: print("   ", x["days"], x["mask"], "->", x["domain"] or "?", x["reg"], x["page"], "| now:", x["now"], "| fb" if x["fbpage"] else "")
