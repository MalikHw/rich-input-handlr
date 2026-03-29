"""
word db for RichInputHandlr.
these are built-in lists — devs can extend them via RichInput(extra_yes=[...], extra_no=[...], etc.)
"""

from itertools import product as _product


_SWEARS = [
    "fuck", "shit", "hell", "damn", "ass", "crap", "bloody",
    "fck", "f*ck", "sh*t", "d*mn",
    "effing", "freaking", "frickin", "freakin", "friggin", "flipping", "bleeding",
]

_PRE_INTENSIFIERS = ["", "oh ", "oh my god ", "omg ", "holy ", "sweet ", "jesus "]

_YES_CORES = ["yes", "yeah", "yep", "yup", "right", "way", "absolutely", "totally", "for real", "straight"]
_NO_CORES  = ["no", "nah", "nope", "way", "chance", "not", "never"]

_YES_TEMPLATES = [
    "{p}{s} {c}",
    "{p}{c} {s}",
    "{p}{s} to the {c}",
    "{p}hot {s} {c}",
    "{p}{s} {s} {c}",
]
_NO_TEMPLATES = [
    "{p}{s} {c}",
    "{p}absolutely {s} {c}",
    "{p}oh {s} {c}",
    "{p}{s} {s} {c}",
    "{p}no {s} way",
    "{p}{c} {s}",
]

_UWU_INTENSIFIERS = [
    "", "oh ", "omg ", "oh my gawd ", "oh my god ", "eee ", "owo ",
    "uwu ", "hehe ", "teehee ", "kyaa ", "squee ",
]

_UWU_YES_CORES = [
    "yes", "yesh", "yus", "yiss", "yeah", "yea", "yay", "yaaaay",
    "ok", "oki", "okii", "okie", "okiee", "okie dokie",
    "pwease", "pwetty pwease", "pweese",
    "sure", "suwe", "shure",
    "absolutely", "absowutewy", "absowootewy",
    "totally", "totawwy", "totes",
    "of course", "of couwse", "owf couwse",
    "please", "pwease", "pwees",
    "yay", "yayyy", "yayy", "yaay",
]

_UWU_NO_CORES = [
    "no", "nyo", "nuu", "nuuu", "nope", "nopee",
    "no thanks", "no fank you", "no thwanks",
    "never", "nevew", "neva",
    "stop", "stawp", "stahp",
    "go away", "go awway", "weave me awone",
    "leave me alone", "weave me awone",
]

_UWU_UNCERTAIN_CORES = [
    "maybe", "maaybe", "maybeee", "mebby", "mebbe",
    "idk", "idkk", "idkkk",
    "not sure", "not suwe", "unsure", "unsuwee",
    "perhaps", "pehwaps", "pewchance",
    "i dunno", "i dunnow", "dunno",
    "hmm", "hmmm", "hmmmm",
    "could be", "couwd be",
]

_UWU_TEMPLATES = [
    "{i}{c}",
    "{i}{c} uwu",
    "{i}{c} owo",
    "{i}{c}~",
    "{i}{c}~~",
    "{i}{c} >w<",
    "{i}{c} ^w^",
    "{i}{c} :3",
    "{i}{c}!! uwu",
    "{i}{c}!!! owo",
    "w-well... {c}",
    "{c} p-pwease",
    "{c}!! >w<",
]

def _gen_uwu_yes() -> list[str]:
    out: set[str] = set()
    for intensifier, core, tmpl in _product(_UWU_INTENSIFIERS, _UWU_YES_CORES, _UWU_TEMPLATES):
        out.add(tmpl.format(i=intensifier, c=core).strip())
    return sorted(out)

def _gen_uwu_no() -> list[str]:
    out: set[str] = set()
    for intensifier, core, tmpl in _product(_UWU_INTENSIFIERS, _UWU_NO_CORES, _UWU_TEMPLATES):
        out.add(tmpl.format(i=intensifier, c=core).strip())
    return sorted(out)

def _gen_uwu_uncertain() -> list[str]:
    out: set[str] = set()
    for intensifier, core, tmpl in _product(_UWU_INTENSIFIERS, _UWU_UNCERTAIN_CORES, _UWU_TEMPLATES):
        out.add(tmpl.format(i=intensifier, c=core).strip())
    return sorted(out)

def _gen_profanity_yes() -> list[str]:
    out: set[str] = set()
    for pre, swear, core, tmpl in _product(_PRE_INTENSIFIERS, _SWEARS, _YES_CORES, _YES_TEMPLATES):
        out.add(tmpl.format(p=pre, s=swear, c=core).strip())
    for swear, core in _product(_SWEARS, _YES_CORES):
        out.add(f"{swear} {core}")
        if not any(swear.endswith(c) for c in ("*", "k", "g")):
            out.add(f"{swear}ing {core}")
    return sorted(out)

