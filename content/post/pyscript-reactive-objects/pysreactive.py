import html
from functools import partial
from uuid import uuid4

from js import document, console, createObject, Alpine
from pyodide import create_proxy, to_js

initial_globals = set(globals())

createObject(initial_globals, "initial_globals")

createObject(globals(), "pythonGlobals")

console.log("CREATED PYTHON GLOBALS")

from js import pythonGlobals

Alpine.data('pythonGlobals', pythonGlobals)