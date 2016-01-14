__author__ = 'stephane'

from dispersion import *
import unittest

pop1 = [1.0, 2.0, 3.0, 8.0, 7.0]
pop2 = [0.0, 0.0, 5.0, 5.0]

sample1 = [2.0, 2.0, 3.0, 3.0]
sample2 = [0.0, 0.0, 5.0, 5.0]

class VarianceTest(unittest.TestCase):
    def testvariance_population(self):
        self.assertEqual(0.25, variance_population(sample1))
        self.assertEqual(6.25, variance_population(sample2))
        self.assertEqual(7.76, variance_population(pop1))
        self.assertEqual(6.25, variance_population(pop2))

    def testvariance_alternate(self):
        self.assertEqual(0.25, variance_alternate(sample1))
        self.assertEqual(6.25, variance_alternate(sample2))
        self.assertTrue(7.76 - variance_alternate(pop1) < 0.001)
        self.assertEqual(6.25, variance_alternate(pop2))

    def testvariance_alien(self):
        self.assertEqual(0.25, variance_alien(sample1))
        self.assertEqual(6.25, variance_alien(sample2))
        self.assertTrue(7.76 - variance_alien(pop1) < 0.001)
        self.assertEqual(6.25, variance_alien(pop2))

    def testvariance_sample(self):
        self.assertEqual(9.7, variance_sample(pop1))
        self.assertEqual(0.25, variance_sample(sample1))
        self.assertEqual(6.25, variance_sample(sample2))

    def teststandarddeviation(self):
        self.assertTrue(2.79 - standard_deviation(variance_population(pop1)) < 0.01)


if __name__ == "__main__":
    unittest.main()
