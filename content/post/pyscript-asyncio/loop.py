import asyncio
async def add_slowly():
    Element("out").write("One plus two is... wait for it...")
    await asyncio.sleep(1)
    Element("out").write(1+2, append=True)

await add_slowly()