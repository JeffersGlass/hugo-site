from rich.text import Text

el = Element("output-container")

text = Text.from_markup("[red bold]Rich objects[/] can be output with [i]Element.write()[/i]")
el.write(text, append=True)

data = {"Question": "What about standard Python Objects?", "Answers": ["Yes!", "They Can!", "How neat!"]}
el.write(data, append=True)


