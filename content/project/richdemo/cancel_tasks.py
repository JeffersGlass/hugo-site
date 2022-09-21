import asyncio
from operator import methodcaller

from js import console, createJSObject
from pyodide import create_proxy, webloop


async def cancel_tasks(*args):
    console.warn("Cancelling Async Tasks")
    for t in sorted(asyncio.all_tasks(), key=methodcaller('get_name')):
        console.warn(str(type(t)))
        console.warn(f"Cancelling {t.get_name()}")
        
        try:
            t.cancel()
            await t
        except asyncio.CancelledError:
            console.error(f"Task {t.get_name()} threw cancelled error in cancel_tasks")

createJSObject(create_proxy(cancel_tasks), "cancelTasks")