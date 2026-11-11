import csv
from pathlib import Path
p=Path(__file__).resolve().parent;f=p/'cogs.csv'
url='https://isuperpet.en.made-in-china.com/product/FwdGoaBOcVUZ/China-Safe-Long-Silvervine-Corn-Feathers-Cat-Teaser-Toy.html'
with f.open(encoding='utf-8-sig',newline='') as stream:
 r=csv.DictReader(stream);fields=r.fieldnames;rows=list(r)
if not any(x['source_url']==url for x in rows):rows.append(dict(category='silvervine_cat_chew_sticks',supplier='Shandong Super Pet Supply Co., Ltd.',product='Silvervine teaser/chew with gall nut and raffia; differs from plain-sticks format',price_at_500_usd='$1.00 per listed piece, tier 500–999',price_at_5000_usd='$0.50 per listed piece, tier 1,000+',moq='1 piece in listed price tier; private-label MOQ unknown',private_label='custom service and logo printing listed as available; specific MOQ and cost unknown',lead_time='15–45 days in product table; volume-specific lead time unknown',source_url=url,source_date='2026-11-10',tier='◈',notes='Live logged-off supplier page, listing prices not quotes. Product includes extras, not confirmed identical to leader; packaging states three items per bag or one on cardboard, unclear which corresponds to a listed piece. Identical price tiers appear on unrelated products by this supplier, suggesting templated pricing: do not use as confirmed economics. Shipping excluded.'))
with f.open('w',encoding='utf-8-sig',newline='') as stream:
 w=csv.DictWriter(stream,fieldnames=fields);w.writeheader();w.writerows(rows)
with (p/'METHOD_LOG.md').open('a',encoding='utf-8') as stream:stream.write('\n- 2026-11-10: live Made-in-China Shandong Super Pet listing '+url+'; retained prices with explicit product/packaging ambiguity. The search result https://www.made-in-china.com/video-channel/houeware01_wEOYhptkvTUa_Wholesale-Silvervine-Natural-Teeth-Cleaning-Stick-Cat-Interactive-Chew-Toy.html redirected to generic video-channel landing, so historical search-cache prices were not recorded as live.\n')
