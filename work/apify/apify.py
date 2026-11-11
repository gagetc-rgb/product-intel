"""Minimal Apify client (2026-11-11). Reads APIFY_TOKEN from the project .env; never prints it.
Usage: python work/apify/apify.py me | schema <actor> | run <actor> <input.json> <out.json>"""
import json, sys, time, pathlib, urllib.request, urllib.error
R = pathlib.Path(__file__).resolve().parents[2]
TOK = next(l.split("=", 1)[1].strip() for l in open(R / ".env", encoding="utf-8") if l.startswith("APIFY_TOKEN="))
API = "https://api.apify.com/v2"
def call(path, data=None, method=None):
    req = urllib.request.Request(API + path, data=None if data is None else json.dumps(data).encode(), method=method,
                                 headers={"Authorization": "Bearer " + TOK, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r: return json.loads(r.read() or b"null")
    except urllib.error.HTTPError as e: sys.exit(f"HTTP {e.code}: {e.read()[:400].decode(errors='replace')}")
cmd = sys.argv[1]
if cmd == "me":
    u = call("/users/me")["data"]; p = u.get("plan", {})
    print("user ok, plan:", p.get("id"), "| monthly usage credits $:", p.get("monthlyUsageCreditsUsd"))
    lim = call("/users/me/limits")["data"]; print("used this cycle $:", lim.get("current", {}).get("monthlyUsageUsd"), "of", lim.get("limits", {}).get("maxMonthlyUsageUsd"))
elif cmd == "schema":
    a = call(f"/acts/{sys.argv[2].replace('/', '~')}")["data"]
    print("actor:", a["name"], "| pricing:", json.dumps(a.get("pricingInfos", [])[-1:], ensure_ascii=False)[:600])
    b = call(f"/acts/{sys.argv[2].replace('/', '~')}/builds/{a['taggedBuilds']['latest']['buildId']}")["data"]
    s = b.get("inputSchema"); s = json.loads(s) if isinstance(s, str) else (s or b.get("actorDefinition", {}).get("input", {}))
    for k, v in (s or {}).get("properties", {}).items(): print(f"  {k}: {v.get('type')} | {v.get('title','')} | default={v.get('default', v.get('prefill'))}"[:220])
elif cmd == "run":
    actor, inp, out = sys.argv[2].replace("/", "~"), json.load(open(sys.argv[3], encoding="utf-8")), sys.argv[4]
    cap = sys.argv[5] if len(sys.argv) > 5 else "0.5"
    run = call(f"/acts/{actor}/runs?maxTotalChargeUsd={cap}&timeout=3000", inp)["data"]; rid = run["id"]; print("run", rid, "started")
    while True:
        time.sleep(10); run = call(f"/actor-runs/{rid}")["data"]
        if run["status"] not in ("READY", "RUNNING"): break
    items = call(f"/datasets/{run['defaultDatasetId']}/items?clean=true&format=json")
    json.dump(items, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("status", run["status"], "| items", len(items), "| cost $", run.get("usageTotalUsd"), "| charged events", run.get("chargedEventCounts"))
