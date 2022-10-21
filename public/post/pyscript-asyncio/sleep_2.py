import asyncio
from itertools import count

output_2 = Element("output-2")
for i in count():
    output_2.write(f"Counted to {i}")
    await asyncio.sleep(.7) #Note the smaller sleep time!
