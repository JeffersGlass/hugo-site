from pyodide.http import pyfetch

_ = 'asyncio' #pyodide allows top-level await if 'asyncio' anywhere in code

response = await pyfetch('gooddog.jpg')
content = await response.bytes()
with open ('gooddog.jpg', 'wb') as f:
    f.write(content)