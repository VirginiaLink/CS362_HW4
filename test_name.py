# Virginia Link
# CS 362
# HW4 program to test the fullname generator
# 02/07/2021

import unittest
import name

class Test(unittest.TestCase):
    def test_non_str_first_name(self):
        result = name.full(4, 'Johnson')
        self.assertEqual(result, 0)
    def test_non_str_last_name(self):
        result = name.full('Joe', 6)
        self.assertEqual(result,0)
    def test_normal(self):
        result = name.full('Joe','Johnson')
        self.assertEqual(result, 'Joe Johnson')

if __name__ == '__main__':
    unittest.main()
