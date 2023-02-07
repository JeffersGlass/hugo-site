from js import createObject
from pyodide.ffi import create_proxy
createObject(create_proxy(globals()), "pyodideGlobals")