import csv
from pathlib import Path

p=Path(__file__).parent
ids='''6aed201f0e8a551cebc98018 6aed12f3df8a1de487d0ab54 6aed0e97b5772d81eaa3662f 6aed0c37bfd1a92e852db524 6aecb6ae454186b3d9f37e30 6aecaa132f6a2aba11ec78c6 6aeca876146a74d4709c226f 6aec496c0638f2c15aaed12c 6aebd4f6f55c8c4a38b21219 6aeba1d29cfa9e8ae2fcaf35 6aeb8f2cb05736d94487a1aa 6aeb70bf4c99850686dec213 6aeb68e4f8481a25b4cfe0a5 6aeb63c8824dce060402e839 6aeb60a122b470f29a2c6fa5 6aeb55374cace8fd782d9256 6aea4f46410d4b589fb1e7b2 6aea49f083e6e99d64ab0ff4 6ae91b2192d3e54c8fff6b76 6ae916b130629403d01a8081 6ae8a84b16347164efc144da 6ae767ba8967fd450d7a5f91 6ae7465e1ee4f878f17b6404 6ae726fa1d22827deed00af9 6ae618870efa0aee5d492f32 6ae56806cb2191d4fa429178 6ae55421526870673f4e7d07 6ae53c09be560d6a4d560546 6ae3894117cd07b0f6dab034 6ae3717aa28dda7b43793b94 6ae37147624c3d9b1d8cfcfc 6ae27c73dc86b05e6b8ef5bd 6ae26a46a983aa0c731953a4 6ae243aa46b42d43ae408334 6ae23cc14e48acb314d13bd6'''.split()
stars=[3,3,3,2,2,2,3,2,3,3,1,1,2,3,1,2,3,1,3,2,2,1,1,3,3,3,3,1,2,1,3,1,3,1,1]
themes={'shipping_delivery':{4,5,9,14,18,19,20,21,22,30,31,32},'billing_subscription':{12,14,15,22},'support_refunds':{12,15,24,26},'product_experience':{8,9,11,16,19,21,25,28,29},'no_perceived_effect':{1,5,6,7,13,25,28,34,35}}
assert len(ids)==len(stars)==35
fields=['review_url','stars','shipping_delivery','billing_subscription','support_refunds','product_experience','no_perceived_effect','source_date','tier','scope']
with (p/'mirai_low_review_codes.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for n,(review,star) in enumerate(zip(ids,stars),1):
        row=dict(review_url='https://www.trustpilot.com/reviews/'+review,stars=star,source_date='2026-11-10',tier='◈',scope='35 low-star reviews in latest 200; non-exclusive manual codes')
        row.update({key:int(n in val) for key,val in themes.items()});w.writerow(row)

f=p/'leader_complaints.csv'
with f.open(encoding='utf-8-sig',newline='') as x:
    r=csv.DictReader(x);fields=r.fieldnames;rows=list(r)
for row in rows:
    if row['domain']=='miraiclinical.com':
        row['complaint_theme_counts']='35 low-star of latest 200; non-exclusive: shipping/delivery 12; billing/subscription 4; support/refunds 4; product experience 9; no perceived effect 9; see mirai_low_review_codes.csv'
        row['limitations']='Global profile includes several product lines; reviews are unverified allegations. Codes based on reviewer text; other or unclear reviews may have no theme.'
with f.open('w',encoding='utf-8-sig',newline='') as x:
    w=csv.DictWriter(x,fieldnames=fields);w.writeheader();w.writerows(rows)
print({k:len(v) for k,v in themes.items()})
