"""Full 90+ day pull for lash serum, tallow balm, color foundation, tooth powder (work/apify/runW*, watch_candidates_2026-11-11.json, watch_rdap_2026-11-11.json; 2026-11-11).
Owner: only strong signals. Bar used: 5+ ads alive 90+ days (US impressions are not public, so the count of long ads stands in for reach).
New young copies: Hestia (hestiacosmetics.com 2026-03-08 + trylumineskin.com 2025-09-25; 383 + 40 ads 90+, oldest 371 d), Yuki (officialyuki.com 2026-01-30; 40 ads, 125 d, page 'Korean Foundation Tips'),
TryNova (trynova.store 2026-04-09; 5 ads, 100 d, page 'Trending On K-Beauty'), Holicow (tryholicow.com 2025-05-26; 7 ads, 163 d). Lash serum: no new young copy. Tooth powder: none new.
Below the bar (not on the site): Aurellee (3), Beaumont Voss (1), Kreain (gum, 1), Honey Glow (1)."""
import json, pathlib, re
H = pathlib.Path(__file__).parent
s = (H / "make_story.py").read_text(encoding="utf-8")
for pid, n, y in [("color_foundation", 7, 5), ("tallow_balm", 11, 3), ("persimmon_soap", 4, 3)]:
    s, k = re.subn(rf'\["{pid}", \d+, \d+\]', f'["{pid}", {n}, {y}]', s); assert k == 1, pid
(H / "make_story.py").write_text(s, encoding="utf-8"); print("ok story")

p = H / "groups_ru.json"; g = json.loads(p.read_text(encoding="utf-8"))
g["why"]["color_foundation"] = ("Facebook: держатся пять молодых копий. Сильнее всех Hestia, тот самый магазин из видео: домен с марта 2026-го, 383 объявления 90+ дней, а её вторая витрина Lumine Skin держит объявление 371 день ◆. "
    "Дальше Hanae (стик, 245 дней), Yuki (40 объявлений, 125 дней, от страницы «Korean Foundation Tips»), Facelove (167 дней) и TryNova (5 объявлений, 100 дней) ◆. "
    "На Amazon пробивается каждый четвёртый новичок, но почти все безымянные, и почти половина рынка у Luxe.")
g["change"]["color_foundation"] = "Копий уже пять, повторить модель можно. Решит, продаётся ли стик без обещаний, которые нельзя повторить, и сколько остаётся с заказа в своём магазине."
g["why"]["tallow_balm"] = g["why"]["tallow_balm"].replace("Facebook: держатся две молодые копии, Wild Gold и Bare Ritual;", "Facebook: держатся три молодые копии, Wild Gold, Bare Ritual и Holicow (7 объявлений, 163 дня);")
assert "Holicow" in g["why"]["tallow_balm"], g["why"]["tallow_balm"][:120]
g["followers"] += [
 {"brand": "Hestia", "domain": "hestiacosmetics.com", "pid": "color_foundation", "age": "домен с марта 2026 (витрина Lumine Skin с сентября 2025)",
  "fact": "Магазин из видео про тональный стик. 383 объявления старше 90 дней, все от своей страницы ◆; вторая витрина trylumineskin.com: 40 объявлений 90+, 32 старше 180, самое старое 371 день ◆. Сумма из видео ($12,7–19,5 млн) не подтверждена, но реклама держится ◈.",
  "leader": "Лидеры: Luxe, Prime Prometics, Smooche", "reg": "2025-09-25", "ad_days": 371},
 {"brand": "Yuki", "domain": "officialyuki.com", "pid": "color_foundation", "age": "домен с января 2026", "fact": "Тональный крем «4 в 1». 40 объявлений старше 90 дней, самое старое 125 дней; все от страницы «Korean Foundation Tips», а не от бренда ◆.", "leader": "Лидеры: Luxe, Prime Prometics, Smooche", "reg": "2026-01-30", "ad_days": 125},
 {"brand": "TryNova", "domain": "trynova.store", "pid": "color_foundation", "age": "домен с апреля 2026", "fact": "5 объявлений старше 90 дней, самое старое 100 дней; все от страницы «Trending On K-Beauty» и ведут на статью-подборку ◆. Сигнал на нижней планке ◈.", "leader": "Лидеры: Luxe, Prime Prometics, Smooche", "reg": "2026-04-09", "ad_days": 100},
 {"brand": "Holicow", "domain": "tryholicow.com", "pid": "tallow_balm", "age": "домен с мая 2025", "fact": "Взбитый бальзам из жира с мёдом. 7 объявлений старше 90 дней, самое старое 163 дня; 5 от страницы бренда, 2 от «Rebecca Brown» ◆.", "leader": "Лидер: Ancestral", "reg": "2025-05-26", "ad_days": 163}]
g["_followers_note"] += " Watch products updated 2026-11-11 from the full 90+ day phrase pull; bar: 5+ long ads (owner: only strong signals)."
p.write_text(json.dumps(g, ensure_ascii=False, indent=1), encoding="utf-8"); print("ok groups")

q = H / "ru.json"; r = json.loads(q.read_text(encoding="utf-8")); a = r["article"]["color_foundation"]
for item in a["reality"]:
    if item[0] == "В рекламе держатся два молодых магазина":
        item[0] = "В рекламе держатся пять молодых магазинов"
        item[1] = ("Hestia (магазин из видео; домен с марта 2026-го, витрина Lumine Skin с сентября 2025-го): 383 объявления 90+ дней, самое старое 371 день ◆. Hanae: стик «подстраивается под тон кожи», 66 объявлений 90+, 12 старше 180 ◆. "
                   "Yuki: 40 объявлений 90+ от страницы «Korean Foundation Tips» ◆. Facelove: 14 объявлений стика 90+, 167 дней ◆. TryNova: 5 объявлений, 100 дней ◆ (архив Meta через Apify, 11.11.2026).")
a["take"] = a["take"].replace("В Facebook держатся две молодые копии, Facelove и Hanae, у Hanae стик рекламируется 245 дней;", "В Facebook держатся пять молодых копий, сильнее всех Hestia из видео (383 объявления 90+ дней);")
assert "Hestia" in a["take"] and any("пять молодых" in i[0] for i in a["reality"])
q.write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8"); print("ok ru")
