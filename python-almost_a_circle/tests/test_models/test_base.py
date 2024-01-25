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
        obj1 = Base()  # Output : 1
        obj2 = Base()  # Output : 2
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_id_sync(self):
        """
        Tests sync between nb_objects and ID #
        """
        obj1 = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), obj1.id)

