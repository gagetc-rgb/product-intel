"""Tools page update, 2026-11-11 (owner): Apify is in use, EchoTik has a paid tier, Kalodata/FastMoss are one row, Semrush/Similarweb limits stated."""
import json, pathlib
H = pathlib.Path(__file__).parent
p = H / "tools_ru.json"; t = json.loads(p.read_text(encoding="utf-8"))
G = {g[0]: g for g in t["groups"]}
have, free, trial = G["have"][3], G["free"][3], G["trial"][3]

for r in have:
    if r[0] == "EchoTik":
        r[1] = "$0 · Pro $14,9/мес"
        r[2] = "Продажи товаров и магазинов в TikTok Shop: сколько штук продал товар за последние 30 дней."
        r[3] = "Бесплатно: топ-10 и только 30 дней, около 6 поисков в день. Есть платный Pro за $14,9 в месяц; что он открывает сверх этого, проверить до оплаты ◈."
apify = next(r for r in free if r[0] == "Apify"); free.remove(apify)
have.insert(1, ["Apify", "$5 в месяц бесплатно",
                "Готовые сборщики данных. 11 ноября выгрузили 2 524 объявления из архива Meta за $1,97: все долгие объявления 8 копий (какой товар продаёт каждое и от какой страницы) и новую волну по 6 товарам.",
                "Сборщик curious_coder, $0,75 за 1 000 объявлений. Повтор 8 декабря около $2. Сборщики Amazon дороже (~$5 за 1 000 строк) и истории продаж не дают."])
for r in free:
    if r[0] == "Semrush":
        r[3] = "10 запросов в день. Считает только переходы из поиска Google без рекламы, а наши магазины живут на рекламе в Meta, поэтому у них часто ноль. Это оценка, а не счётчик."
    if r[0] == "Similarweb без аккаунта":
        r[3] = "Около 3 проверок в день, только 3 последних месяца. Это оценка по панели пользователей, а не счётчик; у маленьких сайтов пишет «мало данных», а копии почти все маленькие."
k = next(r for r in trial if r[0] == "Kalodata"); f = next(r for r in trial if r[0] == "FastMoss")
trial[trial.index(k)] = ["Kalodata или FastMoss", "7 дней",
                         "История TikTok Shop до ~1 000 дней: кто там вырос, а кто пропал. Берём один; второй только для сверки, если цифры покажутся странными.",
                         "Kalodata: без карты, 10 поисков в день, потом ~$50–60 в месяц. FastMoss: без карты и автопродления, потом $49–89 в месяц."]
trial.remove(f)
for r in trial:
    if r[0] == "Similarweb, полная версия":
        r[3] = "Нужна карта; на 8-й день спишут $199, отменить в ту же неделю. Те же оценки, что и без аккаунта, только подробнее; маленькие сайты видит так же плохо."
for sec in t["matrix"]:
    for r in sec[1]:
        if r[0] == "Apify": r[1] = "реклама Meta целиком: все объявления магазина"; r[3] = "have"
        if r[0] == "Semrush": r[1] = "переходы из поиска Google (оценка)"
        if r[0] == "Similarweb": r[1] = "визиты и каналы (оценка, крупные сайты)"
        if r[0] == "EchoTik": r[1] = "продажи за 30 дней; есть платный Pro"
p.write_text(json.dumps(t, ensure_ascii=False, indent=1), encoding="utf-8"); print("tools ok")

s = H / "make_story.py"; x = s.read_text(encoding="utf-8")
a = '["EchoTik", "продажи в TikTok Shop за 30 дней"]'; assert x.count(a) == 1
x = x.replace(a, '["EchoTik", "продажи в TikTok Shop за 30 дней; есть платный Pro"]')
a = '["Meta Ad Library", "возраст рекламы каждого магазина"]'; assert x.count(a) == 1
x = x.replace(a, a + ', ["Apify", "вся реклама магазина из архива Meta, $5 в месяц бесплатно"]')
s.write_text(x, encoding="utf-8"); print("story ok")
