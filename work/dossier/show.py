import json, sys
for p in sys.argv[1:]:
    d=json.load(open(f"digest/{p}.json",encoding="utf-8")); a=d["amazon_us"]; v=d["verdict_row"]
    print("=====",p,"| shelf",a["shelf_units"],"lst",a["listings_on_target"],"win1k",a["winners_1k"],"| price",d["price_us"])
    print(" age",a["units_by_brand_age"],"| kind",a["units_by_kind"])
    for b in a["top_brands"][:8]: print(f"  {b['key'][:14]:14} {b['units']:>7,} lst{b['listings']:>2} {b['entry_months']}mo {b['status'][:5]:5} {b['best']['price']} {b['best']['stars']} | {b['best']['amazon_brand']} | {b['best']['title'][:55]}")
    print(" gen:",[(x[0],x[3],x[4],x[2][:35]) for x in a["top_generics"][:3]])
    m=d["meta_category"]; print(" meta",m["phrase"],m["active"],m["aged30"],m["aged90"],m["aged180"],"| stores90",v["stores90"],"/",v["stores"])
    print(" stores",[(s[0][:24],s[1],s[2]) for s in d["meta_stores_top"][:6]])
    print(" pages",{k:(sum(p['active'] or 0 for p in x['own'].values()),sum(p['aged90'] or 0 for p in x['own'].values()),sum(p['aged180'] or 0 for p in x['own'].values()),f"{x['own_domain']}/{x['phrase_sample']}") for k,x in d["meta_brand_pages"].items()})
    print(" trend",d["trend"]["term"],d["trend"]["rel_yoy"],d["trend"]["yearly_means_v20"],"z",d["trend"]["zero_share_2y"],"| TT",d["tiktok_top_item_sold_k"])
    for c in d["creatives"]: print("  cre",c["domain"],"180d+:",c["ads_180d_total_meta"],"|",c["product"][:30],"|",[(o["days"],o["page"][:18],o["headline"][:45]) for o in c["oldest"][:2]])
