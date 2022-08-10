from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.cell(txt="hello world")
pdf.output("document.pdf")

import matplotlib.pyplot as plt
plt.plot([1,2,3,4,10])
plt.savefig('graph.png')

from PIL import Image
image = Image.new('RGB', (240, 120), (150,255,200))
image.save("green.png", "PNG")