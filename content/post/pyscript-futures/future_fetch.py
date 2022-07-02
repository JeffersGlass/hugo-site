import itertools
import asyncio

from pyodide.http import pyfetch

future_div = Element("future-output")

endpoint = "https://jsonplaceholder.typicode.com/posts/2"
ms_delay = "7000"
delayed_endpoint = f"https://deelay.me/{ms_delay}/{endpoint}"

future_div.write("Starting to fetch results (future):", append=True)

async def fetch_it():
    result = await pyfetch(delayed_endpoint)
    j = await result.json()
    return j

def print_results(result):
    future_div.write(f"Results are: {result}", append=True)

future_result = pyscript.loop.create_task(fetch_it())
future_result.add_done_callback(print_results)
future_div.write("This will output before results are in!", append=True)

for num in itertools.count(start = 1):
    await asyncio.sleep(1)
    if isinstance(future_result, asyncio.Task) and not future_result.done(): future_div.write(f"We've waited {num} seconds for the result", append=True)
    else: break