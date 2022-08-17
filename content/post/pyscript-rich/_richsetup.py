from typing import Iterable
from rich import get_console
from rich.console import Console
from rich.segment import Segment
import rich.jupyter
from pyodide import JsException
from sys import stdout, modules

from js import console

#Per pyodide docs, determine if we're running inside pyodide at Runtime
def is_pyodide() -> bool:
    return "pyodide" in modules

c = get_console()
c.is_jupyter = is_pyodide #monkeypatch jupyter detection @propety

def display_pyscript(segments: Iterable[Segment], text: str) -> None:
    """Allow output of raw HTML within pyscript/pyodide"""
    html = rich.jupyter._render_segments(segments)
    stdout.write(html)

#patch jupyter display method to write processed HTML to stdout
rich.jupyter.display = display_pyscript 

#Overwrite print with Rich Jupyter print function
#print = rich.jupyter.print

from html import escape

stdout.flush = lambda: None

def new_print(*args, **kwargs):
    c = Console(record=True, force_jupyter=True)
    c.print(*args, **kwargs)
    result = c.export_html()
    #console.log(escape(result))
    #stdout.write(result)

print = new_print

class output_buffer():
    """ A (inefficient) buffer to capture stdout to a string """
    def __init__(self):
        self._internal_buffer = ''

    def write(self, value: any):
        if len(self._internal_buffer):
            self.internal_buffer += '<br>'
        self._internal_buffer += value

    def read(self):
        return self._internal_buffer

from contextlib import contextmanager

@contextmanager
def stdout_to_buffer(el:Element, append):
    """ A context manager to manage an output_buffer, writes to an Element on closure"""
    global stdout #sys.stdout
    _old_stdout = stdout
    stdout = output_buffer()
    try:
        yield stdout
    finally:
        el._write(stdout.read(), append)
        stdout = _old_stdout 

Element._write = Element.write

#Allow Element.write() to take an object from rich
def newWrite(self, value, append=False) -> None:
    con = get_console()
    """ A Monkeypatched version of Pyscript's Element.write(), auto-transforming Rich objects and rendering standard objects. """
    if isinstance(value, (str, Exception, JsException)):
        console.warn(f"Using newWrite() as passthrough on {str(value)[:min(30, len(str(value)))]}... with type {type(value)}")
        self._write(value, append)
    else:
        console.warn(f"Using newWrite() with Pretty interpretted on {str(value)[:min(30, len(str(value)))]}... with type {type(value)}")
        with stdout_to_buffer(self, append):
            con.print(value)

Element.write = newWrite