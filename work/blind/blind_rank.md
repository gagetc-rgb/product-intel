# Blind popularity ranking (2026-11-07)

Rules in `score.py` docstring. AMZ = Amazon units/month (top-20 organic, 'bought in past month'); TT = TikTok Shop top on-target product, thousand sold lifetime; META180 = Meta US ads live 180+ days for the category phrase. Scores 0-5 per channel; POP = mean; CONF = channels scoring 3+. n/a = no data (not zero).

## Main block (non-ingestible)

| # | Product | Flag | AMZ units/mo | AMZ 1K+ listings | TT k sold | META all / 180+ | advertisers 180+ | sA sT sM | POP | CONF | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Collagen multi-balm stick |  | 195,250 | 7 | 1,200 | 2,400 / 25 | 7 | 5 5 3 | 5.0 | 3 | medicube 1.2M, Dr.Melaxin calcium 1.1M (brand-led K-beauty) |
| 2 | Handheld steam cleaner |  | 30,800 | 8 | 371.3 | 730 / 72 | 9 | 4 5 4 | 4.5 | 3 |  |
| 3 | Eyelash growth serum (cosmetic) | COMPLIANCE | 86,700 | 11 | 343.7 | 3,200 / 90 | 11 | 4 5 4 | 4.5 | 3 |  |
| 4 | Color-changing foundation stick |  | 267,400 | 8 | 68.4 | 7,700 / 120 | 7 | 5 4 4 | 4.5 | 3 |  |
| 5 | Beef tallow balm |  | 49,900 | 8 | 662.5 | 2,500 / 52 | 10 | 4 5 4 | 4.5 | 3 |  |
| 6 | Compression socks |  | 109,900 | 16 | 70.9 | 14,000 / 610 | 14 | 5 4 5 | 4.5 | 3 |  |
| 7 | Hair-growth scalp serum | COMPLIANCE | 133,000 | 9 | 111.8 | 2,900 / 62 | 13 | 5 4 4 | 4.5 | 3 | overlaps rosemary roll-ons |
| 8 | Neck firming cream |  | 70,050 | 7 | 653 | 4,300 / 83 | 13 | 4 5 4 | 4.5 | 3 | GoPure 653K |
| 9 | Rosemary hair oil (roller) |  | 46,200 | 13 | 598 | 4,100 / 60 | 14 | 4 5 4 | 4.5 | 3 | Be Bodywise roll-on 598K (the Bodywise clone from an excluded video); Bask&Lather 327K |
| 10 | Retinol firming cream |  | 227,600 | 12 | 23.9 | 660 / 66 | 3 | 5 3 4 | 4.0 | 3 | k/retinol: Anua 24K, medicube 23K (brand-led) |
| 11 | Men's body hair removal cream |  | 64,350 | 8 | 135 | 2,800 / 54 | 7 | 4 4 4 | 4.0 | 3 |  |
| 12 | Exfoliating shower towel |  | 37,100 | 12 | 79.5 | 460 / 64 | 5 | 4 4 4 | 4.0 | 3 | AD re-check: k/japanese-exfoliating-towel -> GOSHI 79.5K; first slug showed 0.17K |
| 13 | Topical magnesium oil spray |  | 24,700 | 7 | 105.4 | 540 / 53 | 4 | 3 4 4 | 3.5 | 3 |  |
| 14 | Filtered shower head (+ cartridges) |  | 46,450 | 14 | 14.9 | 1,300 / 42 | 10 | 4 3 3 | 3.5 | 3 |  |
| 15 | Stainless-steel pet water fountain |  | 61,800 | 12 | 35.1 | 2,800 / 22 | 6 | 4 3 3 | 3.5 | 3 |  |
| 16 | Waterless luxury scent diffuser (+ oils) |  | 28,900 | 8 | 87.2 | 670 / 17 | 9 | 3 4 3 | 3.5 | 3 |  |
| 17 | LED face / neck mask | COMPLIANCE | 16,300 | 9 | 28.4 | 1,900 / 70 | 9 | 3 3 4 | 3.0 | 3 |  |
| 18 | Collagen overnight wrapping mask |  | 141,300 | 9 | 262.3 | 2,500 / 210 | 13 | 5 5 n/a | 5.0 | 2 |  |
| 19 | Hydrocolloid nose pore / sebaceous filament patches |  | 42,300 | 7 | 209.3 | 1 / 0 | 0 | 4 5 0 | 4.5 | 2 | strips 209K; Peach Slices nose patches 43K |
| 20 | Turmeric soap (glow / dark spots) |  | 57,800 | 11 | 819 | 300 / 12 | 3 | 4 5 2 | 4.5 | 2 | AD re-check: k/turmeric-soap and k/kojic-acid-soap -> Honey Glow lemon-turmeric-kojic bar 819K, 3PCS 243K; first slug (turmeric-soap-bar) showed only 888 |
| 21 | Face lymphatic drainage brush/roller |  | 92,700 | 15 | 194.6 | 79 / 3 | 1 | 4 4 1 | 4.0 | 2 |  |
| 22 | Mini portable projector |  | 19,200 | 8 | 300.7 | 170 / 9 | 2 | 3 5 2 | 4.0 | 2 |  |
| 23 | Teeth whitening powder |  | 17,100 | 5 | 292.5 | 170 / 0 | 0 | 3 5 0 | 4.0 | 2 |  |
| 24 | Travel vacuum compression bags with pump |  | 70,900 | 13 | n/a | 1,700 / 23 | 10 | 4 n/a 3 | 4.0 | 2 |  |
| 25 | Work insoles for construction workers |  | 93,000 | 8 | 33 | 34 / 0 | 0 | 4 3 0 | 3.5 | 2 | AD re-check: k/insoles -> WALKHERO heavy-duty orthotic 33K (Upstright comfort 63K, general) |
| 26 | Body oil for crepey skin |  | 79,900 | 8 | 16.5 | 10,000 / 85 | 14 | 4 3 n/a | 3.5 | 2 | k/body-oil: GODA Silk Body Oil 16.5K = corpus 'God Silk' |
| 27 | Collagen chin / V-line wrap |  | 21,250 | 6 | 84.4 | 7,700 / 150 | 23 | 3 4 n/a | 3.5 | 2 |  |
| 28 | Persimmon soap (aging odor) |  | 59,700 | 11 | 12.1 | 2,800 / 11 | 2 | 4 3 2 | 3.5 | 2 |  |
| 29 | Natural rodent repellent pouches | COMPLIANCE | 21,100 | 2 | 139.7 | 9,300 / 1 | 1 | 3 4 1 | 3.5 | 2 | Reliant 140K; Sofyre 9.6K |
| 30 | Wireless CarPlay / Android Auto adapter |  | 41,600 | 9 | 16 | 15,000 / 560 | 11 | 4 3 n/a | 3.5 | 2 |  |
| 31 | Pre-wash hair oil (squeeze bottle) |  | 83,200 | 10 | 46.9 | 530 / 10 | 9 | 4 3 2 | 3.5 | 2 |  |
| 32 | Sleep mouth tape |  | 8,700 | 2 | 249.6 | 2,700 / 110 | 9 | 2 5 4 | 3.5 | 2 |  |
| 33 | Women's facial hair remover / epilator |  | 74,000 | 13 | 4.6 | 500 / 17 | 5 | 4 2 3 | 3.0 | 2 |  |
| 34 | Enzyme pet odor eliminator spray/fogger |  | 15,750 | 4 | n/a | 3,900 / 80 | 8 | 3 n/a 4 | 3.0 | 2 |  |
| 35 | Screen-free retro digital camera |  | 28,100 | 6 | 22.6 | 280 / 4 | 1 | 3 3 1 | 3.0 | 2 |  |
| 36 | Pet hair remover roller |  | 73,300 | 5 | 5 | 760 / 95 | 8 | 4 2 4 | 3.0 | 2 |  |
| 37 | Electrostatic pet hair glove |  | 19,500 | 5 | 24.4 | 120 / 9 | 2 | 3 3 2 | 3.0 | 2 |  |
| 38 | T-handle ratchet screwdriver set |  | 11,650 | 6 | n/a | 130 / 35 | 2 | 3 n/a 3 | 3.0 | 2 |  |
| 39 | Sunset projection lamp |  | 20,300 | 7 | 39.1 | 10 / 1 | 1 | 3 3 1 | 3.0 | 2 |  |
| 40 | Kids handheld digital microscope | COMPLIANCE | 26,950 | 8 | 36.1 | 48 / 0 | 0 | 3 3 0 | 3.0 | 2 |  |
| 41 | Microcurrent / ultrasonic face sculpting device |  | 7,500 | 1 | 45.7 | 5,200 / 250 | 9 | 2 3 5 | 2.5 | 2 |  |
| 42 | Sonic toothbrush with UV case |  | 8,850 | 5 | 12 | 3,600 / 49 | 13 | 2 3 3 | 2.5 | 2 |  |
| 43 | Men's compression / slimming tank |  | 9,500 | 4 | 31.9 | 1,600 / 30 | 12 | 2 3 3 | 2.5 | 2 |  |
| 44 | Sound-healing tuning fork set |  | 3,050 | 0 | 40 | 820 / 270 | 4 | 2 3 5 | 2.5 | 2 |  |
| 45 | Yoga mat with carry strap |  | 20,150 | 7 | 1.4 | 1,900 / 160 | 17 | 3 1 5 | 2.0 | 2 |  |
| 46 | Silvervine / matatabi cat dental chew |  | 2,250 | 0 | 20.8 | 690 / 52 | 3 | 1 3 4 | 2.0 | 2 |  |
| 47 | Moissanite / non-tarnish tennis bracelet |  | 100 | 0 | 64.6 | 2,900 / 52 | 11 | 0 4 4 | 2.0 | 2 |  |
| 48 | Ceramide hydrating face cleanser |  | 172,500 | 11 | n/a | 37 / 0 | 0 | 5 n/a 0 | 5.0 | 1 |  |
| 49 | Giant clear storage bag |  | 38,100 | 7 | n/a | 55 / 0 | 0 | 4 n/a 0 | 4.0 | 1 |  |
| 50 | Pheromone perfume / cologne oil |  | 30,150 | 8 | n/a | 1,400 / 0 | 0 | 4 n/a 0 | 4.0 | 1 |  |
| 51 | Body mousse-to-oil |  | 125,750 | 10 | 7.3 | 28 / 4 | 1 | 5 2 1 | 3.5 | 1 |  |
| 52 | Aesthetic pendant necklace |  | 17,050 | 10 | n/a | 2,800 / 180 | 14 | 3 n/a n/a | 3.0 | 1 |  |
| 53 | Skin tightening wand (RF/EMS) |  | 18,100 | 5 | n/a | 5,200 / 230 | 20 | 3 n/a n/a | 3.0 | 1 |  |
| 54 | Non-iron men's shirt |  | 10,100 | 3 | n/a | 180 / 1 | 1 | 3 n/a 1 | 3.0 | 1 |  |
| 55 | Ultrasonic bark deterrent |  | 26,300 | 5 | n/a | 85 / 0 | 0 | 3 n/a 0 | 3.0 | 1 |  |
| 56 | Washable / pheromone puppy pads |  | 23,800 | 9 | n/a | 12,000 / 28 | 1 | 3 n/a n/a | 3.0 | 1 |  |
| 57 | Natural flea & tick spray | COMPLIANCE | 12,900 | 3 | n/a | 220 / 0 | 0 | 3 n/a 0 | 3.0 | 1 |  |
| 58 | Dog crate / car fan |  | 17,800 | 4 | n/a | 16 / 1 | 1 | 3 n/a 1 | 3.0 | 1 |  |
| 59 | 2-in-1 garment duffel / weekender |  | 2,200 | 0 | 87.3 | 250 / 1 | 1 | 1 4 1 | 2.5 | 1 |  |
| 60 | Dog/cat calming pheromone diffuser |  | 22,250 | 4 | 9.5 | 620 / 0 | 0 | 3 2 0 | 2.5 | 1 | TherapetMD 9.5K = corpus brand |
| 61 | Women's high-waist stretch capri |  | 7,800 | 2 | 46.3 | 370 / 5 | 4 | 2 3 2 | 2.5 | 1 |  |
| 62 | Hair-growth inhibitor serum |  | 350 | 0 | 597.2 | 51 / 0 | 0 | 0 5 0 | 2.5 | 1 | Caramela Cyperus oil 597K = the exact corpus product |
| 63 | Grounding bed sheet |  | 4,150 | 1 | 5.3 | 1,100 / 27 | 6 | 2 2 3 | 2.0 | 1 |  |
| 64 | Red-light scalp massager with oil applicator |  | 5,350 | 3 | 7.8 | 760 / 16 | 8 | 2 2 3 | 2.0 | 1 |  |
| 65 | EMS neck massager | COMPLIANCE | 8,000 | 4 | n/a | 1,300 / 40 | 14 | 2 n/a 3 | 2.0 | 1 |  |
| 66 | Red light therapy pad / wrap |  | 10,450 | 2 | 1 | 180 / 2 | 2 | 3 1 1 | 2.0 | 1 |  |
| 67 | Micro-infusion microneedling kit | COMPLIANCE | 6,250 | 2 | n/a | 6,500 / 130 | 7 | 2 n/a 4 | 2.0 | 1 |  |
| 68 | Split-end trimmer |  | 8,250 | 1 | 9.5 | 190 / 24 | 3 | 2 2 3 | 2.0 | 1 |  |
| 69 | Men's athletic-fit t-shirt (hides belly) |  | 4,900 | 1 | n/a | 3,500 / 130 | 10 | 2 n/a 4 | 2.0 | 1 |  |
| 70 | Instant line-blur primer / wrinkle filler |  | 42,050 | 8 | 0.22 | 180 / 0 | 0 | 4 0 0 | 2.0 | 1 |  |
| 71 | Portable kids nebulizer | COMPLIANCE | 9,400 | 1 | n/a | 3,900 / 62 | 9 | 2 n/a 4 | 2.0 | 1 |  |
| 72 | Cat calming pheromone collar |  | 12,600 | 7 | 0.19 | 1,100 / 7 | 1 | 3 0 2 | 1.5 | 1 |  |
| 73 | Lavender / weighted sleep eye mask |  | 13,550 | 2 | 0.24 | 15,000 / 250 | 18 | 3 0 n/a | 1.5 | 1 |  |
| 74 | Hematite bracelet |  | 1,800 | 0 | 0.01 | 4,000 / 88 | 3 | 1 0 4 | 0.5 | 1 |  |
| 75 | Ultrasonic skin scrubber spatula |  | 7,250 | 3 | n/a | 37 / 0 | 0 | 2 n/a 0 | 2.0 | 0 |  |
| 76 | Nicotine-free herbal / wooden inhaler |  | 8,400 | 2 | n/a | 81 / 0 | 0 | 2 n/a 0 | 2.0 | 0 |  |
| 77 | Anti-aging skincare set for women 50+ |  | 3,200 | 1 | n/a | 76 / 0 | 0 | 2 n/a 0 | 2.0 | 0 |  |
| 78 | No-rinse dog paw cleaner foam |  | 6,450 | 2 | 3.2 | 60 / 0 | 0 | 2 2 0 | 2.0 | 0 |  |
| 79 | Neuropathy / nerve pain cream (OTC) | COMPLIANCE | 3,900 | 2 | 8 | 61 / 1 | 1 | 2 2 1 | 2.0 | 0 |  |
| 80 | Inflatable airplane seat cushion |  | 7,950 | 5 | 9.2 | 11,000 / 6,800 | 11 | 2 2 n/a | 2.0 | 0 |  |
| 81 | 5-in-1 air cushion hair brush |  | 8,250 | 1 | 1.1 | 390 / 0 | 0 | 2 1 0 | 1.5 | 0 |  |
| 82 | Back / spine stretcher board |  | 2,800 | 1 | 2.3 | 56 / 4 | 3 | 1 2 1 | 1.5 | 0 |  |
| 83 | Bone-conduction pillow speaker |  | 700 | 0 | 0.57 | 180 / 1 | 1 | 1 1 1 | 1.0 | 0 |  |
| 84 | Inflatable 2-step camping tent |  | 500 | 0 | 0.7 | 100 / 0 | 0 | 1 1 0 | 1.0 | 0 |  |
| 85 | Natural acne & redness kit |  | 2,200 | 0 | n/a | 26 / 0 | 0 | 1 n/a 0 | 1.0 | 0 |  |
| 86 | Schumann / frequency 'healing' device | FALSE_CLAIM | 1,750 | 0 | n/a | 250 / 4 | 3 | 1 n/a 1 | 1.0 | 0 |  |
| 87 | Magnetic-valve tea maker |  | 1,700 | 0 | n/a | 32 / 3 | 2 | 1 n/a 1 | 1.0 | 0 |  |
| 88 | Men's leak-proof / incontinence boxers | COMPLIANCE | 2,450 | 0 | 0.45 | 13,000 / 860 | 20 | 1 1 n/a | 1.0 | 0 | AD re-check: k/mens-incontinence-underwear -> CARER 445 sold; men's category weak on TikTok |
| 89 | 16-head handheld vibration massager |  | 1,950 | 0 | 0.2 | 77 / 0 | 0 | 1 0 0 | 0.5 | 0 | 16-head 216; 20-head gun 2.6K |
| 90 | Dissolving microneedle eye patches |  | 1,250 | 0 | 0.07 | 1,200 / 0 | 0 | 1 0 0 | 0.5 | 0 |  |
| 91 | Gel ski shin sleeve |  | 100 | 0 | n/a | 0 / 0 | 0 | 0 n/a 0 | 0.0 | 0 |  |
| 92 | Kids Bluetooth sleep headband | COMPLIANCE | 100 | 0 | n/a | 70 / 3 | 2 | 0 n/a 1 | 0.0 | 0 |  |
| 93 | Self-heating period / pain patches |  | 0 | 0 | n/a | 230 / 0 | 0 | 0 n/a 0 | 0.0 | 0 |  |
| 94 | Pet calming aromatherapy stickers |  | 200 | 0 | n/a | 5 / 2 | 2 | 0 n/a 1 | 0.0 | 0 |  |

