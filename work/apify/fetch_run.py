"""Wait for an existing Apify run and download its dataset (retries on network errors). Usage: python fetch_run.py <run_id> <out.json>"""
import json, sys, time, pathlib, urllib.request
R = pathlib.Path(__file__).resolve().parents[2]
TOK = next(l.split("=", 1)[1].strip() for l in open(R / ".env", encoding="utf-8") if l.startswith("APIFY_TOKEN="))
def call(path):
    for i in range(6):
        try:
            req = urllib.request.Request("https://api.apify.com/v2" + path, headers={"Authorization": "Bearer " + TOK})
            with urllib.request.urlopen(req, timeout=120) as r: return json.loads(r.read())
        except Exception as e: print("retry", i, str(e)[:60]); time.sleep(10)
    sys.exit("network failed")
rid, out = sys.argv[1], sys.argv[2]
while True:
    run = call(f"/actor-runs/{rid}")["data"]
    if run["status"] not in ("READY", "RUNNING"): break
    time.sleep(10)
items = call(f"/datasets/{run['defaultDatasetId']}/items?clean=true&format=json")
json.dump(items, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("status", run["status"], "| items", len(items), "| cost $", run.get("usageTotalUsd"))
