import asyncio
from itertools import count

output_1 = Element("output-1")
for i in count():
    output_1.write(f"Counted to {i}")
    await asyncio.sleep(1)
