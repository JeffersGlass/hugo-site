"""
This example demonstrates a simple text highlighter.
"""

from rich.console import Console
from rich.highlighter import RegexHighlighter
from rich.theme import Theme

class EmailHighlighter(RegexHighlighter):
    """Apply style to anything that looks like an email."""

    base_style = "example."
    highlights = [r"(?P<email>[\w-]+@([\w-]+\.)+[\w-]+)"]


theme = Theme({"example.email": "bold magenta"})
c = Console(highlighter=EmailHighlighter(), theme=theme, force_jupyter=True)

c.print("Send funds to money@example.org")
