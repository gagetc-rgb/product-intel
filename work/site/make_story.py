"""Build work/site/story_ru.json: the data and texts for the story blocks on the home page (site plan v2.5, 2026-11-10).
Numbers come from: work/lensm/M2_RESULT.md, work/bigspy/persimmon_soap_advertisers_2026-11-10.tsv, work/margin/margin.json,
work/audit/cred_check.json, work/report/SUMMARY_RU_2026-11-10.md (checked in work/report/DEVILS_ADVOCATE_2026-11-10.md).
Usage: python work/site/make_story.py  (then build_site.py)."""
import csv, json, pathlib
H = pathlib.Path(__file__).resolve().parent
R = H.parents[1]

# BigSpy, "persimmon soap", 2 years, United States only (2026-11-11), sorted by running days: the 60 longest of 150 advertisers,
# one ad per advertiser; dates = first/last seen ("Special Creative" cards show 2 running days, so the span is used). Owner 2026-11-11: US only, like the method.
race = []
LAB = {"mira***l.com": "Mirai Clinical (лидер), 513 дней", ("try***.com", "Grand***ournal"): "Kaori, 235 дней, ещё крутится", ("try***.com", "Ai***ori"): "Kaori, другая страница, 61 день",
       "aur***.co": "aur***.co, 88 дней, ещё крутится"}
for r in csv.DictReader(open(R / "work/bigspy/persimmon_soap_us_advertisers_2026-11-11.tsv", encoding="utf-8"), delimiter="	"):
    lab = LAB.get((r["domain"], r["page"])) or LAB.get(r["domain"], "")
    row = [max(r["first_seen"], "2026-03-01"), r["last_seen"], int(r["span_days"]), lab]
    # Kaori: BigSpy last saw this page on 2026-10-22, but Meta shows its ad (2330372864056320, started 2026-03-20) still active on 2026-11-11:
    # a BigSpy crawl gap (work/bigspy/BIGSPY_2026-11-11.md), so the line follows Meta
    if (r["domain"], r["page"]) == ("try***.com", "Grand***ournal"): row = ["2026-03-20", "2026-11-11", 235, lab]
    race.append(row)

