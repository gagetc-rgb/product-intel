"""M8 step 1: Trustpilot pages for the leaders. One request per URL, 2.5 s apart, no retry beyond one."""
import urllib.request, urllib.error, time, re, json, pathlib
R = pathlib.Path(__file__).parent; OUT = R / "raw_tp"; OUT.mkdir(exist_ok=True)
LEADERS = "try-kaori.com miraiclinical.com earthlyderm.com goda.co smooche.com primeprometics.com luxe.com terralotus.shop ancestralcosmetics.com borboleta.com sproos.co scentifyhome.com everstridesocks.com tryskult.com".split()
UA = "Mozilla/5.0 (X11; Linux x86_64) research"
def get(u):
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA, "Accept-Language": "en-US"}), timeout=30)
        return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e: return e.code, ""
    except Exception as e: return -1, str(e)[:80]
for d in LEADERS:
    for tag, q in (("all", ""), ("low", "?stars=1&stars=2")):
        f = OUT / f"{d}_{tag}.html"
        if f.exists(): continue
        s, h = get(f"https://www.trustpilot.com/review/{d}{q}")
        f.write_text(h, encoding="utf-8"); print(d, tag, s, len(h), flush=True)
        if s != 200 and tag == "all": break
        time.sleep(2.5)
