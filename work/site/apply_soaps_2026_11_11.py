"""Soaps after the full 90+ day Meta pull (work/apify/runSoap*, runSoapDom*, soap_candidates_2026-11-11.json; 2026-11-11).
Persimmon: young copies Kaori, Cachi Naturals (2026-08-03, 7 ads, 91 d), Bella Via (2026-03-25, 6 ads, 90 d, persona page); old Swarva (2024-04-27, 13 ads, 124 d); Aurellee (age unknown, 3 ads, 96 d).
Turmeric: young Solrise (2025-04-23, 6 ads, 5 at 180+, 477 d), Glowvani (2025-01-15, 14 ads, 112 d), Derm Glow / myskincycle.com (2026-04-10, 16 ads, 112 d, kojic acid soap);
STEM & SOUL (age unknown: .co registry silent, first Wayback 2026-05-15; 166 ads, 91 at 180+, 371 d); old: Honey Glow, Herb'N Eden, Herbal Ciddy."""
import json, pathlib, re
H = pathlib.Path(__file__).parent
def rep(path, pairs):
    p = H / path; t = p.read_text(encoding="utf-8")
    for a, b in pairs:
        n = t.count(a); assert n == 1, (path, a[:60], n); t = t.replace(a, b)
    p.write_text(t, encoding="utf-8"); print("ok", path)

s = (H / "make_story.py").read_text(encoding="utf-8")
s = re.sub(r'\["persimmon_soap", \d+, \d+\]', '["persimmon_soap", 5, 3]', s); s = re.sub(r'\["turmeric_soap", \d+, \d+\]', '["turmeric_soap", 7, 3]', s)
(H / "make_story.py").write_text(s, encoding="utf-8"); print("ok make_story")

NOW = "Сейчас в Meta 90+ дней держат ещё Swarva (давний магазин, 124 дня), Cachi Naturals (91 день) и Bella Via (90 дней) ◆; обе последние молодые и перешли 90 дней только что"
rep("template_ru.html", [
 ("90 дней прошли только лидер Mirai и Kaori ◆.</p>", "В архиве BigSpy 90 дней прошли только лидер Mirai и Kaori ◆. " + NOW + " (архив Meta, 11 ноября).</p>"),
 ('persimmon_soap:"150 рекламодателей за два года, 90+ дней продержали двое"', 'persimmon_soap:"150 рекламодателей за два года, в архиве 90+ дней продержали двое; сейчас в Meta держат ещё Swarva, Cachi Naturals и Bella Via"'),
])
pr = [("За два года мыло с хурмой рекламировали в США 150 магазинов и страниц; 90+ дней продержали только двое:", "За два года мыло с хурмой рекламировали в США 150 магазинов и страниц; в архиве BigSpy 90+ дней продержали только двое:"),
      ("декабрьская проверка покажет, перейдут ли они 90 ◈.", "декабрьская проверка покажет, перейдут ли они 90 ◈. " + NOW + "; Cachi Naturals рекламируется от своего имени, Bella Via от выдуманной «Mari Tanaka» (архив Meta, 11.11.2026)."),
      ('"Из 150 рекламодателей удержались двое"', '"Копии начинают держаться"'),
      ("Окно: свой магазин и реклама в Meta на аудиторию 55+, как делает Kaori.", "Окно: свой магазин и реклама в Meta на аудиторию 55+, как делает Kaori; за ней уже держатся ещё две молодые копии, Cachi Naturals и Bella Via.")]
rep("ru.json", pr); rep("ru_content.py", pr)

p = H / "groups_ru.json"; g = json.loads(p.read_text(encoding="utf-8"))
g["why"]["persimmon_soap"] = ("Facebook: держатся три молодые копии: Kaori (235 дней, в основном через страницы с именами людей), Cachi Naturals (91 день, от своего имени) и Bella Via (90 дней, от выдуманной «Mari Tanaka») ◆; "
    "давняя Swarva держит рекламу 124 дня. На Amazon пробивается каждый десятый новичок, с продажи остаётся 27–44%; в TikTok продажи главного продавца растут (×2,4).")
