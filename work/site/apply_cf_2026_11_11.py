"""Color foundation texts after the Apify pull (2026-11-11): two young copies, Facelove and Hanae."""
import json, pathlib
H = pathlib.Path(__file__).parent
def rep(path, pairs):
    p = H / path; t = p.read_text(encoding="utf-8")
    for a, b in pairs:
        n = t.count(a); assert n == 1, (path, a[:60], n); t = t.replace(a, b)
    p.write_text(t, encoding="utf-8"); print("ok", path)
pairs = [
 ('"В рекламе держится один молодой магазин"', '"В рекламе держатся два молодых магазина"'),
 ("Facelove Cosmetics: домен с декабря 2025-го, косметика для женщин 50+. У магазина ~40 объявлений старше 90 дней; старейшее объявление тонального стика идёт 166 дней ◆. Из 12 старых объявлений стика 7 идут от страниц бренда, 5 от страниц вроде «The Glow Up» ◆. Старше 180 дней объявлений нет, так что это ранний сигнал ◈ (архив Meta, 11.11.2026).",
  "Facelove Cosmetics: домен с декабря 2025-го, косметика для женщин 50+. Объявлений тонального стика старше 90 дней 14, самое старое 167 дней, старше 180 нет ◆; 9 из 14 от страниц бренда ◆. Hanae (домен с ноября 2025-го, известна по сыворотке для ресниц) продаёт стик, который «подстраивается под тон кожи»: 66 объявлений старше 90 дней, 12 старше 180, самое старое 245 дней, все от страниц магазина ◆ (архив Meta через Apify, 11.11.2026)."),
 ("Самый большой рынок. В Facebook держится одна молодая копия, Facelove; на Amazon пробиваются безымянные.",
  "Самый большой рынок. В Facebook держатся две молодые копии, Facelove и Hanae, у Hanae стик рекламируется 245 дней; на Amazon пробиваются безымянные."),
 ('"Facelove: доживёт ли реклама стика до 180 дней (замер 8 декабря)"', '"Facelove: доживёт ли реклама стика до 180 дней (замер 8 декабря)", "Новые стики Beaumont Voss и TryNova: уже перешли 90 дней, проверить товар и возраст"'),
]
rep("ru.json", pairs); rep("ru_content.py", pairs)
p = H / "groups_ru.json"; g = json.loads(p.read_text(encoding="utf-8"))
g["change"]["color_foundation"] = "Две молодые копии уже есть (Facelove и Hanae). Решит, продаётся ли стик без обещаний, которые нельзя повторить, и сколько остаётся с заказа в своём магазине."
p.write_text(json.dumps(g, ensure_ascii=False, indent=1), encoding="utf-8"); print("groups ok")
