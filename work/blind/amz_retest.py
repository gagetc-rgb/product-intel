"""Test-retest: re-run Amazon for a sample and for alternative keywords; output amazon_retest.json."""
import json, pathlib, urllib.parse
from playwright.sync_api import sync_playwright
from amz_common import JS, num, UA
Q = {  # id -> query (same as first run) ; alt_* -> alternative phrasing
 "turmeric_soap":"turmeric soap bar","persimmon_soap":"persimmon soap","compression_socks":"compression socks",
 "tallow_balm":"beef tallow balm","rosemary_oil":"rosemary oil for hair","neck_cream":"neck firming cream",
 "lash_serum":"eyelash growth serum","shower_filter":"filtered shower head","dog_fountain":"stainless steel pet water fountain",
 "magnesium_spray":"magnesium oil spray","pore_patch":"hydrocolloid nose pore patches","lymph_brush":"face lymphatic drainage tool",
 "alt_turmeric":"turmeric kojic acid soap","alt_turmeric2":"turmeric soap for dark spots","alt_persimmon":"soap for old people smell",
 "alt_boxers":"leak proof boxer briefs for men","alt_socks":"bamboo compression socks","alt_tallow":"tallow and honey balm",
 "alt_tennis":"tennis bracelet","alt_lymph":"lymphatic drainage face massager",
}
OUT = pathlib.Path(__file__).with_name("amazon_retest.json")
res = {}
with sync_playwright() as pw:
    br = pw.chromium.launch(headless=True); pg = br.new_context(user_agent=UA, locale="en-US").new_page()
    for k, q in Q.items():
        try:
            pg.goto("https://www.amazon.com/s?k=" + urllib.parse.quote_plus(q), wait_until="domcontentloaded", timeout=60000)
            pg.wait_for_timeout(2500)
            org = [i for i in pg.evaluate(JS) if not i["sp"]][:20]
            for i in org: i["b"] = num(i["bought"]); i["r"] = num(i["rev"])
            res[k] = {"q": q, "items": org}
            print(k, sum(i["b"] for i in org), flush=True)
        except Exception as e:
            print(k, "ERR", str(e)[:100], flush=True)
        OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        pg.wait_for_timeout(1500)
    br.close()
