from pyodide.http import pyfetch
import asyncio

response = await pyfetch('https://jsonplaceholder.typicode.com/users/1')
data = await response.json()
print(f"{data= }")