def _gen_profanity_no() -> list[str]:
    out: set[str] = set()
    for pre, swear, core, tmpl in _product(_PRE_INTENSIFIERS, _SWEARS, _NO_CORES, _NO_TEMPLATES):
        out.add(tmpl.format(p=pre, s=swear, c=core).strip())
    for swear, core in _product(_SWEARS, _NO_CORES):
        out.add(f"{swear} {core}")
        if not any(swear.endswith(c) for c in ("*", "k", "g")):
            out.add(f"{swear}ing {core}")
    return sorted(out)


_YES_BASE: list[str] = [
    # classic
    "y", "yes", "yeah", "yep", "yup", "yea", "aye", "ok", "okay", "okie",
    "sure", "alright", "alrighty", "absolutely", "definitely", "certainly",
    "of course", "indeed", "affirmative", "positive", "confirmed", "confirm",
    "gladly", "willingly", "righto", "right", "correct", "true",
    # slang
    "ye", "ya", "yah", "k", "kk", "mkay", "mhm", "mmhm", "mm", "uh huh",
    "for sure", "fosho", "fo sho", "totally", "totes", "obv", "obviously",
    "duh", "bet", "fax", "facts", "fr", "fr fr", "no cap", "real",
    "say less", "lets go", "let's go", "lesgo", "letsgo", "lets goo",
    "based", "valid", "W", "big W", "hard yes",
    # formal
    "yep yep", "yeppers", "yepperino", "yeperoni", "yeperooni",
    "yes indeedy", "yes indeed", "indeedy", "indeedy do",
    "indubitably", "undoubtedly", "unquestionably", "without a doubt",
    "without question", "by all means", "with pleasure",
    "most certainly", "most definitely", "most assuredly",
    "you bet", "you betcha", "betcha", "you know it",
    "you know that's right", "that's right", "thats right",
    "roger", "roger that", "copy", "copy that", "10-4", "10 4",
    "loud and clear", "understood", "i understand", "gotcha",
    "got it", "gotchu", "on it", "i'm on it", "im on it",
    "say no more", "no need to ask twice",
    "well duh", "well yeah", "well yes",
    "goes without saying", "needless to say",
    "1", "+1", "👍", "✅", "✔", "☑",
    "yes!!", "yes!!!", "yeah!!", "yeah!!!",
    "omg yes", "omg yeah", "omg totally", "omg absolutely",
    "oh yes", "oh yeah", "oh absolutely", "oh definitely",
    "oh for sure", "oh totally", "oh most definitely",
    "YESSS", "YASSS", "YEAH", "YEP", "YUP",
    "yws", "yw", "ofc", "ofc!", "obvi", "abso-lutely",
    "yeahhh", "yeahh", "yesss", "yessss", "yessir", "yessirr",
    "mhm mhm", "mhmm", "mhmmm", "mhmhm",
    "ofc ofc", "yuppers", "yupperino", "yupp", "yuppp",
    "yeeee", "yeee", "yeaaa", "yeaaaa", "myes", "mehyes",
    # discord/internet
    "pog", "poggers", "pogchamp", "lets fkin go", "let's fkin go",
    "slay", "periodt", "periodt yes", "period",
    "understood the assignment", "sheesh",
    "lowkey yes", "highkey yes", "highkey",
    "on god", "on god yes",
    # gaming
    "gg", "accept", "accepted", "agree", "agreed",
    "approved", "approve", "very well", "as you wish", "so be it",
    "it shall be done", "consider it done", "will do", "can do",
    "i'll do it", "ill do it", "i will", "i will do it",
    "i am willing", "i am down", "i'm down", "im down",
    "down", "down for it", "down for that",
    # typos
    "yse", "eys", "yas",
    # multilang
    "si", "sí", "claro", "claro que sí", "por supuesto",
    "oui", "oui oui", "bien sûr",
    "ja", "jawohl", "genau", "natürlich",
    "da", "hai", "はい",
    "sim", "com certeza",
    "ken", "כן", "نعم", "أيوه",
    "evet", "io", "ναι", "haan", "हाँ", "ne", "네",
    # agreements
    "go for it", "do it", "just do it", "make it happen",
    "make it so", "engage", "proceed", "proceed please",
    "i consent", "i agree", "i concur", "concur",
    "that works", "works for me", "works", "sounds good",
    "sounds great", "sounds perfect", "sounds like a plan",
    "that's fine", "thats fine", "fine by me", "fine",
    "good by me", "good with me", "i'm good with that",
    "im good with that", "i'm cool with that", "im cool with that",
    "cool with me", "cool", "cool cool",
    "no problem", "no prob", "no probs", "np",
    "no objections", "no issues", "no complaints",
    "yass", "yasss", "yassss", "yas queen", "yas",
    "yes please", "yes pls", "pls yes", "please yes",
    "sign me up", "im in", "i'm in", "count me in", "in",
    # passive/reluctant yes
    "ugh fine", "ugh fine ok", "ugh ok", "fine ok", "fine fine",
    "screw it fine", "screw it ok", "screw it yes", "screw it",
    "i guess if i have to", "if i have to", "i suppose if i must",
    "sure why not", "why not", "eh why not", "ugh why not",
    "do whatever you want", "whatever you want", "just do it then",
    "yeah sure whatever", "yeah whatever", "sure whatever",
    "yeah sure whatever just do it",
    "tis a yes", "tis a yes from me", "i say yes", "that'd be a yes",
    "ye ye ye", "ye ye ye ye ye",
    "yes yes yes", "yeah yeah yeah",
]

