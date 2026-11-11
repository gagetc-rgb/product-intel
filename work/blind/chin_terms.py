"""Chin wrap demand (2026-11-10). 'double chin' measured the problem, not the product, so the product's own phrasings
(how Amazon listings name it) and the leader brands are pulled instead: trends_pulls/chin_<day>.txt (each term alone)
and chin_together_<day>.txt (main phrasings on one shared scale).
Per term: yoy = last 12 full weeks / same 12 weeks a year earlier (trends_calc.yoy), share of zero weeks in 2 years.
Together: each phrasing's share of volume (last 52 weeks) and the yoy of their sum. Sector correction = that day's
sum of 5 broad personal-care terms (trends_combined.sector: x1.13 on 11-09, x1.11 on 11-10), same as for tallow and turmeric.
Usage (from work/blind): python chin_terms.py"""
import pathlib, statistics as st
from trends_calc import yoy, zero_share
from trends_combined import sector
D = pathlib.Path(__file__).with_name("trends_pulls")
def load(f): return {l.split("|")[0]: [float(x) for x in l.split("|")[2].split(",")] for l in f.read_text(encoding="utf-8").splitlines() if l.strip()}
for f in sorted(D.glob("chin_2*.txt")):
    SECTOR = sector(f.stem.rsplit("_", 1)[1]); print(f"== {f.name} (each term alone, sector x{SECTOR:.2f})")
    for t, v in load(f).items():
        y = yoy(v); print(f"  {t:22} yoy {y}  rel {round(y / SECTOR, 2) if y else None}  zeros {zero_share(v)}  mean52 {round(st.mean(v[-53:-1]), 1)}")
for f in sorted(D.glob("chin_together_*.txt")):
    SECTOR = sector(f.stem.rsplit("_", 1)[1]); P = load(f); tot = [sum(x) for x in zip(*P.values())]; vol = {t: st.mean(v[-53:-1]) for t, v in P.items()}; s = sum(vol.values()) or 1
    print(f"== {f.name} (shared scale, sector x{SECTOR:.2f})")
    for t in P: print(f"  {t:22} share of volume {vol[t] / s:.0%}  yoy alone-in-group {yoy(P[t])}")
    y = yoy(tot); print(f"  SUM yoy {y}  -> sector-corrected {round(y / SECTOR, 2) if y else None}  zeros {zero_share(tot)}")
