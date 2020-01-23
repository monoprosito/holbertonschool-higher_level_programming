#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A class to test a max integer function
    """

    def test_max_integer(self):
        """
        Test the max integer in a list of integers when the integers
        are positive or negative numbers
        """
        self.assertIsNone(max_integer([]))
        self.assertAlmostEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertAlmostEqual(max_integer([-4, -3, -2, -1, 0]), 0)
        self.assertAlmostEqual(max_integer([-90, -120, -150, -180]), -90)
        self.assertAlmostEqual(max_integer([1.0, 1.5, 1.6, 3.7, 2.3]), 3.7)
        self.assertAlmostEqual(max_integer([7.7]), 7.7)

    def test_wrong_types(self):
        """
        Test the max integer with wrong parameters types
        """
        with self.assertRaises(TypeError):
            max_integer(None)

        with self.assertRaises(TypeError):
            max_integer(["Monty", 89, 34, -9.7, "Python"])
