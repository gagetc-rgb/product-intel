import csv
from pathlib import Path

out = Path(__file__).parent
date = '2026-11-10'
meta = 'https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=try-kaori.com&search_type=keyword_unordered'
product = 'https://try-kaori.com/products/deodorizing-persimmon-soap'
shipping = 'https://try-kaori.com/policies/shipping-policy'
reviews = 'https://www.trustpilot.com/review/try-kaori.com'
filtered = reviews + '?stars=1&stars=2&stars=3'

def write_csv(name, rows):
    with (out / name).open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)

ads = []
for ad_id, page, start in [
    ('1621971626261673','Margaret Whittaker','2026-08-01'),
    ('967935396231214','Kaori','2026-05-18'),
    ('1804257660950823','Sara Garret','2026-07-04'),
    ('1565581295012773','Kaori','2026-07-29'),
    ('1502590001354906',"Grandma's Glow",'2026-05-29'),
]:
    ads.append(dict(category='persimmon_soap', ad_id=ad_id, page_name=page,
      start_date=start, creative_group_count='unknown: not displayed', format='unknown: not verified',
      landing_url=product if ad_id=='1502590001354906' else 'unknown: final redirect not opened',
      displayed_landing_domain='try-kaori.com', domain_basis='visible ad text / CTA, not verified final redirect',
      search_url=meta, source_date=date, source_tier='◆', coverage='convenience sample; not age-balanced'))
write_csv('meta_ads.csv', ads)

write_csv('meta_stores.csv', [dict(category='persimmon_soap',domain='try-kaori.com',
    active_results='~750', active_results_note='Meta keyword-search results; not verified as store-owned ads; may include irrelevant matches and grouped versions',
    active_30_plus='unknown: date filter not applied',active_90_plus='unknown: date filter not applied',
    active_180_plus='unknown: date filter not applied',oldest_ad_date='unknown: search not sorted by oldest',
    pages_used='unknown: complete set not collected',search_url=meta,collected_on=date,tier='◆')])

write_csv('store_facts.csv',[dict(category='persimmon_soap',domain='try-kaori.com',sells='yes',
  product_url=product, price_one_bar='unknown: one-bar purchase option not confirmed',
  bundles='2 bars $29.90; 4 bars $48.00; 6 bars $59.94', default_bundle='4 bars',
  subscription='20% discount offered; default one-time purchase',refill_interval='unknown: not inspected',
  subscription_cancellation='page says cancel anytime; method not verified',
  shipping='free on all orders; processing 1–3 business days; US delivery 6–12 business days',
  ships_from='unknown: not stated on shipping policy',returns='product page states 60-day money-back guarantee; contact for refund',
  review_widget='unknown: widget provider not identified',review_count='unknown: 8,000+ satisfied customers is not a review count',
  country='unknown: site did not expose a selected delivery country; US pricing therefore not confirmed',
  currency='dollar sign displayed; USD not confirmed via country selector',
  domain_registration='unknown: registry not independently checked', first_wayback='unknown',oldest_review='unknown',
  facebook_creation='unknown',oldest_shopify_product='unknown',age_class='unclear: not independently checked',
  source_urls=product+' ; '+shipping,source_date=date,tier='◆',
  note='Post-load product options differ from initial accessibility tree; final settled UI recorded. Do not use prices as confirmed US pricing.')])

write_csv('leader_complaints.csv',[dict(domain='try-kaori.com',source=reviews,source_date=date,tier='◆',
  displayed_score='4.7 (numeric text); star-image accessible label says 4.5',total_reviews='768',
  stars_5='617',stars_4='119',stars_3='16',stars_2='2',stars_1='14',
  scope='all reviews on profile, not the latest 200',sample_latest_200='unknown: not collected',
  complaint_theme_counts='unknown: full coding not completed',filtered_reviews_url=filtered,
  limitations='Counts are profile-wide; ratings and customer claims are not independently verified.')])

write_csv('leader_claims.csv',[dict(domain='try-kaori.com',ad_id='967935396231214',start_date='2026-05-18',
  format='unknown',hook='Annual limited-time discount',
  result_claims='Persimmon tannins break down odor-associated oil; one bar lasts about six weeks; change noticeable within first week',
  classification='product efficacy and cosmetic freshness claims; duration claim; not independently substantiated',
  offer='up to 64% off plus 3 free gifts',landing_page_type='unknown: final redirect not inspected',
  source_url=meta,source_date=date,tier='◈',coverage='convenience sample; not established as one of ten longest-running ads')])
