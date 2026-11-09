"""Rebuild a monthly review curve from sampled review-widget pages.

Input: TSV lines "page<TAB>M/D/YYYY" taken from a widget sorted newest-first
(Loox: ...reviews/<product_id>?h=<hash>&page=N&sort=newest, 15 reviews/page).
Between two samples, (page gap x per_page) reviews are spread evenly over the
days between their dates, then summed by calendar month.

Usage: python review_curve.py <samples.tsv> [per_page=15]
"""
import sys
from collections import defaultdict
from datetime import datetime, timedelta


def load(path):
    rows = []
    for line in open(path, encoding="utf8"):
        parts = line.strip().split("\t")
        if len(parts) != 2:
            continue
        rows.append((int(parts[0]), datetime.strptime(parts[1], "%m/%d/%Y")))
    return rows


def curve(rows, per_page=15):
    months = defaultdict(float)
    for (p1, d1), (p2, d2) in zip(rows, rows[1:]):
        n = (p2 - p1) * per_page          # reviews between the two samples
        days = max(1, (d1 - d2).days)     # newest-first, so d1 >= d2
        for k in range(days):
            day = d2 + timedelta(days=k)
            months[day.strftime("%Y-%m")] += n / days
    return dict(sorted(months.items()))


if __name__ == "__main__":
    rows = load(sys.argv[1])
    per = int(sys.argv[2]) if len(sys.argv) > 2 else 15
    c = curve(rows, per)
    first, last = rows[-1][1].strftime("%Y-%m"), rows[0][1].strftime("%Y-%m")
    print(f"covered {rows[-1][1].date()} .. {rows[0][1].date()}; "
          f"edge months {first} and {last} are partial")
    for m, v in c.items():
        print(f"{m}\t{v:7.0f}\t" + "#" * int(v / max(c.values()) * 40))
