"""TikTok Shop US keyword pages (shop.tiktok.com/us/k/<slug>), read 2026-11-07 via keenable cache.
Value = highest lifetime 'sold' count of an ON-TARGET product on the page (thousands). None = page missing/blocked (unknown, not zero).
Lifetime counts, not monthly; brand-led categories (medicube etc.) inflate the max."""
TT = {
 "ski_sleeve":None,"cat_collar":0.19,"lymph_brush":194.6,"skin_scrubber":None,"ceramide_wash":None,"projector":300.7,
 "clear_bag":None,"air_brush":1.1,"work_insoles":33.0,"kids_headband":None,"pheromone_perfume":None,"herbal_inhaler":None,
 "pillow_speaker":0.57,"antiaging_set":None,"steam_cleaner":371.3,"yoga_mat":1.4,"pore_patch":209.3,"inflatable_tent":0.7,
 "grounding_sheet":5.3,"silvervine":20.8,"acne_kit":None,"massager16":0.2,"paw_cleaner":3.2,"back_stretcher":2.3,
 "face_epilator":4.6,"tennis_bracelet":64.6,"pendant":None,"scalp_massager":7.8,"tightening_wand":None,"microcurrent":45.7,
 "heat_patch":None,"eye_mask":0.24,"toothbrush":12.0,"compression_tank":31.9,"pet_odor":None,"lash_serum":343.7,"ems_neck":None,
 "body_oil":16.5,"retro_camera":22.6,"pet_hair_roller":5.0,"pet_hair_glove":24.4,"duffel":87.3,"retinol_cream":23.9,
 "microneedle_patch":0.07,"collagen_mask":262.3,"noniron_shirt":None,"dog_diffuser":9.5,"whitening_powder":292.5,
 "neuropathy_cream":8.0,"redlight_pad":1.0,"multibalm":1200,"led_mask":28.4,"hematite":0.01,"microinfusion":None,
 "tuning_fork":40.0,"color_foundation":68.4,"chin_wrap":84.4,"magnesium_spray":105.4,"split_ender":9.5,
 "hair_removal_cream":135.0,"persimmon_soap":12.1,"turmeric_soap":819.0,"frequency_device":None,"rodent_pouch":139.7,
 "exfoliating_towel":79.5,"teapot":None,"shower_filter":14.9,"leakproof_boxers":0.45,"capri_pants":46.3,"bark_deterrent":None,
 "belly_tshirt":None,"carplay":16.0,"dog_fountain":35.1,"hair_inhibitor":597.2,"puppy_pad":None,"tallow_balm":662.5,
 "screwdriver":None,"compression_socks":70.9,"sunset_lamp":39.1,"hair_serum":111.8,"pet_calming_patch":None,
 "scent_diffuser":87.2,"vacuum_bags":None,"wrinkle_primer":0.22,"prewash_oil":46.9,"body_mousse":7.3,"kids_microscope":36.1,
 "neck_cream":653.0,"rosemary_oil":598.0,"mouth_tape":249.6,"flea_spray":None,"seat_cushion":9.2,"dog_car_fan":None,"nebulizer":None,
 "s_magnesium":9.0,"s_cinnamon":0.1,"s_parasite":None,"s_nac":0.92,"s_dog_probiotic":None,"s_menopause":99.3,
 "s_men_metabolism":None,"s_fertility_tea":0.28,"s_cayenne":26.9,"s_dog_dental":10.2,"s_shilajit_honey":73.2,
 "s_shilajit_gummies":411.2,"s_energy_gummies":1.6,"s_acne_gummies":0.15,"s_moringa":184.0,"s_vitamin_patch":3.0,
 "s_sleep_patch":7.4,"s_creatine_women":162.0,"s_colostrum":15.6,"s_pumpkin_oil":183.9,"s_beef_liver":48.0,
 "s_energy_gum":110.8,"s_dog_multivit":21.7,"s_oregano":3.9,"s_dht":None,"s_methylfolate":None,"s_mushroom":25.0,
 "s_strips":12.1,"s_berberine_patch":None,"s_collagen_jelly":2.2,
}
NOTES = {"rosemary_oil":"Be Bodywise roll-on 598K (the Bodywise clone from an excluded video); Bask&Lather 327K",
 "hair_serum":"overlaps rosemary roll-ons","multibalm":"medicube 1.2M, Dr.Melaxin calcium 1.1M (brand-led K-beauty)",
 "neck_cream":"GoPure 653K","hair_inhibitor":"Caramela Cyperus oil 597K = the exact corpus product",
 "rodent_pouch":"Reliant 140K; Sofyre 9.6K","s_moringa":"Rosabella 171K = corpus brand","s_energy_gum":"Neuro = corpus brand",
 "dog_diffuser":"TherapetMD 9.5K = corpus brand","pore_patch":"strips 209K; Peach Slices nose patches 43K",
 "leakproof_boxers":"page for women's period underwear only; no men's product found","massager16":"16-head 216; 20-head gun 2.6K"}
NOTES.update({
 "turmeric_soap": "AD re-check: k/turmeric-soap and k/kojic-acid-soap -> Honey Glow lemon-turmeric-kojic bar 819K, 3PCS 243K; first slug (turmeric-soap-bar) showed only 888",
 "leakproof_boxers": "AD re-check: k/mens-incontinence-underwear -> CARER 445 sold; men's category weak on TikTok",
 "retinol_cream": "k/retinol: Anua 24K, medicube 23K (brand-led)",
 "body_oil": "k/body-oil: GODA Silk Body Oil 16.5K = corpus 'God Silk'",
})
NOTES.update({
 "exfoliating_towel": "AD re-check: k/japanese-exfoliating-towel -> GOSHI 79.5K; first slug showed 0.17K",
 "work_insoles": "AD re-check: k/insoles -> WALKHERO heavy-duty orthotic 33K (Upstright comfort 63K, general)",
})
