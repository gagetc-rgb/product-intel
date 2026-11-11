import csv
from pathlib import Path

p = Path(__file__).resolve().parent
file = p / 'leader_complaints.csv'
with file.open(encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    fields, rows = reader.fieldnames, list(reader)
row = dict(domain='primeprometics.com', source='https://www.trustpilot.com/review/primeprometics.com?sort=recency', source_date='2026-11-10', tier='◆ / ◈', displayed_score='4.3 numeric; star-image label 4.5', total_reviews='4475', stars_5='3316', stars_4='252', stars_3='100', stars_2='139', stars_1='668', scope='all-profile star counts; separate latest-200 distribution in next column', sample_latest_200='200 unique: five 148; four 13; three 3; two 6; one 30; displayed endpoint timestamps 2026-11-10 and 2026-10-01', complaint_theme_counts='39 low-star; non-exclusive: product 23; shipping 4; billing 3; support/refunds 21; no perceived effect 9; other 2; see prime_low_review_codes.csv', filtered_reviews_url='https://www.trustpilot.com/review/primeprometics.com?sort=recency', limitations='Global multi-product profile, not US foundation reviews; review timestamps may be updated; sample snapshot is not stable as new reviews arrive. Company disputes some allegations. Trustpilot reports merged profiles.')
if not any(r['domain'] == row['domain'] for r in rows):
    rows.append(row)
    with file.open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)

entry = '''
## Prime Prometics — live Trustpilot sample, 2026-11-10

◆ [Profile sorted by most recent](https://www.trustpilot.com/review/primeprometics.com?sort=recency): numeric TrustScore 4.3, 4,475 reviews; profile-wide five/four/three/two/one-star counts 3,316/252/100/139/668. Trustpilot says this profile includes merged reviews. Counts are a live snapshot and can change.

◈ The first 200 **distinct** displayed review IDs across ten pages have 148 five-star, 13 four-star, 3 three-star, 6 two-star and 30 one-star reviews. The newest and oldest displayed endpoint timestamps were 2026-11-10 and 2026-10-01; some review timestamps reflect edits. This is a global, multi-product and self-selected sample, not a US-only or color-changing-foundation sample. The 39 low-star review IDs and non-exclusive codes are in `prime_low_review_codes.csv`; the 161 other IDs were not retained individually. Reviewers' accounts are allegations, not verified findings.

◈ Of 39 low-star reviews: product experience 23; support/refunds 21; no perceived effect 9; shipping 4; billing/checkout 3; other 2. Codes can overlap. In particular, a complaint about color, texture or a broken applicator is product experience, while no perceived promised result is coded as no effect. A hypothetical fear of being denied a return is not coded as an actual support failure. The company disputes some accounts; one [response](https://www.trustpilot.com/reviews/6af27c6506afb6cfd78124c4) says a refund was processed.

Examples, paraphrased and linked:

- **Product:** [foundation appeared yellow and heavy](https://www.trustpilot.com/reviews/6adadd413aba7dd5b99626d9); [eye product's applicator dispensed unevenly](https://www.trustpilot.com/reviews/6ae66a5cade265ece769bb3d); [lip product was dry on arrival](https://www.trustpilot.com/reviews/6ae7be72d297a470a90a9318).
- **Support/refunds:** [one buyer reported repeated return requests](https://www.trustpilot.com/reviews/6af27c6506afb6cfd78124c4); [a purchaser reported no response](https://www.trustpilot.com/reviews/6ae0b25c269d40a890d12bd5); [a buyer said a faulty item's replacement was refused](https://www.trustpilot.com/reviews/6adf939d9b9c8f9cdbd9a61a).
- **No perceived effect:** [eye product did not reduce puffiness](https://www.trustpilot.com/reviews/6aea7c504f7b7fc3476b66c3); [lip color faded quickly](https://www.trustpilot.com/reviews/6adcef17c86a9d7d75397d6f); [a buyer reported no difference from eye cream](https://www.trustpilot.com/reviews/6acff4c71a1a5093e07e064f).
- **Shipping:** [buyer reported non-delivery](https://www.trustpilot.com/reviews/6ad82e068ad5682ec800b7d1); [items allegedly omitted from order](https://www.trustpilot.com/reviews/6aca1ce9bddf8685cc399de7); [tracking allegedly did not show processing](https://www.trustpilot.com/reviews/6ac56896d5754a2220c580f5).
- **Billing:** [discount and free-shipping interaction was unclear](https://www.trustpilot.com/reviews/6af1280240493511ab1104d7); [checkout total appeared inconsistent](https://www.trustpilot.com/reviews/6ae3991e5a9635a05dad2e4e); [bundle price allegedly exceeded promotion](https://www.trustpilot.com/reviews/6ac39d6e8369e4608720f552). A discrepancy is not independently reconciled with tax, shipping or promotion terms.

**Potentially fixable:** clearer checkout and refund terms, reliable applicators, visible order tracking and responsive support. **Not established:** whether a follower's formulation would suit all skin tones or prevent individual sensitivity; these reviews cannot establish product-wide defect or reaction rates.
'''
out = p / 'LEADER_COMPLAINTS.md'
text = out.read_text(encoding='utf-8')
if '## Prime Prometics — live Trustpilot sample' not in text:
    out.write_text(text + entry, encoding='utf-8')
with (p / 'METHOD_LOG.md').open('a', encoding='utf-8') as f:
    f.write('\n- 2026-11-10: Trustpilot Prime Prometics via logged-off in-app browser, '+row['source']+'; kept 200 distinct cards from pages 1–10, and coded 39 low-star IDs. Pagination initially returned previous DOM immediately after URL changed; discarded duplicate and waited for old card to detach. Trustpilot reports profile merges. ◈ Sample is global and multi-product.\n')
