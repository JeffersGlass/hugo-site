from js import document, console, Uint8Array, window, File
from pyodide import create_proxy
import asyncio
import io

from PIL import Image, ImageFilter

async def _upload_change_and_show(e):
    #Get the first file from upload
    file_list = e.target.files
    first_item = file_list.item(0)

    #Get the data from the files arrayBuffer as an array of unsigned bytes
    array_buf = Uint8Array.new(await first_item.arrayBuffer())

    #BytesIO wants a bytes-like object, so convert to bytearray first
    bytes_list = bytearray(array_buf)
    my_bytes = io.BytesIO(bytes_list) 

    #Create PIL image from np array
    my_image = Image.open(my_bytes)

    #Log some of the image data for testing
    console.log(f"{my_image.format= } {my_image.width= } {my_image.height= }")

    # Now that we have the image loaded with PIL, we can use all the tools it makes available. 
    # "Emboss" the image, rotate 45 degrees, fill with dark green
    my_image = my_image.filter(ImageFilter.EMBOSS).rotate(45, expand=True, fillcolor=(0,100,50)).resize((300,300))

    #Convert Pillow object array back into File type that createObjectURL will take
    my_stream = io.BytesIO()
    my_image.save(my_stream, format="PNG")

    #Create a JS File object with our data and the proper mime type
    image_file = File.new([Uint8Array.new(my_stream.getvalue())], "new_image_file.png", {type: "image/png"})

    #Create new tag and insert into page
    new_image = document.createElement('img')
    new_image.src = window.URL.createObjectURL(image_file)
    document.getElementById("output_upload_pillow").appendChild(new_image)

# Run image processing code above whenever file is uploaded    
upload_file = create_proxy(_upload_change_and_show)
document.getElementById("file-upload-pillow").addEventListener("change", upload_file)