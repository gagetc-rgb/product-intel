import csv
from pathlib import Path
p=Path(__file__).resolve().parent
def append_unique(path,new,keys):
 with path.open(encoding='utf-8-sig',newline='') as f:
  reader=csv.DictReader(f);fields=reader.fieldnames;rows=list(reader)
 for row in new:
  if not any(all(old[k]==row[k] for k in keys) for old in rows):rows.append({k:row.get(k,'') for k in fields})
 with path.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
def store(domain,url,price,bundles,default,shipping,returns,widget,reviews,registration,note):
 return dict(category='work_insoles',domain=domain,sells='yes',product_url=url,price_one_bar=price,bundles=bundles,default_bundle=default,subscription='unknown: no subscription seen in observed controls; storewide availability not verified',refill_interval='unknown; replacement cycle not established',subscription_cancellation='unknown',shipping=shipping,ships_from='unknown' if domain=='stepprs.com' else 'page states US',returns=returns,review_widget=widget,review_count=reviews,country='United States shown in site country selector',currency='USD in country selector',domain_registration=registration,first_wayback='unknown',oldest_review='unknown',facebook_creation='unknown',oldest_shopify_product='unknown',age_class='unclear: remaining age checks incomplete',source_urls=url+' ; https://rdap.verisign.com/com/v1/domain/'+domain,source_date='2026-11-10',tier='◆ / ◈',note=note)
stores=[store('stepprs.com','https://stepprs.com/products/massage','$22 per pair','1 pair $22; 2 at $17.60 each = $35.20; 3 at $13.20 each = $39.60; 5 at $11 each = $55; bundle totals calculated ◈','2 pairs selected','5–8 business days worldwide stated; price and threshold unknown','90-day money-back guarantee stated','Judge.me','88,552 displayed; 4.80/5; not independent quality evidence','2024-01-31','Seller states useful life over 12 months; no repeat-purchase SKU confirmed. Domain registration alone is not business age.'),store('orthoflexx.com','https://orthoflexx.com/products/max-arch-support-insoles','$64.95 per pair','one $64.95; buy 2 get 1 free $129.90; buy 4 get 2 free $259.80','unknown','free shipping stated; timing unknown','free returns and 30-day money-back guarantee stated','unknown','unknown','2020-08-10','Domain registration alone does not establish business age. Subscription and replacement interval unknown.')]
append_unique(p/'store_facts.csv',stores,['category','domain'])
meta=[]
for domain,total in [('stepprs.com','~910'),('orthoflexx.com','~670')]:
 meta.append(dict(category='work_insoles',domain=domain,active_results=total,active_results_note='Meta domain keyword result count; not verified as owned or product-specific ad count',active_30_plus='unknown: no start-date count',active_90_plus='unknown: no start-date count',active_180_plus='unknown: no start-date count',oldest_ad_date='unknown: full search not sorted by oldest',pages_used='unknown: full list not collected',search_url='https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q='+domain+'&search_type=keyword_unordered',collected_on='2026-11-10',tier='◆ / ◈'))
append_unique(p/'meta_stores.csv',meta,['category','domain'])
with (p/'METHOD_LOG.md').open('a',encoding='utf-8') as f:f.write('\n- 2026-11-10: transcribed earlier live-browser Stepprs and OrthoFlexx product and Meta domain observations from INSOLES_2026-11-10.md into store_facts.csv and meta_stores.csv; preserve unknowns and do not equate domain-keyword counts with store-owned advertising.\n')
