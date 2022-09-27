import asyncio
from random import random, choice, randint
from rich.table import Table
from rich.emoji import Emoji
from datetime import datetime
from faker import Faker
#from livepatch import Live

fake = Faker()

print('[i]Source (Partial)[/]')

from rich.syntax import Syntax

syntax = Syntax.from_path('liverunner.py', padding=1, line_range=(18, None), line_numbers=True)
print(syntax)

table = Table(width = 80)
table.add_column("Time", width=5)
table.add_column("Source", width=15)
table.add_column("Destination", width=15)

with Live(table, "output-container"):
    for _ in range(12):
        await asyncio.sleep(.4 + random() * .7)
        time = datetime.now().strftime('%S.%f')
        time = time[:min(len(time), 5)]
        source, dest = fake.ipv4(), fake.ipv4()
        table.add_row(time, source, dest)