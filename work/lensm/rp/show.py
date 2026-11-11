import json,glob,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
for f in sorted(glob.glob(f'stepc_{sys.argv[1]}/*.json')):
    d=json.load(open(f,encoding='utf-8'));h=d['home'];l=d.get('landing',{})
    print('==',d['domain'],d['oldest_ad'],h.get('status'),'|',h.get('title','')[:80],'|n',h.get('kw_n'),h.get('prices','')[:5] if h.get('prices') else '',h.get('currency_meta'))
    print('  hits',[x[:140] for x in h.get('kw_hits',[])[:2]],'| bundle',[b[:70] for b in h.get('bundle',[])[:2]],'| sub',[s[:80] for s in h.get('sub',[])[:2]],'| epa',[s[:90] for s in h.get('epa',[])[:3]])
    if l: print('  landing',l.get('status'),l.get('title','')[:60],l.get('kw_n'),l.get('prices','')[:4] if l.get('prices') else '', [x[:100] for x in l.get('kw_hits',[])[:1]])
    print('  ',d['rdap'],d['wayback'],d['age_class'])
