import html
from functools import partial
from uuid import uuid4

from js import document, console, createObject, Alpine, Event
from pyodide import create_proxy, to_js

initialGlobals = create_proxy(set(globals()))

createObject(initialGlobals, "initialGlobals")

g = create_proxy(globals())

createObject(g, "pythonGlobals")

#console.log(to_js(dir(g)))

ready = Event.new('pyscriptGlobalsReady')
console.warn("Dispatching ready event")
document.dispatchEvent(ready);