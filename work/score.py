"""Score product hypotheses from the Daily Ecommerce 2026 corpus for a US launch.
Scores are analyst judgment (1-5) informed by video briefs + quick US web checks on 2026-11-06.
Run: python score.py  -> writes top20_products.md and scores.csv
"""
import csv, json, urllib.parse

W = dict(D=20, C=15, R=20, O=10, E=15, A=15, T=5)  # weights, sum 100
CRIT = dict(
    D="US demand signal (US-targeted competitor ads, ad longevity, US market presence)",
    C="Competition / room to differentiate (5 = open niche or clear angle)",
    R="Regulatory ease in US (5 = none; FDA/CPSC/FCC/EPA/claims risk lowers)",
    O="Ops & logistics (light, unbreakable, no battery/liquids, few sizes, low returns)",
    E="Unit economics (price >= $35, markup >= 3x, bundles, repeat purchase)",
    A="AI-creative reproducibility (visual demo, long-running ads to model)",
    T="Timing fit for a launch Dec 2026 - Mar 2027",
)

# key, name, video ids, D,C,R,O,E,A,T, brand query for Ad Library, note on creatives, main risks
P = [
 ("leakproof_men", "Men's leak-proof boxer briefs (light bladder leaks)", ["jC7fF7CjQ64"], 5,3,3,3,5,4,4, "menvault.com",
  "3-min AI story videos (life after prostate surgery) + static absorption tests (pour liquid on fabric). 360+ active ads, 100% US traffic, live since May.",
  "Incontinence garments may fall under FDA Class I device listing (verify); sizing; Amazon full of $15-25 2-packs."),
 ("ski_shin", "Gel shin sleeve for ski-boot shin bang", ["-DLkqhQOE84"], 4,3,5,5,4,4,4, "skiguards.com",
  "Bestseller ad live since last Nov, 1.9M reach; family bundles; pre-order discount from July; kids version aimed at moms 35-44.",
  "Seasonal (Dec-Mar): stock must land by mid-Dec. Source targeted DE/DK; US players: SkiGuards ($39.95), Cased, cheap Amazon pads."),
 ("tennis_bracelet", "Non-tarnish moissanite tennis bracelet", ["VnO1tOOoTR8","EM68Zc6E7Ig"], 4,2,4,5,5,5,5, "mylovemytreasure",
  "Mostly AI static images: macro sparkle, marble surface, text plates ('so comfortable you forget you're wearing it'), free shipping + 30-day returns. 656 active ads.",
  "Very crowded; FTC Jewelry Guides (disclose moissanite, plating); trust/brand matters; refunds on 'fake' perception."),
 ("ratchet_driver", "T-handle ratchet screwdriver + 24-in-1 bit set (gift for men)", ["qMc7qegtp7I"], 3,2,5,4,3,5,5, "Toolson",
  "1-2 hero videos running since May without pause: original Chinese factory demos with English VO; 477-500 active ads; men 35-44 UK.",
  "Amazon/Newegg flooded with $20-35 sets; DTC needs gift packaging + bundle; metal weight."),
 ("massager16", "16-head vibration body massager sold as a gift", ["X73eocoHeP8","CNcOd8J6OhQ"], 3,3,3,3,5,5,5, "Athetheria",
  "UGC-style 'my husband got me this' + emotional VO, no medical claims; 320 ads since Oct; $142 price vs ~$49 landed cost (author claim).",
  "Electronics + Li-ion battery (shipping, FCC); avoid pain-treatment claims; returns on heavy item."),
 ("persimmon_soap", "Persimmon deodorizing soap for age-related body odor (nonenal)", ["fylkQEOxacg"], 5,1,3,5,4,4,4, "swarva.com",
  "2-3 min AI story videos about nonenal from pages like 'Over 60 and Thriving'; targets 60-80 in US/UK/CA/AU; live since July; subscription.",
  "Mirai Clinical owns Amazon search; cosmetic under MoCRA (listing, labeling); low ticket needs bundles/subscription."),
 ("compression_tank", "Men's compression shaping tank (hides belly/chest)", ["HEeCa2ozwBs"], 5,3,4,3,4,5,4, "north-alpine.com",
  "100% AI humor skits for older men (coworker jokes, restroom talk); 1,900 active ads, 11k total; traffic 40k -> 1.9M in 4 months.",
  "Sizing returns; avoid gynecomastia/posture medical claims; author revenue $9.5-17M/mo is an estimate."),
 ("work_insoles", "Shock-absorbing work insoles for people on concrete all day", ["4YkG30JRedU"], 3,2,4,4,4,5,4, "Soul Brace",
  "Viral hook: egg dropped on insole doesn't break; 6-min AI videos + worker testimonials; 780 active ads (Australia).",
  "Dr. Scholl's/PowerStep + Amazon flood; avoid plantar fasciitis treatment claims; sizes (trim-to-fit helps)."),
 ("garment_duffel", "2-in-1 convertible garment duffel (suit bag + weekender)", ["1gxW7JT6VuA","OL99jJXMCQI"], 4,2,5,3,4,4,4, "luhxe.com",
  "Demo of transformation + 'save $150 on baggage fees'; retargeting with 56% off; lifetime warranty; 700 active ads.",
  "Bulky (dimensional weight), quality complaints if cheap; competitor estimate $10-18M/mo is unverified."),
 ("pillow_speaker", "Under-pillow bone-conduction speaker", ["6WVEj-IZ3Jk"], 5,3,3,3,4,4,4, "Dreamwave pillow speaker",
  "30-sec videos with popular song snippet + 2-hour auto-off timer; couple conflict angle; 200+ ads targeting US/CA/AU/NZ.",
  "FCC + Li-ion; sound leakage disappoints; Amazon $20-40 alternatives; music in ads = licensing risk."),
 ("paw_cleaner", "No-rinse foaming paw cleaner with silicone brush head", ["P1WZAFvFuKg","Dcchgv8VuzQ","VSqKTsFXfBI"], 3,3,4,4,3,5,5, "Paw cleaner",
  "Organic TikTok clips (muddy paws, licking) + 4 rotating AI presenters; 3-step demo; 2-3 bottle bundles.",
  "Dandylion Clean Paws is the known US brand; liquid (MSDS for shipping); low ticket; no 'antibacterial' claims without EPA."),
 ("enzyme_fogger", "Enzyme odor spray with UV-light finder for pet urine", ["HMP23Mr4yq8"], 4,3,3,3,4,5,4, "Pet Meiser",
  "16-sec AI videos: blue UV light reveals stains, then spray; up to 100 new ads/day; 1,300 active ads; ads from personal-looking profiles.",
  "Any 'kills bacteria/germs' claim needs EPA registration; liquid + device; ads from fake persona profiles = policy/FTC risk, don't copy that."),
 ("chin_wrap", "Collagen chin & jawline sculpt wrap", ["dZRoQlQF9WQ"], 4,3,3,5,4,5,4, "tryskult.com",
  "Influencer videos applying the mask, visible chin 'lift'; 2,000 active ads to one landing page.",
  "Cosmetic: 'lifting' must stay appearance-only; results are temporary -> refunds; claimed $8.2M/mo is estimate."),
 ("split_trimmer", "Split-end hair trimmer", ["ehNjnJlXwFg"], 3,3,3,4,4,5,4, "Luxe split end",
  "Single top creative running continuously since Jan 2026: before/after 'magic' on hair; cost $11-14, price $50 (author).",
  "Electronics + battery; Split-Ender incumbent; hair damage complaints if blades poor."),
 ("silk_body_oil", "Body oil for crepey/aging skin (menopause angle)", ["MUyL2RAaBw8","ezFy2gHYXSE"], 4,2,3,4,5,4,4, "God Silk body oil",
  "Close-ups of mature skin before/after, glossy 'liquid gold' application, menopause testimonials; 1,700 active ads.",
  "Crowded beauty; MoCRA; 'reduces wrinkles' wording must stay cosmetic; AI-celebrity likeness in ads is not allowed."),
 ("seat_cushion", "Inflatable airplane seat cushion", ["YQPP28Le9e0"], 4,2,5,5,4,4,3, "shoptravlr.com",
  "Top creative live since Dec 2025; 2-step funnel: advertorial then product page; $8 cost / $80 price (author).",
  "Niche; travel seasonality; quality of valve/material."),
 ("scent_diffuser", "Waterless scent diffuser shaped like a perfume bottle", ["ta3BYsDhaSI"], 3,3,3,3,5,4,5, "Ulfia Studio",
  "30-sec videos: 'smells like a 5-star hotel', lasts 6 months; women 55-64 UK; ~300 ads since mid-Sep; refill oils = repeat.",
  "Electronics + fragrance oil shipping; source targets UK; Amazon has many waterless diffusers."),
 ("puppy_pads", "Reusable washable puppy pads with pheromone attractant", ["pvzVvkZUmbQ"], 3,3,4,4,4,4,4, "Puppy pad pheromone",
  "2,700 active ads, mostly images and short AI dog clips.",
  "Pheromone efficacy claims need care; bulky textile; washable pads already common on Amazon."),
 ("retro_camera", "Screen-free retro digital camera", ["MZKabWfKSE0"], 4,2,3,3,4,4,5, "That One Street camera",
  "890 active ads; hook: sawing a disposable camera in half; 'type a heart emoji for secret discount'; 1,000 shots per charge.",
  "Branded competitors (Camp Snap at Target, Flashback); electronics QA; Christmas lead time tight."),
 ("kids_headband", "Kids' soft headband with Bluetooth headphones (animal designs)", ["ZQBdwG_HIgo","58Uc09pYDqI"], 4,3,2,4,4,4,4, "MyBando",
  "10-sec video 'calm mom on the plane' running since Apr 2025 (1+ yr); 1,500 active ads; cart upsell to ~$80.",
  "Children's product: CPSIA third-party testing + CPC, plus FCC and battery; volume limiting expected."),
 ("bark_deterrent", "Handheld ultrasonic bark deterrent", ["PHfBPuHQsFg"], 3,2,3,4,4,4,3, "Furry Basics",
  "Button press + '3, 2, 1' effect demo; neighbor's-dog angle; live since March, men 55-64 UK; 170 active ads.",
  "Efficacy disputes and returns; animal-welfare backlash; many cheap Amazon units."),
 ("face_epilator", "Facial hair epilator for women 40+", ["l005j2UHfh8","ECUydseZYvI","bdjZvoR32Qo"], 4,2,3,4,4,5,4, "Pluxie",
  "30-sec AI stories (old painful methods vs gentle device), 'gift from husband' unboxing; hybrid landing with 'Us vs Them'.",
  "Flawless (Finishing Touch) dominates; battery; skin irritation reviews."),
 ("lymph_brush", "Lymphatic face contour brush", ["-M6GjzDLw5M","dsr56NFmH3k"], 3,2,4,5,3,5,4, "Geta lymphatic",
  "Unedited TikTok creator clips: brush one side of face, instant contrast; '5 reasons why' advertorial; 320-400 ads.",
  "Gua sha/face tools saturated; effect is temporary; low price ceiling."),
 ("kids_microscope", "Kids' portable digital microscope", ["zLfyumMl6iI"], 3,3,2,3,4,4,4, "Kittio microscope",
  "TikTok Shop videos re-voiced; 'screen-free alternative to iPad' angle; 400 active ads (CH/FR).",
  "CPSIA + battery + optics quality; Christmas lead time; established edu-toy brands."),
 ("shower_towel", "Exfoliating Japanese-style body towel", ["iIYC7y0Xxvs"], 4,2,4,5,2,4,4, "Blissell",
  "Hook 'how Australians/Japanese wash'; seniors can't reach their back; live 30+ days; US/UK/CA/AU.",
  "Salux-type towels cheap on Amazon ($10-15); drop 'antibacterial' claim (EPA treated-article rule)."),
 ("spine_stretcher", "Back stretcher / spine decompression board", ["DdfY-52ZMOw"], 3,2,3,3,4,4,4, "Aromanda spine",
  "Static banners: back pain, sciatica, 'Buy 1 Gift 1 Free'; 1,100 active ads.",
  "Disc/sciatica claims are medical; many Amazon clones; bulky."),
 ("pet_hair", "Pet-hair remover glove / roller", ["qpbGtEd23us","N2MXHL8zWNk"], 4,1,5,5,2,5,4, "Pure Path glove",
  "Advertorial '7 reasons pet owners quit regular brushes' + couch demos; 1,000 active ads.",
  "ChomChom and dozens of clones; low price ceiling."),
 ("cat_collar", "Cat calming pheromone collar", ["-FE7NdFIQHQ"], 3,2,3,5,3,3,3, "Gentle Paws",
  "2-min Fiverr-actor UGC; retargeting 'we over-ordered, 3+2 free'; collar vs diffuser angle.",
  "Feliway/Sentry incumbents; weak efficacy evidence; 'over-ordered' fake scarcity is an FTC risk."),
 ("compression_socks", "Bamboo compression socks", ["qey4n7UHRXc"], 3,2,3,5,4,4,3, "Everstrides",
  "1-min UGC, 30 cuts, emotional before/after, '8 pairs for the price of 3'.",
  "Lymphedema/lipedema wording = medical claims; crowded."),
]

