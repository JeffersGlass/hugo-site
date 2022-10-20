from datetime import datetime
import asyncio

async def clock_forever():
    while(True):
        now = datetime.now()
        Element('clock-output').write(f"{now.hour}:{now.minute:02}:{now.second:02}")
        await asyncio.sleep(1)

PyScript.loop.create_task(clock_forever())