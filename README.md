# rich-input-handlr

> Because nobody types exactly `Y` or `N`.

![PyPI version](https://img.shields.io/pypi/v/rich-input-handlr?color=blueviolet&style=flat-square)
![Python versions](https://img.shields.io/pypi/pyversions/rich-input-handlr?style=flat-square)
![License: GPLv3](https://img.shields.io/badge/license-GPLv3-blue?style=flat-square)
![Zero dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen?style=flat-square)
![Tests](https://img.shields.io/badge/tests-81%20passing-brightgreen?style=flat-square)

a Python lib that accepts **human-flavored yes/no input** and gives you back a clean `True` / `False` / `None`. understands slang, uwu-speak, profanity, typos, multilingual stuff, and the full spectrum of how people actually answer shit.

```
"You sure wanna download Miku songs? (yes/no): fuck yeah"
→ True
```

---

## install

```bash
pip install rich-input-handlr
```

---

## quick start

```python
from rich_input_handlr import ask

if ask("Wanna overwrite this file?"):
    overwrite()
else:
    print("okay skipping lol")
```

that's literally it. `ask()` prints your question, reads input, returns `True`, `False`, or `None`. no more babysitting users who can't type a capital Y.

---

## what it understands

### YES → `True`
`yes`, `y`, `yeah`, `yep`, `yup`, `sure`, `absolutely`, `ofc`, `bet`, `fr`, `no cap`, `hell yeah`, `fuck yeah`, `yass`, `yas`, `lets go`, `lesgo`, `im in`, `yesh`, `yus`, `oki`, `si`, `oui`, `ja`, `da`, and like 50 more

### NO → `False`
`no`, `n`, `nope`, `nah`, `nay`, `never`, `negative`, `hell no`, `fuck no`, `hard pass`, `pass`, `nuh uh`, `not a chance`, `L`, `big L`, `nein`, `niet`, `non`, and like 50 more

### UNCERTAIN → `None` or random (your call)
`idk`, `maybe`, `meh`, `eh`, `depends`, `kinda`, `sorta`, `whatever`, `idrc`, `50/50`, `dunno`, `perhaps`, `flip a coin`, and more

---

## full config

wanna customize stuff? instantiate `RichInput` directly:

```python
from rich_input_handlr import RichInput

handler = RichInput(
    uncertain_behavior="random",   # "random" | "none" | "prompt"
    fuzzy_threshold=0.82,          # 0.0–1.0 — lower = more lenient with typos
    extra_yes=["affirmativo"],     # add your own YES words
    extra_no=["no bueno"],         # add your own NO words
    extra_uncertain=["on the fence"],
    prompt_suffix=" (yes/no): ",   # appended to your question
)

result = handler.ask("Continue?")
```

### `uncertain_behavior` options

| value | what happens on "idk" / "meh" / unrecognized input |
|---|---|
| `"random"` | randomly returns `True` or `False` (50/50, default) |
| `"none"` | always returns `None`, you deal with it |
| `"prompt"` | re-asks the user once, then gives up and returns `None` |

---

## async support

yep it's async-ready too

```python
import asyncio
from rich_input_handlr import RichInput

handler = RichInput()

async def main():
    result = await handler.ask_async("Proceed?")
    print(result)

asyncio.run(main())
```

---

## parse without prompting

already have the input from somewhere else (a bot, a GUI, whatever)? skip the prompt:

```python
handler.parse("hell yeah")   # → True
handler.parse("nah fam")     # → False
handler.parse("idk man")     # → None or random, depends on your uncertain_behavior
```

async version:

```python
await handler.parse_async("yup")  # → True
```

---

## fuzzy matching

typos handled via Python's built-in `difflib.SequenceMatcher`. default threshold is `0.82` — catches stuff like `"yse"`, `"noo"`, `"mabe"` without going too crazy with false positives.

loosen it up if you want:

```python
handler = RichInput(fuzzy_threshold=0.65)  # more lenient
```

---

## return values

| situation | returns |
|---|---|
| recognized YES | `True` |
| recognized NO | `False` |
| uncertain/unrecognized + `uncertain_behavior="none"` | `None` |
| uncertain/unrecognized + `uncertain_behavior="random"` | `True` or `False` |
| uncertain/unrecognized + `uncertain_behavior="prompt"` | re-asks; `None` if still unclear |

---

## zero dependencies

pure stdlib only — `difflib`, `random`, `asyncio`. nothing to install, nothing to break, nothing to audit.

---

## license

[GPL-3.0](./LICENSE)

### [Youtube Channel](https://www.youtube.com/@MalikHw47) - [Donate](https://MalikHw.github.io/donate) - ...nothing else thx for using
