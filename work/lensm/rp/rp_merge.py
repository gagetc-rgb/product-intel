import sys, json, csv
from rp_lib import *
prod = sys.argv[1]
rows = list(csv.DictReader(open(RP / f"stores_{prod}.csv", encoding="utf-8")))
dec = json.loads((RP / f"decisions_{prod}.json").read_text(encoding="utf-8"))
cols = ["sells_product", "reason", "product_name", "price_as_shown", "usd", "bundle_text", "sub_refill_text", "epa_text", "rdap_registration", "wayback_first", "age_class", "http_status"]
extra = ["meta_active", "meta_30plus", "meta_90plus", "meta_180plus"]
for r in rows:
    d = r["domain"]; st = RP / f"stepc_{prod}" / f"{d}.json"
    x = dec.get(d, {})
    if st.exists():
        s = json.loads(st.read_text(encoding="utf-8"))
        r.update(rdap_registration=s["rdap"], wayback_first=s["wayback"], age_class=s["age_class"], http_status=s["home"].get("status"))
    else:
        r.update(rdap_registration="", wayback_first="", age_class="", http_status="not checked (outside step C selection or no domain)")
    for c in cols:
        if c in x: r[c] = x[c]
    for c in cols + extra: r.setdefault(c, "")
    sd = RP.parent.parent / "blind" / "meta_ages"
    for tag in (x.get("dom_pid"),) if x.get("dom_pid") else ():
        j = json.loads((sd / f"{tag}.json").read_text(encoding="utf-8"))
        r.update(meta_active=j["active"] if j["active"] is not None else "unknown", meta_30plus=j["aged30"] if j["aged30"] is not None else "unknown", meta_90plus=j["aged90"] if j["aged90"] is not None else "unknown", meta_180plus=j["aged180"] if j["aged180"] is not None else "unknown")
fn = list(rows[0].keys())
with open(RP / f"stores_{prod}_full.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=fn); w.writeheader(); w.writerows(rows)
print("ok", len(rows))
