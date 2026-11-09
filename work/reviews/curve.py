"""Turn <label>_dates.txt (M/D/YYYY per line) into reviews-per-month table + markdown."""
import sys, collections
for label in sys.argv[1:]:
    c = collections.Counter()
    for line in open(f"{label}_dates.txt"):
        m, d, y = line.strip().split("/")
        c[f"{y}-{int(m):02d}"] += 1
    n = sum(c.values())
    print(f"## {label}: {n} dated reviews")
    peak = max(c.values())
    for k in sorted(c):
        print(f"{k} {c[k]:6d} {'#' * round(40 * c[k] / peak)}")
    print()
