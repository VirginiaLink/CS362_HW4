# Virginia Link
# CS 362
# HW4 program to test the volume calculator program
# 02/07/2021

import unittest
import volume


class Test(unittest.TestCase):
    def test_float_input(self):
        result = volume.calc(3.4)
        self.assertEqual(result, (3.4*3.4*3.4))
    def test_negative_input(self):
        result = volume.calc(-3)
        self.assertEqual(result, 0)
    def test_zero_input(self):
        result = volume.calc(0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()




