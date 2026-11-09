"""Fetch dated reviews from public Judge.me / Loox widgets and print monthly counts.

Usage:
  python review_fetch.py judgeme <shop>.myshopify.com <product_id> [<product_id>...]
  python review_fetch.py loox <shop>.myshopify.com <product_id> [<product_id>...]

Judge.me: every review is fetched (20 per page), exact dates.
Loox: if the product has <= 3000 reviews every page is read (15 per page, all
dates); above that, every Nth page is sampled and the result is approximate
(use review_curve.py on page->date pairs instead).
Output: total per product and a merged month -> count table (stdout, TSV).
"""
import json
import re
import sys
import time
import urllib.request
from collections import Counter
from datetime import datetime

UA = {"User-Agent": "Mozilla/5.0"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def judgeme(shop, pid):
    """Judge.me stops paginating deep (~page 50: later pages repeat the last one),
    so reviews are de-duplicated by id and the walk stops when nothing new arrives.
    Older reviews beyond that depth are not reachable this way."""
    seen, dates, page, total = set(), [], 1, None
    while True:
        u = (f"https://judge.me/reviews/reviews_for_widget?url={shop}&shop_domain={shop}"
             f"&platform=shopify&page={page}&per_page=20&product_id={pid}"
             f"&sort_by=created_at&sort_dir=desc")
        d = json.loads(get(u))
        total = d.get("total_count", total)
        h = d.get("html", "")
        ids = re.findall(r"data-review-id='([^']+)'", h)
        stamps = re.findall(r"jdgm-rev__timestamp[^>]*data-content='(\d{4}-\d{2}-\d{2})", h)
        new = [(i, s) for i, s in zip(ids, stamps) if i not in seen]
        if not new:
            break
        for i, s in new:
            seen.add(i)
            dates.append(s)
        if len(seen) >= (total or 0):
            break
        page += 1
        time.sleep(0.3)
    return total, [datetime.strptime(x, "%Y-%m-%d") for x in dates]


def loox_client(shop):
    js = get(f"https://loox.io/widget/loox.js?shop={shop}")
    return re.search(r"LOOX\.clientId = '([^']+)'", js).group(1)


def loox(shop, pid):
    cid = loox_client(shop)
    base = f"https://loox.io/widget/{cid}/reviews/{pid}?h=1&sort=newest"
    first = get(base + "&page=1")
    m = re.search(r"total=(\d+)", first)
    total = int(m.group(1)) if m else None
    pages = (total or 15) // 15 + 1
    step = 1 if pages <= 200 else pages // 100
    dates, prev = [], None
    for p in range(1, pages + 1, step):
        h = first if p == 1 else get(base + f"&page={p}")
        found = re.findall(r"\b(\d{1,2}/\d{1,2}/\d{4})\b", h)
        if not found or found == prev:  # end, or the widget repeats a page
            break
        prev = found
        dates += [datetime.strptime(x, "%m/%d/%Y") for x in found] * step
        time.sleep(0.3)
    return total, dates


if __name__ == "__main__":
    kind, shop, pids = sys.argv[1], sys.argv[2], sys.argv[3:]
    fn = judgeme if kind == "judgeme" else loox
    months = Counter()
    for pid in pids:
        try:
            total, dates = fn(shop, pid)
        except Exception as e:  # keep going on one bad product
            print(f"# {pid}: error {e}")
            continue
        print(f"# {pid}: total={total} dated={len(dates)} "
              f"range={min(dates).date() if dates else '-'}..{max(dates).date() if dates else '-'}")
        months.update(d.strftime("%Y-%m") for d in dates)
    for m in sorted(months):
        print(f"{m}\t{months[m]}")
