from pyodide import to_js
from js import File

with open("document.pdf", 'rb') as infile:
    data = infile.read()
    file_object = File.new([to_js(data)], "document.pdf", {type: "image/png"})
    print(f"Loaded file '{file_object.name}' of size {file_object.size} bytes")