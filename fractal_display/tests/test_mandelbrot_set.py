""" Test module for MandelbrotSet class.
"""

import unittest
import sys
sys.path.append('..')
import complex_fractal as cplxf


class TestMandelbrotSet(unittest.TestCase):

    def test_default(self):
        fractal = cplxf.MandelbrotSet()
        self.assertIsInstance(fractal, cplxf.MandelbrotSet)
        self.assertEqual(fractal.max_iterations, 20)

    def test_max_iterations(self):
        fractal = cplxf.MandelbrotSet(max_iterations = 100)
        self.assertEqual(fractal.max_iterations, 100)
        fractal.max_iterations = 10
        self.assertEqual(fractal.max_iterations, 10)

    def test_max_iteration_exceptions(self):
        with self.assertRaises(TypeError):
            fractal = cplxf.MandelbrotSet(max_iterations = 'string')
        with self.assertRaises(ValueError):
            fractal = cplxf.MandelbrotSet(max_iterations = -1)

    def test_escape_count(self):
        fractal = cplxf.MandelbrotSet()
        # point inside Mandelbrot set (convergent)
        self.assertEqual(fractal.escape_count(0), fractal.max_iterations)
        # point outside Mandelbrot set (divergent)
        self.assertEqual(fractal.escape_count(10), 0)
        # point on the edge (depends on max_iterations)
        fractal.max_iterations = 30
        self.assertEqual(fractal.escape_count(-1+0.3j), 30)
        fractal.max_iterations = 100
        self.assertEqual(fractal.escape_count(-1+0.3j), 34)
        
    def test_escape_count_exceptions(self):
        with self.assertRaises(TypeError):
            fractal = cplxf.MandelbrotSet()
            escape_count = fractal.escape_count('string')
    
    def test_stability(self):
        fractal = cplxf.MandelbrotSet()
        # point inside Mandelbrot set (convergent)
        self.assertEqual(fractal.stability(0), 1)
        # point outside Mandelbrot set (divergent)
        self.assertEqual(fractal.stability(10), 0)
        # point on the edge (depends on max_iterations)
        fractal.max_iterations = 30
        self.assertEqual(fractal.stability(-1+0.3j), 1)
        fractal.max_iterations = 100
        self.assertEqual(fractal.stability(-1+0.3j), 0.34)
    
    def test_stability_exceptions(self):
        with self.assertRaises(TypeError):
            fractal = cplxf.MandelbrotSet()
            escape_count = fractal.stability('string')
    
    def test_str(self):
        fractal = cplxf.MandelbrotSet()
        self.assertEqual(str(fractal), f'Mandelbrot_maxIt{fractal.max_iterations}')

if __name__ == '__main__':
    unittest.main()