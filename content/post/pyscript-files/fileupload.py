from distutils.command.upload import upload
from pyodide import create_proxy
from js import console, document

async def file_upload(event):
    file_list = event.target.files
    for uploaded_file in file_list:
        console.log("Saving " + uploaded_file.name)
        data = await uploaded_file.arrayBuffer()
        with open('gooddog.jpg', 'wb') as local_file:
            local_file.write(data.to_py())

document.getElementById("id="file_upload"").addEventListener("change", create_proxy(file_upload))