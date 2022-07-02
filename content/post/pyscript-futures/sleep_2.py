import asyncio

output_2 = Element("output-2")
for i in range(20+1):
    output_2.write(f"Counted to {i}")
    await asyncio.sleep(.7) #Note the smaller sleep time!
output_2.write("I did the counting,!", append=True)
