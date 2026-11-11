"""Hand classification of each store (my reading of the saved pages), used by m2_build.py. Y has yes/unclear rows; every other row is 'no' with a reason in NO."""
Y = {}
def y(c, d, s, title="", price="", bundle="", note=""): Y[(c, d)] = (s, title, price, bundle, note)
# persimmon
y("persimmon_soap","miraiclinical.com","yes","Persimmon soap / body care (home page: NEW Eucalyptus Persimmon Soap; nav Body Soap)","","free shipping $70+","home prices $50/$60/$70 not matched to a product")
y("persimmon_soap","try-kaori.com","yes","Japanese Persimmon Soap (home title)","","upsells: Exfoliating Soap Bag 2-pack $12.99 (was $19.99); Persimmon Deodorant $14.99; Body Wash $19.99; fall flash sale up to 30% off","soap bar price not visible on home page")
# turmeric
y("turmeric_soap","glomelanin.com","yes","Turmeric Brightening Soap with Vitamin C (product slug)","","melanin-skin-bundle exists","price not matched; home prices $14.95-$47")
y("turmeric_soap","earthlyderm.com","yes","turmeric soap (known leader; Loox data in work/reviews)","","","home page text empty (cart overlay); sells_product from leader list and work/reviews files, not from this read")
y("turmeric_soap","trystrawberry.com","unclear","","","","keratosis pilaris formulas; soap bar not confirmed")
y("turmeric_soap","honeyglownewyork.com","unclear","","","","honey/superfood skincare; soap bar not confirmed")
y("turmeric_soap","herbneden.com","unclear","Plant-based bar soaps (home title)","","","bar soaps seen; turmeric not confirmed")
y("turmeric_soap","fourerasbeauty.com","unclear","","","","African skincare; soap not confirmed")
y("turmeric_soap","stemandsoul.co","unclear","Superfood Soap Bar For Dark Spots","24.99","Bundle 3-pack $29.99; 4-pack $39.98","from products.json; turmeric not in titles")
y("turmeric_soap","merakihealthy.com","unclear","","","","dark-spot skincare; soap not confirmed")
y("turmeric_soap","trykaoli.com","yes","Turmeric Bars (nav)","","","price not read; home shows Kojic Acid Cleansing Pads $24.99 (was $40)")
y("turmeric_soap","nolimitbeautyshop.com","unclear","","","Buy 2 save 10%, Buy 3 save 22% (store-wide)","product not readable from home text")
# body oil
y("body_oil","try-turmskin.com","unclear","","","","quiz page only (TurmSkin Quiz); product not shown")
y("body_oil","shopseravita.com","unclear","","","","offer. host returned 404; product not read")
y("body_oil","goda.co","yes","Goda Silk Body Oil","39.00 and 49.00 (two listings)","also Body Butter $39, Miracle Body Wash $39, For Her/For Him $34-39","products.json readable; 66 products")
y("body_oil","vitaecharm.com","yes","Body Oil (nav item)","29.95 (first price tier, unmatched)","tiers on page $29.95/$49.95/$69.95 (compare-at $40/$80/$120)","tier reading is mine; tiers may be 1/2/3 bottles")
# foundation
y("color_foundation","magnixa.com","unclear","","","","home text has no product names; free ship over $55")
y("color_foundation","primeprometics.com","yes","Pro-age makeup; Face collection (color-changing foundation per category)","","bundles up to 40% off","prices shown in IDR to this server; USD not read")
y("color_foundation","trylumineskin.com","yes","Hestia Color-Changing Foundation Stick","","","identical home page to hestiacosmetics.com")
y("color_foundation","vimacosmetics.com","yes","VIMA Changing Foundation","19.95","","single price on home page")
y("color_foundation","shopbeautylust.com","yes","color changing foundation + Mushroom CC cream (home desc)","","","price not matched")
y("color_foundation","hestiacosmetics.com","yes","Color-Changing Foundation Stick","","Black Friday buy 1 get 1 free","price not matched; $56.50/$100 on page look like Shopify defaults")
y("color_foundation","smooche.com","yes","Foundation (nav; Stick & Stain)","","VIP Black Friday 60% off","prices shown in IDR to this server")
y("color_foundation","trynova.store","unclear","Korean Age Reversing Foundation Stick","39.99","","color-adapting not stated in title; products.json readable (5 products)")
y("color_foundation","dermamuse.co","yes","Korean roll-on foundation that adapts to skin tone (home desc)","","","price not read")
y("color_foundation","luxe.com","yes","By Luxe Color Changing Foundation","39.95","free shipping; Halloween sale; lash/brow lines also sold (Lashlift Kit, Lash Growth Serum)","not in ad sample; home page lists the foundation at $39.95; first read of title wrongly suggested a salon")
# tallow
y("tallow_balm","ancestralcosmetics.com","yes","Original Tallow & Honey Balm","","Christmas bundles up to 35% off; free ship over $60","price not matched")
y("tallow_balm","terralotus.shop","yes","Whole-food tallow skincare for mature skin (home)","","membership/subscription","not in ad sample; price not matched")
y("tallow_balm","cattle-creek.com","yes","Grass-fed tallow skincare (home)","","","price not matched")
y("tallow_balm","wildgoldtallow.com","yes","Colostrum Tallow Balm","","","price not matched ($45/$31.50 on page)")
y("tallow_balm","summersolacetallow.com","yes","Tallow skincare, balms, soaps, candles (home)","","","since 2014 per its own text")
y("tallow_balm","bare-ritual.com","yes","Beef Tallow Balm for Men","","90-day money-back","price not read")
y("tallow_balm","toupsandco.com","yes","Tallow Balm among organic products (home desc)","","","multi-product organic brand")
y("tallow_balm","thetallowedtruth.com","yes","Animal-based cosmetics (tallow) (home)","","","price not read")
y("tallow_balm","thepapabear.com","yes","Farm to Skin Essentials kit (4-piece tallow skincare)","29 (kit)","kit $29 vs $121 regular; 76% off spring-sale page","lp. landing page text")
y("tallow_balm","neptunehealthco.com","yes","grass-fed tallow and honey skincare (home)","","","home shows $33.98 / $79.96 / $50 unmatched")
y("tallow_balm","shoppuregood.com","yes","Small-batch tallow balms (home title)","","","price not matched")
y("tallow_balm","try-forge.com","yes","Forge Rejuvenating Tallow Balm (men)","","Black Friday up to 50% off","hosts shop./store.try-forge.com")
# lash
y("lash_serum","borboleta.com","yes","Lash Serum / Lash + Brow serum bundle","","Lash Serum + Brow Serum bundle; free ship $65+","price not matched")
y("lash_serum","babeoriginal.com","yes","Eyelash serums (Advanced/Gentle/Peptide lash serum)","","Sets & bundles; holiday sets","price not matched")
y("lash_serum","diablocosmetics.com","unclear","","","","at-home beauty; lash serum not seen in text")
y("lash_serum","facelove-cosmetics.com","unclear","","","","nav Eyes/Face/Lips; lash serum not confirmed")
y("lash_serum","hanaekorea.com","yes","Eyelash Serum (nav, also Foundation Stick, Brow Tint)","","","price not read")
# shower
y("shower_filter","santevia.com","unclear","Mineral water filters (home title)","","","shower filter not confirmed")
y("shower_filter","purewaterfreedom.com","unclear","","","","home page 403 (blocked)")
y("shower_filter","aquatru.com","unclear","AquaTru Shower 2-Pack","298.00 (2-pack)","","filter type of shower not shown; products.json readable")
y("shower_filter","sproos.co","yes","Filtered Hand Shower / Filtered Shower Kit","","Shower kits and bundles","not in ad sample; price not matched")
# scent
y("scent_diffuser","scentifyhome.com","yes","Scentify diffusers + Try Before You Buy starter kit","99 / 199 / 249 on page, unmatched","Starter kit; free shipping & returns","")
y("scent_diffuser","scentfinity.com","yes","Home scent diffusion systems (home desc)","","","price not matched")
y("scent_diffuser","houseofduaa.com","unclear","","","","home fragrance brand; diffuser not confirmed")
y("scent_diffuser","aurahouse.com","yes","Aura Diffuser (4 colors)","79","Luxe Membership 20% off + oil subscription; starter kit","price from page")
y("scent_diffuser","hotelcollection.com","unclear","Luxury hotel scents (home title)","","","diffuser type not confirmed")
y("scent_diffuser","aroma360.com","yes","Mini Pro Scent Diffuser","99.95 MSRP","$49.95 with a one-oil-per-month subscription","price from page terms")
y("scent_diffuser","drift.co","unclear","Home scent diffusers + car air fresheners (home title)","","Scent of the Month subscription","wood/stone diffusers, not clearly the nebulizing form")
y("scent_diffuser","scentiment.com","yes","Scent Diffusers, oils, air fresheners (home title)","","","")
# hair serum
y("hair_serum","jcsmiracleproducts.com","unclear","","","","all-natural hair growth product; form not shown")
y("hair_serum","officialbodywise.com","unclear","","","free ship $80+","product not readable")
y("hair_serum","cphgrooming.com","unclear","","","","redir. host; product not readable")
y("hair_serum","reversehairco.com","unclear","","","","product not readable")
y("hair_serum","averastore.co","unclear","","","","product not readable (60-day guarantee banner)")
y("hair_serum","rennorabeauty.com","unclear","","","","try. host returned 404")
y("hair_serum","hinu.co","yes","Hair growth oil (home desc)","","","")
y("hair_serum","kerotin.com","unclear","","","","natural hair products; growth serum not confirmed")
y("hair_serum","vedix.com","yes","Root-stimulating hair oils; Vithan scalp nourishing serum (slugs)","","Keshamrut oil buy 2 get 1 / buy 3 get 2","us. host")
y("hair_serum","ekmiveda.com","yes","Custom Ayurvedic hair oil / hair thickening (home title)","","","price not matched ($60-75)")
y("hair_serum","curlmix.com","yes","Growth Serum for Curly Hair (slug)","","vip-membership; summer styler bundle","mainly a curly-hair brand")
y("hair_serum","trycuradose.com","unclear","The Growth System","","","form (topical vs supplement) not shown")
y("hair_serum","simplyrevival.com","unclear","Natural DHT Support Blend","","","form not shown; may be supplement")
y("hair_serum","peptonix.com","unclear","","","","quiz. host; product not shown")
# compression
y("compression_socks","everstridesocks.com","yes","Bamboo Wide Compression Socks","34.00 (reg 39.00)","Black Friday buy 2 get 2 free + gift; Ankle Bamboo also listed","price from page")
y("compression_socks","mommycarekits.com","unclear","","","","home 403 (blocked)")
y("compression_socks","hushedsocks.com","yes","Eucalyptus knee-high compression socks","35.00","","")
y("compression_socks","onecompress.com","yes","Onecompress recovery compression (home)","","","price not matched ($44-$95)")
y("compression_socks","comradsocks.com","yes","Everyday compression socks","","","price not matched")
y("compression_socks","sockwellusa.com","yes","Merino wool compression socks","","","price not matched")
y("compression_socks","bombas.com","unclear","","","","home 429 (blocked); large established brand, registered 2000")
# chin
y("chin_wrap","thestudiomd.com","unclear","","","","home 403 (blocked)")
y("chin_wrap","osanyinherbs.com","unclear","","","","HTTP 202 empty page")
y("chin_wrap","tryskult.com","yes","Collagen Face Sculpt Wrap","","Black month sale up to 50%","price shown in IDR to this server; USD not read")
y("chin_wrap","clueblog.com","unclear","","","","home 403 (blocked); page name 'Online Data Center'")
y("chin_wrap","buykglow.com","yes","Double Chin Mask (1 pack / 3 pack)","","3-pack listing exists","price not matched")
y("chin_wrap","evercushion.com","unclear","","","","home text has no product names")
y("chin_wrap","restoradaily.com","unclear","","","","product not readable; Black Friday banner")
# dog fountain
y("dog_fountain","formulaaffiliate.com","unclear","","","","site did not load; ad page name 'Trending News'")
y("dog_fountain","lilesy.com","unclear","","","","site did not load; ad page name 'Trending News'")
y("dog_fountain","theflowzy.com","unclear","","","","home mentions omega-3 fish oil; fountain not seen")
y("dog_fountain","winkflo.com","unclear","","","","general pet store; fountain not confirmed")
y("dog_fountain","selenepets.com","yes","Kitty Fountain / Doggy Fountain + filters","70 and 135 on page, unmatched","Save Big with Bundles; pre-Black Friday up to $70 off","most of the listed product slugs are filters")
y("dog_fountain","petkit.com","yes","Water Fountain (home title)","","","established brand, registered 2003")
y("dog_fountain","happywags.co","unclear","","","","product not readable")
# hair removal cream
y("hair_removal_cream","shopluuma.com","unclear","","","free shipping from $45","nav Hair Removal; form (cream/spray) not shown")
y("hair_removal_cream","simplesnatched.com","yes","Snatched Hair Removal Cream (nav)","","Black Friday up to 60% off + 2 free gifts","")
y("hair_removal_cream","meravae.co","yes","Meravae Facial Hair Removal Cream","","launch offer save up to 53%","claims '50,000+ orders' on page, unverified")
y("hair_removal_cream","nohaircrew.us","yes","Hair removal creams for men","","","prices not matched")
# neck cream
y("neck_cream","whatgracebought.com","unclear","","","","site did not load")
y("neck_cream","nourishmax.com","unclear","","","","anti-aging face and body care; neck cream not confirmed")
y("neck_cream","kindscience.com","unclear","","","","skincare range; neck cream not confirmed")
y("neck_cream","saeskyn.com","unclear","","","","home text empty")
# rosemary
y("rosemary_oil","jcsmiracleproducts.com","unclear","","","","hair growth product; rosemary not confirmed")
y("rosemary_oil","officialbodywise.com","unclear","","","","product not readable")
y("rosemary_oil","spoiledchild.com","unclear","","","","home 403 (blocked)")
y("rosemary_oil","sringe.com","unclear","","","Fall sale buy 2 get 1 free + free ship over $45","product not readable")
y("rosemary_oil","simplyrevival.com","unclear","","","","DHT support blend; form unknown")
y("rosemary_oil","vitaprima.com","unclear","","","","hair and skin care; rosemary oil not confirmed")
y("rosemary_oil","trylumin.co","unclear","","","","scalp formula; form unknown")
y("rosemary_oil","chebeauty.com","unclear","","","","chebe hair products; rosemary oil not confirmed")
y("rosemary_oil","aureph.com","unclear","","","Fall sale buy 2 get 1 free","product not readable")
y("rosemary_oil","azureboutique.co","unclear","Ultimate Growth Set","","","hair growth set + quiz; form unknown")
# magnesium
y("magnesium_spray","ozcogoods.com","yes","Topical Magnesium Spray for sleep and anxiety","36.00 or 49.00 (unmatched)","","")
y("magnesium_spray","sringe.com","unclear","","","","product not readable")
y("magnesium_spray","magsskin.com","unclear","MAGS Skin sensitive-skin deodorant (magnesium spray for eczema per home desc)","","","deodorant positioning")
# towel
y("exfoliating_towel","goshi.com","yes","Japanese exfoliating towels (home desc)","","","price not matched")
y("exfoliating_towel","melbob.com","unclear","","","Buy 3 get 10% off; free ship $50+","product not readable")
y("exfoliating_towel","simabrand.com","yes","Exfoliating Towel (home title)","","","prices $41.70-$64.70 on page unmatched")
y("exfoliating_towel","ecoviabrand.com","unclear","","","","home text has no product names")
NO = {"thehealthcarpenter.com":"med spa / wellness clinic","beflawlessmn.com":"med spa (offer page 404)","spaoffers.co":"clinic offer-page platform","myskindealer.com":"medical aesthetics clinic",
"eightsaintsskincare.com":"face skincare serums and creams","drmtlgy.com":"medical-grade sunscreens and serums","trymiamimd.com":"med spa","byminus.com":"moisturizer, serum, cleanser",
"magnolia.com":"home decor retailer","moxielash.com":"lash clusters, not serum","sephora.com":"multi-brand retailer","thelashhause.co.uk":"lash extension supplies","wywrd.com":"analytics host, no store",
"trendhunter.com":"trend news site","alltimeairconditioning.com":"HVAC service","weareluna.store":"apparel and shapewear","mariahbeautyservice.com":"beauty service, page 404","whatsapp.com":"messaging app",
"royalmedspaillinois.com":"med spa","kojeva.com":"lymphatic face brush, not wrap","google.com":"search engine","callixe.com":"pain-relief wellness brand","skinnyboutique.com":"Cryoskin clinic",
"mellowsleep.com":"comforters and pillows","ortaclinic.com":"clinic","thecushionlab.com":"memory-foam pillows","lymphoria.co":"lymph supplement","propondandlakes.com":"pond services",
"activelyblack.com":"athleisure apparel","boxiecat.com":"cat litter","valspar.com":"paint","bumzzy.com":"shaving device","aurlux.co":"hair inhibiting oil, not removal cream","anrdre.com":"general dropship store",
"sreemed.com":"ayurvedic pharmacy","vibriance.com":"vitamin C serum","imaree.com":"glycolic pads, hair masks, eye gels","exotichairdoctor.com":"hair salon","hairqare.co":"hair coaching program",
"lgbeauty.com":"K-beauty multi-brand retailer","irestorelaser.com":"light therapy device","glovbeauty.com":"supplements","theearthlingco.com":"shampoo bars, personal care","pioneerpam.com":"herbal tinctures and tallow skincare",
"getblessedbotanicals.com":"herbal extracts","drteals.com":"epsom salt bath products","hiyahealth.com":"kids vitamins","vitaecharm.com":"body oil store, no rosemary oil seen","everymarket.com":"online marketplace",
"elevarekoreanbeauty-global.com":"K-beauty multi-category","dawaveessentials.shop":"wave brushes and durags","ugcmasteryacademy.com":"creator training","senzio.store":"herbal balm, not socks",
"pacas.com":"casual socks and knitwear, no compression seen","goda.co":"body oil store, not hair product",
"earthlyderm.com":"turmeric soap store, not this category","hestiacosmetics.com":"foundation store, not this category","spoiledchild.com":"unreadable"}
