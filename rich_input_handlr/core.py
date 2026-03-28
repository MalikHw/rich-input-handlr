from __future__ import annotations

import random
from difflib import SequenceMatcher
from typing import Optional
import asyncio

from .words import YES_WORDS, NO_WORDS, UNCERTAIN_WORDS


def _similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


class RichInput:
    """
    The main configurable handler. Instantiate once, reuse everywhere.

    Args:
        uncertain_behavior: What to do on uncertain input.
            "random"  — 50/50 True/False (default)
            "none"    — always return None
            "prompt"  — re-ask the user (sync only)
        fuzzy_threshold: 0.0–1.0 similarity cutoff for fuzzy matching.
            Lower = more lenient. Default: 0.82
        extra_yes: Additional words/phrases to treat as YES.
        extra_no: Additional words/phrases to treat as NO.
        extra_uncertain: Additional words/phrases to treat as UNCERTAIN.
        prompt_suffix: Appended to the question when re-prompting. Default: " (yes/no): "
    """

    UNCERTAIN_BEHAVIORS = ("random", "none", "prompt")

    def __init__(
        self,
        uncertain_behavior: str = "random",
        fuzzy_threshold: float = 0.82,
        extra_yes: Optional[list[str]] = None,
        extra_no: Optional[list[str]] = None,
        extra_uncertain: Optional[list[str]] = None,
        prompt_suffix: str = " (yes/no): ",
    ):
        if uncertain_behavior not in self.UNCERTAIN_BEHAVIORS:
            raise ValueError(
                f"uncertain_behavior must be one of {self.UNCERTAIN_BEHAVIORS}, "
                f"got {uncertain_behavior!r}"
            )
        if not (0.0 <= fuzzy_threshold <= 1.0):
            raise ValueError("fuzzy_threshold must be between 0.0 and 1.0")

        self.uncertain_behavior = uncertain_behavior
        self.fuzzy_threshold = fuzzy_threshold
        self.prompt_suffix = prompt_suffix

        self._yes = [w.lower() for w in (YES_WORDS + (extra_yes or []))]
        self._no = [w.lower() for w in (NO_WORDS + (extra_no or []))]
        self._uncertain = [w.lower() for w in (UNCERTAIN_WORDS + (extra_uncertain or []))]

    # internal matching

    def _classify(self, raw: str) -> Optional[bool]:
        """
        Classify raw input as True (yes), False (no), or None (uncertain).
        Returns None for uncertain and for completely unrecognized input.
        """
        text = raw.strip().lower()

        # Exact match first (fast path)
        if text in self._yes:
            return True
        if text in self._no:
            return False
        if text in self._uncertain:
            return None

        # Fuzzy match — find best candidate across all lists
        best_score = 0.0
        best_result: Optional[bool] = None

        for word in self._yes:
            score = _similarity(text, word)
            if score > best_score:
                best_score = score
                best_result = True

        for word in self._no:
            score = _similarity(text, word)
            if score > best_score:
                best_score = score
                best_result = False

        for word in self._uncertain:
            score = _similarity(text, word)
            if score > best_score:
                best_score = score
                best_result = None

        if best_score >= self.fuzzy_threshold:
            return best_result

        # Completely unrecognized — treat as uncertain
        return None

    def _resolve_uncertain(self, question: str) -> Optional[bool]:
        """Apply uncertain_behavior policy."""
        if self.uncertain_behavior == "random":
            return random.choice([True, False])
        elif self.uncertain_behavior == "none":
            return None
        elif self.uncertain_behavior == "prompt":
            print(f"Couldn't understand that. Please answer yes or no.")
            new_raw = input(question + self.prompt_suffix)
            result = self._classify(new_raw)
            if result is None:
                # One retry, then fall back to None
                print("Still couldn't understand. Treating as no answer.")
                return None
            return result

    # public sync API

    def parse(self, raw: str) -> Optional[bool]:
        """
        Parse a pre-collected string. Useful when you handle input yourself.

        Returns:
            True  — yes
            False — no
            None  — uncertain / unresolved (based on uncertain_behavior="none")
                    or a random True/False (uncertain_behavior="random")
        """
        result = self._classify(raw)
        if result is None:
            return self._resolve_uncertain(raw)
        return result

    def ask(self, question: str) -> Optional[bool]:
        """
        Print a question, collect input(), classify it, return True/False/None.

        Args:
            question: The question to show the user (no suffix neded).

        Returns:
            True / False / None
        """
        raw = input(question + self.prompt_suffix)
        result = self._classify(raw)
        if result is None:
            return self._resolve_uncertain(question)
        return result

    # public async API

    async def ask_async(self, question: str) -> Optional[bool]:
        """
        Async version of ask(). Reads stdin in a thread pool so it doesn't
        block the event loop.

        Args:
            question: The question to show the user.

        Returns:
            True / False / None
        """
        loop = asyncio.get_event_loop()
        print(question + self.prompt_suffix, end="", flush=True)
        raw = await loop.run_in_executor(None, input)
        result = self._classify(raw)
        if result is None:
            if self.uncertain_behavior == "random":
                return random.choice([True, False])
            elif self.uncertain_behavior == "none":
                return None
            elif self.uncertain_behavior == "prompt":
                print("Couldn't understand that. Please answer yes or no.")
                print(question + self.prompt_suffix, end="", flush=True)
                raw2 = await loop.run_in_executor(None, input)
                result2 = self._classify(raw2)
                return result2  # None if still unclear
        return result

    async def parse_async(self, raw: str) -> Optional[bool]:
        """Async version of parse(). Useful in async pipelines."""
        result = self._classify(raw)
        if result is None:
            if self.uncertain_behavior == "random":
                return random.choice([True, False])
            return None
        return result

# module-level convenience function (uses default settings)

_default_handler = RichInput()


def ask(question: str) -> Optional[bool]:
    """
    Quick one-liner for simple use cases. Uses default RichInput settings.

    Example::

        from rich_input_handlr import ask

        if ask("Wanna download Miku songs?"):
            download()

    For custom behavior, instantiate RichInput() directly.
    """
    return _default_handler.ask(question)
