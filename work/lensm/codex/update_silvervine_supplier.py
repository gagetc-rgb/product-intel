import csv
from pathlib import Path
p=Path(__file__).resolve().parent
f=p/'cogs.csv';url='https://cupabear.en.made-in-china.com/product/NmWYAPQxqsVH/China-Wholesale-Natural-Cat-Chew-Catnip-Silvervine-Wooden-Stick-Molar-Interactive-Cat-Toy.html'
with f.open(encoding='utf-8-sig',newline='') as stream:
 reader=csv.DictReader(stream);fields=reader.fieldnames;rows=list(reader)
if not any(row['source_url']==url for row in rows):
 rows.append(dict(category='silvervine_cat_chew_sticks',supplier='Anhui Keynovo Biotech Co., Ltd.',product='Silvervine chew sticks, listed as pieces; packaging says 10 pcs/bag',price_at_500_usd='$0.47 per listed piece at 500–999; unit/pack ambiguity unresolved',price_at_5000_usd='$0.45 per listed piece at 1,000+; unit/pack ambiguity unresolved',moq='200 listed pieces',private_label='OEM/ODM and logo customization available; minimum for custom order unknown',lead_time='5–15 days in attributes; generic page text also says dispatch within 3–5 days; 500/5000-specific production lead time unknown',source_url=url,source_date='2026-11-10',tier='◈',notes='Live public Made-in-China page accessed; seller listing, not quote. Packing says 10PCS/bag and product-name attribute inconsistently says cat climbing tree. Verify what price unit includes and obtain a binding quote; shipping excluded.'))
with f.open('w',encoding='utf-8-sig',newline='') as stream:
 writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader();writer.writerows(rows)
with (p/'METHOD_LOG.md').open('a',encoding='utf-8') as stream:stream.write('\n- 2026-11-10: live logged-off Made-in-China supplier listing '+url+'; USD tiers, customization and caveats recorded in cogs.csv. Second product page https://www.made-in-china.com/showroom/449a126ba7addd05/product-detailoRFYzIDuAcVN/China-Natural-Silvervine-Cat-Toy-with-Feather-Catnip-Wood-Stick-Wrapped-with-Jute-Rope.html timed out in browser; search copy last month, not counted as current listing.\n')
