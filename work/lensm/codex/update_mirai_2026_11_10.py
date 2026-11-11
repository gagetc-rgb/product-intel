import csv
from pathlib import Path
p=Path(__file__).parent/'leader_complaints.csv'
with p.open(encoding='utf-8-sig',newline='') as f:
    r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
if not any(r['domain']=='miraiclinical.com' for r in rows):
    d=dict(domain='miraiclinical.com',source='https://www.trustpilot.com/review/miraiclinical.com?sort=recency',source_date='2026-11-10',tier='◆ / ◈',displayed_score='4.3 numeric; star image label says 4.5',total_reviews='271',stars_5='190',stars_4='29',stars_3='22',stars_2='10',stars_1='20',scope='all-profile counts; separate latest-200 distribution in next column',sample_latest_200='200 unique; 5-star 143; 4-star 22; 3-star 15; 2-star 9; 1-star 11; publication dates 2026-10-28 through 2026-11-10',complaint_theme_counts='unknown: full coding of 35 low-star reviews not completed',filtered_reviews_url='https://www.trustpilot.com/review/miraiclinical.com?sort=recency',limitations='Global profile includes several product lines. Review allegations not independently verified. See LEADER_COMPLAINTS.md for examples.')
    rows.append({k:d.get(k,'') for k in fields})
with p.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
