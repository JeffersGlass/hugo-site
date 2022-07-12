from rich import get_console
import rich.jupyter

from sys import stdout, modules

#Per pyodide docs, determine if we're running inside pyodide at Runtime
def is_pyodide() -> bool:
    return "pyodide" in modules

c = get_console()
c.is_jupyter = is_pyodide #monkeypatch jupyter detection @propety

def display_pyscript(segments, text: str) -> None:
    """Allow output of raw HTML within pyscript/pyodide"""
    html = rich.jupyter._render_segments(segments)
    stdout.write(html)

#monkeypatch jupyter display method to write processed HTML to stdout
rich.jupyter.display = display_pyscript 
print = rich.jupyter.print

#Allow Element.write() to take an object from rich
def newWrite(self, value, append=False):
    if hasattr(value, '__rich_console__'):
        #console.error(f"Using newWrite() __rich_console__ on {str(value)[:min(30, len(str(value)))]}...")
        self._write(rich.jupyter._render_segments(value.__rich_console__(c, c.options)), append)
        return
    elif hasattr(value, '__rich__'):
        #console.error(f"Using newWrite() __rich__ on {str(value)[:min(30, len(str(value)))]}...")
        self._write(rich.jupyter._render_segments(value.__rich__(c, c.options)), append)
    else:
        #console.error(f"Using newWrite() as passthrough on {str(value)[:min(30, len(str(value)))]}...")
        self._write(value, append)

setattr(Element, '_write', Element.write)
setattr(Element, 'write', newWrite)