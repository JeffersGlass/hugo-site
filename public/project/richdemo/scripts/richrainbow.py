"""

This example demonstrates how to write a custom highlighter.

"""

from random import randint

from rich import print
from rich.highlighter import Highlighter
from rich.style import Style


class RainbowHighlighter(Highlighter):
    def highlight(self, text):
        for index in range(len(text)):
            text.stylize(f"color({randint(16, 255)})", index, index + 1)
        text.stylize(Style(bgcolor='grey27'))



rainbow = RainbowHighlighter()
print(rainbow("I must not fear. Fear is the mind-killer."))
