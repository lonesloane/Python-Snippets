__author__ = 'stephane'

import central_tendency
import unittest

sample1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sample2 = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
sample3 = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
sample4 = [1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5]
sample5 = [5, 5.5, 5.75, 5, 5.5, 5.75, 5, 5, 5]
sample6 = [3, 5, 2, 3, 7, 9, 3, 6, 3, 9, 3, 5]
sample7 = [3, 3, 3, 3, 100, 3, 3, 3, 3]

class MeanTests(unittest.TestCase):
    def testMeanResult(self):
        self.assertEqual(5.5, central_tendency.mean(sample1))
        self.assertTrue((13.78 - central_tendency.mean(sample7)) < 0.01)

class MedianTests(unittest.TestCase):
    def testMedianResult(self):
        self.assertEqual(5.5, central_tendency.median(sample1))
        self.assertEqual(5, central_tendency.median(sample2))
        self.assertEqual(6, central_tendency.median(sample3))
        self.assertEqual(3, central_tendency.median(sample7))

class ModeTests(unittest.TestCase):
    def testModeResult(self):
        self.assertEqual(3, central_tendency.mode(sample4))
        self.assertEqual(5, central_tendency.mode(sample5))
        self.assertEqual(3, central_tendency.mode(sample6))
        self.assertEqual(3, central_tendency.mode(sample7))


if __name__ == "__main__":
    unittest.main()
