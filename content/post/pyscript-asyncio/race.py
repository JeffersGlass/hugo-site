import asyncio
from functools import partial
import random

from pyodide.ffi.wrappers import add_event_listener
from js import document

async def racer(lane_element):
    speed = random.random() + .3
    lane_element.value = 0
    while lane_element.value < 100:
        lane_element.value += speed
        await asyncio.sleep(.1)
    lane_element.classList.remove('border-yellow-700')
    lane_element.classList.add('border-green-500')
    

NUM_RACERS = 5

racers = []

for n in range(NUM_RACERS):
    new_lane = document.createElement("progress")
    new_lane.id = f"lane-{n}"
    new_lane.max = 100
    new_lane.classList.add('border-4', 'border-yellow-500', 'm-2', 'h-6', 'w-full')
    

    new_lane_label = document.createElement("label")
    setattr(new_lane_label, "for", f"lane-{n}")
    new_lane_label.innerText = f"Lane {n}"

    document.getElementById("race-output").appendChild(new_lane_label)
    document.getElementById("race-output").appendChild(new_lane)

    racers.append(racer(new_lane))

asyncio.gather(*racers)