"""
word db for RichInputHandlr.
these are built-in lists — devs can extend them via RichInput(extra_yes=[...], etc.)
"""

YES_WORDS: list[str] = [
    # classic
    "y", "yes", "yeah", "yep", "yup", "yea", "aye", "ok", "okay", "okie",
    "sure", "alright", "alrighty", "absolutely", "definitely", "certainly",
    "of course", "indeed", "affirmative", "positive", "confirmed", "confirm",
    "gladly", "willingly", "righto", "right", "correct", "true",

    # slang bs
    "ye", "ya", "yah", "k", "kk", "mkay", "mhm", "mmhm", "mm", "uh huh",
    "for sure", "fosho", "fo sho", "totally", "totes", "obv", "obviously",
    "duh", "bet", "fax", "facts", "fr", "fr fr", "no cap", "real",
    "say less", "lets go", "let's go", "lesgo", "letsgo", "lets goo",
    "based", "valid", "W", "big W", "hard yes",

    # profanity/badwords
    "hell yeah", "hell yes", "heck yeah", "heck yes",
    "fuck yeah", "fuck yes", "fck yeah", "f yeah",
    "hell to the yes", "oh hell yeah",
    "damn right", "damn straight",
    "yass", "yasss", "yassss", "yas queen", "yas",
    "yes please", "yes pls", "pls yes", "please yes",
    "sign me up", "im in", "i'm in", "count me in", "in",

    # uwuspeak (fml)
    "yws", "yw", "uwu yes", "yesh", "yus", "yiss", "yers",
    "myes", "mehyes", "oki", "okie dokie", "okey dokey",
    "ofc", "ofc!", "obvi", "abso-lutely", "absoluely",
    "yeahhh", "yeahh", "yesss", "yessss", "yessir", "yessirr",
    "si", "oui", "ja", "da",  # for japanese ngas

    # some typos even tho i did make fuzzy but eh, better be sorry
    "yse", "eys", "eys", "yas",
]

NO_WORDS: list[str] = [
    # classic
    "n", "no", "nope", "nah", "nay", "negative", "negatory",
    "never", "not", "not really", "no way", "no thanks", "no thank you",
    "absolutely not", "definitely not", "certainly not",
    "declined", "decline", "reject", "rejected", "denied", "deny",
    "false", "incorrect", "wrong", "nope",

    # slang bs
    "na", "nahhh", "nahh", "nope nope", "nopee", "nope",
    "hell no", "hell nah", "heck no", "heck nah",
    "no no", "nono", "nonono",
    "not a chance", "no chance", "fat chance",
    "pass", "hard pass", "im good", "i'm good", "i'm okay", "im okay",
    "L", "big L", "hard no",
    "gtfo", "get out", "no way jose",
    "nuh uh", "nuh-uh", "nu uh", "unh uh",
    "not today", "not today satan",

    # profanity/badwords
    "fuck no", "fuck nah", "fck no",
    "hell fucking no", "absolutely fucking not",
    "no fucking way", "nfw",
    "shit no", "hell naw", "naw",

    # uwusoeak (fml)
    "nwo", "nuuu", "nuu", "nuuuu", "nooo", "noooo", "nooooo",
    "nope uwu", "no thx", "no ty", "ty but no", "thx but no",
    "ew no", "ew nope", "eww no", "yikes no",
    "non", "nein", "niet",  # for japanese ngas

    # some typos even tho i did make fuzzy but eh, better be sorry
    "on", "noo", "nou",
]

UNCERTAIN_WORDS: list[str] = [
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

    # uwuspeak (fml)
    "maaaybe", "maybeee", "mebby", "mebbe",
    "idkkk", "idkkkk", "idk idk",
    "perhaps uwu", "uwu idk",

    # badwords
    "fuck if i know", "shit idk", "hell if i know",
    "beats the fuck out of me", "beats me",

    # ngas not englih
    "peut-être", "tal vez", "vielleicht",
]
