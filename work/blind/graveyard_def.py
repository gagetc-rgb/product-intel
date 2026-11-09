"""Pre-registered category definitions for the graveyard (2026-11-07).

A category = the product FORM we would actually sell. Written before looking at survival results.
Substitutes in other forms (oral magnesium, net sponges, liquid body wash) are excluded:
they compete for the same need, but a newcomer's survival in them says little about ours.
Each entry: (MUST regex, NOT regex), both case-insensitive, applied to the listing title.
"""
STRICT = {
    "magnesium_spray": (r"magnesium.*(spray|\boil\b|mist)|(spray|\boil\b|mist).*magnesium",
                        r"capsul|tablet|gumm|powder|softgel|supplement|glycinate|citrate|threonate|chewable|"
                        r"drink|\d+\s?mg\b|flake|bath salt|epsom|vitamin"),
    "exfoliating_towel": (r"^(?=.*(towel|washcloth|wash cloth|cloth))(?=.*(exfoliat|scrub|nylon|korean|japanese|salux|italy))",
                          r"sponge|loofah|luffa|glove|mitt|brush|disposable|makeup|wipe|face towels|"
                          r"hand towel|bath towel set|microfiber hair|net\b"),
    "turmeric_soap": (r"turmeric.*(soap|bar)|(soap|bar).*turmeric",
                      r"body wash|liquid|shower gel|serum(?! soap)|lotion|cream(?! soap)"),
}

def on_target(pid, title):
    import re
    if pid not in STRICT: return True
    must, nott = STRICT[pid]
    return bool(re.search(must, title, re.I)) and not re.search(nott, title, re.I)

# Added 2026-11-07, before the search scrape of these categories (pre-registered).
STRICT.update({
    "compression_socks": (r"compression.*(sock|stocking)|(sock|stocking).*compression", r"sleeve|glove|legging|tights|pantyhose|shorts"),
    "color_foundation": (r"^(?=.*(colou?r.?(chang|adapt|adjust)|tone.?adjust))(?=.*foundation)", r"\blip|lipstick|blush|nail|hair dye|mood"),
    "tallow_balm": (r"^(?=.*tallow)(?=.*(balm|cream|moistur|butter|whip|salve))", r"soap|candle|\blip|deodorant|cooking|\blard|\bdog"),
    "neck_cream": (r"^(?=.*neck)(?=.*(cream|firming|lotion|moistur|serum|balm))", r"mask|massager|device|wand|pillow|patch|\bpad|tape|strap|wrap|roller|tool|machine|\bled\b"),
    "rosemary_oil": (r"rosemary.*\boil|\boil.*rosemary", r"shampoo|conditioner|\bmask|gumm|supplement|capsule|\btea\b|cooking|candle|diffuser|mousse|leave.in spray"),
    "hair_removal_cream": (r"^(?=.*hair remov)(?=.*(cream|lotion|\bgel|depilat))", r"laser|\bipl\b|device|epilator|razor|wax strip|powder|trimmer|shaver"),
    "chin_wrap": (r"^(?=.*(chin|v.?line|jawline))(?=.*(mask|strap|wrap|band|patch|tape|belt|bandage))", r"device|machine|\bems\b|massager|exerciser|roller|cream|serum|\bball|trainer"),
    "persimmon_soap": (r"^(?=.*persimmon)(?=.*(soap|\bbar))", r"body wash|liquid|spray|deodorant|lotion|cream"),
    "shower_filter": (r"^(?=.*(shower head|showerhead))(?=.*filt)", r"replacement|refill|cartridges? only|curtain|drain|hair catcher"),
    "dog_fountain": (r"^(?=.*fountain)(?=.*(\bpet|\bcat|\bdog))", r"replacement filter|filters? only|pump only|garden|outdoor|solar|chocolate"),
    "scent_diffuser": (r"^(?=.*diffuser)(?=.*(waterless|nebuli[sz]|cold air|hvac|scent machine|smart scent|scent air))", r"\breed\b|humidifier|ultrasonic|car vent|refill|oils? only"),
    "pore_patch": (r"^(?=.*(nose|pore|blackhead|sebaceous))(?=.*(patch|strip))", r"pimple|acne patch|\beye|\blip|vacuum|extractor|\btool|tweezer"),
    "whitening_powder": (r"^(?=.*whiten)(?=.*powder)", r"strip|\bgel\b|\bpen\b|\bled\b|toothpaste|mouthwash|\bdog|\bpet"),
    "lash_serum": (r"^(?=.*(lash|brow))(?=.*(serum|growth|enhanc|conditioner))", r"glue|adhesive|extension|curler|mascara|remover|false|magnetic|tint|lift kit|cluster"),
    "hair_serum": (r"^(?=.*(hair|scalp))(?=.*(serum|\boil|spray|foam|tonic))(?=.*(growth|regrow|thinning|loss|thicken))", r"supplement|gumm|capsule|tablet|vitamin|softgel|shampoo|conditioner|minoxidil"),
    "body_oil": (r"body oil|crep", r"hair|lotion|cream|serum|wash|scrub|baby|massage"),
    "prewash_oil": (r"pre.?wash|pre.?shampoo|scalp oil|hair oil", r"\bbody\b|\bface\b|conditioner|\bmask|spray"),
})

# v2.1 (2026-11-08, written before re-reading neck-cream results): a neck cream is a product SOLD for the neck.
# v2.0 let face creams that also mention the neck through ("Face & Neck Cream", "Eye, Neck & Face").
STRICT_V20_NECK = STRICT["neck_cream"]
STRICT["neck_cream"] = (
    r"neck\s*(cream|firming|tighten|lift|wrinkle|moistur|serum|balm|lotion)|(firming|tightening|lifting|crepey)\s+neck|"
    r"neck\s*(&|and)\s*(chest|d.collet)",
    r"face\s*(&|and|,)\s*neck|neck\s*(&|and|,)\s*face|facial|\bface\b.*\bneck\b.*\b(eye|body)|"
    r"mask|massager|device|wand|pillow|patch|\bpad|tape|strap|wrap|roller|tool|machine|\bled\b|belly|thigh")

