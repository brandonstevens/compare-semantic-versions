#! /usr/bin/env python

from semver import version
import unittest

class testversion(unittest.TestCase):
    def setUp(self):
        self.v100 = version('1.0.0')
        self.v101 = version('1.0.1')
        self.v110 = version('1.1.0')
        self.v200 = version('2.0.0')
        self.v210 = version('2.1.0')
        self.v211 = version('2.1.1')
    def test_equals(self):
        self.assertTrue(self.v100.equals(self.v100))
        self.assertFalse(self.v100.equals(self.v200))
    def test_lt(self):
        self.assertTrue(self.v200.lt(self.v100))
        self.assertTrue(self.v210.lt(self.v200))
        self.assertTrue(self.v211.lt(self.v210))
        self.assertFalse(self.v200.lt(self.v200))
        self.assertFalse(self.v100.lt(self.v200))
    def test_lte(self):
        self.assertTrue(self.v200.lte(self.v100))
        self.assertTrue(self.v210.lte(self.v200))
        self.assertTrue(self.v211.lte(self.v210))
        self.assertTrue(self.v200.lte(self.v200))
        self.assertFalse(self.v100.lte(self.v200))
    def test_satisfies(self):
        self.assertTrue(self.v100.satisfies(self.v100))
        self.assertTrue(self.v100.satisfies(self.v101))
        self.assertFalse(self.v100.satisfies(self.v110))
        self.assertFalse(self.v100.satisfies(self.v200))
    def test_gt(self):
        self.assertTrue(self.v100.gt(self.v200))
        self.assertTrue(self.v100.gt(self.v110))
        self.assertTrue(self.v100.gt(self.v101))
        self.assertFalse(self.v100.gt(self.v100))
        self.assertFalse(self.v200.gt(self.v100))
    def test_gte(self):
        self.assertTrue(self.v100.gte(self.v200))
        self.assertTrue(self.v100.gte(self.v110))
        self.assertTrue(self.v100.gte(self.v101))
        self.assertTrue(self.v100.gte(self.v100))
        self.assertFalse(self.v200.gte(self.v100))

if __name__ == '__main__':
    unittest.main()
