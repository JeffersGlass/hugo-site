from rich.console import Group
from rich.panel import Panel

panel_group = Group(
    Panel("Hello", style="on cyan1"),
    Panel("World", style="white on red"),
)
print(Panel(panel_group))
