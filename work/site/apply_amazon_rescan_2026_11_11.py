"""Hand-written texts after the automated Amazon re-scan of lash serum and tooth powder (2026-11-11), replacing the manual 2026-11-08 data.
Lash: 5 of 40 newcomers sell 1,000+ (12.5%, Wilson 6-26%), shelf 211K, top-3 46%. Powder: shelf 16,750, 2 of 22 newcomers."""
import pathlib, re
H = pathlib.Path(__file__).parent
def sub(path, pairs):
    p = H / path; t = p.read_text(encoding="utf-8")
    for a, b in pairs:
        n = t.count(a); assert n >= 1, (path, a[:60]); t = t.replace(a, b)
    p.write_text(t, encoding="utf-8"); print("ok", path)
lash = [
 ("На Amazon пробивается 8% новичков", "На Amazon пробивается 13% новичков"),
 ("пробиваются 8% новичков", "пробиваются 13% новичков"),
 ("У трёх лидеров 49% полки ◆.", "У трёх лидеров 46% полки ◆."),
 ("Из 50 новых продавцов 4 продают 1 000+ в месяц: 8% (с учётом погрешности от 3 до 19%) ◈.", "Из 40 новых продавцов 5 продают 1 000+ в месяц: 13% (с учётом погрешности от 6 до 26%) ◈. Замер 11 ноября, автоматический; ручной замер 8 ноября дал 4 из 50, а совпадение значков «куплено за месяц» 173 из 208 общих товаров."),
 ("Большой рынок, но пробивается 8% новичков", "Большой рынок, но пробивается 13% новичков"),
]
for f in ["ru.json", "ru_content.py", "groups_ru.json"]:
    p = H / f; t = p.read_text(encoding="utf-8")
    for a, b in lash: t = t.replace(a, b)
    t = t.replace("(16 тыс. покупок в месяц)", "(17 тыс. покупок в месяц)")
    p.write_text(t, encoding="utf-8"); print("ok", f)
t = (H / "template_ru.html").read_text(encoding="utf-8")
assert "пробивается 8% новичков, а не 16%" in t
t = t.replace("пробивается 8% новичков, а не 16%", "пробивается 13% новичков (5 из 40), а не 16%")
(H / "template_ru.html").write_text(t, encoding="utf-8"); print("ok template")
