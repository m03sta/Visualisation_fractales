""" Test module for Viewport class.
"""

import unittest
import sys
sys.path.append('..')
from viewport import Viewport
import complex_fractal as cplxf


class TestViewport (unittest.TestCase):

    def test_default(self):
        viewport = Viewport()
        self.assertIsInstance(viewport.fractal, cplxf.MandelbrotSet)
        self.assertEqual(viewport.size, (4,3))
        self.assertEqual(viewport.resolution, (720,540))
        self.assertEqual(viewport.offset, (0.0,0.0))
        self.assertEqual(viewport.zoom, 1.0)
        self.assertEqual(viewport.colormap, 'binary')
    
    def test_size(self):
        viewport = Viewport(size = (100,100))
        self.assertEqual(viewport.size, (100,100))
        viewport.size = (200.75,300.05)
        self.assertEqual(viewport.size, (200.75,300.05))
    
    def test_size_exceptions(self):
        with self.assertRaises(TypeError):
            viewport = Viewport(size = 100)
        with self.assertRaises(ValueError):
            viewport = Viewport(size = (100,))
        with self.assertRaises(TypeError):
            viewport = Viewport(size = ('string',100))
        with self.assertRaises(TypeError):
            viewport = Viewport(size = (100,'string'))
        with self.assertRaises(ValueError):
            viewport = Viewport(size = (-1,100))
        with self.assertRaises(ValueError):
            viewport = Viewport(size = (100,-1))
    
    def test_resolution(self):
        viewport = Viewport(resolution = (100,100))
        self.assertEqual(viewport.resolution, (100,100))
        viewport.resolution = (200,300)
        self.assertEqual(viewport.resolution, (200,300))
    
    def test_resolution_exceptions(self):
        with self.assertRaises(TypeError):
            viewport = Viewport(resolution = 100)
        with self.assertRaises(ValueError):
            viewport = Viewport(resolution = (100,))
        with self.assertRaises(TypeError):
            viewport = Viewport(resolution = (100.0,100))
        with self.assertRaises(TypeError):
            viewport = Viewport(resolution = (100,100.0))
        with self.assertRaises(ValueError):
            viewport = Viewport(resolution = (-1,100))
        with self.assertRaises(ValueError):
            viewport = Viewport(resolution = (100,-1))
    
    def test_colormap(self):
        viewport = Viewport(colormap = 'plasma')
        self.assertEqual(viewport.colormap, 'plasma')
        viewport.colormap = 'viridis'
        self.assertEqual(viewport.colormap, 'viridis')
    
    def test_colormap_exceptions(self):
        with self.assertRaises(TypeError):
            viewport = Viewport(colormap = 2)
        with self.assertRaises(ValueError):
            viewport = Viewport(colormap = 'colormap_that_does_not_exist')
    
    def test_offset(self):
        viewport = Viewport(offset = (-2,-3.5))
        self.assertEqual(viewport.offset, (-2,-3.5))
        viewport.offset = (10.1,0)
        self.assertEqual(viewport.offset, (10.1,0))
    
    def test_offset_exceptions(self):
        with self.assertRaises(TypeError):
            viewport = Viewport(offset = 1-3j)
        with self.assertRaises(ValueError):
            viewport = Viewport(offset = (1,))
        with self.assertRaises(TypeError):
            viewport = Viewport(offset = ('string',1))
        with self.assertRaises(TypeError):
            viewport = Viewport(offset = (1,'string'))

if __name__ == '__main__':
    unittest.main()