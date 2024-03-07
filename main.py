import matplotlib.pyplot as plt
import matplotlib as mpl
import fractal_display.complex_plane as cplxp
import fractal_display.complex_fractal as cplxf
from fractal_display.viewport import Viewport

def test10(): 
    mpl.rcParams['toolbar'] = 'None'
    
    fractal = cplxf.MandelbrotSet(256)
    viewport = Viewport(fractal, size = (1028,720), resolution = (1028,720), offset = (-0.7435,0.1314), zoom = 200000)
    image = viewport.img_grey()
    plt.imshow(image, cmap='binary')
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()
    
def test20():
    mpl.rcParams['toolbar'] = 'None'
    
    fractal = cplxf.JuliaSet(c=0.3+0.5j)
    viewport = Viewport(fractal, size = (4,3), resolution = (720,540), offset = (0,0), zoom = 1, colormap = 'plasma')
    image = viewport.img_rgb()
    plt.imshow(image, cmap='plasma')
    plt.axis("off")
    plt.tight_layout()
    plt.show()