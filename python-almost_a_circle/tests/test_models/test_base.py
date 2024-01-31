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
        Cleans up after each test
        """
        pass

    def test_auto_ID_assign(self):
        
        self.assertEqual(Base._Base__nb_objects, 0)
        b = Base()
        b2 = Base()
        b3 = Base()
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

    def test_negative_ID(self):
        """
        Tests negative ID input
        """
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_json_string_empty(self):
        """
        Tests when to_json_string receives empty list
        """
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_json_string_not_dict(self):
        """
        Tests when to_json_string receives non-dictionary parameter
        """
        self.assertEqual(Base.to_json_string([1, 4, 8]), "[1, 4, 8]")

    def test_json_string_valid(self):
        """
        Tests for when to_json_string receives valid input
        """
        obj_list = [{"id": 1, "name": "Test", "value": 42}]
        json_string = Base.to_json_string(obj_list)
        expected_json_string = '[{"id": 1, "name": "Test", "value": 42}]'
        self.assertEqual(json_string, expected_json_string)
