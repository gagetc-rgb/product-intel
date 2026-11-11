import csv
from pathlib import Path
p=Path(__file__).resolve().parent; f=p/'cogs.csv'
with f.open(encoding='utf-8-sig',newline='') as stream:
 r=csv.DictReader(stream);fields=r.fieldnames;rows=list(r)
for row in rows:
 if row['supplier']=='Shandong Super Pet Supply Co., Ltd.' and 'templated pricing' not in row['notes']:
  row['notes']+=' Identical tiers also appear on unrelated products by this supplier, suggesting templated pricing; do not use as confirmed economics. Compare https://isuperpet.en.made-in-china.com/product/RwZaMWKcSkYN/China-Factory-Price-Wholesale-Hot-Sale-Interactive-3-Layer-Pet-Cat-Turntable-Toy-with-Rotating-Ball.html (search copy read 2026-11-10).'
with f.open('w',encoding='utf-8-sig',newline='') as stream:
 w=csv.DictWriter(stream,fieldnames=fields);w.writeheader();w.writerows(rows)
