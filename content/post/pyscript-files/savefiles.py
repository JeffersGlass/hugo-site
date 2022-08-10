from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.cell(txt="hello world")
pdf.output("document.pdf")
print("Created and saved PDF as document.pdf")

import matplotlib.pyplot as plt
plt.plot([1,2,3,4,10])
plt.savefig('graph.png')
print("Created and saved matplotlib plot as graph.png")

from PIL import Image
with open("gooddog.jpg") as picture:
    image = Image.open("./gooddog.jpg")
image.save("gooddog.jpg", "JPEG")
print("Loaded image from server and saved as gooddog.jpg")