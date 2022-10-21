import asyncio
from functools import partial
import random

from pyodide.ffi.wrappers import add_event_listener
from js import document

#Our awaitable coroutine - we'll use asyncio.gather() to run lots of these
async def racer(lane_element):
    speed = random.random() + .4
    lane_element.value = 0
    while lane_element.value < 100:
        lane_element.value += speed
        await asyncio.sleep(.1)
    
    #race is over for this lane; change border color
    lane_element.classList.remove('border-yellow-700')
    lane_element.classList.add('border-green-500')
    

NUM_RACERS = 5

def run_race():
    racers = []

    #clear output
    output = document.getElementById('race-output')
    while output.firstChild:
        output.removeChild(output.firstChild)

    for n in range(NUM_RACERS):
        #Create new progress bars as lanes for our "racers"
        new_lane = document.createElement("progress")
        new_lane.id = f"lane-{n}"
        new_lane.max = 100
        new_lane.classList.add('border-4', 'border-yellow-500', 'm-2', 'h-6', 'w-11/12')
        

        #Add the progress bars and labels to the document
        document.getElementById("race-output").appendChild(new_lane)

        racers.append(racer(new_lane))

    # Return a Promise representing the results.
    # If you don't need the results, no need to return or await this
    return asyncio.gather(*racers)

#Run the race over and over
async def race_monitor():
    while True:
        results = run_race()
        await results
        await asyncio.sleep(1)

#Start the monitoring task
asyncio.create_task(race_monitor())