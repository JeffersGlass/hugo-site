#Inspect Module
from rich import inspect
from rich.color import Color
color = Color.parse("red")
inspect(color, methods=True)

#Tables
from rich.table import Table
table = Table("First table using rich!")
table.add_column("Language", justify="right", style="bright_yellow", no_wrap=True)
table.add_column("Year Initially Released", style="green")
table.add_column("Most recent version", justify="right", style="red")
 
table.add_row("", "Python", "1991", "3.9.1")
table.add_row("", "R", "1993", "4.0.3")
table.add_row("", "Java", "1995", "Java 15")
 
print(table)