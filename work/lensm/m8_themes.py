"""M8: keyword themes for 1-3 star review texts (multi-label; a review counts once per theme). Usage: python m8_themes.py <raw_rev/<label>_loox_low.json>"""
import sys, json, re, collections
T = {
 "shipping and delivery": r"\bship|deliver|arriv(?:e|ed) (?:late|damag)|tracking|never (?:received|came|arrived)|(?:not|n't|haven.t|have not) (?:yet )?(?:received|gotten)|took (?:too )?(?:long|weeks)|\blate\b|\bstill waiting|lost in|missing (?:item|bottle|order)|wrong item|damaged|broken box|messy",
 "billing and subscription": r"subscri|charged|\bbill|auto.?ship|membership|cancel|checkout|double charge|recurring",
 "support and refunds": r"refund|\breturn|exchange|support|customer service|customer care|emailed|e-?mail|no (?:answer|reply|response)|didn.t (?:get a|hear)|money.?back|chase|contact|guarantee|\bchina\b",
 "does not work": r"no (?:visible|noticeable)|doesn.t do anything|does not do anything|not do what|not doing|did(?:n.t| not)? nothing|nothing (?:for|to)|no (?:results?|difference|change|effect|improvement)|not work|n.t work|didn.t work|doesn.t work|no help|didn.t help|not help|did nothing|ineffective|swelled more|swelling|not (?:as )?advertised|as advertised|claims?|hype|expected more|results were too mild|subtle at best|not much change|attract|compliments? (?:didn|did not)|not a wow|wasn.t effective|useless|waste of money|doesn.t last|does not last|didn.t last|not last|faded|projection|stay long|doesnt stay|not stay",
 "product itself": r"too (?:tight|small|big|large|long|short|loose|heavy|strong|sweet|thin|greasy|sticky|thick|rich)|\btight|\bsiz(?:e|ing)|\bfit\b|rol(?:l|ls|led|ling) (?:down|up)|fall(?:s|ing)? down|rode down|indent|cut(?:s|ting)? (?:in|off)|circulation|hole|rip|tore|leak|\blid\b|cap|bottle|texture|scent|smell|fragrance|greasy|sticky|irritat|rash|itch|burn|allerg|material|fabric|quality|construction|stretch|uncomfortable|hurt|pain|dry|breakout|broke out|residue|packag",
}
SUB = {
 "fit / sizing / too tight": r"too (?:tight|small|big|large|long|short|loose)|\btight|\bsiz(?:e|ing)|\bfit\b|indent|cut(?:s|ting)? (?:in|off)|circulation|stretch|wide|calf",
 "rolls or slips down": r"rol(?:l|ls|led|ling) (?:down|up)|fall(?:s|ing)? down|rode down|slip",
 "durability / defect": r"hole|rip|tore|defect|flaw|fell apart|construction|quality",
 "leak / packaging damage": r"leak|\blid\b|\bcap\b|residue|messy|packag|box",
 "scent (too weak, fades, not liked)": r"scent|smell|fragrance|perfume|projection|faded",
 "texture / skin feel": r"texture|heavier|rich|greasy|sticky|dry|irritat|rash|itch|burn|allerg|breakout|broke out",
 "slow or missing delivery": r"\bship|deliver|tracking|never (?:received|came|arrived)|not (?:yet )?received|took (?:too )?(?:long|weeks)|\blate\b|still waiting|missing",
 "refund / return / exchange friction": r"refund|\breturn|exchange|money.?back|\bchina\b",
 "slow or generic support": r"support|customer service|emailed|e-?mail|no (?:answer|reply|response)|chase|generic repl",
 "subscription or checkout confusion": r"subscri|checkout|charged|membership|auto.?ship",
 "no effect / claim not met": r"no (?:visible|noticeable)|doesn.t do anything|not doing|nothing|no (?:results?|difference|change|effect)|not work|did nothing|not as advertised|expected more|hype|claims?|attract|mild|subtle",
}
d = json.load(open(sys.argv[1], encoding="utf-8")); rv = [r for r in d["reviews"] if r["text"].strip(". ")]
empty = len(d["reviews"]) - len(rv)
c = collections.Counter(); s = collections.Counter(); star = collections.Counter(r["stars"] for r in d["reviews"]); unc = 0
for r in rv:
    t = r["text"].lower(); hit = False
    for k, p in T.items():
        if re.search(p, t): c[k] += 1; hit = True
    for k, p in SUB.items():
        if re.search(p, t): s[k] += 1
    if not hit: unc += 1
print("dist 1..5:", d["dist"], "| low reviews read by stars:", dict(star), "| with text:", len(rv), "empty/dots:", empty)
for k, v in c.most_common(): print(f"  {k}: {v}")
print("  (no theme matched):", unc); print("-- sub-themes")
for k, v in s.most_common(): print(f"  {k}: {v}")
json.dump({"stars": dict(star), "with_text": len(rv), "themes": dict(c), "sub": dict(s), "no_theme": unc}, open(sys.argv[1].replace("_low.json", "_themes.json"), "w"), indent=1)
