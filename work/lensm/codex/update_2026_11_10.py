import csv
from pathlib import Path

P = Path(__file__).parent
D = '2026-11-10'

def append_unique(name, rows, keys):
    path = P / name
    with path.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        existing = list(reader)
    indices = {tuple(r.get(k, '') for k in keys) for r in existing}
    for row in rows:
        if tuple(row.get(k, '') for k in keys) not in indices:
            existing.append({k: row.get(k, '') for k in fields})
            indices.add(tuple(row.get(k, '') for k in keys))
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(existing)

def store(category, domain, product, **kw):
    data = dict(category=category, domain=domain, sells='yes', product_url=product,
                price_one_bar='unknown: unit price not independently confirmed',
                bundles='unknown',default_bundle='unknown', subscription='unknown',
                refill_interval='unknown', subscription_cancellation='unknown',shipping='unknown',
                ships_from='unknown',returns='unknown',review_widget='unknown',review_count='unknown',
                country='unknown',currency='unknown',domain_registration='unknown',first_wayback='unknown',
                oldest_review='unknown',facebook_creation='unknown',oldest_shopify_product='unknown',
                age_class='unclear: other evidence not checked',source_urls=product,source_date=D,tier='◆')
    data.update(kw)
    return data

append_unique('store_facts.csv', [
 store('tallow_balm','wildgoldtallow.com','https://wildgoldtallow.com/',
   price_one_bar='$45 one-time; $31.50 subscription; currency/destination unconfirmed',
   bundles='1 balm; 2 save 10%; 3 save 15%; discount at checkout',default_bundle='unknown',
   subscription='30% discount; page offers subscription; selected state not verified',
   refill_interval='monthly selected; or every 2 months',subscription_cancellation='pause or cancel anytime, method not verified',
   shipping='free US shipping over $50; subscription says always free',returns='60-day money-back guarantee',
   review_widget='Judge.me',review_count='141; 4.83/5',country='unknown: not selected',currency='unknown: dollar symbol only',
   domain_registration='2025-03-17', source_urls='https://wildgoldtallow.com/ ; https://rdap.verisign.com/com/v1/domain/wildgoldtallow.com'),
 store('tallow_balm','bare-ritual.com','https://bare-ritual.com/products/tallow-balm',
   price_one_bar='$47.99 as displayed; purchase type affects amount',
   bundles='1 jar $47.99; 2 jars $47.99; 4 jars $79.99 under selected subscription; one-time 4 jars $99.99',
   default_bundle='4 jars, buy 2 get 2',subscription='20% discount; preselected',
   refill_interval='4 jars initially then 2 every 4 weeks',subscription_cancellation='cancel easily anytime; method not verified',
   shipping='unknown: page still displayed ID shipping after US country selected',returns='90-day money-back guarantee',
   review_widget='unknown',review_count='8,672 displayed; not independently verified',
   country='US selected in footer; page still displayed ID shipping',currency='USD selected; shipping region contradictory',
   domain_registration='2025-08-04',source_urls='https://bare-ritual.com/products/tallow-balm ; https://rdap.verisign.com/com/v1/domain/bare-ritual.com'),
 store('lash_serum','hanaekorea.com','https://hanaekorea.com/products/korean-eyelash-serum',
   price_one_bar='$34.95 per bottle',bundles='1 bottle $34.95; buy 1 get 1 free $34.95',
   subscription='unknown: none visible in purchase controls; not checked sitewide',
   shipping='US 2–5 business days as stated',returns='90-day guarantee; contact within 90 days; no return stated',
   review_count='9,425 displayed; provider and integrity not checked',country='US selected',currency='USD symbol; US country selected',
   domain_registration='2025-11-02',source_urls='https://hanaekorea.com/products/korean-eyelash-serum ; https://rdap.verisign.com/com/v1/domain/hanaekorea.com',
   note='Domain search mixes lash serum with concealer and brow products; old domain ad alone does not prove a long-running lash ad.'),
 store('rodent_repellent_pouches','sofyre.com','https://sofyre.com/products/mouse-repellent-pouches',
   price_one_bar='unknown: USD view not achieved; currency=USD still displayed non-USD formatted amounts',
   bundles='12 pouches; 36 pouches buy 2 get 1; 60 pouches buy 3 get 2',default_bundle='unknown',
   subscription='30% discount; auto-refill checkbox checked by default',
   refill_interval='policy says 30-day billing; product recommends replacement every 90 days',
   subscription_cancellation='portal; at least 3 days before billing according to policy',
   shipping='typically 1 business day dispatch, 5–12 business days delivery',returns='30-day refund as stated',
   review_count='1,668 displayed; provider and authenticity not verified',country='unknown: Indonesia displayed',currency='unknown: currency=USD did not produce clear USD',
   domain_registration='2025-07-23',source_urls='https://sofyre.com/products/mouse-repellent-pouches ; https://sofyre.com/policies/subscription-policy ; https://rdap.verisign.com/com/v1/domain/sofyre.com',
   note='No EPA or state-registration statement found in visible product-page text; that is not proof of nonregistration.'),
 store('silvervine_chew','purriq.com','https://purriq.com/products/purriq-natural-silvervine-dental-sticks?currency=USD',
   price_one_bar='5 sticks $29.99 (USD requested via query; US destination not confirmed)',
   bundles='5 sticks $29.99; 10 sticks $39.99; 20 sticks $64.99',default_bundle='unknown',
   subscription='site has subscription policy; whether these sticks are offered by subscription unknown',
   refill_interval='policy says every 30 days for subscriptions; relation to sticks unverified; product says each stick lasts up to a week',
   subscription_cancellation='sitewide policy: account portal or email, at least 5 days before billing',
   shipping='US 2–5 business days stated',returns='contact within 60 days of receipt for return or refund',
   review_widget='Judge.me',review_count='1,124 widget reviews, 4.18/5; header separately claims 11,527 and 4.8/5',
   country='unknown: US delivery country not selected',currency='USD requested with ?currency=USD; displayed $',
   domain_registration='2025-08-20',source_urls='https://purriq.com/products/purriq-natural-silvervine-dental-sticks?currency=USD ; https://purriq.com/pages/subscription-policy ; https://rdap.verisign.com/com/v1/domain/purriq.com')
], ['category','domain'])

