from contextlib import contextmanager
import os
import sys

from pyscript import RUNNING_IN_WORKER
from pyodide.ffi import create_proxy
from pyscript import window, document

console = window.console
class xterm_stdout:
    def __init__(self, xterm):
        self.xterm = xterm

    def write(self, line):
        self.element.xterm.write(line)

@contextmanager
def output_redirect_to_xterm(id):
    import pyscript
    if RUNNING_IN_WORKER:
        raise EnvironmentError("output_redirect only works on the main thread for now?")
    
    _old_stdout = sys.stdout

    wrapper = document.getElementById(id)
    print("Wrapper", wrapper)
    if not hasattr(wrapper, "terminal"):
        wrapper.terminal = pyscript.js_modules.xterm.Terminal.new()
        wrapper.terminal.open(pyscript.document.getElementById("id"))

    sys.stdout = xterm_stdout(wrapper.terminal)
    try:
        yield
    finally:
        sys.stdout = _old_stdout

def get_input(id):
    local_file_path = f'./{id}-input.txt'
    if os.path.exists(local_file_path):
        with open(local_file_path) as fp:
            return fp.read()
    else:
        textId = f"{id}-textinput"
        console.log(f"Looking for value of #{textId}")
        obj = document.getElementById(f"{id}-textinput")
        console.log(obj)
        val = document.getElementById(f"{id}-textinput").value
        if val is not None: return val
        else:
            console.warn(f"No input found for id {id}")

async def file_upload(event):
    file_list = event.target.files
    src = event.srcElement.id.split("-")[0]
    local_file_name = src + "-input.txt"
    for uploaded_file in file_list:
        console.log("Saving " + uploaded_file.name + "to " + local_file_name)
        data = await uploaded_file.arrayBuffer()
        with open(local_file_name, 'wb') as local_file:
            local_file.write(data.to_py())

def attach_upload_listener(id):
    document.getElementById(id).addEventListener("change", create_proxy(file_upload))