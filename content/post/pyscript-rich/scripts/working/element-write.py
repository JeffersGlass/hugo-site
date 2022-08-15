from rich.text import Text

el = Element("write-to-me")

text = Text.from_markup("[red bold]Rich objects[/] can be output with [i]Element.write()[/i]")
el.write(text, append=True)

data = {"Question": "Can standard Python Objects?", "Answers": ["Yes!", "They Can!", "How neat!"]}
el.write(data, append=True)


