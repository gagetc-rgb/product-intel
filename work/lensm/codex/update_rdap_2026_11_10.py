import csv
from pathlib import Path
p=Path(__file__).resolve().parent;f=p/'store_facts.csv'
dates={'try-kaori.com':'2026-02-11','herbneden.com':'2015-07-24','honeyglownewyork.com':'2024-10-08','diablocosmetics.com':'2018-09-18','facelove-cosmetics.com':'2025-12-28','houseofduaa.com':'2025-08-25','hotelcollection.com':'2003-04-15','cphgrooming.com':'2017-09-01'}
with f.open(encoding='utf-8-sig',newline='') as stream:
 r=csv.DictReader(stream);fields=r.fieldnames;rows=list(r)
for row in rows:
 domain=row['domain']
 if domain not in dates:continue
 url='https://rdap.verisign.com/com/v1/domain/'+domain
 row['domain_registration']=dates[domain]
 if url not in row['source_urls']:row['source_urls']+=' ; '+url
 row['source_date']='2026-11-10'
 marker='Registration date alone does not establish business or brand age; other age sources remain incomplete.'
 if marker not in row['note']:row['note']+=' '+marker
with f.open('w',encoding='utf-8-sig',newline='') as stream:
 w=csv.DictWriter(stream,fieldnames=fields);w.writeheader();w.writerows(rows)
with (p/'METHOD_LOG.md').open('a',encoding='utf-8') as stream:stream.write('\n- 2026-11-10: public Verisign RDAP via logged-off browser: herbneden.com, honeyglownewyork.com, diablocosmetics.com, facelove-cosmetics.com, houseofduaa.com, hotelcollection.com and cphgrooming.com registrations read. Added earlier directly observed try-kaori.com registration to its store row. Other age checks not completed; no brand-age classification inferred from domain alone.\n')
