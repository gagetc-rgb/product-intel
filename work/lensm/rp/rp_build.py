import sys, json, csv, pathlib
from rp_lib import *
prod, cmd = sys.argv[1], sys.argv[2]
pids = [f"rp_{prod}_{i}" for i in (1, 2, 3)]
ds, out = merged(pids)
LAB = json.loads((RP / f"labels_{prod}.json").read_text(encoding="utf-8"))  # store key -> on/off/unclear (hand reading)
def lab(k):
    if k.startswith("nonstore:"): return "off"
    return LAB.get(k, "unclear")
if cmd == "kw":
    f = RP / "KEYWORDS.md"
    s = "" if f.exists() else "# Keyword report, repeat-purchase pass (2026-11-10)\n\n Counts are Meta's own (diamond = read from Meta). On/off/unclear is my reading from domain and page name only (hand reading, not verified). A count shown as unknown was returned as None by the script; see recount notes.\n\n"
    s += f"## {prod}\n\n| phrase id | phrase | active | 30+ | 90+ | 180+ | sample | no domain | on | off | unclear | off-target examples |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n"
    for p in pids:
        d = dict(ds[p]); ads = d["ads"]
        rc = RP / f"recount_{p}_active.json"
        if d['active'] is None and rc.exists(): d['active'] = json.loads(rc.read_text())['value']; d['phrase'] += ' (active count re-read once after None)'
        _, o = merged([p]) if False else (None, [a for a in out if a["phrase_id"] == p])
        wd = [a for a in o if a["hasdom"]]
        c = {"on": 0, "off": 0, "unclear": 0}
        for a in wd: c[lab(a["key"])] += 1
        ex = []
        for a in wd:
            if lab(a["key"]) == "off" and a["page"] not in ex: ex.append(a["page"])
        def n(v): return "unknown (None)" if v is None else v
        s += f"| {p} | {d['phrase']} | {n(d['active'])} | {n(d['aged30'])} | {n(d['aged90'])} | {n(d['aged180'])} | {len(ads)} | {len(ads)-len(wd)} | {c['on']} | {c['off']} | {c['unclear']} | {'; '.join(ex[:3]) or '-'} |\n"
    s += "\n"
    with open(f, "a", encoding="utf-8") as fh: fh.write(s)
    print(s)
elif cmd == "stores":
    f = RP / f"stores_{prod}.csv"
    rows = groups(out)
    for r in rows: r["label_name_only"] = lab(r["store"])
    with open(f, "x", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["store", "domain", "ads", "oldest", "age", "pages", "phrases", "label_name_only"], extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    print("wrote", f)
