"""complexFractal module. Draws fractals from complex numbers.

Based on Pillow library, this module is used to draw fractals
calculated from complex numbers.

Classes:
    JuliaSet:
    MandelbrotSet:
    Viewport:
    Pixel:
"""

from PIL import Image

class JuliaSet:
    """Julia sets class.
    
    Julia sets are the sets of z_0 so that the sequence z_(n+1) = z_n^2 + c converges.
    Each different complex c leads to a different Julia set.
    
    Attributes
        c: constant caracterising Julia set.
        max_iterations: maximum number of iterations for considering sequence as convergent.
    """
    def __init__(self, c: complex, max_iterations: int):
        self.c = c
        self.max_iterations = max_iterations
    
    def __contains__(self, z_0: complex) -> bool:
        """Tells if a given z_0 is in Julia set set or not (in/not in override).
        """
        return self.stability(z_0) == 1
    
    def stability(self, z_0: complex) -> float:
        """Gives the stability of a given z_0.
        
        This function gives a normalized measurement of sequence divergence speed by dividing escape count by self.max_iterations.
        
        Parameters
            z_0: number to measure divergence speed.
        Return
            Normalized divergence measurement.
            0: most divergent point.
            1: most convergent point.
        """
        return self.escape_count(z_0) / self.max_iterations
    
    def escape_count(self, z_0: complex) -> int:
        """Gives the number of iterations before diverging.
        
        This function is used to measure divergence speed of the sequence by returning the escape count (number of iterations it takes
        to diverge). The sequence is considered as convergent if that number is equal to self.max_iterations.
        
        Parameters
            z_0: number to evaluate divergence.
        Return
            Number of iterations before diverging. 0 <= iteration <= self.max_iterations.
        """
        z = z_0
        for iteration in range(self.max_iterations):
            z = z ** 2 + self.c
            if abs(z) > 2:
                return iteration
        return self.max_iterations

class MandelbrotSet:
    """Mandelbrot sets class.
    
    Mandelbrot set is the set of c so that the sequence z_(n+1) = z_n^2 + c with z_0 = 0 converges.
    
    Attributes
        max_iterations: maximum number of iterations for considering sequence as convergent.
    """
    def __init__(self, max_iterations: int):
        self.max_iterations = max_iterations

    def __contains__(self, c: complex) -> bool:
        """Tells if a given c is in Mandelbrot set or not (in/not in override).
        """
        return self.stability(c) == 1

    def stability(self, c: complex) -> float:
        """Gives the stability of a given c.
        
        This function gives a normalized measurement of sequence divergence speed by dividing escape count by self.max_iterations.
        
        Parameters
            c: number to measure divergence speed.
        Return
            Normalized divergence measurement.
            0: most divergent point.
            1: most convergent point.
        """
        return self.escape_count(c) / self.max_iterations

    def escape_count(self, c: complex) -> int:
        """Gives number of iterations before diverging.
        
        This function is used to measure divergence speed of the sequence by returning the escape count (number of iterations it takes
        to diverge. The sequence is considered as convergent if that number is equal to self.max_iterations.
        
        Parameters
            c: number to evaluate divergence speed.
        Return
            iteration: number of iterations before diverging. 0 <= iteration <= self.max_iterations.
        """
        z = 0
        for iteration in range(self.max_iterations):
            z = z ** 2 + c
            if abs(z) > 2:
                return iteration
        return self.max_iterations

class Viewport:
    """Viewport class.
    
    Creates a smart image that handles zoom and center in complex plane.
    
    Attributes
        image: image to scale and translate.
        center: center of image in complex plane.
        zoom: zoom value (> 1: zoom in; < 1: zoom out)
    Properties
        height: height in pixels of viewport.
        width: width in pixels of viewport.
    """
    def __init__(self, image: Image.Image, center: complex = 0, zoom: float = 200):
        self.image = image
        self.center = center
        self.zoom = zoom

    @property
    def height(self) -> float:
        return self.image.height
    
    @property
    def width(self) -> float:
        return self.image.width

    def __iter__(self):
        for y in range(self.height):
            for x in range(self.width):
                yield Pixel(self, x, y)

class Pixel:
    """Pixels class.
    
    Creates a smart pixel that encapsulates conversion between coordinate system and complex numbers and handles color.
    
    Attributes
        viewport: viewport in which pixels are drawn.
        x: x coordinate.
        y: y coordinate.
    Properties
        color: color of the pixel.
    """
    def __init__(self, viewport: Viewport, x: int, y: int):
        self.viewport = viewport
        self.x = x
        self.y = y

    @property
    def color(self):
        return self.viewport.image.getpixel((self.x, self.y))

    @color.setter
    def color(self, value):
        self.viewport.image.putpixel((self.x, self.y), value)

    def __complex__(self):
        """Returns the complex value asssociated to the pixel according to zoom factor and center position.
        """
        return (
                (complex(self.x, -self.y) # reversing y axis orientation
                + complex(-self.viewport.width, self.viewport.height) / 2) # positioning at (0,0)
                / self.viewport.zoom  # applying zoom factor
                + self.viewport.center # translating to viewport.center
        )