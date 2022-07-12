from rich.progress_bar import ProgressBar
from rich.jupyter import _render_segments
from asyncio import sleep
from random import random

progress_bar_div = Element("progress_bar_div")

p_progress = 0.0

progress_bar = ProgressBar(total=100.0, completed = 0.0)
c = get_console()

#progress_bar_div.write(_render_segments(bar.__rich_console__(c, c.options)), append=False)
progress_bar_div.write(progress_bar, append=False)
await sleep(1)

while (True):
    await sleep(random()*1.1 + 0.3)
    p_progress += random() * 9 + 1
    progress_bar.completed = p_progress
    progress_bar_div.write(progress_bar, append=False)
    progress_bar_div.write(f"{round(p_progress)}% of bar is filled", append=True)

    if p_progress >= 100.0:
        p_progress = 100.0
        progress_bar_div.write(progress_bar, append=False)
        progress_bar_div.write(f"100% of bar is filled, bar will reset itself soon", append=True)

        await sleep(3)
        p_progress = 0.0
