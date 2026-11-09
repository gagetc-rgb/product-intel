"""Category openness from Amazon top-20 snapshot (amazon.json + retest).
Per product: on-target listings (amz_filter MUST/NOT), dedup by title[:60].
units = sum badge floors; top3 share; newcomer = reviews < 500;
newcomer_units_share; newcomers_with_badge / newcomers_total (denominator);
median price USD (IDR / 16,500)."""
import json, re, sys, statistics as st
sys.path.insert(0, r"C:\Users\Kirill\Desktop\product int\work\blind")
from amz_filter import MUST, NOT
B = r"C:\Users\Kirill\Desktop\product int\work\blind\\"
amz = json.load(open(B+"amazon.json", encoding="utf-8"))
ret = json.load(open(B+"amazon_retest.json", encoding="utf-8"))
sl = {x["id"]: x for x in json.load(open(B+"shortlist.json", encoding="utf-8"))}

def items_of(v):
    if isinstance(v, dict) and "items" in v: return v["items"]
    if isinstance(v, list):
        out=[]
        for e in v: out += items_of(e)
        return out
    if isinstance(v, dict):
        out=[]
        for e in v.values(): out += items_of(e)
        return out
    return []

def price_usd(p):
    m = re.sub(r"[^0-9.]", "", (p or "").split("IDR")[-1].replace(",", ""))
    try: return float(m)/16500
    except: return None

rows=[]
for pid, rec in sl.items():
    if rec["tier"] not in ("A","B"): continue
    its = items_of(amz.get(pid, {})) + items_of(ret.get(pid, {}))
    must, nott = MUST.get(pid), NOT.get(pid)
    seen={}
    for it in its:
        t = it.get("title","")
        if must and not re.search(must, t, re.I): continue
        if nott and re.search(nott, t, re.I): continue
        k = t[:60].lower()
        if k not in seen or it.get("b",0) > seen[k].get("b",0): seen[k]=it
    L = list(seen.values())
    if not L: continue
    units = sum(i.get("b",0) for i in L)
    top = sorted((i.get("b",0) for i in L), reverse=True)
    top3 = sum(top[:3])/units if units else 0
    new = [i for i in L if i.get("r",0) < 500]
    new_b = [i for i in new if i.get("b",0) >= 100]
    new_units = sum(i.get("b",0) for i in new)
    prices = [p for p in (price_usd(i.get("price")) for i in L) if p]
    rows.append(dict(id=pid, tier=rec["tier"], block=rec["block"], n=len(L), units=units,
        top3=round(top3,2), new_share=round(new_units/units,2) if units else 0,
        new_hit=f"{len(new_b)}/{len(new)}", price=round(st.median(prices),1) if prices else None,
        repeat=rec.get("repeat"), tt=rec["tt_k"], m180=rec["meta_180"], adv180=rec["adv_180"]))
rows.sort(key=lambda r:(r["block"], -r["new_share"]))
print(f"{'id':22}{'t':2}{'n':>4}{'units':>8}{'top3':>6}{'new%':>6}{'newHit':>8}{'$med':>7}{'rep':>6}{'TTk':>7}{'M180':>6}{'adv':>5}")
for r in rows:
    print(f"{r['id']:22}{r['tier']:2}{r['n']:>4}{r['units']:>8}{r['top3']:>6}{r['new_share']:>6}{r['new_hit']:>8}{str(r['price']):>7}{str(r['repeat'])[:5]:>6}{r['tt']:>7}{r['m180']:>6}{r['adv180']:>5}")
