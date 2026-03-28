"""
RichInputHandlr — pecause nobody types exactly "Y" or "N".
Accepts human-flavored yes/no/maybe input and returns clean True/False/None.
"""

from .core import ask, RichInput
from .words import YES_WORDS, NO_WORDS, UNCERTAIN_WORDS

__all__ = ["ask", "RichInput", "YES_WORDS", "NO_WORDS", "UNCERTAIN_WORDS"]
__version__ = "1.0.0"
