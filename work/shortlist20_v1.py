"""Evidence-based ranking of 'working' products from the Daily Ecommerce corpus (US).
Data collected 2026-11-06/07: Meta Ad Library (US, active, logged-off, top ~30 by impressions),
Google Trends API (US, 12 months, % of 'ski boots'), competitor sites, Alibaba, tariff tables.
Run: python shortlist20.py -> shortlist20.md
"""

# Each row: name, leader (domain), A = leader active US ads, M = months since oldest top-impression ad started,
# S = search % of 'ski boots', P = active US ads matching category phrase, D = distinct domains in top-30,
# F = feasibility 1-5 (regulation/ops, judgment with reason), CAC = max CAC per order (model, USD), est = which inputs are estimates,
# why = why it works, risk = main pitfalls
R = [
 ("Non-tarnish tennis bracelet", "mylovemytreasure.com", 280, 8, 140, 2700, 8, 5, 55, "",
  "Huge search demand; image ads; from $69 vs $1.5-3.5 cost", "Most crowded category; Amazon floor $15; tarnish quality"),
 ("Turmeric 'fade & glow' soap (melanin-rich skin)", "earthlyderm.com", 510, 9, 21, 320, 7, 3, 23, "",
  "Search demand exists; leader 10x traffic in 2026; $1 bar sells 3 for $39; repeat buys", "Drug-like claims (pigment); race wording vs Meta policy; irritation"),
 ("Persimmon soap (aging body odor)", "try-kaori.com / swarva.com", 750, 11, 13, 2600, 4, 3, 22, "",
  "Rising search; 60+ buyers on Facebook; subscriptions", "Flooded with clones; fake-persona playbook"),
 ("Bamboo compression socks", "everstridesocks.com", 1600, 26, 289, 15000, 8, 4, 28, "CAC",
  "Leader advertising nonstop for 2+ years; biggest search demand on the list; bundles of 8", "Crowded; avoid lymphedema/medical claims; sizing"),
 ("Natural rodent repellent pouches", "sofyre", 13000, 2, 28, 9700, 4, 2, 25, "CAC",
  "Massive current ad scale; cheap consumable; repeat", "EPA 25(b) minimum-risk rules + state registrations; efficacy complaints"),
 ("Men's leak-proof boxers", "menvault.com", 330, 11, 3, 560, 6, 2, 49, "",
  "100% US traffic; $149.95 six-pack; repeat", "FDA establishment fee $11.4K/yr if importing; leader underdelivers"),
 ("Collagen chin/jaw wrap", "tryskult.com", 770, 14, 2, 610, 2, 4, 28, "",
  "Top ad live 14 months; one brand owns the phrase", "No search demand; temporary effect, refunds"),
 ("2-in-1 garment duffel", "luhxe.com", 490, 4, 3, 1500, 10, 4, 62, "",
  "$129 AOV; 'bag pays for itself' angle", "Bulky shipping; ~55% duty; fake-giveaway playbook"),
 ("Men's compression tank", "north-alpine.com", 1700, 2, 1, 3800, 6, 3, 14, "",
  "Scaling hard right now; 100% AI ads", "Short US history; high apparel duty; sizes/returns"),
 ("Inflatable airplane seat cushion", "shoptravlr.com", 410, 10, 3, 1100, 5, 5, 51, "",
  "Long-running; $80 price vs <$8 cost", "Crowded (Sondur, Travlr…); persona playbook"),
 ("Gel ski shin sleeve", "skiguards.com", 230, 12, 0, 130, 2, 5, 40, "",
  "Same ads ran all last season", "No search demand; seasonal; skiers skeptical"),
 ("Dog calming pheromone diffuser", "therapet", 810, 2, 38, 1000, 6, 3, 35, "P,D,CAC",
  "Strong search ('dog calming'); plug-in + refills = repeat", "Adaptil incumbent; efficacy disputes; plug-in electronics"),
 ("Silvervine cat chew sticks", "purriq", 270, 13, 7, 670, 3, 4, 22, "CAC",
  "Leader live 13 months; consumable; low competition", "Low ticket; cat-safety claims"),
 ("Back stretcher board", "lhanel.co", 600, 6, 7, 54, 5, 4, 28, "CAC",
  "Leader 600 ads, few clones on the phrase", "Disc/sciatica wording is medical; bulky-ish"),
 ("Exfoliating body towel", "blissal.com", 190, 8, 5, 460, 5, 5, 22, "CAC",
  "Leader live 8 months; no regulation; multipacks", "Low ticket; Salux-type cheap on Amazon"),
 ("Lash serum (peptide, cosmetic)", "several (no single leader)", 150, 10, 138, 3200, 8, 3, 30, "A,CAC",
  "Big search demand; $1-2 cost", "Prostaglandin = drug; growth claims; crowded"),
 ("Red-light LED face mask (FDA-cleared OEM)", "solawave.co / omniluxled.com", 300, 6, 86, 440, 6, 2, 60, "A,M,CAC",
  "Big demand; high AOV", "Needs a cleared OEM (K-number) for wrinkle claims; big brands"),
 ("16-head vibration massager (gift)", "several (vitalhorse, zevessa…)", 150, 15, 21, 460, 6, 3, 86, "A",
  "High AOV leaves room for ad costs; gift angle", "Battery/FCC; pain claims; heavy returns"),
 ("Men's/body hair removal cream", "nohaircrew / meravae / shopluuma", 40, 17, 65, 2800, 11, 4, 25, "CAC",
  "Strong search; ads live 17 months in category", "Many sellers; chemical burns → refunds"),
 ("Teeth whitening powder", "ecobrightsmile.com", 30, 2, 7, 59, 6, 4, 25, "A,CAC",
  "Few advertisers; cheap to make", "Small proven scale; enamel claims"),
 ("Dog water fountain (steel)", "goodorigins", 110, 6, 18, 300, 4, 3, 30, "P,D,CAC",
  "Search demand; vet-expert angle", "Amazon cheap; pump electronics"),
 ("Ultrasonic bark deterrent", "purestwaves.com", 290, 1, 3, 510, 7, 3, 25, "CAC",
  "Fresh scaling", "New (1 month); efficacy disputes; animal-welfare backlash"),
 ("Split-end trimmer", "luxmend.com", 150, 6, 3, 2100, 6, 3, 36, "A,M",
  "$59 vs $4-7 cost", "Battery/FCC; low search"),
 ("Pillow speaker", "radoxtech.com", 160, 2, 23, 160, 3, 3, 15, "",
  "Search exists", "Thin margin; FCC/battery"),
 ("Kids Bluetooth headband", "mybandou.com", 190, 6, 2, 190, 1, 2, 35, "CAC",
  "One advertiser, long-running ad", "CPSIA + FCC + battery"),
 ("Pheromone perfume oil", "goda.co / venomscent.com", 100, 13, 14, 4900, 6, 4, 30, "A,CAC",
  "Category ads live 13 months", "Crowded; attraction claims"),
 ("Beef tallow balm", "ancestralcosmetics.com", 100, 11, 175, 5600, 13, 4, 25, "A,CAC",
  "Huge search", "Saturated (13 domains in top 30)"),
 ("Scalp massager", "various", 50, 9, 20, 790, 12, 3, 25, "A,CAC",
  "Search exists", "No leader; scattered"),
 ("Color-changing foundation stick", "various", 50, 16, 16, 7700, 5, 4, 25, "A,CAC",
  "Category long-running", "Saturated; shade complaints"),
 ("Tanning balm (summer)", "brunaebody.com", 88, 3, 49, 70, 10, 4, 25, "CAC",
  "Search strong in season", "Seasonal: launch Apr-Jun only"),
 ("Calming cat/dog collar", "pawlax / veterinarian's choice", 60, 7, 6, 1000, 6, 4, 20, "A,CAC",
  "Category active", "Low ticket; weak efficacy evidence"),
]

