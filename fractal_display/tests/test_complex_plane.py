"""Test module for Plane class.
"""

import unittest
import numpy as np # array(), array_equal()
import sys
sys.path.append('..')
import complex_plane as cplxp

class TestPlane(unittest.TestCase):

    def test_default(self):
        plane = cplxp.Plane()
        self.assertEqual(plane.xmin, -10.0)
        self.assertEqual(plane.xmax, 10.0)
        self.assertEqual(plane.ymin, -10.0)
        self.assertEqual(plane.ymax, 10.0)
        self.assertEqual(plane.xpoints, 21)
        self.assertEqual(plane.ypoints, 21)

    def test_xmin(self):
        plane = cplxp.Plane(xmin = -5)
        self.assertEqual(plane.xmin, -5)
        plane.xmin = -12.75
        self.assertEqual(plane.xmin, -12.75)
    
    def test_xmin_exceptions(self):
        with self.assertRaises(TypeError):
            plane = cplxp.Plane(xmin = 1+2j)

    def test_xmax(self):
        plane = cplxp.Plane(xmax = 5)
        self.assertEqual(plane.xmax, 5)
        plane.xmax = 12.75
        self.assertEqual(plane.xmax, 12.75)
    
    def test_xmax_exceptions(self):
        with self.assertRaises(TypeError):
            plane = cplxp.Plane(xmax = 1+2j)

    def test_ymin(self):
        plane = cplxp.Plane(ymin = -5)
        self.assertEqual(plane.ymin, -5)
        plane.ymin = -12.75
        self.assertEqual(plane.ymin, -12.75)
    
    def test_ymin_exceptions(self):
        with self.assertRaises(TypeError):
            plane = cplxp.Plane(ymin = 1+2j)

    def test_ymax(self):
        plane = cplxp.Plane(ymax = 5)
        self.assertEqual(plane.ymax, 5)
        plane.ymax = 12.75
        self.assertEqual(plane.ymax, 12.75)
    
    def test_ymax_exceptions(self):
        with self.assertRaises(TypeError):
            plane = cplxp.Plane(ymax = 1+2j)

    def test_xpoints(self):
        plane = cplxp.Plane(xpoints = 15)
        self.assertEqual(plane.xpoints, 15)
        plane.xpoints = 101
        self.assertEqual(plane.xpoints, 101)
    
    def test_xpoints_exceptions(self):
        with self.assertRaises(TypeError):
            plane = cplxp.Plane(xpoints = 2.0)
        with self.assertRaises(ValueError):
            plane = cplxp.Plane(xpoints = 0)

    def test_ypoints(self):
        plane = cplxp.Plane(ypoints = 15)
        self.assertEqual(plane.ypoints, 15)
        plane.ypoints = 101
        self.assertEqual(plane.ypoints, 101)
    
    def test_ypoints_exceptions(self):
        with self.assertRaises(TypeError):
            plane = cplxp.Plane(ypoints = 2.0)
        with self.assertRaises(ValueError):
            plane = cplxp.Plane(ypoints = 0)

    def test_toMatrix(self):
        plane = cplxp.Plane(
            xmin = 0,
            xmax = 2,
            ymin = 0,
            ymax = 3,
            xpoints = 3,
            ypoints = 4)
        expected = np.array([
            [3j, 1+3j, 2+3j],
            [2j, 1+2j, 2+2j],
            [1j, 1+1j, 2+1j],
            [0, 1, 2]
            ])
        recover = plane.toMatrix()
        self.assertTrue(np.array_equal(recover, expected))
    
    def test_toMatrix_exceptions(self):
        with self.assertRaises(ValueError):
            matrix = cplxp.Plane(xmin = 1, xmax = -1).toMatrix()
        with self.assertRaises(ValueError):
            matrix = cplxp.Plane(ymin = 1, ymax = -1).toMatrix()
    
if __name__ == '__main__':
    unittest.main()