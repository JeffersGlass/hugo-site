from js import createObject
from pyodide import create_proxy
createObject(create_proxy(globals()), "pyodideGlobals")