"""Turmeric soap after the 2026-11-11 checks (work/turmeric/TURMERIC_2026-11-11.md): Apify Meta pull, TikTok Shop pull, store prices.
Glowvani (domain 2025-01-15) holds a turmeric-soap ad 102 days -> one young copy by the v2.4 rule; group moves to watch.
Also: counter labels for the two '20' counters (owner)."""
import json, pathlib, re
H = pathlib.Path(__file__).parent
def rep(path, pairs):
    p = H / path; t = p.read_text(encoding="utf-8")
    for a, b in pairs:
        n = t.count(a); assert n == 1, (path, a[:60], n); t = t.replace(a, b)
    p.write_text(t, encoding="utf-8"); print("ok", path)

s = (H / "make_story.py").read_text(encoding="utf-8")
s2 = re.sub(r'\["turmeric_soap", \d+, \d+\]', '["turmeric_soap", 5, 1]', s); assert s2 != s
s2 = s2.replace('[20, "", "товаров сверили с Amazon"]', '[20, "", "товаров сверили с Amazon: 4 774 карточки поиска, по 5 страниц на товар"]')
s2 = s2.replace('[20, "", "расчётов денег с продажи"]', '[20, "", "расчётов денег с продажи: что остаётся с заказа до рекламы"]')
assert "4 774" in s2 and "до рекламы" in s2
(H / "make_story.py").write_text(s2, encoding="utf-8"); print("ok make_story")

p = H / "groups_ru.json"; g = json.loads(p.read_text(encoding="utf-8"))
g["no"].remove("turmeric_soap"); g["watch"].append("turmeric_soap")
g["why"]["turmeric_soap"] = ("Facebook: держится одна молодая копия, Glowvani (домен с января 2025-го), её объявление мыла идёт 102 дня ◆; доказательство слабое, одно объявление. "
    "Лидер Earthly Derm держит 88 объявлений 90+ дней, все от своей страницы ◆. За ним идёт свежая волна: Curculia Paris, Kaoli, Kevaros, Truetona, всем 1–41 день ◆. "
    "В TikTok Shop это корейская тема «койевая кислота + куркума»: medicube и Dr.Melaxin продают десятки тысяч штук ◆. На Amazon по $11 за брусок денег нет, но в своём магазине мыло продают наборами.")
g["change"]["turmeric_soap"] = "Вторая молодая копия с рекламой 90+ дней и деньги своего магазина по наборам (3 бруска за $39–49). Возраст STEM & SOUL (109 дней рекламы) не проверен: реестр .co не отвечает."
g["followers"].append({"brand": "Glowvani", "domain": "glowvani.com", "pid": "turmeric_soap", "age": "домен с января 2025",
    "fact": "Мыло с куркумой «Brightening Beauty Bar». Одно объявление идёт 102 дня, остальные моложе 90 ◆; реклама от своей страницы ◆. Слабый сигнал: одно объявление ◈. Найден 11 ноября при выгрузке рекламы по фразе «turmeric soap» через Apify.",
    "leader": "Лидер: Earthly Derm", "reg": "2025-01-15", "ad_days": 102})
p.write_text(json.dumps(g, ensure_ascii=False, indent=1), encoding="utf-8"); print("ok groups")

take_old = "Товар одного бренда: Earthly Derm растёт, пока общий спрос падает. Это история бренда, а не категории. Входить имеет смысл, только если повторять модель Earthly Derm (свой магазин, отзывы, Meta), а не продавать мыло на Amazon."
take_new = ("Не только Earthly Derm. В Facebook за лидером уже держится молодая Glowvani и идёт свежая волна копий; в TikTok Shop тему «койевая кислота + куркума» продают корейские бренды. "
            "Вывод «денег нет» верен только для одного бруска на Amazon за $11: в своём магазине мыло продают наборами (у Earthly Derm 3 бруска за $39–49), и с такого заказа на рекламу остаётся заметно больше ◈. "
            "Против: поиск в Google падает, обещания про пятна похожи на лечебные.")
facts_add = [
    ["В TikTok Shop это большая тема", "По запросу «turmeric soap» в TikTok Shop лидируют корейские бренды: у medicube набор с койевой кислотой и куркумой продан 154 тыс. раз, гель для душа 109 тыс.; у Dr.Melaxin спрей с куркумой 741 тыс., мыло 45,6 тыс. по $24,70 ◆ (счётчики продаж за всё время, TikTok Shop через Apify, 11.11.2026). Earthly Derm в TikTok Shop нет."],
    ["В рекламе Facebook за лидером идёт волна", "Earthly Derm: 88 объявлений старше 90 дней, 44 старше 180, все от своей страницы ◆. Молодая Glowvani (домен с января 2025-го) держит одно объявление 102 дня ◆. STEM & SOUL крутит 109 дней, но возраст домена не проверен ◈. Новые магазины Curculia Paris, Kaoli (оба с мая 2026-го), Kevaros, Truetona запустились 1–41 день назад ◆ (архив Meta через Apify, 11.11.2026)."],
    ["Деньги: наборы, а не брусок", "На Amazon один брусок за $11 почти ничего не оставляет ◈. Но Earthly Derm продаёт в своём магазине наборы по 1–5 брусков с подпиской (3 бруска $39–49), Dr.Melaxin берёт $24,70 за брусок в TikTok Shop ◆. С заказа на $40–50 после товара, почты и комиссий остаётся грубо $25–30 до рекламы, как у мыла с хурмой ◈."],
]
for f in ["ru.json"]:
    q = H / f; r = json.loads(q.read_text(encoding="utf-8")); a = r["article"]["turmeric_soap"]
    assert a["take"] == take_old; a["take"] = take_new
    a["reality"] = facts_add + a["reality"]
    a["next"] = ["Возраст STEM & SOUL и доживут ли до 90 дней Curculia Paris и Kaoli (замер 8 декабря)", "Деньги своего магазина по наборам: точный расчёт", "Регуляторика: койевая кислота и обещания про пятна"]
    q.write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8"); print("ok", f)
rc = (H / "ru_content.py").read_text(encoding="utf-8")
if take_old in rc:
    (H / "ru_content.py").write_text(rc.replace(take_old, take_new), encoding="utf-8"); print("ok ru_content take (facts only in ru.json)")
