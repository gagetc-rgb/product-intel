import csv
from pathlib import Path

root = Path(__file__).resolve().parent
# IDs are the 39 low-star reviews in the 200 unique, most-recently displayed
# review cards, read on 2026-11-10. Codes are non-exclusive and describe
# reviewer allegations, not verified events.
rows = '''6af27c6506afb6cfd78124c4,1,product;support
6af1280240493511ab1104d7,1,billing
6aea7c504f7b7fc3476b66c3,1,no_effect
6ae8bf7741766e202b1f0612,1,product
6ae7be72d297a470a90a9318,2,product
6ae74d06e17182a134980baa,1,other
6ae66a5cade265ece769bb3d,1,product;no_effect
6ae538f2c7927f0243a5d3ba,1,no_effect;support
6ae4a5ca15e4dac6bad802d1,1,product;support
6ae3991e5a9635a05dad2e4e,2,billing
6ae0b25c269d40a890d12bd5,1,product;support
6adf939d9b9c8f9cdbd9a61a,1,product;support
6adf3f68bc36380b1c07912c,1,product;support
6adedcd7db8fdafbe1b224d8,3,product
6adeb7ae6fc117170b1aa9e5,1,product;support
6adeb6fb88ee5c28c464f55b,2,product;support
6ade36f6bc8a41f47fddf511,1,no_effect
6add50f4b05083e8d32e630c,1,product;no_effect
6adcef17c86a9d7d75397d6f,1,no_effect
6adadd413aba7dd5b99626d9,3,product
6ada592a11e9d39fde9af116,2,product;support
6ad82e068ad5682ec800b7d1,1,shipping;support
6ad630ac9771db245734d166,1,product;no_effect
6ad25b025c9aadd0d7f10aae,1,shipping;support
6ad1708b4094e4bff14e51b1,1,product;support
6acff4c71a1a5093e07e064f,1,no_effect
6acaad7339ddbcbc170e69df,1,support
6aca1ce9bddf8685cc399de7,1,shipping;support
6ac90d8744bd3362a56d3201,3,product
6ac731306ecac9c9ecf75e79,1,product;support
6ac6561dbec825caa2b67c1f,1,product;support
6ac64dce029232d3345698ed,2,product;support
6ac63e2e928d1b2fd1d41350,1,no_effect
6ac638ff2a3f99a7928a842e,1,product;support
6ac56896d5754a2220c580f5,1,shipping;support
6ac39d6e8369e4608720f552,1,billing;support
6ac0c34788b967ab5a952306,2,other
6abfcdff287d0ba2731ec8f7,1,product
6abf6a0528672ff286f666d4,1,product;support'''
parsed = [line.split(',') for line in rows.splitlines()]
assert len(parsed) == 39 and len({r[0] for r in parsed}) == 39
themes = ('product', 'shipping', 'billing', 'support', 'no_effect', 'other')
with (root / 'prime_low_review_codes.csv').open('w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['review_url', 'stars', *themes, 'source_date', 'tier'])
    for ident, stars, labels in parsed:
        codes = labels.split(';')
        writer.writerow(['https://www.trustpilot.com/reviews/' + ident, stars,
                         *(int(theme in codes) for theme in themes), '2026-11-10', '◈'])
counts = {theme: sum(theme in labels.split(';') for _, _, labels in parsed) for theme in themes}
print(counts)