## Supplements block

| # | Product | Flag | AMZ units/mo | AMZ 1K+ listings | TT k sold | META all / 180+ | advertisers 180+ | sA sT sM | POP | CONF | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Menopause / hormone-balance supplement |  | 48,050 | 6 | 99.3 | 5,800 / 85 | 19 | 4 4 4 | 4.0 | 3 |  |
| 2 | Shilajit gummies |  | 15,900 | 6 | 411.2 | 1,500 / 210 | 4 | 3 5 5 | 4.0 | 3 |  |
| 3 | Moringa capsules |  | 32,800 | 10 | 184 | 4,200 / 83 | 9 | 4 4 4 | 4.0 | 3 | Rosabella 171K = corpus brand |
| 4 | Pumpkin seed oil softgels |  | 81,800 | 15 | 183.9 | 10,000 / 32 | 6 | 4 4 3 | 4.0 | 3 |  |
| 5 | Beef liver capsules |  | 55,200 | 11 | 48 | 2,200 / 32 | 11 | 4 3 3 | 3.5 | 3 |  |
| 6 | Cayenne / capsaicin softgels |  | 17,300 | 7 | 26.9 | 4,500 / 45 | 10 | 3 3 3 | 3.0 | 3 |  |
| 7 | Colostrum powder |  | 14,900 | 5 | 15.6 | 5,100 / 93 | 22 | 3 3 4 | 3.0 | 3 |  |
| 8 | Creatine for women |  | 175,500 | 18 | 162 | 380 / 1 | 1 | 5 4 1 | 4.5 | 2 |  |
| 9 | Parasite cleanse drops (black walnut/wormwood) |  | 90,600 | 9 | n/a | 8,000 / 53 | 9 | 4 n/a 4 | 4.0 | 2 |  |
| 10 | Caffeine / nootropic gum |  | 31,250 | 4 | 110.8 | 96 / 0 | 0 | 4 4 0 | 4.0 | 2 | Neuro = corpus brand |
| 11 | Magnesium glycinate gummies |  | 226,000 | 18 | 9 | 12,000 / 140 | 18 | 5 2 4 | 3.5 | 2 |  |
| 12 | Dog dental powder (food topper) |  | 13,250 | 6 | 10.2 | 1,300 / 4 | 1 | 3 3 1 | 3.0 | 2 |  |
| 13 | Mushroom (focus) gummies |  | 20,100 | 6 | 25 | 670 / 7 | 4 | 3 3 2 | 3.0 | 2 |  |
| 14 | Dog multivitamin chews |  | 5,000 | 2 | 21.7 | 200 / 23 | 6 | 2 3 3 | 2.5 | 2 |  |
| 15 | Oral sleep / energy strips |  | 250 | 0 | 12.1 | 140 / 32 | 2 | 0 3 3 | 1.5 | 2 |  |
| 16 | Men's metabolism / belly-fat supplement |  | 36,800 | 9 | n/a | 24,000 / 5,700 | 19 | 4 n/a n/a | 4.0 | 1 |  |
| 17 | DHT blocker (hair loss) |  | 35,200 | 7 | n/a | 1,900 / 9 | 6 | 4 n/a 2 | 4.0 | 1 |  |
| 18 | Methylfolate drops |  | 51,800 | 7 | n/a | 2,200 / 12 | 4 | 4 n/a 2 | 4.0 | 1 |  |
| 19 | Berberine appetite patch |  | 31,550 | 4 | n/a | 460 / 0 | 0 | 4 n/a 0 | 4.0 | 1 |  |
| 20 | Oregano + black seed oil softgels |  | 126,600 | 8 | 3.9 | 13,000 / 8 | 6 | 5 2 n/a | 3.5 | 1 |  |
| 21 | Shilajit honey sticks |  | 4,200 | 1 | 73.2 | 51 / 6 | 1 | 2 4 2 | 3.0 | 1 |  |
| 22 | NAC (N-acetyl cysteine) |  | 74,400 | 10 | 0.92 | 860 / 3 | 1 | 4 1 1 | 2.5 | 1 |  |
| 23 | Caffeine energy gummies |  | 39,350 | 8 | 1.6 | 1,000 / 4 | 2 | 4 1 1 | 2.5 | 1 |  |
| 24 | Vitamin patches |  | 11,350 | 4 | 3 | 18 / 0 | 0 | 3 2 0 | 2.5 | 1 |  |
| 25 | Collagen jelly sticks |  | 18,300 | 3 | 2.2 | 1,000 / 2 | 1 | 3 2 1 | 2.5 | 1 |  |
| 26 | Ceylon cinnamon capsules (blood sugar) |  | 46,700 | 15 | 0.1 | 26,000 / 73 | 6 | 4 0 n/a | 2.0 | 1 |  |
| 27 | Acne / clear-skin gummies |  | 36,200 | 8 | 0.15 | 260 / 7 | 3 | 4 0 2 | 2.0 | 1 |  |
| 28 | Dog probiotics |  | 8,900 | 2 | n/a | 93 / 1 | 1 | 2 n/a 1 | 2.0 | 0 |  |
| 29 | Sleep patches |  | 6,550 | 2 | 7.4 | 160 / 5 | 2 | 2 2 2 | 2.0 | 0 |  |
| 30 | Fertility tea |  | 1,650 | 1 | 0.28 | 130 / 5 | 2 | 1 0 2 | 0.5 | 0 |  |
