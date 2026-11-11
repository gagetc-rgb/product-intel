"""New wave from run B: landing domains whose oldest ad in the sample is 30-100 days old, 3+ ads; domain age from RDAP (rdap.org)."""
import json, re, pathlib, urllib.request, time
P = pathlib.Path(__file__).parent; B = json.load(open(P / "runB_domains.json", encoding="utf-8"))
SKIP = re.compile(r"amazon|walmart|tiktok|facebook|instagram|fb\.me|bit\.ly|linktr|etsy|ebay|target\.com|sephora|\(none\)|a\.co$")
def root(h): parts = h.split("."); return ".".join(parts[-3:]) if parts[-2] in ("co", "com") and len(parts[-1]) == 2 else ".".join(parts[-2:])
def rdap(d):
    try:
        with urllib.request.urlopen(urllib.request.Request(f"https://rdap.org/domain/{d}", headers={"User-Agent": "research-script"}), timeout=20) as r:
            j = json.loads(r.read()); return next((e["eventDate"][:10] for e in j.get("events", []) if e.get("eventAction") == "registration"), "?")
    except Exception as e: return "err"
out = []
for pid, v in B.items():
    for r in v["domains"]:
        if r["ads"] >= 3 and 30 <= r["oldest_days"] <= 100 and not SKIP.search(r["domain"]):
            d = root(r["domain"]); reg = rdap(d); time.sleep(0.4)
            out.append({"product": pid, "domain": r["domain"], "root": d, "ads": r["ads"], "oldest_days": r["oldest_days"], "registered": reg, "pages": r["pages"]})
            print(pid, r["ads"], r["oldest_days"], d, reg, "|", "; ".join(r["pages"])[:60])
json.dump(out, open(P / "newcomers_2026-11-11.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
