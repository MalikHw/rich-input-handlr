"""
Tests for RichInputHandlr.
"""

import pytest
from rich_input_handlr.core import RichInput


@pytest.fixture
def handler():
    return RichInput(uncertain_behavior="none", fuzzy_threshold=0.82)


@pytest.mark.parametrize("word", [
    "yes", "y", "yeah", "yep", "yup", "sure", "absolutely",
    "hell yeah", "fuck yeah", "yass", "yasss", "yas",
    "ofc", "bet", "fr", "no cap", "lets go", "lesgo",
    "in", "im in", "count me in",
    "yesh", "yus", "oki", "okie",
    "si", "oui", "ja", "da",
])
def test_yes_words(handler, word):
    assert handler.parse(word) is True


def test_yes_case_insensitive(handler):
    assert handler.parse("YES") is True
    assert handler.parse("YeAh") is True
    assert handler.parse("HELL YEAH") is True

@pytest.mark.parametrize("word", [
    "no", "n", "nope", "nah", "nay", "never", "negative",
    "hell no", "fuck no", "hard pass", "pass",
    "nuh uh", "nuh-uh", "not a chance",
    "nein", "niet", "non",
    "L", "big L", "hard no",
])
def test_no_words(handler, word):
    assert handler.parse(word) is False


def test_no_case_insensitive(handler):
    assert handler.parse("NO") is False
    assert handler.parse("NOPE") is False
    assert handler.parse("Hell No") is False


@pytest.mark.parametrize("word", [
    "maybe", "idk", "dunno", "meh", "eh", "perhaps",
    "kinda", "sorta", "depends", "whatever", "idrc",
    "50/50", "flip a coin",
])
def test_uncertain_returns_none_when_behavior_is_none(handler, word):
    assert handler.parse(word) is None


def test_uncertain_random_returns_bool():
    h = RichInput(uncertain_behavior="random")
    results = {h.parse("idk") for _ in range(30)}
    # With 30 tries and 50/50 odds, we should almost certainly see both
    assert True in results
    assert False in results

@pytest.mark.parametrize("typo,expected", [
    ("yse", True),   # "yes" typo
    ("eys", True),
    ("noo", False),  # "no" typo
    ("nou", False),
    ("yep", True),   # not a typo but sanity check
])
def test_fuzzy_matching(typo, expected):
    h = RichInput(fuzzy_threshold=0.6)  # loosen for obvious typos
    assert h.parse(typo) is expected


def test_fuzzy_threshold_respected():
    h = RichInput(uncertain_behavior="none", fuzzy_threshold=0.99)
    assert h.parse("xzqwerty") is None



def test_extra_yes_words():
    h = RichInput(extra_yes=["affirmativo", "si senor"])
    assert h.parse("affirmativo") is True
    assert h.parse("si senor") is True


def test_extra_no_words():
    h = RichInput(extra_no=["negatorio", "no bueno"])
    assert h.parse("negatorio") is False
    assert h.parse("no bueno") is False


def test_extra_uncertain_words():
    h = RichInput(extra_uncertain=["on the fence", "coin toss"], uncertain_behavior="none")
    assert h.parse("on the fence") is None
    assert h.parse("coin toss") is None



def test_whitespace_stripped(handler):
    assert handler.parse("  yes  ") is True
    assert handler.parse("  no  ") is False


def test_completely_unrecognized_treated_as_uncertain(handler):
    assert handler.parse("xyzzy gobbledygook") is None


def test_invalid_uncertain_behavior():
    with pytest.raises(ValueError):
        RichInput(uncertain_behavior="yolo")


def test_invalid_fuzzy_threshold():
    with pytest.raises(ValueError):
        RichInput(fuzzy_threshold=1.5)


# synca

import asyncio

def test_parse_async_yes():
    h = RichInput()
    result = asyncio.run(h.parse_async("yes"))
    assert result is True

def test_parse_async_no():
    h = RichInput()
    result = asyncio.run(h.parse_async("nah"))
    assert result is False

def test_parse_async_uncertain_random():
    h = RichInput(uncertain_behavior="random")
    results = {asyncio.run(h.parse_async("idk")) for _ in range(20)}
    assert True in results or False in results  # at least one bool
