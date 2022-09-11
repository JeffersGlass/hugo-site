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
