import csv
from pathlib import Path
p=Path(__file__).resolve().parent;f=p/'meta_stores.csv'
with f.open(encoding='utf-8-sig',newline='') as stream:
 r=csv.DictReader(stream);fields=r.fieldnames;rows=list(r)
q='https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=tryskult.com&search_type=keyword_unordered'
row=dict(category='chin_wrap',domain='tryskult.com',active_results='~870',active_results_note='Meta domain keyword result count, not verified as store-owned or product-specific ad count; first 12 visible cards matched chin wrap',active_30_plus='unknown: date-filter count not collected',active_90_plus='unknown: date-filter count not collected',active_180_plus='unknown: date-filter count not collected',oldest_ad_date='unknown: oldest among all active ads not established; earliest among first 12 was 2025-09-11',pages_used='Skult; Tryskult in first 12 cards only',search_url=q,collected_on='2026-11-10',tier='◆ / ◈')
if not any(r['domain']==row['domain'] and r['category']==row['category'] for r in rows):rows.append(row)
with f.open('w',encoding='utf-8-sig',newline='') as stream:
 w=csv.DictWriter(stream,fieldnames=fields);w.writeheader();w.writerows(rows)
