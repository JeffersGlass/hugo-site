import asyncio
async def add_slowly():
    Element("out").write("One plus two is... wait for it...")
    await asyncio.sleep(5)
    Element("out").write(1+2, append=True)

#This isn't normally possible:
await add_slowly()