def ad(category, aid, page, start, domain, query, landing, fmt='unknown', group='unknown'):
    return dict(category=category,ad_id=aid,page_name=page,start_date=start,creative_group_count=group,
       format=fmt,landing_url=landing,displayed_landing_domain=domain,
       domain_basis='Meta visible link or destination parameter; final redirect not opened',
       search_url='https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q='+query+'&search_type=keyword_unordered',
       source_date=D,source_tier='◆',coverage='convenience sample, not age-balanced')

append_unique('meta_ads.csv',[
 ad('tallow_balm','925993013445887','Wild Gold Tallow','2026-02-12','wildgoldtallow.com','wildgoldtallow.com','http://wildgoldtallow.com/'),
 ad('tallow_balm','3370216843147057','Bare Ritual','2026-02-18','bare-ritual.com','bare-ritual.com','https://bare-ritual.com/products/tallow-balm','video'),
 ad('lash_serum','988967054235650','Trending In Korea','2026-10-11','hanaekorea.com','hanaekorea.com','https://hanaekorea.com/products/korean-eyelash-serum','video','2'),
 ad('rodent_repellent_pouches','1958710542044048','Best Mouse Repellents','2026-10-05','sofyre.com','natural%20rodent%20repellent%20pouches','https://sofyre.com/products/mouse-repellent-pouches'),
 ad('silvervine_chew','1442135477559638','Purriq','2026-01-22','purriq.com','silvervine%20cat%20chew%20sticks','https://purriq.com/products/purriq-natural-silvervine-dental-sticks','video','2')
],['ad_id'])

append_unique('meta_stores.csv', [
 dict(category=c,domain=d,active_results=n,active_results_note='Meta active domain keyword results, all products; not verified as unique product-specific ads',
 active_30_plus='unknown: no start-date count',active_90_plus='unknown: no start-date count',active_180_plus='unknown: no start-date count',
 oldest_ad_date='unknown: full search not sorted by age',pages_used='unknown',search_url='https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q='+d+'&search_type=keyword_unordered',collected_on=D,tier='◆')
 for c,d,n in [('tallow_balm','wildgoldtallow.com','~35'),('tallow_balm','bare-ritual.com','~2,200'),('lash_serum','hanaekorea.com','~1,800'),('rodent_repellent_pouches','sofyre.com','~15,000')]
], ['category','domain'])
