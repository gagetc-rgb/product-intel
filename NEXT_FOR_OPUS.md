# Handoff to the next session (written 2026-11-10 by the Fable session)

Start a NEW session (short context) and read only these, in this order:
1. `HANDOFF.md` → section "START HERE" (top five bullets are today's state).
2. `METRICS.md` → sections "v2.4" and "v2.3".
3. `PLAN_V24_2026-11-10.md` (site edits, animation idea, who does what, "to be clarified").

Rules: documents in English, chat with the owner in Russian. No commit, no publish until the owner has seen the result. Do not run `work/site/ru_content.py`. No automated Amazon access. Owner's decision (2026-11-10): no subagents; do the tasks directly in this session, and give volume scraping to Codex. Where the tasks below say "Sonnet", do it yourself. Spot-check any outside numbers against their sources.

## State

- Site (local, not committed): first edition under v2.3 is applied and checked. `http://localhost:8765/site/index.html`.
- Method: v2.4 = "copy the leader's store and scale it with ads" (lens M, metrics M1-M8). The site does not show it yet.
- Lens M data so far: `work/lensm/M2_RESULT.md` (the 20 products), `work/lensm/rp/RP_RESULT.md` (five extra products), Codex step 1 accepted in `work/lensm/codex/ACCEPTANCE_STEP1_2026-11-11.md`. Only tallow balm has two young, brand-only followers holding 90+ and 180+ days (wildgoldtallow.com, bare-ritual.com). Work insoles dropped off this list on 2026-11-11 (getxstance.com is tied to thexstance.com, 2020; movaracare.com's 90+ ads sell boots). Kaori (persimmon) holds mostly through persona pages; MYTO (tooth powder) is a new young brand-only follower.
- Codex task, ready to hand over: `work/prompts/CODEX_SCRAPE_LENS_M.md`.

## Tasks, in order

1. Site edits that need no new data (`PLAN_V24` §2, items 1, 9, 10, 11): cover wording for the copy model, the block of young follower stores, the limits of the sample, lens M on the methodology page. Write the exact Russian texts, give them to a Sonnet subagent to apply, rebuild, check.
2. Compile `work/site/ranking_history.json` from the files listed in `PLAN_V24` §3.2 (Sonnet). Verify three steps by hand.
3. Insoles: check what is still open before it can be shown as a candidate: the 30-89 day stores, store prices in USD, whether "orthopedic" wording makes it a medical device (primary source: FDA), margin for an own store (`METRICS.md` M4).
4. When Codex returns: acceptance by 10 random rows against their source URLs, then the verdicts under lens M.
5. Owner's open decision: show ad evidence per store (advertising without a break; ads older than 30 days; change since last check) instead of the single 90-day cut (`PLAN_V24` §2, item 7).
6. 2026-12-08: repeat the saved Meta searches (follower death rate, M3), one Trends pull.

## Keep for Fable (short, separate sessions, one task each)

- A second opinion on a method change before it is frozen.
- Review of a finished report or site edition before it goes to the investor: what is unproven, what contradicts what.
- The investor's narrative: cover, order of the argument, the one-page summary.
- The animation storyboard and the caption of each step (`PLAN_V24` §3.5).
- The design of the money test and its pass bar.