def w(A, M):  # leader is live and long-running
    return min(5, 1 + (A >= 100) + (A >= 300) + (M >= 6) + (M >= 12))
def s(S):
    return 5 if S >= 100 else 4 if S >= 30 else 3 if S >= 10 else 2 if S >= 3 else 1
def c(P, D):
    return max(1, 5 - (P >= 1000) - (P >= 3000) - (P >= 8000) - (D >= 8))
def e(CAC):
    return 5 if CAC >= 50 else 4 if CAC >= 35 else 3 if CAC >= 20 else 2 if CAC >= 10 else 1

WT = dict(W=25, S=20, C=15, F=25, E=15)
rows = []
for name, lead, A, M, S, P, D, F, CAC, est, why, risk in R:
    sc = dict(W=w(A, M), S=s(S), C=c(P, D), F=F, E=e(CAC))
    tot = round(sum(WT[k] * v for k, v in sc.items()) / 5, 1)
    rows.append((tot, name, lead, A, M, S, P, D, CAC, est, why, risk, sc))
rows.sort(key=lambda r: -r[0])

out = ["# 20 'working' products: evidence-based shortlist (US)", "",
       "Date: 2026-11-07. A product counts as 'working' when its leader is advertising in the US now, its ads have lasted, and we can legally and practically sell it.",
       "",
       "## Scoring rules",
       "",
       "Each criterion is scored 1-5 by fixed thresholds, so anyone can recompute it. Feasibility (F) is the only judgment score. Weights: W 25%, S 20%, C 15%, F 25%, E 15%.",
       "",
       "- **W (working):** start at 1. Add 1 each if the leader has ≥100 active US ads, ≥300 active US ads, its oldest top ad has run ≥6 months, ≥12 months. Cap at 5.",
       "- **S (search demand):** Google searches as % of 'ski boots'. ≥100 → 5, ≥30 → 4, ≥10 → 3, ≥3 → 2, else 1.",
       "- **C (clone pressure):** start at 5. Subtract 1 each if category-phrase ads ≥1,000, ≥3,000, ≥8,000, or if there are ≥8 distinct seller domains in the top 30. Floor 1.",
       "- **F (feasibility):** 5 = no special rules. 4 = cosmetic or claims care. 3 = electronics/battery, apparel sizes, or efficacy-claims risk. 2 = registration or cleared-device needs (FDA fee, EPA, CPSIA, 510(k) OEM).",
       "- **E (economics):** max CAC per order (model). ≥$50 → 5, ≥$35 → 4, ≥$20 → 3, ≥$10 → 2.",
       "",
       "Marked with ◇ in 'est' = that input is an estimate, not observed. Ad counts are Ad Library hits; the top 30 are grouped by landing domain, so persona pages of one company count once.",
       "",
       "## Top 20",
       "",
       "| # | Product | Score | W | S | C | F | E | Leader | Leader US ads / months | Search % | Phrase ads / domains | Max CAC | ◇ est | Why it works | Main risk |",
       "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for i, r in enumerate(rows[:20], 1):
    tot, name, lead, A, M, S, P, D, CAC, est, why, risk, sc = r
    out.append(f"| {i} | {name} | **{tot}** | {sc['W']} | {sc['S']} | {sc['C']} | {sc['F']} | {sc['E']} | {lead} | {A:,} / {M} | {S}% | {P:,} / {D} | ${CAC} | {est} | {why} | {risk} |")
out += ["", "## Below the cut", ""]
out += [f"- {r[1]} — {r[0]} (W{r[12]['W']} S{r[12]['S']} C{r[12]['C']} F{r[12]['F']} E{r[12]['E']}): {r[11]}" for r in rows[20:]]
out += ["", "Excluded before scoring (cannot sell as advertised or not physical):",
        "- ingestibles;",
        "- hair/lash growth drugs;",
        "- neuropathy creams;",
        "- berberine patches;",
        "- smoking-cessation inhalers;",
        "- red-light hearing devices, EMS neck devices, the baby nebulizer, microneedling (FDA);",
        "- the infant sleep positioner (CPSC ban);",
        "- grounding sheets, tuning forks, frequency devices and 'virility' bracelets (pseudoscience claims);",
        "- digital products and methodology-only videos;",
        "- CarPlay adapters, projectors and steam cleaners (marketplace-saturated electronics);",
        "- the dog car fan (summer only)."]
open("shortlist20.md", "w", encoding="utf-8").write("\n".join(out))
for i, r in enumerate(rows, 1):
    print(f"{i:2}. {r[0]:5} {r[1]}  W{r[12]['W']} S{r[12]['S']} C{r[12]['C']} F{r[12]['F']} E{r[12]['E']}")
