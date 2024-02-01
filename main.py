from PIL import Image, ImageTk
import tkinter as tk
from complexFractal import *
import matplotlib.cm


def denormalize(palette):
    return [
        tuple(int(channel * 255) for channel in color)
        for color in palette
    ]


fractal = MandelbrotSet(max_iterations=256)

image = Image.new(mode="RGB", size=(720, 512))

colormap = matplotlib.cm.get_cmap("twilight").colors
palette = denormalize(colormap)

for pixel in Viewport(image, center=-0.7435 + 0.1314j, zoom=200000):
    stability = fractal.stability(complex(pixel))
    index = int(min(stability * len(palette), len(palette) - 1))
    pixel.color = palette[index % len(palette)]

root = tk.Tk()
image = ImageTk.PhotoImage(image)
label = tk.Label(root, image=image)
label.pack(expand = True, fill = tk.BOTH)
root.mainloop()