g["change"]["persimmon_soap"] = "Это история своего магазина и рекламы, как у Kaori. Cachi Naturals и Bella Via только что перешли 90 дней: замер 8 декабря покажет, удержатся ли они; Cachi интереснее, она рекламируется от своего имени."
g["why"]["turmeric_soap"] = ("Facebook: держатся три молодые копии: Solrise (домен с апреля 2025-го, объявление 477 дней), Glowvani (14 объявлений, 112 дней) и Derm Glow (16 объявлений мыла с койевой кислотой, 112 дней), все от своего имени ◆. "
    "STEM & SOUL держит 166 объявлений 90+ дней и 91 старше 180, но возраст домена не проверен ◈. Лидер Earthly Derm: 88 объявлений 90+ дней ◆. "
    "В TikTok Shop тему «койевая кислота + куркума» продают корейские бренды десятками тысяч штук ◆. На Amazon по $11 за брусок денег нет, но в своём магазине мыло продают наборами.")
F = {(f["brand"], f["pid"]): f for f in g["followers"]}
F[("Glowvani", "turmeric_soap")].update(fact="Мыло с куркумой «Brightening Beauty Bar». 14 объявлений старше 90 дней, самое старое 112 дней, все от своей страницы ◆.", ad_days=112)
g["followers"] += [
 {"brand": "Cachi Naturals", "domain": "cachinaturals.com", "pid": "persimmon_soap", "age": "домен с августа 2026", "fact": "Мыло с хурмой против запаха 2-ноненала. 7 объявлений старше 90 дней, самое старое 91 день, все от своей страницы ◆. Перешла 90 дней только что ◈.", "leader": "Лидер: Mirai Clinical, с 2014 года", "reg": "2026-08-03", "ad_days": 91},
 {"brand": "Bella Via", "domain": "bellaviashop.com", "pid": "persimmon_soap", "age": "домен с марта 2026", "fact": "6 объявлений старше 90 дней, самое старое 90 дней; все от страницы выдуманной «Mari Tanaka» и ведут на статью «Is your persimmon soap real?» ◆.", "leader": "Лидер: Mirai Clinical, с 2014 года", "reg": "2026-03-25", "ad_days": 90},
 {"brand": "Solrise", "domain": "shopsolrise.com", "pid": "turmeric_soap", "age": "домен с апреля 2025", "fact": "Мыло с куркумой и койевой кислотой «Glow Bar». 6 объявлений старше 90 дней, 5 старше 180, самое старое 477 дней, все от своей страницы ◆.", "leader": "Лидер: Earthly Derm", "reg": "2025-04-23", "ad_days": 477},
 {"brand": "Derm Glow", "domain": "myskincycle.com", "pid": "turmeric_soap", "age": "домен с апреля 2026", "fact": "Мыло с койевой кислотой, пробный набор. 16 объявлений старше 90 дней, самое старое 112 дней, все от своей страницы ◆.", "leader": "Лидер: Earthly Derm", "reg": "2026-04-10", "ad_days": 112}]
g["_followers_note"] += " Soaps updated 2026-11-11 from the full 90+ day pull (work/apify/soap_candidates_2026-11-11.json)."
p.write_text(json.dumps(g, ensure_ascii=False, indent=1), encoding="utf-8"); print("ok groups")

q = H / "ru.json"; r = json.loads(q.read_text(encoding="utf-8")); a = r["article"]["turmeric_soap"]
for item in a["reality"]:
    if item[0] == "В рекламе Facebook за лидером идёт волна":
        item[1] = ("Earthly Derm: 88 объявлений старше 90 дней, 44 старше 180, все от своей страницы ◆. За ним держатся молодые Solrise (домен с апреля 2025-го, объявление 477 дней), Glowvani (14 объявлений, 112 дней) и Derm Glow (16 объявлений, 112 дней), все от своего имени ◆. "
                   "STEM & SOUL держит 166 объявлений 90+ дней, 91 старше 180, самое старое 371 день; возраст домена не проверен (реестр .co не отвечает, первая копия сайта в Wayback — май 2026-го) ◈. "
                   "Новые Curculia Paris, Kaoli, Kevaros, Truetona запустились 1–41 день назад ◆ (архив Meta через Apify, 11.11.2026).")
a["take"] = a["take"].replace("уже держится молодая Glowvani и идёт свежая волна копий", "держатся три молодые копии (Solrise, Glowvani, Derm Glow) и STEM & SOUL, и идёт свежая волна")
assert "три молодые копии" in a["take"]
q.write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8"); print("ok ru turmeric")
