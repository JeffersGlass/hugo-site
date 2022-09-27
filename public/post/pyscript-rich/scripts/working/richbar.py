from rich.bar import Bar
from rich.jupyter import _render_segments
from asyncio import sleep

bar_div = Element("bar_div")

progress = 0.0

bar = Bar(size=1.0, begin = 0.0, end = progress)
c = get_console()

bar_div.write(bar)

while (True):
    for _ in range(100):
        await sleep(0.1)
        progress += 1
        bar.end = progress / 100
        bar_div.write(bar)
        bar_div.write(f"{round(progress)}% of bar is filled", append=True)
        
    progress = 0.0