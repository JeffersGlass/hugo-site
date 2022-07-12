from rich.panel import Panel
from rich.text import Text
from faker import Faker

text = Text("Panels add borders to content, and can add titles", justify="center")
panel = Panel(text, title="Panel Title", subtitle = "Panel Subtitle")
print(panel)