_NO_BASE: list[str] = [
    # classic
    "n", "no", "nope", "nah", "nay", "negative", "negatory",
    "never", "not", "not really", "no way", "no thanks", "no thank you",
    "absolutely not", "definitely not", "certainly not",
    "declined", "decline", "reject", "rejected", "denied", "deny",
    "false", "incorrect", "wrong",
    # slang
    "na", "nahhh", "nahh", "nope nope",
    "no no", "nono", "nonono",
    "not a chance", "no chance", "fat chance",
    "pass", "hard pass", "im good", "i'm good", "i'm okay", "im okay",
    "L", "big L", "hard no",
    "gtfo", "get out", "no way jose",
    "nuh uh", "nuh-uh", "nu uh", "unh uh",
    "not today", "not today satan",
    "nope nope nope", "no no no",
    "under no circumstances", "not in a million years",
    "not in your life", "not on your life", "over my dead body",
    "when pigs fly", "when hell freezes over",
    "not gonna happen", "ain't gonna happen", "aint gonna happen",
    "not happening", "never happening", "never ever",
    "never ever ever", "not now not ever",
    # internet/discord
    "L + ratio", "ratio", "ratio + no",
    "0", "f", "-1", "👎", "❌", "✖", "🚫",
    "no shot", "no shot bruh", "cap", "that's cap", "thats cap",
    "big cap", "massive cap", "nah fr", "nah fr fr",
    "nah bro", "nah man", "nah homie", "nah dawg", "nah fam",
    "nope dot com",
    "not even", "not even a little", "not even close",
    # formal
    "i decline", "i refuse", "i object", "i disagree", "disagree",
    "objection", "vetoed", "veto", "blocked", "block",
    "not approved", "disapproved", "disapprove",
    "i will not", "i wont", "i won't", "i shall not",
    "i am not willing", "unwilling",
    "count me out", "leave me out", "leave me out of it",
    "not interested", "no interest",
    "thanks but no thanks", "thanks but no",
    "nty", "no ty", "ty no", "thanks no",
    "nahhhh", "nahhhhh", "nooope",
    "negativo", "nop", "nope-a-dope",
    "nopenopenope", "naw man", "naw bro", "nawww",
    "negatory ghost rider", "that's a negative",
    "thats a no from me", "thats a no", "that's a no",
    "that's gonna be a no", "gonna be a no",
    "i'm gonna have to say no", "ima have to say no",
    # disgust
    "ew", "eww", "ewww", "gross no", "yuck", "yuck no",
    "ugh no", "ugh nope", "bleh", "bleh no",
    # typos
    "on", "noo", "nou",
    # multilang
    "non", "nein", "niet", "nee",
    "no gracias", "non merci", "nein danke",
    "iie", "いいえ", "hayır", "όχι",
    "nahi", "नहीं", "lo", "לא", "لا", "아니요", "아니",
    # misc
    "i'd rather not", "i would rather not", "i'd rather die",
    "rather not", "prefer not", "prefer not to",
    "i'll pass", "ill pass", "passing",
    "skip", "skip it", "skipping",
    "nope out", "opting out", "opt out", "i opt out",
    "not for me", "not my thing", "not my jam", "not my vibe",
    "doesn't work for me", "doesn't work", "wont work",
    "won't work", "that won't work", "that doesn't work",
    "bad idea", "terrible idea", "awful idea",
    "i don't think so", "dont think so", "i think not",
    "naw",
]

