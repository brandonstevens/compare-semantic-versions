#! /usr/bin/env python

import semver
import unittest

class testversion(unittest.TestCase):
    def test_equals(self):
        self.assertTrue(semver.equals('1.0.0', '1.0.0'))
        self.assertFalse(semver.equals('1.0.0', '2.0.0'))
    def test_gt(self):
        self.assertTrue(semver.gt('2.0.0', '1.0.0'))
        self.assertTrue(semver.gt('2.1.0', '2.0.0'))
        self.assertTrue(semver.gt('2.1.1', '2.1.0'))
        self.assertFalse(semver.gt('2.0.0', '2.0.0'))
        self.assertFalse(semver.gt('1.0.0', '2.0.0'))
    def test_gte(self):
        self.assertTrue(semver.gte('2.0.0', '1.0.0'))
        self.assertTrue(semver.gte('2.1.0', '2.0.0'))
        self.assertTrue(semver.gte('2.1.1', '2.1.0'))
        self.assertTrue(semver.gte('2.0.0', '2.0.0'))
        self.assertFalse(semver.gte('1.0.0', '2.0.0'))
    def test_satisfies(self):
        self.assertTrue(semver.satisfies('1.0.0', '1.0.0'))
        self.assertTrue(semver.satisfies('1.0.0', '1.0.1'))
        self.assertFalse(semver.satisfies('1.0.0', '1.1.0'))
        self.assertFalse(semver.satisfies('1.0.0', '2.0.0'))
    def test_lt(self):
        self.assertTrue(semver.lt('1.0.0', '2.0.0'))
        self.assertTrue(semver.lt('1.0.0', '1.1.0'))
        self.assertTrue(semver.lt('1.0.0', '1.0.1'))
        self.assertFalse(semver.lt('1.0.0', '1.0.0'))
        self.assertFalse(semver.lt('2.0.0', '1.0.0'))
    def test_lte(self):
        self.assertTrue(semver.lte('1.0.0', '2.0.0'))
        self.assertTrue(semver.lte('1.0.0', '1.1.0'))
        self.assertTrue(semver.lte('1.0.0', '1.0.1'))
        self.assertTrue(semver.lte('1.0.0', '1.0.0'))
        self.assertFalse(semver.lte('2.0.0', '1.0.0'))
    def test_other(self):
        with self.assertRaises(RuntimeError):
            semver.lte('1.0.0', '2.0')
        with self.assertRaises(RuntimeError):
            semver.lte('1.0.0', 'fail')
        with self.assertRaises(RuntimeError):
            semver.lte('1.0.0', '2.0.0-fail')

if __name__ == '__main__':
    unittest.main()
