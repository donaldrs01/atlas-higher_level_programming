#!/usr/bin/python3
"""
Module for Base unit tests
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_base_instance_creation(self):
        obj1 = Base()  # Output : 1
        obj2 = Base()  # Output : 2
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
