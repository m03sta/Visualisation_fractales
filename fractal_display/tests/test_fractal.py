"""Test module for Fractal class.
"""

import unittest
import sys
sys.path.append('..')
import complex_fractal as cplxf


class TestFractal(unittest.TestCase):
    def test_instantiation(self):
        with self.assertRaises(TypeError):
            fractal = cplxf.Fractal()

if __name__ == '__main__':
    unittest.main()