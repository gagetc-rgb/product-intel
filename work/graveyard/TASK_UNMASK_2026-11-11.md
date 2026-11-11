# Task: unmask the graveyard domains (Кладбище копий)

Read first: `work/bigspy/BIGSPY_2026-11-11.md` (method and the "Kaki" example), `work/graveyard/make_graveyard.py`, `work/site/graveyard_ru.json`.

Goal: for every stopped advertiser that ran 30+ days in `graveyard_ru.json` (persimmon soap 10, lash serum 39, whitening powder 4), find the full landing domain that BigSpy masked (`sap***com`), its registration date, and whether it advertises in the US today.

How (logged-off browser, Meta Ad Library, US, active_status=all; no BigSpy needed):
1. Search the ad's headline as an exact phrase (`search_type=keyword_exact_phrase`). Keep a result only if the page name fits the masked page name (`Sa***in`) and the domain fits the mask (visible start and end). Read the domain from the card's link caption or the ad's link.
2. Rows without a headline ("Special Creative") or with a Facebook page instead of a domain (`faceboo***…`, blogger pages): try the page name; if it stays ambiguous, leave it masked and say why.
3. For each found domain: RDAP registration date (`https://rdap.org/domain/<domain>`), and the number of active US ads (`q=<domain>`, active_status=active). Do not open checkout or submit anything.
4. Record each match with its source URL in `work/graveyard/unmasked_2026-11-xx.csv` (columns: product, mask, page, domain, how_found, source_url, registered, active_ads_us, checked_on). A match that rests on a page-name guess is ◈, not ◆.
5. Add the CSV to `make_graveyard.py` (a new source of known domains, same product only), run it, then `python work/site/build_site.py`, and check the three product pages in the browser.

Rules: English in files, Russian on the site. Do not run `work/site/ru_content.py`. Do not commit or publish; the owner reviews first. Report how many of the 53 were unmasked, how many are still alive, and which stayed masked and why.
