"""Helpers for the repeat-purchase pass (2026-11-10). Read-only on meta_ages; writes only inside work/lensm/rp/."""
import json, sys, pathlib, datetime as dt, csv, collections
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "work" / "blind"))
from meta_stats import reg, pagekey, MKT
MA = ROOT / "work" / "blind" / "meta_ages"; RP = pathlib.Path(__file__).resolve().parent
NONSTORE = ("google.com", "whatsapp.com", "sephora.com", "linktr.ee", "apple.com", "youtube.com")
def load(pid): return json.loads((MA / f"{pid}.json").read_text(encoding="utf-8"))
def isstore(d): return bool(d) and not any(m in d for m in MKT) and reg(d) not in NONSTORE
def merged(pids):
    ds = {p: load(p) for p in pids}
    p2d = {}
    for p, d in ds.items():
        for a in d["ads"]:
            if isstore(a["domain"]): p2d.setdefault(pagekey(a["page"]), reg(a["domain"]))
    out = []
    for p, d in ds.items():
        for a in d["ads"]:
            a = dict(a); a["phrase_id"] = p; a["rundate"] = d["date"]
            if isstore(a["domain"]): a["key"] = reg(a["domain"]); a["hasdom"] = True
            elif a["domain"]: a["key"] = "nonstore:" + reg(a["domain"]); a["hasdom"] = True
            else:
                a["hasdom"] = False; k = pagekey(a["page"]); a["key"] = p2d.get(k) or ("page:" + k)
            out.append(a)
    return ds, out
def groups(out):
    g = collections.OrderedDict()
    for a in out:
        g.setdefault(a["key"], []).append(a)
    rows = []
    for k, L in g.items():
        # de-duplicate the same ad id found by several phrases
        ids = {}
        for a in L: ids.setdefault(a["id"], a)
        L = list(ids.values())
        dated = [a for a in L if a["start"]]
        o = min(dated, key=lambda a: a["start"]) if dated else None
        age = (dt.date.fromisoformat(o["rundate"]) - dt.date.fromisoformat(o["start"])).days if o else None
        rows.append(dict(store=k, ads=len(L), oldest=o["start"] if o else "", age=age,
                         pages="; ".join(sorted({a["page"] for a in L})), phrases=",".join(sorted({a["phrase_id"].split("_")[-1] for a in L})),
                         domain=k if not (k.startswith("page:") or k.startswith("nonstore:")) else ""))
    rows.sort(key=lambda r: (-(r["age"] if r["age"] is not None else -1)))
    return rows
if __name__ == "__main__":
    prod = sys.argv[1]; pids = [f"rp_{prod}_{i}" for i in (1, 2, 3)]
    ds, out = merged(pids)
    for p, d in ds.items(): print(p, d["phrase"], {k: d[k] for k in ("active", "aged30", "aged90", "aged180")}, len(d["ads"]))
    for r in groups(out): print(r["store"], r["ads"], r["oldest"], r["age"], r["pages"][:60], r["phrases"])
