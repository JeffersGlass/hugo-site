import asyncio
from contextlib import suppress

async def print_A():    
    for i in range(5):
        print(f"A{i}")
        await asyncio.sleep(1)

async def print_B():
    for i in range(5):
        print(f"B{i}")
        await asyncio.sleep(1)

async def runner():
    print("Starting runner")
    async with trio.open_nursery() as nursery:
        nursery.start_soon(print_A)
        nursery.start_soon(print_B)
        print("Waiting for children to finish")
    print("Runner is done")

trio.run(runner)