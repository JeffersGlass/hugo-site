"""Same as the table_movie.py but uses Live to update"""
import asyncio
import time
from contextlib import asynccontextmanager

from rich import box, get_console
from rich.align import Align
from rich.console import Console
#from rich.live import Live
from rich.table import Table
from rich.text import Text
import asyncio

TABLE_DATA = [
    [
        "May 25, 1977",
        "Star Wars Ep. [b]IV[/]: [i]A New Hope",
        "$11,000,000",
        "$1,554,475",
        "$775,398,007",
    ],
    [
        "May 21, 1980",
        "Star Wars Ep. [b]V[/]: [i]The Empire Strikes Back",
        "$23,000,000",
        "$4,910,483",
        "$547,969,004",
    ],
    [
        "May 25, 1983",
        "Star Wars Ep. [b]VI[/b]: [i]Return of the Jedi",
        "$32,500,000",
        "$23,019,618",
        "$475,106,177",
    ],
    [
        "May 19, 1999",
        "Star Wars Ep. [b]I[/b]: [i]The phantom Menace",
        "$115,000,000",
        "$64,810,870",
        "$1,027,044,677",
    ],
    [
        "May 16, 2002",
        "Star Wars Ep. [b]II[/b]: [i]Attack of the Clones",
        "$115,000,000",
        "$80,027,814",
        "$656,695,615",
    ],
    [
        "May 19, 2005",
        "Star Wars Ep. [b]III[/b]: [i]Revenge of the Sith",
        "$115,500,000",
        "$380,270,577",
        "$848,998,877",
    ],
]

#console = Console()
c = get_console()

BEAT_TIME = 0.04
#BEAT_TIME = 0.4


@asynccontextmanager
async def beat(length: int = 1) -> None:
    try:
        yield
    finally:
        await asyncio.sleep(length * BEAT_TIME)


table = Table(show_footer=False)
table_centered = Align.center(table)

with Live(table_centered, "live-div", refresh_per_second=20):
    async with beat(10):
        table.add_column("Release Date", no_wrap=True)

    async with beat(10):
        table.add_column("Title", Text.from_markup("[b]Total", justify="right"))

    async with beat(10):
        table.add_column("Budget", "[u]$412,000,000", no_wrap=True)

    async with beat(10):
        table.add_column("Opening Weekend", "[u]$577,703,455", no_wrap=True)

    async with beat(10):
        table.add_column("Box Office", "[u]$4,331,212,357", no_wrap=True)

    async with beat(10):
        table.title = "Star Wars Box Office"

    async with beat(10):
        table.title = (
            "[not italic]:popcorn:[/] Star Wars Box Office [not italic]:popcorn:[/]"
        )

    async with beat(10):
        table.caption = "Made with Rich"

    async with beat(10):
        table.caption = "Made with [b]Rich[/b]"

    async with beat(10):
        table.caption = "Made with [b magenta not dim]Rich[/]"

    for row in TABLE_DATA:
        async with beat(10):
            table.add_row(*row)

    async with beat(10):
        table.show_footer = True

    table_width = c.measure(table).maximum

    async with beat(10):
        table.columns[2].justify = "right"

    async with beat(10):
        table.columns[3].justify = "right"

    async with beat(10):
        table.columns[4].justify = "right"

    async with beat(10):
        table.columns[2].header_style = "bold red"

    async with beat(10):
        table.columns[3].header_style = "bold green"

    async with beat(10):
        table.columns[4].header_style = "bold blue"

    async with beat(10):
        table.columns[2].style = "red"

    async with beat(10):
        table.columns[3].style = "green"

    async with beat(10):
        table.columns[4].style = "blue"

    async with beat(10):
        table.columns[0].style = "cyan"
        table.columns[0].header_style = "bold cyan"

    async with beat(10):
        table.columns[1].style = "magenta"
        table.columns[1].header_style = "bold magenta"

    async with beat(10):
        table.columns[2].footer_style = "bright_red"

    async with beat(10):
        table.columns[3].footer_style = "bright_green"

    async with beat(10):
        table.columns[4].footer_style = "bright_blue"

    async with beat(10):
        table.row_styles = ["none", "dim"]

    async with beat(10):
        #table.border_style = "bright_yellow"
        table.border_style = "yellow"

    for box_style in [
        box.SQUARE,
        box.MINIMAL,
        box.SIMPLE,
        box.SIMPLE_HEAD,
    ]:
        async with beat(10):
            table.box = box_style

    async with beat(10):
        table.pad_edge = False

    original_width = c.measure(table).maximum

    for width in range(original_width, c.width, 2):
        async with beat(10):
            table.width = width

    for width in range(c.width, original_width, -2):
        async with beat(10):
            table.width = width

    for width in range(original_width, 90, -2):
        async with beat(10):
            table.width = width

    for width in range(90, original_width + 1, 2):
        async with beat(10):
            table.width = width

    async with beat(20):
        table.width = None

from rich.panel import Panel

print(Text.from_markup("[red]DONE![/]"))