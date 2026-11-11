"""Google Trends related queries (METRICS.md K2/K6, 2026-11-10): what people search together with a phrase, US, last 12 months.
Same in-page API route as trends_pull_pw.py (explore -> RELATED_QUERIES widget -> relatedsearches).
Usage: python trends_related_pw.py OUT.json "term1" "term2" ...   -> {term: {"top": [[query, value]], "rising": [[query, value]]}}
Stops on the first HTTP error (429 = rate limit): no retries, no workarounds."""
import sys, json, time, pathlib, os
from playwright.sync_api import sync_playwright

JS = """async (term) => {
  const req = {comparisonItem: [{keyword: term, geo: 'US', time: 'today 12-m'}], category: 0, property: ''};
  const r1 = await fetch('/trends/api/explore?hl=en-US&tz=0&req=' + encodeURIComponent(JSON.stringify(req)));
  const t1 = await r1.text(); if (!r1.ok) return {error: 'explore ' + r1.status};
  const w = JSON.parse(t1.slice(t1.indexOf('{'))).widgets.find(w => w.id === 'RELATED_QUERIES');
  if (!w) return {error: 'no related widget'};
  const r2 = await fetch('/trends/api/widgetdata/relatedsearches?hl=en-US&tz=0&req=' + encodeURIComponent(JSON.stringify(w.request)) + '&token=' + w.token);
  const t2 = await r2.text(); if (!r2.ok) return {error: 'related ' + r2.status};
  const L = JSON.parse(t2.slice(t2.indexOf('{'))).default.rankedList;
  const pick = l => (l ? l.rankedKeyword.map(k => [k.query, k.formattedValue]) : []);
  return {top: pick(L[0]), rising: pick(L[1])};
}"""

def main():
    out = pathlib.Path(sys.argv[1]); terms = sys.argv[2:]
    res = json.loads(out.read_text(encoding="utf-8")) if out.exists() else {}
    delay = float(os.environ.get("TRENDS_DELAY", "4"))
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True); pg = b.new_page(locale="en-US")
        pg.goto("https://trends.google.com/trends/?geo=US", wait_until="domcontentloaded", timeout=60000); pg.wait_for_timeout(4000)
        for t in terms:
            if t in res: continue
            r = pg.evaluate(JS, t)
            if "error" in r:
                print("stop:", t, r["error"]); break
            res[t] = r; print("ok", t, len(r["top"]), "top,", len(r["rising"]), "rising")
            out.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
            time.sleep(delay)
        b.close()

if __name__ == "__main__":
    main()
