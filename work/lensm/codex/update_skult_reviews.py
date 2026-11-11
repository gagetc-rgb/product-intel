import csv
from pathlib import Path
p = Path(__file__).resolve().parent
data = '''6acf490bcdbe5198b7af12a1,1,billing;support
6a980d9131d35805c2012570,1,billing;shipping
6a956706008148c84027d041,1,billing
6a546d8821aea1a520d74a78,1,billing;no_effect
6a261af494bdef9b71d61f78,1,product;support
69ff20a831c8bc31d818a040,2,product
69b728558f95e16bfeab13ab,1,product
69a0879c6a0aa13b206e19fa,1,shipping;support
699bdec854812ac50ade9c2f,1,shipping;support
6999f48b79716ae6b3efb69e,1,shipping;support
699730bd938b41d20eab1228,1,shipping;support
698f76d7e528515468e690fc,1,other
698f4144242ba8dbf34266ef,1,shipping
698e266199843aeecdb6b933,1,other
698b0e18e46e34efd14c29a7,1,shipping;support
6986667be50bc733fe444165,1,shipping;support
697cae85576d9f2b610a15b7,1,shipping;support
697922590b84ecff056d8a42,1,shipping;support
6977b1d103bcb102871e98e4,1,shipping;support'''
rows = [s.split(',') for s in data.splitlines()]
themes = ['product', 'shipping', 'billing', 'support', 'no_effect', 'other']
assert len(rows) == len({r[0] for r in rows}) == 19
counts = {k:sum(k in row[2].split(';') for row in rows) for k in themes}
with (p/'skult_low_review_codes.csv').open('w', encoding='utf-8-sig', newline='') as f:
    w=csv.writer(f); w.writerow(['review_url','stars',*themes,'source_date','tier'])
    for ident, stars, codes in rows:
        w.writerow(['https://www.trustpilot.com/reviews/'+ident, stars, *(int(k in codes.split(';')) for k in themes),'2026-11-10','◈'])
file=p/'leader_complaints.csv'
with file.open(encoding='utf-8-sig',newline='') as f:
    reader=csv.DictReader(f); fields=reader.fieldnames; existing=list(reader)
new=[dict(domain='tryskult.com',source='https://www.trustpilot.com/review/tryskult.com?sort=recency',source_date='2026-11-10',tier='◆ / ◈',displayed_score='1.7 numeric; star-image label 1.5',total_reviews='19',stars_5='0',stars_4='0',stars_3='0',stars_2='1',stars_1='18',scope='all 19 displayed reviews on this exact domain profile',sample_latest_200='19 available; 18 one-star, 1 two-star',complaint_theme_counts='; '.join(f'{k} {v}' for k,v in counts.items()),filtered_reviews_url='https://www.trustpilot.com/review/tryskult.com?sort=recency',limitations='Global; multiple product types including skincare and chin wraps. Unverified individual allegations. Related-looking skult.com Trustpilot profile not merged.'),dict(domain='sproos.co',source='https://www.trustpilot.com/review/sproos.co?sort=recency',source_date='2026-11-10',tier='◆',displayed_score='0.0 placeholder; no usable rating',total_reviews='0',stars_5='0',stars_4='0',stars_3='0',stars_2='0',stars_1='0',scope='exact-domain unclaimed profile',sample_latest_200='0 available',complaint_theme_counts='unknown: no reviews on exact-domain profile',filtered_reviews_url='https://www.trustpilot.com/review/sproos.co?sort=recency',limitations='Unclaimed profile lists Colombia; business identity beyond matching exact outbound domain unclear; no inference from zero reviews.')]
for row in new:
    if not any(x['domain']==row['domain'] for x in existing): existing.append(row)
with file.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(existing)
section=f'''
## TrySkult — 19 Trustpilot reviews, 2026-11-10

◆ [Exact-domain profile](https://www.trustpilot.com/review/tryskult.com?sort=recency): 1.7 numeric score, 19 reviews: 18 one-star and 1 two-star. The profile is claimed and links to tryskult.com. Trustpilot separately shows a `skult.com` profile; the profiles are not merged here. This small, self-selected global set covers different products, including skincare and a chin wrap, not necessarily one SKU.

◈ All 19 reviews were read and manually coded; non-exclusive counts: {', '.join(f'{k} {v}' for k,v in counts.items())}. See `skult_low_review_codes.csv` for individual links. These are unverified reviewer allegations, not independently established transactions or rates. Examples: [alleged unwanted renewal](https://www.trustpilot.com/reviews/6acf490bcdbe5198b7af12a1), [alleged non-delivery and charges](https://www.trustpilot.com/reviews/6a980d9131d35805c2012570), [reported chin-wrap irritation](https://www.trustpilot.com/reviews/69b728558f95e16bfeab13ab), and [tracking and cancellation complaint](https://www.trustpilot.com/reviews/698b0e18e46e34efd14c29a7). A follower could clarify subscription consent and cancellation, monitor delivery and improve fit; these reports do not establish how common such events are among all buyers.

## Sproos — exact-domain Trustpilot check, 2026-11-10

◆ [sproos.co profile](https://www.trustpilot.com/review/sproos.co?sort=recency) displayed zero reviews and a 0.0 placeholder. The profile is unclaimed, lists Colombia, and links to the exact domain; identity beyond the outbound domain was not verified. No complaint distribution can be calculated from zero reviews, and the absence of reviews is not evidence of product quality.
'''
f=p/'LEADER_COMPLAINTS.md'; t=f.read_text(encoding='utf-8')
if '## TrySkult — 19 Trustpilot reviews' not in t:f.write_text(t+section,encoding='utf-8')
with (p/'METHOD_LOG.md').open('a',encoding='utf-8') as f:f.write('\n- 2026-11-10: live logged-off browser, exact-domain Trustpilot profiles tryskult.com and sproos.co. All 19 TrySkult reviews coded with IDs; sproos.co had no reviews. Distinct skult.com profile not merged.\n')
print(counts)
