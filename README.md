# rich-input-handlr

> Because nobody types exactly `Y` or `N`.

`rich-input-handlr` is a zero-dependency Python library that accepts **human-flavored yes/no input** and returns clean `True` / `False` / `None`. It understands slang, uwu-speak, profanity, typos, multilingual affirmatives, and the full chaotic spectrum of how people actually respond to prompts.

```
"You sure wanna download Miku songs? (yes/no): fuck yeah"
→ True
```

---

## Install

```bash
pip install rich-input-handlr
```

---

## Quick start

```python
from rich_input_handlr import ask

if ask("Wanna overwrite this file?"):
    overwrite()
else:
    print("Okay, skipping.")
```

That's it. `ask()` prints the question, reads input, and returns `True`, `False`, or `None`.

---

## What it understands

### YES → `True`
`yes`, `y`, `yeah`, `yep`, `yup`, `sure`, `absolutely`, `ofc`, `bet`, `fr`, `no cap`, `hell yeah`, `fuck yeah`, `yass`, `yas`, `lets go`, `lesgo`, `im in`, `yesh`, `yus`, `oki`, `si`, `oui`, `ja`, `da`, and many more.

### NO → `False`
`no`, `n`, `nope`, `nah`, `nay`, `never`, `negative`, `hell no`, `fuck no`, `hard pass`, `pass`, `nuh uh`, `not a chance`, `L`, `big L`, `nein`, `niet`, `non`, and many more.

### UNCERTAIN → `None` or random (configurable)
`idk`, `maybe`, `meh`, `eh`, `depends`, `kinda`, `sorta`, `whatever`, `idrc`, `50/50`, `dunno`, `perhaps`, `flip a coin`, and many more.

---

## Full configuration

For custom behavior, instantiate `RichInput` directly:

```python
from rich_input_handlr import RichInput

handler = RichInput(
    uncertain_behavior="random",   # "random" | "none" | "prompt"
    fuzzy_threshold=0.82,          # 0.0–1.0 — lower = more lenient typo matching
    extra_yes=["affirmativo"],     # your own YES words
    extra_no=["no bueno"],         # your own NO words
    extra_uncertain=["on the fence"],
    prompt_suffix=" (yes/no): ",   # what's appended to your question
)

result = handler.ask("Continue?")
```

### `uncertain_behavior` options

| Value | What happens on "idk" / "meh" / unrecognized input |
|---|---|
| `"random"` | Randomly returns `True` or `False` (50/50, default) |
| `"none"` | Always returns `None` |
| `"prompt"` | Re-asks the user once, then returns `None` if still unclear |

---

## Async support

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

## Parse without prompting

If you collect input yourself (e.g. from a GUI, a bot, a form):

```python
handler.parse("hell yeah")   # → True
handler.parse("nah fam")     # → False
handler.parse("idk man")     # → None or random, depending on uncertain_behavior
```

Async version:

```python
await handler.parse_async("yup")  # → True
```

---

## Fuzzy matching

Typos are handled via Python's built-in `difflib.SequenceMatcher`. The default threshold is `0.82` — tight enough to avoid false positives, loose enough to catch common fumbles like `"yse"`, `"noo"`, `"mabe"`.

Lower the threshold to be more lenient:

```python
handler = RichInput(fuzzy_threshold=0.65)
```

---

## Return values

| Situation | Returns |
|---|---|
| Recognized YES | `True` |
| Recognized NO | `False` |
| Uncertain / unrecognized + `uncertain_behavior="none"` | `None` |
| Uncertain / unrecognized + `uncertain_behavior="random"` | `True` or `False` |
| Uncertain / unrecognized + `uncertain_behavior="prompt"` | Re-asks; `None` if still unclear |

---

## Zero dependencies

`rich-input-handlr` uses only the Python standard library (`difflib`, `random`, `asyncio`). No installs needed beyond the package itself.

---

## License

MIT
