import asyncio
from sys import modules
from random import randint, random, choice
from datetime import datetime

from rich.live import Live
from rich.table import Table
from rich.text import Text
from rich.emoji import Emoji
from rich.align import Align

from faker import Faker

el = Element("live_div")
fake = Faker()

async def update_live(live: Live) -> None:
    console.warn("Update_live task started")
    while True:
        console.log("Updating")
        #live.update()
        el.write(live)
        console.log("Updated")
        await asyncio.sleep(.25)

def stop(task: asyncio.Task) ->None:
    task.cancel()
    console.warn(f"Task stopped: {task.get_name()}")

if not 'pyodide' in modules:
    from _livepatch import Pyscript_RefreshThread

table = Table()
table.add_column("Time", width=5)
table.add_column("Source", width=15)
table.add_column("Destination", width=15)
table.add_column("Protocol", width=8)
table.add_column("Info", width=9)

async def add_row(table: Table) -> None:
    while True:
        await asyncio.sleep(0.2 + random() * .7)  # arbitrary delay
        time = datetime.now().strftime('%S.%f')
        time = time[:min(len(time), 5)]
        source, dest = fake.ipv4(), fake.ipv4()
        protocol = choice(['URP', 'TCP', 'ARP', 'QUIC', 'STP'])
        info = Emoji.replace(f"Len :arrow_right: {(randint(16, 987))}")
        table.add_row(time, source, dest, protocol, info)
        console.log("Added row to table")

loop = pyscript.loop

update_task = loop.create_task(update_live(live = table))
update_task.set_name("update_live")
loop.call_later(5, stop, (update_task))

add_rows_task = loop.create_task(add_row(table = table))
add_rows_task.set_name("add_rows_task")
loop.call_later(5, stop, (add_rows_task))

await asyncio.sleep(6)
el.write(Align(Text.from_markup('[white on dark_green bold]Tasks Finished[/]'), align='center'), append=True)

""" try:
    loop.run_until_complete(asyncio.gather(update_task, add_rows_task))
except asyncio.CancelledError:
    pass """;