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