rows = []
for key, name, vids, D, C, R, O, E, A, T, bq, cre, risk in P:
    s = dict(D=D, C=C, R=R, O=O, E=E, A=A, T=T)
    total = round(sum(W[k] * v for k, v in s.items()) / 5, 1)
    rows.append(dict(key=key, name=name, vids=vids, total=total, creative=cre, risk=risk, bq=bq, **s))
rows.sort(key=lambda r: -r["total"])

def adlib(q):
    return ("https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q="
            + urllib.parse.quote(q) + "&search_type=keyword_unordered")

with open("scores.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["rank", "key", "product", "total"] + list(W) + ["videos"])
    for i, r in enumerate(rows, 1):
        w.writerow([i, r["key"], r["name"], r["total"]] + [r[k] for k in W] + [" ".join(r["vids"])])

out = ["# Top-20 product hypotheses for a US launch (from Daily Ecommerce 2026)", "",
       "Date: 2026-11-06. Source: 138 in-scope long videos (briefs by NotebookLM), plus quick US web checks.",
       "Scores are analyst judgment on a 1-5 scale, not measured data. Revenue figures in the videos are the author's estimates and were NOT used as a criterion.", "",
       "## Criteria and weights", ""]
out += [f"- **{k}** ({W[k]}%): {CRIT[k]}" for k in W]
out += ["", "Hard exclusions before scoring: ingestibles; drug or disease claims (hair/lash growth serums, neuropathy creams, berberine patches, smoking-cessation inhalers, dark-spot 'treatment'); medical devices needing FDA clearance for the advertised use (LED masks, red-light hearing devices, EMS neck devices, baby nebulizer, microneedling); infant sleep positioner (Safe Sleep for Babies Act); EPA-regulated rodent repellent; pseudoscience wellness (grounding sheets, frequency generators, 'virility' bracelets); saturated electronics (CarPlay adapters, mini projectors, steam cleaners); digital products and methodology-only videos; summer-only items (dog car fan, tanning balm).", "",
       "## Ranking", "", "| # | Product | Score | D | C | R | O | E | A | T |", "|---|---|---|---|---|---|---|---|---|---|"]
for i, r in enumerate(rows[:20], 1):
    out.append(f"| {i} | {r['name']} | **{r['total']}** | " + " | ".join(str(r[k]) for k in W) + " |")
out += ["", "Scores for ranks 1-8 were re-checked on 2026-11-06 against the full transcripts and live US Meta Ad Library counts (see deep_dive_top8.md). Scores sit within a few points: a one-point change in any judgment can reorder them. Treat ranks 1-8 as one tier.", "",
        "## Shortlist of 3 after the deep dive (see deep_dive_top8.md)", "",
        "1. **Gel ski shin sleeve** — no regulation, light, one clear pain; SkiGuards runs ~230 active US ads with the same short demo videos since 6 Nov 2025; season is now. Watch: [-DLkqhQOE84](https://www.youtube.com/watch?v=-DLkqhQOE84)",
        "2. **Non-tarnish moissanite tennis bracelet** — MLMT runs ~280 active US ads, mostly images, price from $69; one sharp angle ('never take off'); Christmas and Valentine's window. Watch: [VnO1tOOoTR8](https://www.youtube.com/watch?v=VnO1tOOoTR8)",
        "3. **Men's compression shaping tank** — North Alpine matches ~1,700 active US ads, all AI-made (skits, 'dad bod' hooks); best test bed for our AI-creative pipeline. Sizing and returns are the risk. Watch: [HEeCa2ozwBs](https://www.youtube.com/watch?v=HEeCa2ozwBs)",
        "", "Reserve: men's leak-proof boxers (Menvault ~330 active US ads, $149.95 six-pack, strong but needs an FDA/claims check). Dropped: persimmon soap (~2,600 active US ads mention it; at least 5 brands with fake-persona pages).",
        "", "Below the cut (21+): " + "; ".join(f"{r['name']} ({r['total']})" for r in rows[20:]), "",
        "## Product cards (top 20)", ""]
for i, r in enumerate(rows[:20], 1):
    links = ", ".join(f"[{v}](https://www.youtube.com/watch?v={v})" for v in r["vids"])
    out += [f"### {i}. {r['name']} — {r['total']}", "",
            f"- Videos: {links}",
            f"- Competitor creatives (from the video): {r['creative']}",
            f"- Risks: {r['risk']}",
            f"- Meta Ad Library, US, active (brand name from transcript, may be misspelled): [{r['bq']}]({adlib(r['bq'])})", ""]
open("top20_products.md", "w", encoding="utf-8").write("\n".join(out))
print("\n".join(f"{i:2}. {r['total']:5} {r['name']}" for i, r in enumerate(rows, 1)))
