#!/usr/bin/python3
"""
Module for Base unit tests
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        """
        Imports module, instantiates class, resets counter
        """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """
        Resets to setUp conditions
        """
        pass

    def test_automatic_ID_assignment(self):
        """
        Tests Base() instantiation and unique IDs
        """
        b = Base()  # Output : 1
        b2 = Base()  # Output : 2
        b3 = Base()  # Output : 3
        self.assertEqual(b.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

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

