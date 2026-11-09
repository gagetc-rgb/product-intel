"""Import the owner's manual Amazon CSVs (US ZIP 10001, collected 2026-11-08 per AMAZON_TASK.md).
Part A (amazon_search_us.csv) -> graveyard_us/<pid>.json in the same schema as graveyard_us.py (source='manual').
Part B (amazon_brands_us.csv) -> amazon_manual/brands_us.json {asin: brand}.
Run from work/blind: python amazon_manual/import_manual.py"""
import csv, json, re, pathlib
B = pathlib.Path(__file__).resolve().parents[1]
def num(s):
    m = re.search(r"([\d.,]+)\s*([KkMm]?)\+?", s or "")
    if not m: return 0
    v = float(m.group(1).replace(",", "")); return int(v * {"k": 1000, "m": 1_000_000}.get(m.group(2).lower(), 1))
rows = list(csv.DictReader(open(B / "amazon_manual/amazon_search_us.csv", encoding="utf-8-sig")))
cats = {}
for r in rows:
    L = cats.setdefault(r["category_id"], {})
    old = L.get(r["asin"], {})
    L[r["asin"]] = {"title": r["title"], "brand": "", "first": "", "b": max(num(r["bought_past_month"]), old.get("b", 0)),
                    "r": max(num(r["review_count"]), old.get("r", 0)), "price": r["price"], "stars": r["rating"], "img": r["image_url"],
                    "page": int(r["page"]), "zip": "10001", "source": "manual", "collected_at": r["collected_at"]}
for pid, L in cats.items():
    q = {"whitening_powder": "teeth whitening powder", "lash_serum": "eyelash growth serum", "hair_serum": "hair growth serum", "prewash_oil": "pre wash hair oil"}[pid]
    (B / "graveyard_us" / f"{pid}.json").write_text(json.dumps({"q": q, "pages_done": 5, "source": "manual (AMAZON_TASK.md)", "listings": L}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(pid, len(L), "listings")
br = {}
for r in csv.DictReader(open(B / "amazon_manual/amazon_brands_us.csv", encoding="utf-8-sig")):
    b = r["brand_table"] or re.sub(r"^(Visit the |Brand:\s*)|( Store)$", "", r["brand_line"]).strip()
    br[r["asin"]] = {"cat": r["category_id"], "brand": b, "brand_line": r["brand_line"], "bought": r["bought_past_month"], "price": r["price"]}
(B / "amazon_manual" / "brands_us.json").write_text(json.dumps(br, ensure_ascii=False, indent=1), encoding="utf-8")
print("brands", len(br))