story = {
 "counters": [[3417, "", "объявлений в Facebook и Instagram разобрали"], [228, "", "магазинов проверили по одному"], [238, "", "рекламодателей из архива рекламы прочитали"],
              [31, "", "магазин: возраст рекламы записан, повтор 11 декабря"], [20, "", "товаров сверили с Amazon и посчитали, сколько остаётся с продажи до рекламы"]],
 # 3417 = 893 ads read in the M2 phrase samples + 2524 pulled through Apify on 2026-11-11 (work/apify/APIFY_RESULTS_2026-11-11.md); 893, 33-70 per product (copies block caption); restored 2026-11-11 at the owner's request
 # 2026-11-11: 228 = distinct domains in work/lensm/m2_stores.csv, rp/stores_*_full.csv, codex/meta_stores.csv, store_facts.csv, follower_pages.csv;
 # 238 = rows read in work/bigspy/*.tsv; 31 = domains counted 30/60/90/180 on 2026-11-11 in codex/meta_stores.csv
 "claims": [
  ["«Товар хорошо продаётся»", "ok", "Да. Лидеры настоящие и растут: у Mirai Clinical отзывов за август–октябрь вдвое больше, чем год назад ◆. У Earthly Derm в 7,6 раза больше ◆."],
  ["«Закупка $1–2 за штуку»", "part", "В 3 видео из 5, где автор называет цену, она совпадает с ценами поставщиков. В двух (патчи для пор, крем для депиляции) у него в 2–10 раз дороже: это цена поштучной покупки, а не оптовая ◈."],
  ["«Магазин делает $7–14 млн в месяц»", "est", "Это оценка сервиса слежки, а не отчёт магазина. Shopify продажи магазинов не публикует, поэтому любая такая сумма посчитана по косвенным признакам. Для вопроса «продаётся ли» годится, для бизнес-плана нет."],
  ["«2 000 объявлений, значит $8 млн в месяц»", "bad", "Долгая реклама и правда говорит, что она окупается. Но число объявлений показывает, сколько магазин тестирует, а не сколько продаёт: в мыле с хурмой у большинства рекламодателей объявление жило 1–3 дня ◆. У Skult при «2 000 объявлений» около 1 000 покупок в месяц на Amazon ◆."]],
 "grid": [["tallow_balm", 11, 3], ["compression_socks", 4, 0], ["hair_serum", 3, 0], ["color_foundation", 7, 5], ["hair_removal_cream", 2, 0],
          ["persimmon_soap", 4, 3], ["whitening_powder", 2, 2], ["lash_serum", 1, 1], ["chin_wrap", 0, 0], ["turmeric_soap", 7, 3], ["body_oil", 1, 0],
          ["scent_diffuser", 1, 0], ["dog_fountain", 1, 0], ["exfoliating_towel", 1, 0], ["prewash_oil", 3, 0], ["shower_filter", 0, 0], ["pore_patch", 0, 0], ["neck_cream", 0, 0],
          ["rosemary_oil", 0, 0], ["magnesium_spray", 0, 0]],
 "race": race,
 "soap": {
  "pair": [["Mirai Clinical", "лидер", [["с 2014 года", "в деле"], ["Shark Tank", "2025"], ["×2", "отзывов за год"]]],
           ["Kaori", "копия", [["9 мес.", "магазину"], ["210", "объявлений старше 3 мес."], ["1 950", "покупок в месяц на Amazon"]]]],
  "money": {"order": 48, "parts": [["Товар с доставкой из Китая и пошлиной", 5, 11], ["Почта до покупателя (USPS)", 10, 14], ["Оплата и возвраты", 2.7, 2.7]],
            "left": [20, 30]},
  "check": [["Слабое место лидера: доставка", "Чаще всего в плохих отзывах Mirai жалуются на доставку: долго или пришло не всё (12 из 35) ◈."],
            ["Заголовки уже затёрты", "Заголовок «Is Your Persimmon Soap Real?» уже у пяти страниц, «обзоры пяти мыл» у четырёх ◆."],
            ["Сколько можно отдать рекламе", "С набора из 4 брусков за $48 после товара, почты и комиссий остаётся $20–30 ◈. Столько в среднем можно тратить на рекламу в расчёте на каждый заказ, чтобы первая покупка не ушла в минус; повторные покупки дают запас сверху."]]},
 "know": [["Знаем точно ◆", ["Кто лидер и сколько живёт его реклама", "Возраст магазинов-копий", "Сколько копий мыла, сыворотки и порошка в США продержались 90 дней", "Сколько покупают на Amazon"]],
          ["Оцениваем ◈", ["Окупается ли реклама, которая живёт 90+ дней", "Сколько остаётся с заказа в своём магазине", "Продажи в TikTok Shop (по оценке EchoTik)"]],
          ["Пока не знаем", ["Сколько стоит реклама за один заказ", "Сколько копий сдалось в бальзаме и остальных товарах", "Продажи в TikTok Shop дальше 30 дней назад"]]],
 "plan": [["10–16 ноября", "Образцы мыла и бальзама от 2–3 поставщиков", "Сделано: в мыле с хурмой 90+ дней держат рекламу три молодые копии (Kaori, Cachi Naturals, Bella Via), в мыле с куркумой тоже три; цены наборов Kaori прочитаны. Осталось: что можно обещать в рекламе мыла по правилам FDA", ""],
          ["17–30 ноября", "Поставщик, упаковка, страница магазина", "Точные деньги с заказа: вес посылки, тарифы склада. Планку успеха теста записываем до запуска", ""],
          ["27 ноября – 1 декабря", "", "Тест не запускаем: в Чёрную пятницу реклама дороже обычного, результат будет искажён ◈", "stop"],
          ["8 декабря", "Магазин готов", "", ""],
          ["9–20 декабря", "Пробная реклама на $200–500", "Читаем результат против записанной планки", "go"],
          ["11 декабря", "Повторный замер", "Те же магазины: кто выключил рекламу, кто вырос, кто из новых копий перешёл 90 дней (11-го, когда обновится кредит Apify)", ""]],
 "tiktok": [["persimmon_soap", "Beamach Oral Care", "~9 мес.", 1400, 3300, "2,4", "up"],
            ["turmeric_soap", "Dr.Melaxin", "~8 мес.", 5700, 6500, "1,1", "flat"],
            ["tallow_balm", "Terra Lotus", "~2 года", 27600, 6900, "0,25", "down"],
            ["tallow_balm", "LOPEIE", "~1 год", 12900, 4000, "0,3", "down"],
            ["lash_serum", "EPAIS", "~2 года", 13400, 91900, "6,9", "up"]],
 "free": [["Meta Ad Library", "возраст рекламы каждого магазина"], ["Apify", "вся реклама магазина из архива Meta, $5 в месяц бесплатно"], ["BigSpy", "выключенная реклама, около 3 поисков в день"],
          ["RDAP и Wayback", "возраст магазина: дата домена и первая копия сайта"], ["Amazon", "покупки за месяц и возраст карточек"],
          ["camelcamelcamel", "цены на Amazon за год"], ["EchoTik", "продажи в TikTok Shop за 30 дней; есть платный Pro"], ["Google Trends", "растёт ли спрос"],
          ["Trustpilot и отзывы магазинов", "на что жалуются покупатели лидеров"], ["Сайты магазинов", "цены, наборы, подписки"],
          ["Made-in-China и Alibaba", "цены поставщиков"]],
 "upgrade": [["Keepa Pro", "€29 в месяц", "нужно", "История продаж и отзывов на Amazon за годы: кто из новичков вырос, а кто зашёл и умер."],
             ["Kalodata или FastMoss", "7 дней бесплатно", "пробный", "История TikTok Shop до ~1 000 дней: кто там вырос и кто пропал."],
             ["Similarweb", "7 дней бесплатно", "пробный", "Сколько трафика у лидеров и какая доля из рекламы. Только для финалистов, потом отменить."],
             ["BigSpy Starter", "$69 в месяц", "по желанию", "Больше поисков в день: весь архив рекламы за день, а не за неделю."],
             ["Apify", "$5 в месяц бесплатно", "объём", "Готовые сборщики: те же источники в сотни раз быстрее, когда переходим от 5 товаров к 20."]],
 "tools": [["BigSpy", "$69 в месяц", "Архив рекламы с уже выключенными объявлениями. Сразу видно, сколько копий пришло в мыло и бальзам и сколько сдалось. Ждать месяц не нужно."],
           ["Keepa", "€29 в месяц", "История Amazon за годы: кто пришёл, вырос и исчез."],
           ["FastMoss", "$29 первый месяц, дальше $49", "Продажи TikTok Shop: продают ли там мыло и бальзам и кто растёт."]],
}
story["toolsPage"]=json.load(open(H / "tools_ru.json", encoding="utf-8"))
json.dump(story, open(H / "story_ru.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("story_ru.json:", len(race), "race rows")
