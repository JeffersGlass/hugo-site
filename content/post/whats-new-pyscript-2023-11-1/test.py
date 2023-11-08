from js import document, Uint8Array
from pyodide.ffi.wrappers import add_event_listener

import pandas as pd

async def storeFile(evt):
    file_list = evt.target.files
    first_item = file_list.item(0)

    #Get the data from the files arrayBuffer as an array of unsigned bytes
    array_buf = Uint8Array.new(await first_item.arrayBuffer())

    #IO wants a bytes-like object, so convert to bytearray first
    bytes_list = bytearray(array_buf)

    #Write the contents of the uploaded file to a file in the virtual FS that looks like "{id}.xls"
    file_name = evt.target.id + ".xls"
    with open(file_name, "wb") as f:
        f.write(bytes_list)

def calculate(*args):
    df = pd.read_excel("file-1.xls", index_col=0)
    df1 = pd.read_excel("file-2.xls", index_col=0)
    print(f"{df.size=}")
    print(f"{df1.size= }")

#Hook up event listeners to the inputs
add_event_listener(document.getElementById("file-1"), "change", storeFile)
add_event_listener(document.getElementById("file-2"), "change", storeFile)