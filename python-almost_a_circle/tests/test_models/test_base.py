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

    def test_auto_ID_assign(self):
        """
        Tests Base() instantiation and unique ID assignment
        """
        b = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_nb_objects_zeroed(self):
        """
        Tests that nb_objects has been zeroed
        """
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

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

    def test_to_json_string(self):
        """
        Tests the to_json_string method
        """
        b = Base()
        json_string = Base.to_json_string([b.to_dictionary()])
        self.assertEqual(json_string, '[{"id": 1}]')
        #  Tests empty list
        empty_json_string = Base.to_json_string([])
        self.assertEqual(empty_json_string, "[]")
