""" Test module for JuliaSet class.
"""

import unittest
import sys
sys.path.append('..')
import complex_fractal as cplxf


class TestJuliaSet(unittest.TestCase):

    def test_default(self):
        fractal = cplxf.JuliaSet()
        self.assertIsInstance(fractal, cplxf.JuliaSet)
        self.assertEqual(fractal.c, -0.75)
        self.assertEqual(fractal.max_iterations, 20)
    
    def test_c(self):
        fractal = cplxf.JuliaSet(c = 0)
        self.assertEqual(fractal.c, 0)
        fractal.c = 1+2j
        self.assertEqual(fractal.c, 1+2j)
    
    def test_c_exceptions(self):
        with self.assertRaises(TypeError):
            fractal = cplxf.JuliaSet(c = 'string')
    
    def test_max_iterations(self):
        fractal = cplxf.JuliaSet(max_iterations = 100)
        self.assertEqual(fractal.max_iterations, 100)
        fractal.max_iterations = 10
        self.assertEqual(fractal.max_iterations, 10)
    
    def test_max_iteration_exceptions(self):
        with self.assertRaises(TypeError):
            fractal = cplxf.JuliaSet(max_iterations = 'string')
        with self.assertRaises(ValueError):
            fractal = cplxf.JuliaSet(max_iterations = -1)
    
    def test_escape_count(self):
        fractal = cplxf.JuliaSet(c = 0.25)
        # point inside Julia set (convergent)
        self.assertEqual(fractal.escape_count(0), fractal.max_iterations)
        # point outside Julia set (divergent)
        self.assertEqual(fractal.escape_count(10), 0)
        # point on the edge (depends on max_iterations)
        fractal.max_iterations = 30
        self.assertEqual(fractal.escape_count(0.53), 30)
        fractal.max_iterations = 100
        self.assertEqual(fractal.escape_count(0.53), 36)
        
    def test_escape_count_exceptions(self):
        with self.assertRaises(TypeError):
            fractal = cplxf.JuliaSet()
            escape_count = fractal.escape_count('string')
    
    def test_stability(self):
        fractal = cplxf.JuliaSet(c = 0.25)
        # point inside Mandelbrot set (convergent)
        self.assertEqual(fractal.stability(0), 1)
        # point outside Mandelbrot set (divergent)
        self.assertEqual(fractal.stability(10), 0)
        # point on the edge (depends on max_iterations)
        fractal.max_iterations = 30
        self.assertEqual(fractal.stability(0.53), 1)
        fractal.max_iterations = 100
        self.assertEqual(fractal.stability(0.53), 0.36)
    
    def test_stability_exceptions(self):
        with self.assertRaises(TypeError):
            fractal = cplxf.JuliaSet()
            escape_count = fractal.stability('string')
    
    def test_str(self):
        fractal = cplxf.JuliaSet()
        self.assertEqual(str(fractal), f'Julia set ; c = {fractal.c} ; max_iterations = {fractal.max_iterations}')

if __name__ == '__main__':
    unittest.main()