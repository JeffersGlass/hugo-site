from PIL import Image

from js import document, console, Uint8Array, window, File
from pyodide.http import pyfetch
import asyncio
import io
import numpy as np
from numpy import asarray

# Get an emoji image and fetch it:
emoji = "🚀"
emoji_code = "-".join(f"{ord(c):x}" for c in emoji).upper()
url = f"https://raw.githubusercontent.com/hfg-gmuend/openmoji/master/color/618x618/{emoji_code}.png"

async def get_emoji_bytes(url: str):
    response = await pyfetch(url)
    if response.status == 200:
        return await response.bytes()

#BytesIO wants a bytes-like object, so convert to bytearray first
bytes_list = bytearray(await get_emoji_bytes(url))
my_bytes = io.BytesIO(bytes_list) 

#Create PIL image from BytesIO 
my_original_image = Image.open(my_bytes)
my_image = Image.open(my_bytes)

#Convert to an np-array to allow for processing
my_array = np.array(my_image.convert()) # convert() is key, as these images use a pallete!!

# -------- Do image processing here ------

from skimage.transform import swirl
my_array = swirl(my_array, rotation = 0, strength = 15, radius = 300)

# -------- End image processing -----------

#convert back to Pillow image:
if my_array[row:= 0][column:= 0][red:= 0] < .99:
    # Many transforms represent RGB as floats in the range 0-1, which pillow does not like
    # This converts their values back to 0-255
    my_image = Image.fromarray((my_array*255).astype(np.uint8)) 
else:
    my_image = Image.fromarray(my_array)

#Export image from Pillow as bytes to get to Javascript
my_processed_stream = io.BytesIO()
my_image.save(my_processed_stream, format="PNG")

#Create a JS File object with our data and the proper mime type
processed_image_file = File.new([Uint8Array.new(my_processed_stream.getvalue())], "new_image_file.png", {type: "image/png"})
original_image_file = File.new([Uint8Array.new(my_bytes.getvalue())], "new_image_file.png", {type: "image/png"})

#Create new tags and insert into page
new_image = document.createElement('img')
new_image.src = window.URL.createObjectURL(processed_image_file)
document.getElementById("new_image").appendChild(new_image)

original_image = document.createElement('img')
original_image.classList.add("w-auto")
original_image.src = window.URL.createObjectURL(original_image_file)
document.getElementById("original_image").appendChild(original_image)

x=1