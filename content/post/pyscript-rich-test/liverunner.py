import asyncio
from rich import get_console
from rich.live import Live
from rich.panel import Panel

c = get_console()
el = Element("live")

while(True):
    with Live(my_text, auto_refresh=False) as live_panel:
        await asyncio.sleep(1)
        live_panel.update(my_text)
        console.log("Updated panel")