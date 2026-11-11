import csv
from pathlib import Path
p=Path(__file__).resolve().parent
data='''6ad5d000568c6602c87ad7bd,1,billing;support
6ab7fc97b82326caeb7b834f,1,product;support
6aa5371de6a49743603fa20f,1,support
6a7a941b370d2d326183b27d,1,product;no_effect
6a5a79b81c6ff77901480e83,1,billing;support
6a2c4b563f1cafe4a089c1ea,2,product;support
6a23da3c5da0dcabbd87d2b7,1,product
69a8801c53bcd4e098d444f9,1,product
6968f4f9f7d4acb15d0a288d,1,shipping
693badf40de61a76b72f3177,3,product
69373ee3fb2d4be01339da0e,1,product
690b4147df1fb060ce6078c9,3,product;shipping
68c2adcd40d8d528bfc6ff36,1,product'''
rows=[s.split(',') for s in data.splitlines()]; themes=['product','shipping','billing','support','no_effect']; assert len(rows)==13
counts={k:sum(k in r[2].split(';') for r in rows) for k in themes}
with (p/'ancestral_low_review_codes.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f);w.writerow(['review_url','stars',*themes,'source_date','tier'])
 for ident,stars,codes in rows:w.writerow(['https://www.trustpilot.com/reviews/'+ident,stars,*(int(k in codes.split(';')) for k in themes),'2026-11-10','◈'])
f=p/'leader_complaints.csv'
with f.open(encoding='utf-8-sig',newline='') as stream:
 reader=csv.DictReader(stream);fields=reader.fieldnames;allrows=list(reader)
row=dict(domain='ancestralcosmetics.com',source='https://www.trustpilot.com/review/ancestralcosmetics.com?sort=recency',source_date='2026-11-10',tier='◆ / ◈',displayed_score='4.5',total_reviews='92',stars_5='76',stars_4='3',stars_3='2',stars_2='1',stars_1='10',scope='entire exact-domain profile',sample_latest_200='92 available, full-profile counts from filter',complaint_theme_counts='; '.join(f'{k} {v}' for k,v in counts.items()),filtered_reviews_url='https://www.trustpilot.com/review/ancestralcosmetics.com?stars=1&stars=2&stars=3',limitations='Global, multiple products, self-selected reviews; allegations unverified; vendor disputes some. Counts reflect all 13 low-star reviews, which may change.')
if not any(r['domain']==row['domain'] for r in allrows):allrows.append(row)
with f.open('w',encoding='utf-8-sig',newline='') as stream:
 writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader();writer.writerows(allrows)
section=f'''
## Ancestral Cosmetics — 92 available Trustpilot reviews, 2026-11-10

◆ [Exact-domain profile](https://www.trustpilot.com/review/ancestralcosmetics.com?sort=recency): score 4.5 and 92 reviews, five/four/three/two/one-star counts 76/3/2/1/10. All 13 reviews in the [1–3-star filter](https://www.trustpilot.com/review/ancestralcosmetics.com?stars=1&stars=2&stars=3) were read and coded; overlapping counts: {', '.join(f'{k} {v}' for k,v in counts.items())}. See `ancestral_low_review_codes.csv`. This is a global, self-selected, multi-product sample and allegations are not independently verified.

Examples: [beef-like scent and a difficult return](https://www.trustpilot.com/reviews/6ab7fc97b82326caeb7b834f); [a reported skin breakout](https://www.trustpilot.com/reviews/6a23da3c5da0dcabbd87d2b7); [a delayed delivery](https://www.trustpilot.com/reviews/6968f4f9f7d4acb15d0a288d); and [a refund dispute](https://www.trustpilot.com/reviews/6ad5d000568c6602c87ad7bd). The seller says it processed the refund in that last case. Potentially fixable issues include product scent, packaging, clear return terms and delivery communications; individual skin responses and the prevalence of reactions cannot be inferred from this sample.
'''
f=p/'LEADER_COMPLAINTS.md';t=f.read_text(encoding='utf-8')
if '## Ancestral Cosmetics — 92 available' not in t:f.write_text(t+section,encoding='utf-8')
with (p/'METHOD_LOG.md').open('a',encoding='utf-8') as stream:stream.write('\n- 2026-11-10: live logged-off Trustpilot Ancestral Cosmetics exact-domain profile and 1–3-star filters; all 13 low-star review IDs coded, 92 total at time read.\n')
print(counts)
