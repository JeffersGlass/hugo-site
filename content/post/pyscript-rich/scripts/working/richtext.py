#Basic Formatting
print("[italic]Italic Text[/italic]")
print("[bold]Bold Text[/bold]")
print("[yellow on default]Colorful Text[/]")
print("[default on cyan1]Background Text Colors[/]")
print("[white on red]Color [reverse]Reversed[/reverse] Text[/]")
print("[strike]Strikethru Text[/]")
print("[u]Underlined[/u]")
print(['Lists', 'get', 'pretty', 'printed', 1234, object()])
print({'Dictionaries':'Get', 'PrettyPrinted?':True, 'Number': 1234})
print("Links, like this link to [link=https://www.willmcgugan.com]William McGugan's blog[/link]!")
print("")

from rich.text import Text
text = Text("WOW! Text objects are powerful, as is the ")
text.stylize("bold", 0, 4)
text.append("append() method", style="underline")
print(text)

###

from rich.layout import Layout
from rich.text import Text
from rich.panel import Panel
from rich.align import Align

layout = Layout()

layout.split_column(
    Layout(name="upper"),
    Layout(name="lower")
)

layout["lower"].split_row(
    Layout(name="left"),
    Layout(name="right"),
)

layout['upper'].update(Panel(Align(Text("This is a big ole panel huh?", style="italic"), align="center", vertical="middle"), title="Big Window"))
layout['left'].update(Panel("[red]The lower right subpanel has no contents, so you'll see a placeholder over there >>> [/]", title="[red bold]WARNING[/]"))

print(layout)

