import asyncio
from js import document, console
from pyodide import create_proxy

my_time = 0
seconds_element = document.getElementById("seconds")
duration_slider = document.getElementById("duration-slider")
progress_bar = document.getElementById("progress-bar")

def _reset_time(*args, **kwargs):
    console.log("Time reset")
    global my_time
    my_time = 0

reset_time = create_proxy(_reset_time)
document.getElementById("reset").addEventListener("click", reset_time)

while True:
    await asyncio.sleep(.1)
    my_time = round(my_time + .1, 2)
    seconds_element.innerText = str(my_time) + " Seconds"

    min_time = int(duration_slider.min)
    max_time = int(duration_slider.value)

    min_bar = 0
    max_bar = int(progress_bar.max)

    progress_bar.value = ((my_time + 1) - min_time) * (max_bar - 0) / (max_time - min_time + .01)