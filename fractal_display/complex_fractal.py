"""complex_fractal module. Provides complex-based fractal templates.

Classes
    Fractal
    JuliaSet
    MandelbrotSet
"""

from abc import ABC, abstractmethod # package for abstract classes


class Fractal(ABC):
    """Fractal abstract class.
    
    Generalizes concept of fractal based on the convergence of a complex sequence.
    
    Virtual methods
        stability(complex): float
        escape_count(complex): int
        __str__(): str
    """    
    @abstractmethod
    def stability(self, candidate: complex) -> float:
        pass
    @abstractmethod
    def escape_count(self, candidate: complex) -> int:
        pass
    @abstractmethod
    def __str__(self) -> str:
        pass

class JuliaSet(Fractal):
    """Julia sets class.
    
    Julia sets are the sets of z_0 so that the sequence z_(n+1) = z_n^2 + c converges.
    Each different complex c leads to a different Julia set.
    
    Attributes
        c: complex
        max_iterations: int
    Methods
        stability(complex): float
            Stability of the sequence with given z_0.
        escape_count(complex): int
            Number of iterations before diverging.
        __str__(): str
    """
    def __init__(self, c: complex = -0.75, max_iterations: int = 20):
        self.c = c
        self.max_iterations = max_iterations
    
    @property
    def c(self) -> complex:
        """Constant c caracterising Julia set."""
        return self._c
    @c.setter
    def c(self, c: complex) -> None:
        if not isinstance(c, complex | float | int): raise TypeError("Attribute 'c' must be a complex number.")
        self._c = c
    
    @property
    def max_iterations(self) -> int:
        """Maximum number of iterations for considering sequence as convergent.
        Must be positive non zero."""
        return self._max_iterations
    @max_iterations.setter
    def max_iterations(self, max_iterations: int) -> None:
        if not isinstance(max_iterations, int): raise TypeError("Attribute 'max_iterations' must be int.")
        if not (max_iterations > 0): raise ValueError("Attribute 'max_iterations' must be positive non zero.")
        self._max_iterations = max_iterations
    
    def stability(self, z_0: complex) -> float:
        """Stability of the sequence with given z_0.
        
        This function gives a normalized measurement of sequence divergence speed by dividing escape count by self.max_iterations.
        
        Parameters
            z_0: number to measure divergence speed.
        Return
            Normalized divergence measurement.
            0: most divergent point.
            1: most convergent point.
        """
        if not isinstance(z_0, complex | float | int): raise TypeError("Given z_0 must be a complex number.")
        return self.escape_count(z_0) / self.max_iterations
    
    def escape_count(self, z_0: complex) -> int:
        """Number of iterations before diverging.
        
        This function is used to measure divergence speed of the sequence by returning the escape count (number of iterations it takes
        to diverge). The sequence is considered as convergent if that number is equal to self.max_iterations.
        
        Parameters
            z_0: number to evaluate divergence.
        Return
            Number of iterations before diverging between 0 and self.max_iterations.
        """
        if not isinstance(z_0, complex | float | int): raise TypeError("Given z_0 must be a complex number.")
        z = z_0
        for iteration in range(self.max_iterations):
            z = z ** 2 + self.c
            if abs(z) > 2:  # numbers whose modulus is greater than 2 are considered to big
                return iteration
        return self.max_iterations
    
    def __str__(self) -> str:
        return f'Julia_c{self.c}_maxIt{self.max_iterations}'

class MandelbrotSet(Fractal):
    """Mandelbrot set class.
    
    Mandelbrot set is the set of c so that the sequence z_(n+1) = z_n^2 + c with z_0 = 0 converges.
    
    Attributes
        max_iterations: int
            Maximum number of iterations for considering sequence as convergent.
    Methods
        stability(complex): float
            Stability of the sequence with given c.
        escape_count(complex): int
            Number of iterations before diverging.
        __str__(): str
    """
    def __init__(self, max_iterations: int = 20):
        self.max_iterations = max_iterations

    @property
    def max_iterations(self) -> int:
        """Maximum number of iterations for considering sequence as convergent."""
        return self._max_iterations
    @max_iterations.setter
    def max_iterations(self, max_iterations: int) -> None:
        if not isinstance(max_iterations, int): raise TypeError("Attribute 'max_iterations' must be int.")
        if not (max_iterations > 0): raise ValueError("Attribute 'max_iterations' must be positive non zero.")
        self._max_iterations = max_iterations

    def stability(self, c: complex) -> float:
        """Stability of the sequence with given c.
        
        This function gives a normalized measurement of sequence divergence speed by dividing escape count by self.max_iterations.
        
        Parameters
            c: number to measure divergence speed.
        Return
            Normalized divergence measurement.
            0: most divergent point.
            1: most convergent point.
        """
        if not isinstance(c, complex | float | int): raise TypeError("Given c must be a complex number.")
        return self.escape_count(c) / self.max_iterations

    def escape_count(self, c: complex) -> int:
        """Number of iterations before diverging.
        
        This function is used to measure divergence speed of the sequence by returning the escape count (number of iterations it takes
        to diverge. The sequence is considered as convergent if that number is equal to self.max_iterations.
        
        Parameters
            c: number to evaluate divergence speed.
        Return
            Number of iterations before diverging between 0 and self.max_iterations.
        """
        if not isinstance(c, complex | float | int): raise TypeError("Given c must be a complex number.")
        z = 0
        for iteration in range(self.max_iterations):
            z = z ** 2 + c
            if abs(z) > 2: # numbers whose modulus is greater than 2 are considered to big
                return iteration
        return self.max_iterations
    
    def __str__(self) -> str:
        return f'Mandelbrot_maxIt{self.max_iterations}'