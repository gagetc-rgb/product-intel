import csv
from pathlib import Path
p=Path(__file__).resolve().parent;f=p/'cogs.csv'
url='https://www.made-in-china.com/price/prodetail_Chemical-Pest-Control_uPrpndRATJcD.html'
with f.open(encoding='utf-8-sig',newline='') as stream:
 r=csv.DictReader(stream);fields=r.fieldnames;rows=list(r)
if not any(x['source_url']==url for x in rows):rows.append(dict(category='rodent_repellent_pouches',supplier='Ningbo Sunda International Trade Co., Ltd.',product='Mouse and rat repellent pouches; specification says 10 pouches',price_at_500_usd='$1.99 per listed set, tier 500–2,999',price_at_5000_usd='$1.89 per listed set, tier 3,000–9,999',moq='500 sets',private_label='OEM/ODM; package, label, logo, quantity and scent customization stated; custom-order MOQ unknown',lead_time='unknown; supplier contact needed',source_url=url,source_date='2026-11-10',tier='◈',notes='Live supplier listing, not quote; table says size 10 pouches but confirm set contents. Description lists botanical extracts but no exact formula; generic attributes say target pests insects and weekly duration. US registration, compliance, actual effectiveness and shipping not established.'))
with f.open('w',encoding='utf-8-sig',newline='') as stream:
 w=csv.DictWriter(stream,fieldnames=fields);w.writeheader();w.writerows(rows)
with (p/'METHOD_LOG.md').open('a',encoding='utf-8') as stream:stream.write('\n- 2026-11-10: public Made-in-China rodent pouch listing '+url+' was slow and initial navigation timed out, then rendered without retry; USD price tiers and unit uncertainty kept in cogs.csv. Closed agent-created tabs after use at user request.\n')
