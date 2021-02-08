# Virginia Link
# CS 362
# HW4 program to test the average calculator program
# 02/07/2021

import unittest
import average


class Test(unittest.TestCase):
        def test_non_numerical_input(self):
            temp = [3,9,'hello']
            result = average.calc(temp)
            self.assertEqual(result, 0)
        def test_empty_list(self):
            temp = []
            result = average.calc(temp)
            self.assertEqual(result, 0)
        def test_neg_members(self):
            temp = [-2,2]
            result = average.calc(temp)
            self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
