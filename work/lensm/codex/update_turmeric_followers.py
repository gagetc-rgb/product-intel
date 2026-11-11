import csv
from pathlib import Path

p=Path(__file__).parent
def add_rows(filename, rows, keys):
    path=p/filename
    with path.open(encoding='utf-8-sig',newline='') as f:
        r=csv.DictReader(f); fields=r.fieldnames; old=list(r)
    seen={tuple(x.get(k,'') for k in keys) for x in old}
    for d in rows:
        key=tuple(d.get(k,'') for k in keys)
        if key not in seen:
            old.append({k:d.get(k,'') for k in fields});seen.add(key)
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(old)

D='2026-11-10'
def st(domain,url,**kwargs):
    d=dict(category='turmeric_soap',domain=domain,sells='yes',product_url=url,price_one_bar='unknown',bundles='unknown',default_bundle='unknown',subscription='unknown',refill_interval='unknown',subscription_cancellation='unknown',shipping='unknown',ships_from='unknown',returns='unknown',review_widget='unknown',review_count='unknown',country='unknown',currency='unknown',domain_registration='unknown',first_wayback='unknown',oldest_review='unknown',facebook_creation='unknown',oldest_shopify_product='unknown',age_class='unclear: full age evidence incomplete',source_urls=url,source_date=D,tier='◆')
    d.update(kwargs);return d

add_rows('store_facts.csv',[
 st('herbneden.com','https://www.herbneden.com/products/tea-tree-turmeric',price_one_bar='$7.00 one time; dollar symbol but US destination not selected',bundles='one 4 oz bar; other bundles not checked',default_bundle='one bar; one-time selected on page load',subscription='$6 per bar, $1 discount; not preselected',refill_interval='after subscription selected: 1 month selected, 2 and 3 months offered',subscription_cancellation='page says three complete shipments required before cancellation; editing schedule offered',shipping='free domestic shipping over $75; delivery times unknown',review_widget='Klaviyo',review_count='1,349; 4.8/5 on page; seller widget not independently audited',country='US delivery destination not selected',currency='dollar symbol; country not confirmed',note='Previously unclear: product page explicitly lists turmeric. Wholesale, age, returns and ad ownership not yet checked.'),
 st('stemandsoul.co','https://www.stemandsoul.co/products/superfood-soap-bar',price_one_bar='$24.99',bundles='1 bar $24.99; 3 bars $29.98; 5 bars $39.97',default_bundle='5 bars checked on home-page offer; product-page default not verified',subscription='unknown: no subscription control visible on product page; sitewide availability not established',refill_interval='seller states one bar lasts about one month',shipping='product page claims 24-hour dispatch and 3–5 day average delivery; cost unknown',ships_from='product page says Phoenix, Arizona; homepage says Arkansas; contradiction unresolved',returns='60-day money-back guarantee, email; seller says no return required',review_widget='Judge.me per homepage link and widget',review_count='product widget 2,077 reviews; 3.77/5; homepage separately claims 1,593 reviews',country='United States selected in footer',currency='USD selected in footer',source_urls='https://www.stemandsoul.co/products/superfood-soap-bar ; https://www.stemandsoul.co/ ; https://www.scamadviser.com/check-website/stemandsoul.co',domain_registration='2025-05-09 reported by third party; authoritative .co registry not yet verified',note='Previously unclear: page identifies turmeric extract in the soap; older first ad is evidence of ad age, not standalone proof of business age.'),
 st('honeyglownewyork.com','https://honeyglownewyork.com/products/glow-bar-kojic-acid-lemon-turmeric-soap',price_one_bar='from $17.99 on collection; US delivery destination not confirmed in live browser view',bundles='1, 2, 3 or 6 bars; default 3 bars at $45.87 once or $40.48 autoship; collection separately shows 4 bars $59.76',default_bundle='3 bars preselected',subscription='autoship preselected; advertised 25% versus $53.97 reference price; 3-bar recurring $40.48',refill_interval='every 3 months for initial 3-bar selection',subscription_cancellation='unknown: policy not read',review_widget='Loox',review_count='1,781 and 4.5/5 displayed; seller widget not audited',country='US delivery destination not independently confirmed',currency='dollar symbol; US destination not independently confirmed',source_urls='https://honeyglownewyork.com/products/glow-bar-kojic-acid-lemon-turmeric-soap ; https://honeyglownewyork.com/collections/bar-soaps',note='Previously unclear: bar explicitly contains turmeric. Product advertised autoship discount against reference price, not the discounted one-time bundle price.')
],['category','domain'])

