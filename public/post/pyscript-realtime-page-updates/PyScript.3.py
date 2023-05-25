from js import document
from asyncio import sleep

async def count():
    for i in range(100):
        print(i)
        display(i, target="myDiv", append=False)
        await sleep(0.01)
        for j in range(1_000_000):
            _ = 1

fut = asyncio.ensure_future(count())