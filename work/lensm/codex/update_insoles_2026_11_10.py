import csv
from pathlib import Path
from urllib.parse import urlparse

p=Path(__file__).parent/'meta_ads.csv'
q='https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=work%20insoles&search_type=keyword_unordered'
data='''700755075654412|2025-10-02|OrthoFlexx|unknown|video|https://orthoflexx.com/orthotics
4178555935748219|2025-07-29|Stepprs|4|video|https://stepprs.com/products/massage?fbclid=fbclid
2303742590036985|2025-09-30|The Xstance|2|video|https://getxstance.com/article/5-reasons
2063475840726648|2025-09-18|Stepprs|3|unknown|https://stepprs.com/products/massage
1352694846621684|2026-04-06|One Compress|2|video|https://www.onecompress.com/products/bamboofootsleeves
2535310046906471|2026-07-04|Stepprs|unknown|video|https://stepprs.com/products/massage
24884026027860602|2025-10-02|OrthoFlexx|unknown|video|https://orthoflexx.com/orthotics
2279104895912708|2026-02-18|PowerStep|unknown|video|https://powerstep.com/pages/discover-your-pain-relief
1607291467694055|2026-09-10|Stepprs|unknown|video|https://stepprs.com/pages/long-shift-li-02
1813116840081678|2025-09-18|Stepprs|unknown|unknown|https://stepprs.com/products/massage
2015263695936236|2025-11-04|OrthoFlexx|unknown|video|https://orthoflexx.com/orthotics
772639112214398|2025-09-18|Stepprs|unknown|unknown|https://stepprs.com/products/massage
2513785135712536|2026-08-19|Feel Your Soul|unknown|video|https://feelyoursoul.com/
1533799197960619|2025-10-22|Stepprs|2|unknown|https://stepprs.com/products/massage
1453071929153538|2025-07-29|Stepprs|5|video|https://stepprs.com/products/massage?fbclid=fbclid
1125811496134634|2025-07-29|Stepprs|4|video|https://stepprs.com/products/massage
1123882333024431|2025-09-18|Stepprs|unknown|unknown|https://stepprs.com/products/massage
1843057880424516|2025-09-18|Stepprs|2|video|https://stepprs.com/products/massage?fbclid=fbclid
385720914611156|2024-10-11|Red Wing Shoes - Memphis, TN|unknown|video|
1516446813485690|2026-06-30|Superfeet Worldwide|unknown|unknown|https://www.superfeet.com/products/casual-womens-easyfit-r?utm_content=Facebook_UA&utm_source=facebook&variant=43158800629943'''
with p.open(encoding='utf-8-sig',newline='') as f:
    r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
known={x['ad_id'] for x in rows}
for line in data.splitlines():
    aid,date,page,group,fmt,url=line.split('|')
    if aid in known: continue
    relevance='off-target: foot sleeves' if aid=='1352694846621684' else ('unclear from visible ad' if aid in {'2513785135712536','385720914611156'} else 'insole product form; work-specific use not always established')
    row=dict(category='work_insoles',ad_id=aid,page_name=page,start_date=date,creative_group_count=group,format=fmt,landing_url=url or 'unknown: no link visible; ad detail not opened',displayed_landing_domain=urlparse(url).hostname or 'unknown',domain_basis='Meta visible link destination; final redirect not checked',search_url=q,source_date='2026-11-10',source_tier='◆',coverage='first 20 visible cards, convenience sample; '+relevance)
    rows.append({k:row.get(k,'') for k in fields}); known.add(aid)
with p.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
