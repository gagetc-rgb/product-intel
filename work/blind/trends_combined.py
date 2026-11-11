"""A1 for tallow and turmeric (2026-11-10). All product phrasings are pulled together on one shared scale and summed;
the sum's yoy (trends_calc rule: last 12 full weeks / same weeks a year earlier) is divided by the yoy of the sector,
5 broad personal-care terms pulled together the same day (shampoo, body lotion, moisturizer, deodorant, face wash).
Files: trends_pulls/combined_<tallow|turmeric|sector>_<day>.txt.
The 2026-11-09 sample exists only as numbers in AUDIT_2026-11-09 section 7 (its raw pull was not saved):
sector x1.13, tallow x0.88 -> x0.78, turmeric x0.81 -> x0.72.
A1 = mean of the daily samples; the result is carried by A1_COMBINED in work/audit/metrics_v22.py.
Usage (from work/blind): python trends_combined.py"""
import pathlib, statistics as st
D = pathlib.Path(__file__).with_name("trends_pulls")
AUDIT_1109 = {"sector": 1.13, "tallow": 0.78, "turmeric": 0.72}  # sector-corrected values, AUDIT section 7

def load(f): return {l.split("|")[0]: [float(x) for x in l.split("|")[2].split(",")] for l in f.read_text(encoding="utf-8").splitlines() if l.strip()}
def yoy(v):  # same rule as trends_calc.yoy, without rounding
    v = v[:-1]; ago = st.mean(v[-64:-52])
    return st.mean(v[-12:]) / ago if ago > 0 else None
def sum_yoy(P): return yoy([sum(x) for x in zip(*P.values())])
def sector(day):
    f = D / f"combined_sector_{day}.txt"
    return sum_yoy(load(f)) if f.exists() else AUDIT_1109["sector"] if day.startswith("2026-11-09") else None

if __name__ == "__main__":
    samples = {g: [AUDIT_1109[g]] for g in ("tallow", "turmeric")}
    print(f"== 2026-11-09 (AUDIT section 7): sector x{AUDIT_1109['sector']}, tallow x{AUDIT_1109['tallow']}, turmeric x{AUDIT_1109['turmeric']}")
    for day in sorted(f.stem.rsplit("_", 1)[1] for f in D.glob("combined_sector_*.txt")):
        s = sector(day); print(f"== {day}: sector sum x{s:.2f}")
        for g in samples:
            f = D / f"combined_{g}_{day}.txt"
            if not f.exists(): continue
            P = load(f); y = sum_yoy(P)
            print(f"  {g}: " + ", ".join(f"{t} x{yoy(v):.2f}" for t, v in P.items()) + f" -> sum x{y:.2f} -> corrected x{y / s:.2f}")
            samples[g].append(y / s)
    for g, v in samples.items(): print(f"A1 {g}: samples {[round(x, 2) for x in v]} -> mean {st.mean(v):.2f}")
