"""B9: ad survival re-check (written 2026-11-08, run on/after 2026-12-08).
Meta keeps no record of stopped commercial ads in the US, so the only way to see failures is to look again.
Input: the ad samples saved by meta_ages.py (meta_ages/<pid>.json, field 'ads', each with Library id, start date, window).
For every sampled ad: open https://www.facebook.com/ads/library/?id=<id> and record whether it is still shown as Active.
Output: meta_recheck_<date>.json and, per category and age window, the share still running.
Usage: python meta_recheck.py [pid ...] [--limit=60]   (limit = ads per category, spread across windows)
"""
import json, sys, pathlib, collections, datetime as dt
from playwright.sync_api import sync_playwright
import meta_ages as M
D = pathlib.Path(__file__).with_name("meta_ages")
LIMIT = int(next((a.split("=")[1] for a in sys.argv if a.startswith("--limit=")), "60"))
PIDS = [a for a in sys.argv[1:] if not a.startswith("--")] or [f.stem for f in D.glob("*.json") if f.stem != "summary"]
OUT = pathlib.Path(__file__).with_name(f"meta_recheck_{dt.date.today().isoformat()}.json")

def pick(ads):
    by = collections.defaultdict(list)
    for a in ads: by[a.get("window", "?")].append(a)
    per = max(1, LIMIT // max(1, len(by)))
    return [a for w in by.values() for a in w[:per]]

if __name__ == "__main__":
    res = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    with sync_playwright() as pw:
        br = pw.chromium.launch(headless=True)
        pg = br.new_page(user_agent=M.UA, viewport={"width": 1280, "height": 900}, locale="en-US")
        for pid in PIDS:
            if pid in res: continue
            src = json.loads((D / f"{pid}.json").read_text(encoding="utf-8"))
            rows = []
            for a in pick(src.get("ads", [])):
                pg.goto(f"https://www.facebook.com/ads/library/?id={a['id']}", wait_until="domcontentloaded", timeout=60000)
                pg.wait_for_timeout(4000)
                t = pg.evaluate("document.body.innerText")
                # the ad opens as a modal: '...Active\nLibrary ID: <id>\nStarted running on ...' (checked by hand 2026-11-08)
                m = __import__("re").search(r"(Active|Inactive)\s*\n\s*Library ID: " + a["id"], t)
                status = m.group(1).lower() if m else "gone"
                rows.append({"id": a["id"], "start": a["start"], "window": a.get("window"), "page": a["page"], "status": status})
            sm = collections.defaultdict(lambda: [0, 0])
            for r in rows: sm[r["window"]][0] += r["status"] == "active"; sm[r["window"]][1] += 1
            res[pid] = {"sampled_on": src.get("date"), "rows": rows, "still_active": {w: f"{a}/{n}" for w, (a, n) in sm.items()}}
            OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
            print(pid, res[pid]["still_active"], flush=True)
        br.close()
