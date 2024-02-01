from PIL import Image, ImageTk
import tkinter as tk
from complexFractal import *

mandelbrot_set = MandelbrotSet(max_iterations=20)

image = Image.new(mode="L", size=(720, 512))
for pixel in Viewport(image, center=-0.75, zoom=200):
    z_0 = complex(pixel)
    pixel.color = int(255 - mandelbrot_set.stability(z_0) * 255)

root = tk.Tk()
image = ImageTk.PhotoImage(image)
label = tk.Label(root, image=image)
label.pack(expand = True, fill = tk.BOTH)
root.mainloop()