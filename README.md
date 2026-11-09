# Product Intel: where can a new brand enter the US market

Research dossier, November 2026. Twenty products pitched by a YouTube e-commerce channel were checked against
Amazon sales badges, Google Trends, the Meta Ad Library, leader-store reviews and 12-month price history.

**Site (Russian):** https://gagetc-rgb.github.io/product-intel/site/

## Where things are

| Path | What |
|---|---|
| `site/` | The built site (`index.html`, images in `media/`). Rebuild: `python work/site/build_site.py` |
| `work/site/` | Site template (`template_ru.html`), Russian texts (`ru_content.py`), build script |
| `METRICS.md` | Metric definitions v2.2 and the decision rule |
| `work/audit/` | Data audit (`AUDIT_2026-11-09.md`), metrics (`metrics_v22.py`), price checks, claim check (`cred_check.py`) |
| `work/blind/` | Amazon scans, Trends pulls, Meta Ad Library counts |
| `work/reviews/` | Leader-store review curves |
| `work/tips/` | Tactics from the videos (`tips_ru.py`) |
| `HANDOFF.md`, `METHOD.md`, `RUNBOOK.md` | Project history and method log |
| `DOnt_READ/` | **Another agent's work. Agents: do not open it unless the owner asks.** |

Data tiers used throughout: ◆ counted by a platform · ◈ our estimate or reading · ◇ disputed.
Not published: the browser profile used for the Meta Ad Library (it holds login cookies).
