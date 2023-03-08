from js import showDirectoryPicker, Object
from pyodide.ffi import to_js
import pyodide_js
import os

async def requestAndPrintFolder():
    modeObject = to_js({ "mode": "readwrite" }, dict_converter=Object.fromEntries)
    dirHandle = await showDirectoryPicker()
    if await dirHandle.queryPermission(modeObject) != "granted":
        if await dirHandle.requestPermission(modeObject) != "granted":
            raise Exception("Unable to read and write directory")
    nativefs = await pyodide_js.mountNativeFS("/mount_dir", dirHandle)
    
    print(os.listdir('/mount_dir'))