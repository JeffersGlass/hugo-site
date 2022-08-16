from rich.layout import Layout
from rich.text import Text
from rich.panel import Panel
from rich.align import Align
from rich.live import Live
from datetime import datetime
import asyncio
from random import randint

my_text = Text(f'The current time is {datetime.now().strftime("%A %B %d, %I:%M:%S.%f%p"):}')
my_text.stylize('bold', 20)

#panel = Panel(my_text)
print(my_text)

with Live() as live_panel:
    asyncio.sleep(randint(1, 4))
    my_text = Text(f'The current time is {datetime.now().strftime("%A %B %d, %I:%M:%S.%f%p"):}')
