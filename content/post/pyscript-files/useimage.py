from js import File, window, document
from pyodide import to_js

with open("gooddog.jpg", "rb") as infile:
    image_file = File.new([to_js(infile.read())], "gooddog.jpg", {"type": "image/jpeg"})

image_file_url = window.URL.createObjectURL(image_file)

tag = document.getElementById("my-img-tag")
print(f"Img alt is originally: '{tag.alt}'")

tag.src = image_file_url
tag.alt = "Winnie the Dog in Color"

print(f"Img source set to {tag.src}")
print(f"Img alt set to: '{tag.alt}'")