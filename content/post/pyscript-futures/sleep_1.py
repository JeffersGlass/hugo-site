import asyncio

output_1 = Element("output-1")
for i in range(20+1):
    output_1.write(f"Counted to {i}")
    await asyncio.sleep(1)
output_1.write("I did the counting, but slower!", append=True)
