from pyodide.http import pyfetch
import asyncio
from js import document

await_output = Element("await-output")

endpoint = "https://jsonplaceholder.typicode.com/posts/1"
ms_delay = "3000"
delayed_endpoint = f"https://deelay.me/{ms_delay}/{endpoint}"

await_output.write("Starting to fetch results (await):", append=True)
await_result = await pyfetch(delayed_endpoint)
await_j = await await_result.json()
await_output.write("This will not print until results are in", append=True)
await_output.write(f"Results are: {await_j}", append=True)