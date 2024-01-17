#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 15, 27]), 27)

    def test_max_at_start(self):
        self.assertEqual(max_integer([14, 2, 7]), 14)

    def test_max_in_mid(self):
        self.assertEqual(max_integer([14, 56, 12]), 56)

    def test_neg_in_list(self):
        self.assertEqual(max_integer([-2, 4, 16, 28]), 28)

    def test_all_negative(self):
        self.assertEqual(max_integer([-5, -14, -2]), -2)

    def test_single_element(self):
        self.assertEqual(max_integer([14]), 14)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
