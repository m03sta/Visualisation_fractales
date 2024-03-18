"""complex_plane module.

Classes
    Plane
"""

import numpy as np # numpy arrays


class Plane:
    """Plane class.

    Encapsulates relationship between (x,y) coordinates and complex numbers.
    
    Attributes
        xmin: float
            Minimum value along X axis.
        xmax: float
            Maximum value along X axis.
        ymin: float
            Minimum value along Y axis.
        ymax: float
            Maximum value along Y axis.
        xpoints: int
            Number of points to create along X axis.
        ypoints: int
            Number of points to create along Y axis.
    Methods
        toMatrix(): np.ndarray[np.complex128]
            Matrix of complex numbers representing the complex plane.
    """
    def __init__(self,
            xmin: float = -10.0,
            xmax: float = 10.0,
            ymin: float = -10.0,
            ymax: float = 10.0,
            xpoints: int = 21,
            ypoints: int = 21
            ):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.xpoints = xpoints
        self.ypoints = ypoints
    
    @property
    def xmin(self) -> float:
        """Minimum value along X axis."""
        return self._xmin
    @xmin.setter
    def xmin(self, xmin) -> None:
        if not isinstance(xmin, float | int): raise TypeError("Attribute 'xmin' must be float.")
        self._xmin = xmin
        
    @property
    def xmax(self) -> float:
        """Maximum value along X axis."""
        return self._xmax
    @xmax.setter
    def xmax(self, xmax) -> None:
        if not isinstance(xmax, float | int): raise TypeError("Attribute 'xmax' must be float.")
        self._xmax = xmax
    
    @property
    def ymin(self) -> float:
        """Minimum value along Y axis."""
        return self._ymin
    @ymin.setter
    def ymin(self, ymin) -> None:
        if not isinstance(ymin, float | int): raise TypeError("Attribute 'ymin' must be float.")
        self._ymin = ymin
        
    @property
    def ymax(self) -> float:
        """Maximum value along Y axis."""
        return self._ymax
    @ymax.setter
    def ymax(self, ymax) -> None:
        if not isinstance(ymax, float | int): raise TypeError("Attribute 'ymax' must be float.")
        self._ymax = ymax
    
    @property
    def xpoints(self) -> int:
        """Number of points to create along X axis."""
        return self._xpoints
    @xpoints.setter
    def xpoints(self, xpoints) -> None:
        if not isinstance(xpoints, int): raise TypeError("Attribute 'xpoints' must be int.")
        if not (xpoints > 0): raise ValueError("Attribute nbPoints must be non zero positive")
        self._xpoints = xpoints
    
    @property
    def ypoints(self) -> int:
        """Number of points to create along Y axis."""
        return self._ypoints
    @ypoints.setter
    def ypoints(self, ypoints) -> None:
        if not isinstance(ypoints, int): raise TypeError("Attribute 'ypoints' must be int.")
        if not (ypoints > 0): raise  ValueError("Attribute nbPoints must be non zero positive")
        self._ypoints = ypoints
    
    def toMatrix(self) -> np.ndarray[np.complex128]:
        """Matrix of complex numbers representing the complex plane."""
        if not (self.xmin < self.xmax): raise ValueError("Attribute 'xmax must be greater than xmin.")
        if not (self.ymin < self.ymax): raise ValueError("Attribute 'ymax must be greater than ymin.")
        re = np.linspace(self.xmin, self.xmax, self.xpoints)
        im = np.linspace(self.ymin, self.ymax, self.ypoints)
        # flip() is used to reverse Y axis
        # so that python's top-left corner coordinate frame
        # turns into a bottom-left corner coordinate frame (traditionally used in maths)
        return np.flip(re[np.newaxis, :] + im[:, np.newaxis] * 1j, 0)