from random import choice, randint
import string
from js import document
from pyodide import create_proxy, to_js

def makePythonObject(*args, **kwargs):
    name = ''.join([choice(string.ascii_lowercase) for _ in range(5)])
    value = randint(0, 100)
    exec_string = f"global {name}\n{name} = {value}"
    exec(exec_string)

document.getElementById("makeObject").addEventListener("click", create_proxy(makePythonObject))