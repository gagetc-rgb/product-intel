import json,sys
cand=json.load(open('m2_candidates.json',encoding='utf-8'))
cats=sys.argv[1:]
import os
for c in cats:
    print('=====',c,cand[c]['phrase'])
    for s in cand[c]['stores']:
        if not(s['max_age']>=90 or s['max_age']<30): continue
        o=json.load(open(f"raw/{s['domain']}.json",encoding='utf-8'))
        print(f"## {s['domain']} age={s['max_age']} ads={s['ads']} pages={s['pages'][:3]} hosts={s['hosts'][:3]} pj={o['pj_status']} rdap={o['rdap_reg']} wb={o['wb_first']}")
        if o['products']:
            print('  PRODUCTS',len(o['products']),'oldest',min(p['c'] for p in o['products']),[ (p['t'][:50],p['pr']) for p in o['products'][:12]])
        else:
            print('  HOME',o.get('home_status'),(o.get('home_title') or '')[:100],'|',(o.get('home_desc') or '')[:140],'|',o.get('home_prices'))
