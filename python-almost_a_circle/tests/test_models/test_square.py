import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Tests Square class
    """

    def setUp(self):
        """
        Imports base model, instantiates Square, resets counter
        """
        Base._Base__nb_objects = 0

    def test_class(self):
        """
        Tests Square class type
        """
        s = Square(6)
        self.assertIsInstance(s, Square)

    def test_construction_size_arg(self):
        """
        Tests constructor when size arg is passed
        """
        s = Square(6)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        
    def test_construction_all_args(self):
        """
        Tests constructor when all args passed
        """
        s2 = Square(5, 4, 4, 15)
        self.assertEqual(s2.size, 5)
        self.assertEqual(s2.x, 4)
        self.assertEqual(s2.y, 4)
        self.assertEqual(s2.id, 15)


