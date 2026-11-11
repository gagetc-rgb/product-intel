import csv
from pathlib import Path
p=Path(__file__).resolve().parent
f=p/'leader_complaints.csv'
with f.open(encoding='utf-8-sig',newline='') as stream:
 reader=csv.DictReader(stream);fields=reader.fieldnames;rows=list(reader)
for domain,limit in [('borboleta.com','Unclaimed exact-domain profile; no reviews. Do not infer quality.'),('luxe.com','Exact-domain unclaimed profile is categorized as valet parking; identity with intended beauty store is not established. Do not substitute similar names.')]:
 if any(r['domain']==domain for r in rows):continue
 url=f'https://www.trustpilot.com/review/{domain}?sort=recency'
 row=dict(domain=domain,source=url,source_date='2026-11-10',tier='◆',displayed_score='0.0 placeholder; no usable score',total_reviews='0',stars_5='0',stars_4='0',stars_3='0',stars_2='0',stars_1='0',scope='exact-domain profile only; business identity may be unclear',sample_latest_200='0 available',complaint_theme_counts='unknown: no reviews',filtered_reviews_url=url,limitations=limit)
 rows.append(row)
with f.open('w',encoding='utf-8-sig',newline='') as stream:
 w=csv.DictWriter(stream,fieldnames=fields);w.writeheader();w.writerows(rows)
section='''\n## Borboleta and Luxe — exact-domain identity checks, 2026-11-10\n\n◆ [borboleta.com](https://www.trustpilot.com/review/borboleta.com?sort=recency) shows zero reviews on an unclaimed exact-domain profile; it has no usable complaint rate. ◆ [luxe.com](https://www.trustpilot.com/review/luxe.com?sort=recency) also shows zero reviews, but Trustpilot categorizes the unclaimed profile as a valet-parking service. Its connection to the intended beauty leader is **unclear**; similarly named cosmetics profiles are separate identities and have not been merged.\n'''
f=p/'LEADER_COMPLAINTS.md';t=f.read_text(encoding='utf-8')
if '## Borboleta and Luxe — exact-domain' not in t:f.write_text(t+section,encoding='utf-8')
with (p/'METHOD_LOG.md').open('a',encoding='utf-8') as stream:stream.write('\n- 2026-11-10: live logged-off Trustpilot exact-domain checks borboleta.com and luxe.com returned zero reviews; luxe.com is categorized by Trustpilot as valet parking, identity with intended beauty business not established.\n')
