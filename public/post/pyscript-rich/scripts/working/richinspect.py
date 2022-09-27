#Inspect Module
from rich import inspect
from rich.color import Color
color = Color.parse("red")
inspect(color, methods=True)