# BigSpy free-plan test (2026-11-07)

Goal: does BigSpy keep STOPPED ads with first/last-seen dates and long history (needed for the survivor/"90+ days" metric)?
Tested through the web UI only (Ad Library, keyword = domain, Time = "Last 2 Years", sort = running days).

## Findings
- Archive depth: ◆ ads back to Oct 2024 found for earthlyderm.com (first_seen 2024-10-21). "Last 2 Years" is selectable on the free plan.
- Stopped ads are kept: ◆ earthlyderm.com ad 2024-10-21 → 2025-09-04 (319 running days, ~1.4M impressions); 4 "Black Men CAN Shave" ads stopped 2026-10-23 after 182-216 days.
- Volume: earthlyderm.com 2.7K ads in last 90 days vs 4.5K in last 2 years (2.4K / 986 after dedup). stemandsoul.co 2.3K ads in 2 years.
- stemandsoul.co: ◆ top ad 2025-12-09 → 2026-10-13 (309 days, 1.3M impressions), stopped; 4 more ads 2026-05-29 → 2026-10-17 (142 days).
- Card fields: first-last date range, Running Days, Last Seen, Impression, Creative Score, Popularity.
- Sorting offers only descending options (relevance, impressions, latest creatives, last seen, running days, ...). No "oldest first".

## Caveats
- ◈ "Running Days" is not last_seen − first_seen: some ads show a 3-month date range but "2 days". Treat it as days with detected delivery, and use the date range for survival logic.
- ◇ Ad Info search matches text, not only the store: one domain search may include affiliates/clones. Not verified.
- ◇ Country (US only) not tested: whether stopped US-delivered ads are retained is still unconfirmed. Next check: Country/Region = United States filter.
- Quota: the app's counter endpoint reported limit 10 / count 1 at first read, later limit 50 / count 0. Unclear which key counts as a "search"; the free limit may differ from 5.
- The browser pane is narrow, so page controls scroll horizontally; direct API replays were blocked by the safety classifier and were not used.

## Update: magnesium oil spray (same day)
- Quota: ◆ the free daily limit was hit after 3 keyword searches plus filter/sort changes (earthlyderm.com, stemandsoul.co, "magnesium oil spray"); the 4th search (Seven Minerals) showed "Today's search quota has been used up". The counter endpoint (limit 10/50) was not reliable. Each filter change likely counts as a search.
- Search "magnesium oil spray", Time = Last 2 Years, eCom: 7.9K ads (4.2K after default dedup), 174 advertisers after advertiser dedup. Top advertisers by running days:
  - Salt Lab (saltlab): 2024-03-19 → 2025-06-08, 447 days, ~2.1M impressions, STOPPED; second domain 2025-11-02 → 2026-05-19, 199 days, stopped. Amazon listing since 2019, only ~366 reviews.
  - Seven Minerals: 2026-01-16 → 2026-10-22, 280 days, ~1.7M impressions, last seen 2026-10-22; ad sends traffic to Amazon (domain am***com). Amazon listing since 2024-03-22, 39,208 reviews (from the graveyard file).
  - Dental brand (jaw pain ad): 2026-03-02 → 2026-06-12, 103 days, stopped (not a direct competitor).
  - An .com.au advertiser "Magnesium Oil Spray": 2026-07-01 → 2026-10-06, 98 days.
- NOT yet checked: Seven Minerals' full ad history (searches exhausted). Next: keyword "Seven Minerals", Last 2 Years, sort by running days, when the quota resets.
