import csv
from pathlib import Path
from urllib.parse import urlparse

P = Path(__file__).parent
Q = 'https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=silvervine%20cat%20chew%20sticks&search_type=keyword_unordered'
# Observed card fields: library ID | start | page | group | format | visible destination.
raw = '''1720974865905227|2026-07-04|Purriq|unknown|unknown|https://try.purriq.com/7-reasons-listicle-v2-japan
1442135477559638|2026-01-22|Purriq|2|video|https://purriq.com/products/purriq-natural-silvervine-dental-sticks
1212098334325862|2026-02-17|Purriq|unknown|video|https://purriq.com/products/purriq-natural-silvervine-dental-sticks
1672493207322965|2026-06-12|Purriq|2|video|https://try.purriq.com/kyoto-sanctuary
2081642202484244|2026-10-26|Susan Mitchell|unknown|unknown|https://heycomfora.com/pages/7-reasons-cats-go-wild-for-comfora-sticks
930662132837309|2026-02-19|Purriq|unknown|video|https://try.purriq.com/testimonial
1889741841696759|2026-05-31|KittyCare|2|unknown|https://kittycare.co/products/hairball-defense
1428232515840292|2026-06-25|Purriq|2|video|https://try.purriq.com/7-reasons-listicle-v2-japan
1900645097263331|2026-06-08|Purriq|unknown|video|https://try.purriq.com/7-reasons-listicle-v2
3471244903042427|2026-10-05|Nylatails|unknown|video|https://nylatails.com/products/nylatails-natural-silvervine-stick
2026412277911124|2026-05-09|Cat Wellness Daily|unknown|video|https://try.purriq.com/7-reasons-listicle-v2
3248463585544357|2026-10-23|Vet Visit Diaries|unknown|unknown|https://tryarleo.com/
1756822275534227|2026-09-29|Purriq|unknown|video|https://try.purriq.com/7-reasons-listicle-v2
1936210060668992|2026-08-23|Comfora|unknown|unknown|https://heycomfora.com/products/comfora-pure-silvervine-dental-sticks
2059156554964169|2026-10-26|Susan Mitchell|unknown|unknown|https://heycomfora.com/pages/7-reasons-cats-go-wild-for-comfora-sticks
1019584467271084|2026-06-13|Purriq|unknown|video|https://try.purriq.com/7-reasons-listicle-v2
1626632392578948|2026-09-26|Cat Wellness Research Center|5|video|https://heycomfora.com/pages/7-reasons-japan
1368404748753913|2026-08-23|Comfora|unknown|unknown|https://heycomfora.com/products/comfora-pure-silvervine-dental-sticks
1066426213093097|2026-10-30|Pawtio Store|unknown|video|https://pawtio.co/products/pawtio-portable-catio
4497105180556041|2026-11-06|Lauren Patterson|unknown|unknown|https://clawval.com/pages/7-reasons-why-clawval-is-driving-cats-absolutely-wild
2301875253965185|2026-09-30|Comfora|unknown|unknown|https://heycomfora.com/products/comfora-pure-silvervine-dental-sticks
2595447507560252|2026-09-05|Susan Mitchell|unknown|unknown|https://heycomfora.com/products/comfora-pure-silvervine-dental-sticks
960397776574038|2026-04-19|Dr. Mia’s Cat Journal|unknown|video|https://try.purriq.com/7-reasons-listicle-v2
821953987099514|2026-04-15|Purriq|unknown|video|https://purriq.com/products/purriq-natural-silvervine-dental-sticks
941456861652275|2026-02-23|Dr. Mia’s Cat Journal|unknown|video|https://try.purriq.com/7-reasons-listicle-v2
867759395946621|2026-06-10|Purriq|unknown|video|https://try.purriq.com/7-reasons-listicle-v2
1430765658450709|2026-10-19|Lauren Patterson|unknown|unknown|https://clawval.com/products/clawval-natural-silvervine-dental-sticks'''

path=P/'meta_ads.csv'
with path.open(encoding='utf-8-sig',newline='') as f:
    reader=csv.DictReader(f); fields=reader.fieldnames; rows=list(reader)
known={r['ad_id'] for r in rows}
for line in raw.splitlines():
    aid,date,page,group,fmt,url=line.split('|')
    if aid in known: continue
    label = 'off-target: primary product is hairball treatment or catio; silvervine is a gift' if aid in {'1889741841696759','1066426213093097'} else ('unclear: ingredient not explicit in card' if aid=='1626632392578948' else 'product relevance not fully verified')
    row=dict(category='silvervine_chew',ad_id=aid,page_name=page,start_date=date,creative_group_count=group,format=fmt,landing_url=url,displayed_landing_domain=urlparse(url).hostname,domain_basis='visible Meta link destination; final redirect not checked',search_url=Q,source_date='2026-11-10',source_tier='◆',coverage='27 visible cards, convenience sample; '+label)
    rows.append({k:row.get(k,'') for k in fields}); known.add(aid)
with path.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)

path=P/'store_facts.csv'
with path.open(encoding='utf-8-sig',newline='') as f:
    reader=csv.DictReader(f); fields=reader.fieldnames; rows=list(reader)
if not any(r['domain']=='petmizer.com' for r in rows):
    u='https://petmizer.com/products/petmizer%E2%84%A2-blue-light-enzyme-deodorizer?currency=USD'
    d={k:'unknown: not verified' for k in fields}
    d.update(category='enzyme_pet_odor_device',domain='petmizer.com',sells='yes',product_url=u,price_one_bar='$59.99 device in USD-requested view; US delivery destination unconfirmed',bundles='two extra enzyme refill bottles option; initial add-on amount unknown',default_bundle='two-refill add-on checkbox preselected',subscription='two refills renew at $24.99 every 30 days, as displayed',refill_interval='30 days',subscription_cancellation='pause or cancel anytime, method not verified',returns='60-day guarantee',country='US delivery destination unconfirmed',currency='USD requested via query parameter',domain_registration='2026-04-20',age_class='unclear: other age evidence not checked',source_urls=u+' ; https://rdap.verisign.com/com/v1/domain/petmizer.com',source_date='2026-11-10',tier='◆',note='Renewal price does not establish initial add-on price; effects and safety are seller claims.')
    rows.append(d)
with path.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
