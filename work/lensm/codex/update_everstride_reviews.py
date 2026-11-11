import csv
from pathlib import Path
p=Path(__file__).resolve().parent
data='''6aef7dc54d6d7bc416f5d2cf,3,product;no_effect
6aed9563a1eaa3c4f7875ef9,2,product;support
6aea709faa9ccf13af7eebf2,1,support
6ada5fde4684a56d27b6472d,1,product;no_effect
6ad185757ba74e67e3988b9f,2,product;no_effect
6acd66aa8aea29500e7ea02c,3,product
6ac40877091e87b7be57e4fa,3,product
6abb6944cb90a2819f49b13a,3,no_effect
6ab9697b187fd1e36beaad4b,2,product
6ab94092bce3422863a32276,2,product
6ab5a6bd5b129a919179068d,3,other
6aac9ffa08d11bf5b5f38742,3,product
6aaad9bb1275a2fdb8a29669,1,product;shipping'''
rows=[s.split(',') for s in data.splitlines()];themes=['product','shipping','billing','support','no_effect','other'];assert len(rows)==13
counts={k:sum(k in r[2].split(';') for r in rows) for k in themes}
with (p/'everstride_low_review_codes.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f);w.writerow(['review_url','stars',*themes,'source_date','tier'])
 for ident,stars,codes in rows:w.writerow(['https://www.trustpilot.com/reviews/'+ident,stars,*(int(k in codes.split(';')) for k in themes),'2026-11-10','◈'])
f=p/'leader_complaints.csv'
with f.open(encoding='utf-8-sig',newline='') as stream:
 reader=csv.DictReader(stream);fields=reader.fieldnames;allrows=list(reader)
def base(domain):return dict(domain=domain,source=f'https://www.trustpilot.com/review/{domain}?sort=recency',source_date='2026-11-10',tier='◆ / ◈',filtered_reviews_url=f'https://www.trustpilot.com/review/{domain}?sort=recency')
e=base('everstridesocks.com');e.update(displayed_score='4.7 numeric; star-image label 4.5',total_reviews='1875',stars_5='1576',stars_4='163',stars_3='31',stars_2='22',stars_1='83',scope='all-profile counts; separate latest-200 distribution',sample_latest_200='200 unique; five 168; four 19; three 6; two 4; one 3; displayed endpoint timestamps 2026-11-09 to 2026-09-11',complaint_theme_counts='; '.join(f'{k} {v}' for k,v in counts.items()),limitations='Global self-selected profile; dates may reflect edits. Reviewers report different models; allegations not independently verified. Other 1875-200 reviews not coded.')
others=[]
for domain,claimed in [('scentifyhome.com','unclaimed'),('terralotus.shop','claimed Nov 2026')]:
 r=base(domain);r.update(displayed_score='0.0 placeholder; no usable score',total_reviews='0',stars_5='0',stars_4='0',stars_3='0',stars_2='0',stars_1='0',scope=f'exact-domain profile, {claimed}',sample_latest_200='0 available',complaint_theme_counts='unknown: no reviews',limitations='No reviews is not evidence of quality. Distinct similar-name profiles not merged.');others.append(r)
r=base('babeoriginal.com');r.update(displayed_score='3.8 numeric; star-image label 4.0',total_reviews='2',stars_5='2',stars_4='0',stars_3='0',stars_2='0',stars_1='0',scope='exact-domain unclaimed profile',sample_latest_200='2 available, both five-star',complaint_theme_counts='unknown: no low-star reviews available',limitations='Two reviews only, not enough to infer complaint prevalence; dates 2023-12-28 and 2026-08-22.');others.append(r)
for row in [e,*others]:
 if not any(old['domain']==row['domain'] for old in allrows):allrows.append(row)
with f.open('w',encoding='utf-8-sig',newline='') as stream:
 writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader();writer.writerows(allrows)
section=f'''
## Everstride — latest 200 Trustpilot reviews, 2026-11-10

◆ [Exact-domain profile](https://www.trustpilot.com/review/everstridesocks.com?sort=recency): TrustScore 4.7, 1,875 reviews; profile-wide five/four/three/two/one-star counts 1,576/163/31/22/83. ◈ The first 200 distinct cards across ten pages are 168/19/6/4/3 respectively; endpoint displayed timestamps 2026-11-09 and 2026-09-11. These are self-selected global reviews of different sock variants, not a US-only sample; timestamps may reflect edits.

◈ Of 13 reviews with 1–3 stars: {', '.join(f'{k} {v}' for k,v in counts.items())}, non-exclusive; individual sources are in `everstride_low_review_codes.csv`. Examples include [a hole after a single wear](https://www.trustpilot.com/reviews/6aef7dc54d6d7bc416f5d2cf), [heels wearing through repeatedly](https://www.trustpilot.com/reviews/6ab94092bce3422863a32276), [perceived weak compression](https://www.trustpilot.com/reviews/6ad185757ba74e67e3988b9f), [too-tight fit](https://www.trustpilot.com/reviews/6ac40877091e87b7be57e4fa), [return dispute](https://www.trustpilot.com/reviews/6aea709faa9ccf13af7eebf2), and [a late order with the wrong size](https://www.trustpilot.com/reviews/6aaad9bb1275a2fdb8a29669). One reviewer reported prompt replacement despite repeat holes. All are unverified accounts. A follower could test durability, size guidance and return handling; these reviews cannot establish population defect or medical outcomes.

## Other exact-domain Trustpilot checks, 2026-11-10

◆ [Scentify Home](https://www.trustpilot.com/review/scentifyhome.com?sort=recency) and [Terra Lotus](https://www.trustpilot.com/review/terralotus.shop?sort=recency) showed zero reviews; 0.0 is a no-review placeholder, not an actual quality rating. Terra Lotus profile was claimed in November 2026; that is not its business-creation date. ◆ [Babe Original](https://www.trustpilot.com/review/babeoriginal.com?sort=recency) showed two five-star reviews, score 3.8, and zero low-star reviews. These sparse profiles cannot support a meaningful complaint rate, and similar domain names are not merged.
'''
f=p/'LEADER_COMPLAINTS.md';t=f.read_text(encoding='utf-8')
if '## Everstride — latest 200 Trustpilot reviews' not in t:f.write_text(t+section,encoding='utf-8')
with (p/'METHOD_LOG.md').open('a',encoding='utf-8') as stream:stream.write('\n- 2026-11-10: live logged-off Trustpilot Everstride: 200 unique cards across ten pages, 13 low-star IDs coded. Page-transition timeouts required checking the loaded first review before saving; duplicates were excluded. Exact-domain Scentify Home and Terra Lotus had zero reviews; Babe Original had two.\n')
print(counts)
