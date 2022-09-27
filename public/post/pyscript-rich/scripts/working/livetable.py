import asyncio
from collections import deque
from random import random, choice, randint
from rich.table import Table
from rich.emoji import Emoji
from datetime import datetime
from faker import Faker
#from livepatch import Live

fake = Faker()

while (True):
    table = Table(width = 80)
    table.add_column("Time", width=5)
    table.add_column("Source", width=15)
    table.add_column("Destination", width=15)

    max_rows = randint(6,10)
    num_rows = 0

    while num_rows <= max_rows:
        with Live(table, "live-table-output"):
            await asyncio.sleep(.3 + random() * .6)
            num_rows += 1

            time = datetime.now().strftime('%S.%f')
            time = time[:min(len(time), 5)]
            source, dest = fake.ipv4(), fake.ipv4()

            #data added here is automatically visible in the Table
            table.add_row(time, source, dest)         