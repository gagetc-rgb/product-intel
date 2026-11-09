"""Detect review widget + public keys on a store homepage (2026-11-09)."""
import re, sys, json, urllib.request
UA={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36"}
def get(u):
    try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=40).read().decode("utf-8","replace")
    except Exception as e: return f"ERR {e}"
out={}
for d in sys.argv[1:]:
    h=get(f"https://{d}/")
    r={"len":len(h)}
    r["myshopify"]=sorted(set(re.findall(r"([a-z0-9-]+\.myshopify\.com)",h)))[:2]
    r["loox"]="loox" in h.lower(); r["judgeme"]="judge.me" in h.lower() or "judgeme" in h.lower()
    r["okendo"]="okendo" in h.lower(); r["yotpo"]="yotpo" in h.lower(); r["stamped"]="stamped" in h.lower(); r["junip"]="junip" in h.lower()
    m=re.search(r"okendo[^\"']*?subscriberId[\"':\s]+([0-9a-f-]{36})",h,re.I) or re.search(r"([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})",h) if "okendo" in h.lower() else None
    r["okendo_id"]=m.group(1) if m else None
    m=re.search(r"yotpo\.com/(?:v1/)?(?:widget/|loader/)?([A-Za-z0-9]{30,50})",h); r["yotpo_key"]=m.group(1) if m else None
    m=re.search(r"data-api-key=[\"']([^\"']+)|apiKey[\"']?\s*[:=]\s*[\"'](pubkey-[^\"']+)",h); r["stamped_key"]=(m.group(1) or m.group(2)) if m else None
    m=re.search(r"shop_id[\"']?\s*[:=]\s*[\"']?(\d+)",h); r["shop_id"]=m.group(1) if m else None
    out[d]=r; print(d,json.dumps(r))
json.dump(out,open("widgets.json","w"),indent=1)
