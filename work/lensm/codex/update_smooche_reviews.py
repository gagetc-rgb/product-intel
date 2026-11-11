import csv
from pathlib import Path
p=Path(__file__).resolve().parent
data='''6af2cfbb132bf116c14d063b,1,billing;support
6af2a7af42eb15efebb0fec9,2,product
6af2668da56374b8406a82f9,1,billing;support;product
6af25b82d53900c2cdd206a3,1,product
6af249349032e7fbd4a5aa4f,1,billing;support
6af241d1b4f05a71e7329712,1,product;no_effect
6af233c8d65015388925c41c,3,other
6af223bb865e4e0d5cc65df6,2,product;no_effect
6af21b9b2997e471969d3bcf,3,other
6af209e78ffe13f829b0ff0c,3,billing
6af1f5c21900695d7b966d46,2,product;no_effect;support
6af1ee5f34edc1129520c461,1,product;no_effect;support
6af1ec130a63fd2e43870dff,1,shipping;support
6af1d62100823dcb9d9f2f59,2,product;billing
6af1d533728c5ba02d773bae,1,billing;support
6af188cc37ada2a7fef9e8c0,3,billing;support;no_effect
6af150284ffa555c3eb5a249,3,other
6af13e5f78300bf2cc7f9da2,1,billing;support'''
rows=[x.split(',') for x in data.splitlines()];themes=['product','shipping','billing','support','no_effect','other'];assert len(rows)==18
counts={k:sum(k in r[2].split(';') for r in rows) for k in themes}
with (p/'smooche_low_review_codes.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f);w.writerow(['review_url','stars',*themes,'source_date','tier'])
 for ident,stars,codes in rows:w.writerow(['https://www.trustpilot.com/reviews/'+ident,stars,*(int(k in codes.split(';')) for k in themes),'2026-11-10','◈'])
f=p/'leader_complaints.csv'
with f.open(encoding='utf-8-sig',newline='') as stream:
 r=csv.DictReader(stream);fields=r.fieldnames;allrows=list(r)
row=dict(domain='smooche.com',source='https://www.trustpilot.com/review/smooche.com?sort=recency',source_date='2026-11-10',tier='◆ / ◈',displayed_score='unavailable: Trustpilot warning',total_reviews='10820',stars_5='7754',stars_4='1298',stars_3='301',stars_2='185',stars_1='1282',scope='profile-wide counts; latest-200 sample separate',sample_latest_200='200 unique; five 151; four 31; three 5; two 4; one 9; displayed endpoint timestamps 2026-11-10 to 2026-11-09',complaint_theme_counts='; '.join(f'{k} {v}' for k,v in counts.items()),filtered_reviews_url='https://www.trustpilot.com/review/smooche.com?sort=recency',limitations='Trustpilot says rating unavailable due to guidelines breach and alleges pressure to alter/remove negative reviews; platform statement. Global, multi-product, self-selected and very short time-window sample; review allegations unverified.')
if not any(x['domain']==row['domain'] for x in allrows):allrows.append(row)
g=dict(domain='goda.co',source='https://www.trustpilot.com/review/goda.co?sort=recency',source_date='2026-11-10',tier='◆',displayed_score='blocked: verifying connection',total_reviews='unknown: blocked',stars_5='unknown',stars_4='unknown',stars_3='unknown',stars_2='unknown',stars_1='unknown',scope='exact-domain profile',sample_latest_200='unknown: blocked by connection verification',complaint_theme_counts='unknown',filtered_reviews_url='https://www.trustpilot.com/review/goda.co?sort=recency',limitations='Direct logged-off browser showed connection verification; not bypassed. godaperfume.com is a separate Trustpilot profile and is not merged.')
if not any(x['domain']==g['domain'] for x in allrows):allrows.append(g)
with f.open('w',encoding='utf-8-sig',newline='') as stream:
 w=csv.DictWriter(stream,fieldnames=fields);w.writeheader();w.writerows(allrows)
section=f'''\n## Smooche — latest 200 Trustpilot reviews, 2026-11-10\n\n◆ [Exact-domain profile](https://www.trustpilot.com/review/smooche.com?sort=recency) displayed 10,820 reviews; Trustpilot withheld the rating and stated the business pressured people to alter or remove negative reviews. This is Trustpilot's notice. Profile-wide five/four/three/two/one-star counts were 7,754/1,298/301/185/1,282. ◈ The first 200 distinct cards across ten pages were 151/31/5/4/9; displayed endpoint timestamps 2026-11-10 to 2026-11-09. This short, global, multi-product and self-selected sample is affected by the platform warning.\n\n◈ Of the 18 low-star reviews: {', '.join(f'{k} {v}' for k,v in counts.items())}; codes overlap. Individual IDs and links are in `smooche_low_review_codes.csv`. Examples are allegations: [another shipment after attempted cancellation](https://www.trustpilot.com/reviews/6af2cfbb132bf116c14d063b), [foundation looked pale and patchy](https://www.trustpilot.com/reviews/6af241d1b4f05a71e7329712), [reported no response to refund requests](https://www.trustpilot.com/reviews/6af1ee5f34edc1129520c461), and [unclear bundle pricing](https://www.trustpilot.com/reviews/6af209e78ffe13f829b0ff0c). A follower could improve opt-in clarity, cancellation, product shade communication and support; these observations do not establish actual rates or verify claims.\n\n## GODA — exact-domain profile blocked, 2026-11-10\n\n◆ The logged-off in-app browser showed connection verification at [goda.co Trustpilot](https://www.trustpilot.com/review/goda.co?sort=recency); no bypass attempted. Its latest 200 reviews remain unknown. `godaperfume.com` is a separate Trustpilot profile and was not merged with this one.\n'''
f=p/'LEADER_COMPLAINTS.md';text=f.read_text(encoding='utf-8')
if '## Smooche — latest 200 Trustpilot reviews' not in text:f.write_text(text+section,encoding='utf-8')
with (p/'METHOD_LOG.md').open('a',encoding='utf-8') as f:f.write('\n- 2026-11-10: live logged-off Trustpilot smooche.com profile: 200 unique most-recent cards, 18 low-star manually coded; Trustpilot rating hidden with guideline-breach notice. Exact-domain goda.co page displayed connection verification and was not bypassed. Both browser tabs closed.\n')
print(counts)
