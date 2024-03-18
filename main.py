"""
This is an example of fractal display program launching.
"""

from fractal_display.gui import GUI


window = GUI()
window.title('Fractal display example') 
window.geometry("1000x600")

window.mainloop()
