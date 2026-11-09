"""Photo contact sheet for all 20 categories (2026-11-09): Amazon top-brand listing images (URLs already in digest,
loaded by the viewer's browser, nothing downloaded) + leader store product photos saved by fetch_longrunning.py."""
import json, glob, html, pathlib
R = pathlib.Path(__file__).resolve().parents[2]
store = {}
for f in ["work/ads/longrunning_v2.json", "work/ads/longrunning_v3a.json", "work/ads/longrunning_v3b.json"]:
    for b in json.load(open(R / f, encoding="utf-8"))["brands"]:
        store.setdefault(b["id"], []).append(b)
order = json.load(open(R / "work/dossier/verdict_v21.json", encoding="utf-8"))
rows = order if isinstance(order, list) else order.get("rows", [])
pids = [r.get("pid") for r in rows if isinstance(r, dict) and r.get("pid")] or [pathlib.Path(f).stem for f in sorted(glob.glob(str(R / "work/dossier/digest/*.json")))]
out = ["<!doctype html><meta charset=utf-8><title>Category photos</title><style>body{font:14px system-ui;margin:16px;background:#fff;color:#111}"
       "h2{margin:28px 0 6px}.row{display:flex;flex-wrap:wrap;gap:10px}.c{width:150px}.c img{width:150px;height:150px;object-fit:contain;background:#f4f4f4;border-radius:6px}"
       ".c div{font-size:12px;line-height:1.3}.s{color:#555;font-size:12px;margin:8px 0 4px}</style><h1>Photos: 20 categories</h1>"]
for pid in pids:
    d = json.load(open(R / f"work/dossier/digest/{pid}.json", encoding="utf-8"))
    out.append(f"<h2>{html.escape(d['name'])}</h2><div class=s>Amazon: top brands by units/mo (best listing)</div><div class=row>")
    for b in d.get("amazon_us", {}).get("top_brands", [])[:8]:
        x = b.get("best", {})
        if x.get("img"):
            out.append(f"<div class=c><img loading=lazy src='{x['img']}'><div><b>{html.escape(b['key'])}</b> · {b['units']:,}/mo · {html.escape(str(x.get('price') or ''))}</div></div>")
    out.append("</div>")
    for b in store.get(pid, []):
        if b["photos"]:
            out.append(f"<div class=s>Store: {b['domain']} — {html.escape(b['productTitle'])}</div><div class=row>")
            out += [f"<div class=c><img loading=lazy src='/{p}'></div>" for p in b["photos"]]
            out.append("</div>")
(R / "work/dossier/photos.html").write_text("\n".join(out), encoding="utf-8")
print("ok", len(pids))
