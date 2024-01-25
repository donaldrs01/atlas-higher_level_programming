#!/usr/bin/python3
"""
Module for Base unit tests
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_base_instance_creation(self):
        """
        Tests Base() instantiation and unique IDs
        """
        b = Base()  # Output : 1
        b1 = Base()  # Output : 2
        self.assertEqual(b.id, 1)
        self.assertEqual(b1.id, 2)

    def test_id_sync(self):
        """
        Tests sync between nb_objects and ID
        """
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_custom_ID(self):
        """
        Tests custom ID input (int)
        """
        i = 54
        b = Base(i)
        self.assertEqual(b.id, i)

