"""Every number >= 100 written in content/NN_*.md must exist in the data behind that page (digest, verdict row,
revenue floor, meta_pages, v2.0 brand table, ID-scan row). Prints numbers it cannot find, for a manual check."""
import json, re, pathlib
H = pathlib.Path(__file__).parent
def nums(o, acc):
    if isinstance(o, dict): [nums(v, acc) for v in o.values()]
    elif isinstance(o, (list, tuple)): [nums(v, acc) for v in o]
    elif isinstance(o, (int, float)): acc.add(round(o))
    elif isinstance(o, str):
        for m in re.findall(r"\d[\d,]*\.?\d*", o): acc.add(round(float(m.replace(",", ""))))
    return acc
D = json.load(open(H / "dossier_data.json", encoding="utf-8"))["categories"]
REV = json.load(open(H / "revenue_floor.json"))
bad = 0
for f in sorted((H / "content").glob("[0-2][0-9]_*.md")):
    pid = f.stem[3:]
    if pid not in D: continue
    known = nums(json.load(open(H / "digest" / f"{pid}.json", encoding="utf-8")), set())
    nums(D[pid], known); nums(REV.get(pid, {}), known)
    text = re.sub(r"\]\([^)]*\)|`[^`]*`|^---.*?^---", "", f.read_text(encoding="utf-8"), flags=re.S | re.M)
    miss = []
    for m in re.finditer(r"(?<![\w.$])(\d{1,3}(?:,\d{3})+|\d{3,})(?![\w%])", text):
        n = int(m.group(1).replace(",", ""))
        if 2000 <= n <= 2030: continue  # years
        if n not in known: miss.append(m.group(1))
    if miss: bad += len(miss); print(f"{f.name}: {sorted(set(miss))}")
print("unmatched:", bad)
