import csv
from pathlib import Path
from urllib.parse import urlparse

p=Path(__file__).parent/'meta_ads.csv'
q='https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=tallow%20balm&search_type=keyword_unordered'
data='''3370216843147057|2026-02-18|Bare Ritual|unknown|video|https://bare-ritual.com/products/tallow-balm
2204667076771093|2026-08-09|Forge Men|unknown|unknown|https://shop.try-forge.com/mens-lifestyle-essentials-1
1170818295161721|2025-11-24|Ancestral Cosmetics|2|video|https://ancestralcosmetics.com/products/original-tallow-honey-balm
955591563601456|2026-03-09|Ancestral Cosmetics|unknown|unknown|https://ancestralcosmetics.com/products/original-tallow-honey-balm
1692555065217500|2026-06-16|Ancestral Cosmetics|unknown|unknown|http://ancestralcosmetics.com/products/original-tallow-honey-balm
962973596277178|2026-05-02|NourishMax|unknown|video|https://www.nourishmax.com/products/advanced-5d-pro-light-therapy-face-mask
839428982013888|2025-12-02|Ancestral Cosmetics|unknown|unknown|https://ancestralcosmetics.com/products/original-tallow-honey-balm
1115066880386623|2025-04-22|Wild Women Herbs|unknown|unknown|https://wildwomenherbs.com/products/bee-pollen-oxymel?utm_content=Facebook_UA&utm_source=facebook&variant=43935306875036
1534456628141141|2026-07-10|Neptune Health|2|unknown|https://www.neptunehealthco.com/pages/tallow-balm-pdp
26727567463512953|2026-02-13|Magnolia|unknown|unknown|https://magnolia.com/products/my-neighbors-tallow-manuka-honey-lavender-hand-balm?variant=43639017078835
1525097902527423|2026-06-09|Ben Corkery Founder at The Tallowed Truth|unknown|video|https://thetallowedtruth.com/pages/quiz
1529380298189669|2026-07-27|Pure Good|unknown|unknown|https://shoppuregood.com/products/revival-balm-for-youthful-looking-skin?utm_content=Facebook_UA&utm_source=facebook&variant=46894289158389
1797435388291367|2026-10-11|Skincare Guide|unknown|video|https://www.basedsupplies.com/pages/skincare-5?utm_source=facebook&utm_medium=social
1779784450102449|2026-08-04|Neptune Health|4|video|https://www.neptunehealthco.com/pages/tallow-balm-pdp
3965602596916081|2026-09-05|Ben Corkery Founder at The Tallowed Truth|2|video|https://thetallowedtruth.com/pages/quiz
1342588754662540|2026-07-10|Neptune Health|unknown|video|https://www.neptunehealthco.com/pages/tallow-balm-pdp
2807538609622819|2026-08-09|Forge Men|unknown|unknown|https://shop.try-forge.com/mens-lifestyle-essentials-1
1436618768148353|2026-04-15|Toups and Co Organics|unknown|unknown|https://toupsandco.com/collections/all
2115909396024637|2026-06-01|The Tallowed Truth|2|video|https://thetallowedtruth.com/products/f-balm
1922014749186445|2026-06-16|Ancestral Cosmetics|2|video|http://ancestralcosmetics.com/products/original-tallow-honey-balm'''
with p.open(encoding='utf-8-sig',newline='') as f:
    r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
seen={r['ad_id'] for r in rows}
for line in data.splitlines():
    aid,date,page,group,fmt,url=line.split('|')
    if aid in seen: continue
    relevance='off-target primary product' if aid in {'962973596277178','1115066880386623'} else ('unclear: multi-product catalog' if aid=='1436618768148353' else 'target form visible or F-Balm identity verified')
    row=dict(category='tallow_balm',ad_id=aid,page_name=page,start_date=date,creative_group_count=group,format=fmt,landing_url=url,displayed_landing_domain=urlparse(url).hostname,domain_basis='visible Meta destination; final redirect not checked',search_url=q,source_date='2026-11-10',source_tier='◆',coverage='first 20 cards, convenience sample; '+relevance)
    rows.append({k:row.get(k,'') for k in fields});seen.add(aid)
with p.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
