from typing import Iterable
from sys import stdout, modules
from contextlib import contextmanager

from rich import get_console
from rich.console import _is_jupyter
from rich.segment import Segment
import rich.jupyter

from pyodide import JsException
from js import console

# Per pyodide docs, determine if we're running inside pyodide at Runtime
def is_pyodide() -> bool:
    return "pyodide" in modules
 
# Patch jupyter detection of the global _console object to detect pyodide
c = get_console()
c.is_jupyter = is_pyodide #monkeypatch jupyter detection @propety

# patch function so if user creates any additional Consoles they behave correctly
# While the global _console us
_is_jupyter = is_pyodide

# Jupyter display method renders html and writes to stdout
def display_pyscript(segments: Iterable[Segment], text: str) -> None:
    """Allow output of raw HTML within pyscript/pyodide"""
    html = rich.jupyter._render_segments(segments)
    stdout.write(html)

#patch jupyter display method to write processed HTML to stdout
rich.jupyter.display = display_pyscript 

print = get_console().print

# PyScripts OutputCTXManager is used for stdout but does not implement
# full fill interface; this prevents a warning each time console tries
# to print
stdout.flush = lambda: None

##---- Redefine Pyscript.write()---
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

    def flush(self):
        pass

@contextmanager
def stdout_to_buffer(el:Element, append: bool) -> None:
    """ A context manager to manage an output_buffer, writes to an Element on closure"""
    global stdout #Usually Pyscript OutputCTXManager at this pont
    _old_stdout = stdout
    stdout = output_buffer()
    try:
        yield
    finally:
        el._write(stdout.read(), append)
        stdout = _old_stdout 

Element._write = Element.write

#Allow Element.write() to take an object from rich
def newWrite(self, value, append: bool =False) -> None:
    """ A Monkeypatched version of Pyscript's Element.write(), auto-transforming Rich objects and rendering standard objects. """
    if isinstance(value, (str, Exception, JsException)):
        self._write(value, append)
    else:
        with stdout_to_buffer(self, append):
            get_console().print(value)

Element.write = newWrite