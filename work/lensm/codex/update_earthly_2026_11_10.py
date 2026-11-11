import csv
from pathlib import Path
p=Path(__file__).parent/'leader_complaints.csv'
with p.open(encoding='utf-8-sig',newline='') as f:
    r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
if not any(r['domain']=='earthlyderm.com' for r in rows):
    d=dict(domain='earthlyderm.com',source='https://www.trustpilot.com/review/earthlyderm.com?sort=recency',source_date='2026-11-10',tier='◆ / ◈',displayed_score='4.8',total_reviews='379',stars_5='355',stars_4='9',stars_3='0',stars_2='0',stars_1='15',scope='all-profile counts; separate latest-200 distribution in next column',sample_latest_200='200 unique; 5-star 183; 4-star 8; 3-star 0; 2-star 0; 1-star 9; publication dates 2025-10-01 through 2026-11-09',complaint_theme_counts='nine 1-star reviews; overlapping themes: shipping 4; billing/subscription 2; support/refunds 6; product experience 4; no perceived effect 3',filtered_reviews_url='https://www.trustpilot.com/review/earthlyderm.com?sort=recency',limitations='Review reports are unverified. Latest 200 global, not US-only; 179 older reviews not coded. Trustpilot displays a notice about incorrect display of its content by this business. See LEADER_COMPLAINTS.md for source links.')
    rows.append({k:d.get(k,'') for k in fields})
with p.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
