import os

from pyodide.ffi import create_proxy
from js import console, document

def get_input(id):
    local_file_path = f'./{id}-input.txt'
    if os.path.exists(local_file_path):
        with open(local_file_path) as fp:
            return fp.read()
    else:
        textId = f"{id}-textinput"
        console.log(f"Looking for value of #{textId}")
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