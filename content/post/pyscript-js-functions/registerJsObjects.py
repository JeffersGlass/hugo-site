import js
from pyodide import create_proxy, to_js

names = ["Jeff Glass"]
js.createObject(create_proxy(names), "names_js")

multiplier = lambda z: z * 2
js.createObject(create_proxy(multiplier), "multiplier_js")