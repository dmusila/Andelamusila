import unittest

import primenumberGen

class TestvalueN(unittest.TestCase):
        def flow(self):
          result = primenumber(4)
          self.assertEqual(result, 2,3)
        def negative(self):
           result = primenumber(-4)
           self.assertEqual(result, "negative num not allowed")
        def checksint(self):
           result = primenumber("d")
           self.assertEqual(result, "strings not allowed input an integer")
        def inputnot1 (self):
           result = primenumber(1)
           self.assertEqual(result, "input needed should be greater than 1")
        def inputnotzero (self):
           result = primenumber(0)
        self.assertEqual(result, "should not be 0")
if __name__ == '__main__':
    unittest.main()