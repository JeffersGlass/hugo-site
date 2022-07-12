from rich import get_console
from rich.traceback import install

install(show_locals = True)

try:
    x = 1/0
except Exception:
    get_console().print_exception(show_locals=True)