def meta(domain,n):
    return dict(category='turmeric_soap',domain=domain,active_results=n,active_results_note='Meta active domain keyword search; may include other products and unrelated matches, not verified unique store-ad count',active_30_plus='unknown: start-date count not collected',active_90_plus='unknown: start-date count not collected',active_180_plus='unknown: start-date count not collected',oldest_ad_date='unknown: unsorted sample',pages_used='unknown',search_url='https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q='+domain+'&search_type=keyword_unordered',collected_on=D,tier='◆')
add_rows('meta_stores.csv',[meta('stemandsoul.co','~1,000'),meta('honeyglownewyork.com','~46')],['category','domain'])

raw='''1302532301965439|2026-06-23|unknown|video|products/superfood-soap-bar
4346176778967160|2026-07-25|unknown|video|pages/100-reasons
1324549699407909|2025-11-09|2|unknown|pages/adv-rose-superfood-soap
908547801950190|2026-03-26|2|video|products/superfood-soap-bar
877649934702604|2025-11-26|2|unknown|products/superfood-soap-bar
1229846531941397|2026-02-08|2|unknown|products/superfood-soap-bar
4069150330064342|2025-11-26|unknown|unknown|products/superfood-soap-bar
925015673664024|2026-04-15|2|video|products/superfood-soap-bar
1377477867087854|2025-12-09|2|video|pages/adv-rose-superfood-soap-main
34363824693233262|2026-03-22|2|video|products/superfood-soap-bar
26182916604698954|2026-03-22|2|video|products/superfood-soap-bar
1439324134813765|2026-07-25|unknown|video|products/superfood-soap-bar
1267996218245068|2026-04-08|2|video|products/superfood-soap-bar
2016939869219959|2026-03-26|unknown|unknown|products/superfood-soap-bar
1153914903582541|2025-12-14|2|video|products/superfood-soap-bar
1555703285585379|2025-11-10|unknown|unknown|pages/adv-rose-superfood-soap
1398677561622894|2025-12-09|2|video|pages/adv-rose-superfood-soap-main
839327495873793|2026-09-12|unknown|video|products/superfood-skin-balm
1704851387410299|2026-08-07|unknown|video|products/superfood-skin-balm
878697081390077|2025-11-26|3|unknown|products/superfood-soap-bar'''
q='https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=stemandsoul.co&search_type=keyword_unordered'
ads=[]
for line in raw.splitlines():
    aid,date,group,fmt,path=line.split('|')
    ads.append(dict(category='turmeric_soap',ad_id=aid,page_name='STEM & SOUL',start_date=date,creative_group_count=group,format=fmt,landing_url='https://www.stemandsoul.co/'+path,displayed_landing_domain='stemandsoul.co',domain_basis='Meta visible destination; final redirect not checked',search_url=q,source_date=D,source_tier='◆',coverage='first 20 domain-search cards, not age-balanced; '+('off-target: skin balm' if 'skin-balm' in path else 'soap ad; destination not opened after Meta redirect')))
ads.append(dict(category='turmeric_soap',ad_id='1988966711761167',page_name='River Fields with Honey Glow',start_date='2026-05-18',creative_group_count='unknown',format='video',landing_url='https://honeyglownewyork.com/products/glow-bar-kojic-acid-lemon-turmeric-soap',displayed_landing_domain='honeyglownewyork.com',domain_basis='Meta visible destination; final redirect not checked',search_url='https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=honeyglownewyork.com&search_type=keyword_unordered',source_date=D,source_tier='◆',coverage='one visible card, not age-balanced'))
add_rows('meta_ads.csv',ads,['ad_id'])
