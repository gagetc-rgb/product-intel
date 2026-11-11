"""Google Trends pull without retyping (2026-11-10). Opens trends.google.com in Playwright (Chromium) and calls the
same in-page API the earlier pulls used (explore -> TIMESERIES widget -> multiline), US, 5 years, weekly.
Usage: python trends_pull_pw.py OUT_FILE "term1" "term2" ...            each term pulled alone -> 'term|last week|v1,...'
       python trends_pull_pw.py OUT_FILE --together "t1" "t2" ...       one comparison (shared 0-100 scale), same format
Stops on the first HTTP error (429 = rate limit): no retries, no workarounds. Waits TRENDS_DELAY seconds between terms (default 4)."""
import sys, json, time, pathlib, os
from playwright.sync_api import sync_playwright

JS = """async (terms) => {
  const req = {comparisonItem: terms.map(k => ({keyword: k, geo: 'US', time: 'today 5-y'})), category: 0, property: ''};
  const r1 = await fetch('/trends/api/explore?hl=en-US&tz=0&req=' + encodeURIComponent(JSON.stringify(req)));
  const t1 = await r1.text(); if (!r1.ok) return {error: 'explore ' + r1.status};
  const w = JSON.parse(t1.slice(t1.indexOf('{'))).widgets.find(w => w.id === 'TIMESERIES');
  const r2 = await fetch('/trends/api/widgetdata/multiline?hl=en-US&tz=0&req=' + encodeURIComponent(JSON.stringify(w.request)) + '&token=' + w.token);
  const t2 = await r2.text(); if (!r2.ok) return {error: 'multiline ' + r2.status};
  const td = JSON.parse(t2.slice(t2.indexOf('{'))).default.timelineData;
  return {last: td[td.length - 1].formattedTime, partial: !!td[td.length - 1].isPartial, n: td.length,
          series: terms.map((_, i) => td.map(d => d.value[i]))};
}"""

def main():
    out = pathlib.Path(sys.argv[1]); args = sys.argv[2:]
    together = args[:1] == ["--together"]; terms = args[1:] if together else args
    # resume: terms already saved in OUT are not pulled again (a together-group file is written once, whole)
    have = {l.split("|")[0] for l in out.read_text(encoding="utf-8").splitlines() if l.strip()} if out.exists() else set()
    if together and have: print("skip, exists:", out); return
    terms = terms if together else [t for t in terms if t not in have]
    if not terms: print("nothing left for", out); return
    lines, stopped = [], False
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        pg = b.new_page(locale="en-US")
        pg.goto("https://trends.google.com/trends/explore?geo=US&date=today%205-y&q=shampoo", wait_until="domcontentloaded")
        groups = [terms] if together else [[t] for t in terms]
        for i, g in enumerate(groups):
            if i: time.sleep(float(os.environ.get("TRENDS_DELAY", 4)))
            r = pg.evaluate(JS, g)
            if "error" in r:
                print("STOP", g, r["error"]); stopped = True; break
            for t, v in zip(g, r["series"]):
                lines.append(f"{t}|{r['last']}|{','.join(str(x) for x in v)}")
            print("ok", g, r["n"], "weeks, last", r["last"], "partial" if r["partial"] else "")
        b.close()
    if lines and not (together and stopped):
        with open(out, "a", encoding="utf-8") as f: f.write("\n".join(lines) + "\n")
        print("wrote", len(lines), "lines ->", out)
    sys.exit(3 if stopped else 0)

if __name__ == "__main__":
    main()
