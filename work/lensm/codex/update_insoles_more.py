import csv
from pathlib import Path
from urllib.parse import urlparse
p=Path(__file__).resolve().parent
q='https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=work%20insoles&search_type=keyword_unordered'
data='''739118252545796|2025-11-09|The Xstance|unknown|video|https://getxstance.com/article/5-reasons|insole form; standing or walking use
1317251743682475|2026-09-21|Stepprs|unknown|video|https://stepprs.com/pages/steel-toe-li-02|insole form; work boots
910501755223788|2026-02-23|BAD Workwear|unknown|video|https://badworkwear.com.au/collections/work-boots-for-men-women/products/bad-flash-safety-work-sneakers|off-target: safety sneakers, not separate insole
1570693074037245|2026-03-11|Stepprs|unknown|unknown|https://stepprs.com/products/massage|insole form; long shifts
1634142860880610|2025-10-24|The Xstance|2|video|https://getxstance.com/article/hip-review-1|insole form; work-specific targeting unclear
898928935810571|2026-01-19|The Xstance|unknown|video|https://getxstance.com/article/5-reasons/|insole form; work-specific targeting unclear
1438454934083562|2025-09-18|Stepprs|unknown|unknown||insole form; no offsite landing link visible, ad details not opened
1394502396043790|2026-03-16|The Xstance|unknown|video|https://getxstance.com/article/5-reasons/|insole form; work-specific targeting unclear
1171769408444145|2025-11-08|The Xstance|unknown|video|https://getxstance.com/article/5-reasons|insole form; standing or walking use'''
f=p/'meta_ads.csv'
with f.open(encoding='utf-8-sig',newline='') as stream:
 r=csv.DictReader(stream);fields=r.fieldnames;rows=list(r)
known={x['ad_id'] for x in rows}
for line in data.splitlines():
 aid,date,page,count,fmt,url,note=line.split('|')
 if aid in known:continue
 row=dict(category='work_insoles',ad_id=aid,page_name=page,start_date=date,creative_group_count=count,format=fmt,landing_url=url or 'unknown: no offsite link visible; ad detail not opened',displayed_landing_domain=urlparse(url).hostname or 'unknown',domain_basis='Meta visible link destination; final redirect not checked',search_url=q,source_date='2026-11-10',source_tier='◆',coverage='positions 21–29 in nonrandom visible search results; '+note)
 rows.append({k:row.get(k,'') for k in fields});known.add(aid)
with f.open('w',encoding='utf-8-sig',newline='') as stream:
 w=csv.DictWriter(stream,fieldnames=fields);w.writeheader();w.writerows(rows)
with (p/'METHOD_LOG.md').open('a',encoding='utf-8') as stream:stream.write('\n- 2026-11-10: live logged-off Meta work insoles category search; collected visible positions 21–29 including one off-target shoe and one without offsite link. Clicking See more did not load further cards; not retried. Destinations were read from visible Meta links, final redirects not followed.\n')
