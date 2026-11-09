"""Pull the passages of the 19 product videos where tactics are discussed (2026-11-09).
Keyword windows (±350 chars, merged) from the full transcripts, so the tips section is built from the
author's own words. Output: work/tips/windows.md (one block per video, with the video id)."""
import json, re, pathlib
T = pathlib.Path(r"C:\Users\Kirill\Documents\Codex-Research\Daily-Ecommerce-2026\transcripts")
OUT = pathlib.Path(__file__).parent / "windows.md"
VIDEOS = {"oDgModChsIo": "dog_fountain", "cmfJ_sxiO68": "color_foundation", "MUyL2RAaBw8": "body_oil", "ezFy2gHYXSE": "body_oil",
          "ta3BYsDhaSI": "scent_diffuser", "q85augBJ9Kk": "tallow_balm", "fylkQEOxacg": "persimmon_soap", "i_dc9klxsX0": "shower_filter",
          "IDYNVcPGtfc": "lash_serum", "aoTzuwQrCiw": "lash_serum", "reFwcjsOYiU": "hair_serum", "z06laDSzT9M": "prewash_oil",
          "fIIQuEV_RCQ": "hair_removal_cream", "9agzs1rK7y8": "pore_patch", "qey4n7UHRXc": "compression_socks", "W65gSMrv2p8": "whitening_powder",
          "e87jdUzxgpY": "magnesium_spray", "iIYC7y0Xxvs": "exfoliating_towel", "zRMForJwsy8": "turmeric_soap"}
KW = r"\b(ban|banned|policy|policies|disapprov\w*|reject\w*|restrict\w*|FDA|FTC|claims?|complian\w*|can't say|cannot say|not allowed|flagged|shut down|suspend\w*|cloak\w*|whitelist\w*|work ?around|get around|bypass|loophole|tricks?|hacks?|instead of saying|wording|legal|lawsuit|trademark|fake|AI (?:influencer|avatar|vet|doctor|model)|persona|advertorial|pre-?lander|listicle|white ?label\w*)\b"
out, total = [], 0
for v, pid in VIDEOS.items():
    d = json.loads((T / f"{v}.json").read_text(encoding="utf-8")); t = re.sub(r"\s+", " ", d["content"])
    spans = []
    for m in re.finditer(KW, t, re.I):
        a, b = max(0, m.start() - 300), min(len(t), m.end() + 300)
        if spans and a <= spans[-1][1]: spans[-1][1] = b
        else: spans.append([a, b])
    txt = "\n\n".join("… " + t[a:b] + " …" for a, b in spans)
    total += len(txt)
    out.append(f"## {v} · {pid} · {d.get('title','')}\n\n{txt}\n")
OUT.write_text("\n".join(out), encoding="utf-8")
print("chars", total, "of", sum(len(json.loads((T / f'{v}.json').read_text(encoding='utf-8'))['content']) for v in VIDEOS))
