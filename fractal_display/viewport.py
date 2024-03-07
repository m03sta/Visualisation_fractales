"""viewport module.

Classes
    Viewport
"""

from . import complex_fractal as cplxf # Fractal()
from . import complex_plane as cplxp # Plane()
import numpy as np # np arrays
import matplotlib.cm as mplcm # get_cmap
import matplotlib.pyplot as plt # colormaps()


class Viewport:
    """Viewport class.

    Encapsulates concept of a window through which an image can be observed
    with given zoom, size, resolution and offset parameters.
    In concrete terms, Viewport class sticks a fractal to a complex plane 
    and creates an image of the fractal in the complex plane.
    
    Attributes
        fractal: complex_fractal.Fractal
            Fractal to be drawn.
        size: tuple[float,float]
            Size of the observed plane.
        resolution: tuple[int,int]
            Number of points along each direction.
        offset: tuple[float,float]
            Position of the center point in complex plane.
        zoom: float
            Zoom value (> 1: zoom in; < 1: zoom out).
        colormap: str
            Name of matplotlib colormap used to colorize RGB image.
    Methods
        img_grey(): np.ndarray[np.float64]
            Generates normalized grey scale image of viewport.
        img_rgb(): np.ndarray[np.float64]
            Generates normalized RGB image of viewport.
    """
    def __init__(self,
            fractal: cplxf.Fractal = cplxf.MandelbrotSet(),
            size: tuple[float,float] = (4,3),
            resolution: tuple[int,int] = (720,540),
            offset: tuple[float,float] = (0.0,0.0),
            zoom: float = 1.0,
            colormap: str = 'binary'
            ):
        self.fractal = fractal
        self.size = size
        self.resolution = resolution
        self.offset = offset
        self.zoom = zoom
        self.colormap = colormap
    
    @property
    def fractal(self) -> cplxf.Fractal:
        """Fractal to be drawn."""
        return self._fractal
    @fractal.setter
    def fractal(self, fractal: cplxf.Fractal) -> None:
        self._fractal = fractal
   
    @property
    def size(self) -> tuple[float, float]:
        """Size of the observed plane.
        Used as x/y bounds for the complex plane.
        Must be positive non zero.
        size[0]: X axis
        size[1]: Y axis
        """
        return self._size
    @size.setter
    def size(self, size: tuple[float,float]) -> None:
        if not isinstance(size, tuple): raise TypeError("Attribute 'size' must be a tuple.")
        if not (len(size) == 2): raise ValueError("Attribute 'size' must have length 2.")
        if not isinstance(size[0], float | int): raise TypeError("Attribute 'size' must be tuple of floats.")
        if not (size[0] > 0): raise ValueError("Attribute 'size' must have positive non zero values.")
        if not isinstance(size[1], float | int): raise TypeError("Attribute 'size' must be tuple of floats.")
        if not (size[1] > 0): raise ValueError("Attribute 'size' must have positive non zero values.")
        self._size = size
    
    @property
    def resolution(self) -> tuple[int,int]:
        """Number of points along each direction.
        Used as the number of points along each direction.
        Must be positive non zero.
        resolution[0]: X axis
        resolution[1]: Y axis
        """
        return self._resolution
    @resolution.setter
    def resolution(self, resolution: tuple[int,int]) -> None:
        if not isinstance(resolution, tuple): raise TypeError("Attribute 'resolution' must be a tuple.")
        if not (len(resolution) == 2): raise ValueError("Attribute 'resolution' must have length 2.")
        if not isinstance(resolution[0], int): raise TypeError("Attribute 'resolution' must be tuple of ints.")
        if not (resolution[0] > 0): raise ValueError("Attribute 'resolution' must have positive non zero values.")
        if not isinstance(resolution[1], int): raise TypeError("Attribute 'resolution' must be tuple of ints.")
        if not (resolution[1] > 0): raise ValueError("Attribute 'resolution' must have positive non zero values.")
        self._resolution = resolution
    
    @property
    def zoom(self) -> float:
        """Zoom value (> 1: zoom in; < 1: zoom out).
        Must be positive non zero.
        """
        return self._zoom
    @zoom.setter
    def zoom(self, zoom: float) -> None:
        if not isinstance(zoom, float | int): raise TypeError("Attribute 'zoom' must be float.")
        if not (zoom > 0): raise ValueError("Attribute 'zoom' must be positive non zero.")
        self._zoom = zoom
    
    @property
    def offset(self) -> tuple[float, float]:
        """Position of the center point in complex plane.
        offset[0]: X axis
        offset[1]: Y axis
        """
        return self._offset
    @offset.setter
    def offset(self, offset: tuple[float, float]) -> None:
        if not isinstance(offset, tuple): raise TypeError("Attribute 'offset' must be a tuple.")
        if not (len(offset) == 2): raise ValueError("Attribute 'offset' must have length 2.")
        if not isinstance(offset[0], float | int): raise TypeError("Attribute 'offset' must be tuple of floats.")
        if not isinstance(offset[1], float | int): raise TypeError("Attribute 'offset' must be tuple of floats.")
        self._offset = offset
    
    @property
    def colormap(self) -> str:
        """Name of matplotlib colormap used to colorize RGB image."""
        return self._colormap
    @colormap.setter
    def colormap(self, colormap) -> None:
        if not isinstance(colormap, str): raise TypeError("Attribute 'colormap' must be str.")
        if not (colormap in plt.colormaps()): raise ValueError("Unknown matplotlib colormap.")
        self._colormap = colormap

    def img_grey(self) -> np.ndarray[np.float64]:
        """Generates normalized grey scale image of viewport.
        
        Return
            Numpy array of normalized floats (1 channel).
        """
        plane = cplxp.Plane(
            xmin = self.offset[0] - (self.size[0] / 2) / self.zoom,
            xmax = self.offset[0] + (self.size[0] / 2) / self.zoom,
            ymin = self.offset[1] - (self.size[1] / 2) / self.zoom,
            ymax = self.offset[1] + (self.size[1] / 2) / self.zoom,
            xpoints = self.resolution[0],
            ypoints = self.resolution[1]
        ).toMatrix()
        image = np.empty(shape = plane.shape, dtype = np.float64)
        for idx, point in np.ndenumerate(plane):
            stability = self.fractal.stability(point)
            image[idx[0], idx[1]] = stability
        return image
    
    def img_rgb(self) -> np.ndarray[np.float64]:
        """Generates normalized RGB image of viewport.
        
        Return
            Numpy array of normalized floats (3 channels).
        """
        plane = cplxp.Plane(
            xmin = self.offset[0] - (self.size[0] / 2) / self.zoom,
            xmax = self.offset[0] + (self.size[0] / 2) / self.zoom,
            ymin = self.offset[1] - (self.size[1] / 2) / self.zoom,
            ymax = self.offset[1] + (self.size[1] / 2) / self.zoom,
            xpoints = self.resolution[0],
            ypoints = self.resolution[1]
        ).toMatrix()
        image = np.empty(shape = plane.shape + (3,), dtype = np.float64)
        colormap = mplcm.get_cmap(self.colormap)
        for idx, point in np.ndenumerate(plane):
            stability = self.fractal.stability(point)
            image[idx[0], idx[1]] = colormap(stability)[:-1]
        return image