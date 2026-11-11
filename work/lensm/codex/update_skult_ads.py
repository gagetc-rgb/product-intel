import csv
from pathlib import Path
p=Path(__file__).resolve().parent
q='https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=tryskult.com&search_type=keyword_unordered'
dest='https://tryskult.com/products/sculpting-face-wrap'
data='''1288993806061037|2025-09-11|Skult|7|video
1277997347412940|2025-12-25|Skult|unknown|video
913755531721489|2026-05-22|Skult|unknown|video
2549613925498814|2026-05-18|Skult|unknown|video
872562865638916|2026-01-15|Tryskult|unknown|video
872826718959970|2026-01-26|Tryskult|unknown|video
1228993945974681|2026-04-26|Skult|unknown|video
1610434409966947|2026-02-02|Skult|unknown|unknown
1232939691517885|2026-02-05|Skult|unknown|video
1929943787951989|2025-11-24|Skult|unknown|video
1196573535329689|2026-01-03|Skult|unknown|video
1575842463655979|2026-01-14|Tryskult|unknown|unknown'''
items=[line.split('|') for line in data.splitlines()]
f=p/'meta_ads.csv'
with f.open(encoding='utf-8-sig',newline='') as stream:
 r=csv.DictReader(stream);fields=r.fieldnames;rows=list(r)
seen={r['ad_id'] for r in rows}
for aid,date,page,count,fmt in items:
 if aid in seen:continue
 row=dict(category='chin_wrap',ad_id=aid,page_name=page,start_date=date,creative_group_count=count,format=fmt,landing_url=dest,displayed_landing_domain='tryskult.com',domain_basis='decoded Meta link destination; final redirect not followed',search_url=q,source_date='2026-11-10',source_tier='◆',coverage='identity search convenience sample; 12 initial cards, not balanced and not proven 10 oldest')
 rows.append({k:row.get(k,'') for k in fields});seen.add(aid)
with f.open('w',encoding='utf-8-sig',newline='') as stream:
 w=csv.DictWriter(stream,fieldnames=fields);w.writeheader();w.writerows(rows)
f=p/'leader_claims.csv'
with f.open(encoding='utf-8-sig',newline='') as stream:
 r=csv.DictReader(stream);fields=r.fieldnames;rows=list(r)
seen={r['ad_id'] for r in rows}
for aid,date,page,count,fmt in items:
 if aid in seen:continue
 row=dict(domain='tryskult.com',ad_id=aid,start_date=date,format=fmt,hook='Wake up with a more sculpted-looking jawline without surgery or filters (visible copy, paraphrased)',result_claims='Instantly lifts/sculpts jawline; result by morning; reusable and washable; soft collagen fabric',classification='cosmetic appearance and timing claims; treatment/growth, authority figure or testimonial not established from visible copy; video contents not independently reviewed',offer='buy one get one, described as sale in visible copy',landing_page_type='product path in visible Meta destination; final redirect and live page not checked',source_url=q,source_date='2026-11-10',tier='◆ / ◈',coverage='initial visible identity-search cards; not established as ten longest-running; additional video/audio claims unknown')
 rows.append({k:row.get(k,'') for k in fields});seen.add(aid)
with f.open('w',encoding='utf-8-sig',newline='') as stream:
 w=csv.DictWriter(stream,fieldnames=fields);w.writeheader();w.writerows(rows)
with (p/'METHOD_LOG.md').open('a',encoding='utf-8') as stream:stream.write('\n- 2026-11-10: Meta US active identity query '+q+' displayed ~870 keyword results and 12 initial Tryskult chin-wrap cards with common visible copy; records added to meta_ads.csv and leader_claims.csv. Count is keyword result, not verified total of a single advertiser; sample is not ten longest, and video/audio was not reviewed. Tab closed after collection.\n')