_UNCERTAIN_BASE: list[str] = [
    # classic
    "maybe", "perhaps", "possibly", "probably", "might", "could be",
    "idk", "i don't know", "i dont know", "dunno", "duno", "donno",
    "not sure", "unsure", "uncertain", "undecided",
    "depends", "it depends", "hard to say", "hard to tell",
    "who knows", "who knows lol",
    # casual
    "eh", "ehhh", "meh", "mehh", "kinda", "kinda sorta", "sorta",
    "sort of", "kind of", "more or less", "ish", "maybe ish",
    "whatever", "whatevs", "w/e", "idrc", "idc",
    "50/50", "flip a coin", "coin flip",
    "prolly", "probs", "prob", "maybe maybe",
    "shrug", "¯\\_(ツ)_/¯", "idk man", "idk bro", "idk lol",
    "could go either way", "either way",
    "i'm not sure", "im not sure", "not entirely sure",
    "not 100%", "not 100 percent",
    "not totally sure", "not quite sure",
    "can't say for sure", "cant say for sure",
    "could be yes could be no", "yes and no",
    "yes but also no", "no but also yes",
    # hedging
    "to be honest", "tbh", "tbh idk", "honestly idk",
    "on the fence", "sitting on the fence",
    "torn", "i'm torn", "im torn",
    "conflicted", "i'm conflicted", "im conflicted",
    "mixed feelings", "i have mixed feelings",
    "it's complicated", "its complicated", "complicated",
    "not black and white", "gray area", "grey area",
    # probability
    "likely", "unlikely", "somewhat likely", "somewhat unlikely",
    "might be", "might not be", "may or may not",
    # internet/discord
    "lmao idk", "lol idk", "idk lmao", "idk lol",
    "bruh idk", "bro idk", "ngl idk", "ngl not sure",
    "lowkey unsure", "lowkey idk", "lowkey maybe",
    "🤷", "🤷‍♂️", "🤷‍♀️", "😐", "🫤", "😑",
    "ehhhhh", "mehhhh", "idkkkk",
    "hmm", "hmmm", "hmmmm", "hm", "hmmmmmm",
    "well", "uhh", "uhhhh", "umm", "ummm", "uhhh", "uhm",
    "i mean", "i mean maybe", "i mean idk",
    "i guess", "i guess so", "i guess maybe",
    "i suppose", "i suppose so", "suppose so", "guess so",
    # profanity uncertain
    "fuck if i know", "shit idk", "hell if i know",
    "beats the fuck out of me", "beats me",
    "fucked if i know", "damned if i know", "shit if i know",
    "fuck knows", "shit knows", "hell knows", "damn knows",
    "who the fuck knows", "who the hell knows", "who the shit knows",
    "who the damn knows", "how the fuck should i know",
    "how the hell should i know", "how the shit should i know",
    "fucked if i care", "shit idc", "hell idc", "damn idc",
    "fuck idk", "hell idk", "damn idk", "shit idk",
    "the fuck do i know", "the hell do i know",
    # tbd/pending
    "tbd", "to be determined", "tba", "to be announced",
    "pending", "unclear", "yet to be determined",
    # sleep on it
    "ask me later", "check back later",
    "let me think about it", "need to think",
    "let me sleep on it", "sleep on it", "i'll sleep on it",
    "rain check", "let's revisit", "revisit",
    "subject to change", "undetermined",
    "remains to be seen", "we'll see", "we shall see",
    "could argue both ways",
    # lean variants
    "leaning yes", "leaning no",
    "leaning towards yes", "leaning towards no", "leaning maybe",
    "somewhere in the middle", "middle ground",
    "partially", "partly", "in part", "somewhat",
    "kind of yes", "kind of no", "sort of yes", "sort of no",
    # multilang
    "peut-être", "tal vez", "vielleicht",
    "probablemente", "wahrscheinlich", "forse",
    "kanske", "belki", "ίσως",
    "शायद", "אולי", "ربما", "아마도",
    "多分", "たぶん",
]


YES_WORDS:       list[str] = list(dict.fromkeys(_YES_BASE       + _gen_uwu_yes()       + _gen_profanity_yes()))
NO_WORDS:        list[str] = list(dict.fromkeys(_NO_BASE        + _gen_uwu_no()        + _gen_profanity_no()))
UNCERTAIN_WORDS: list[str] = list(dict.fromkeys(_UNCERTAIN_BASE + _gen_uwu_uncertain()))
