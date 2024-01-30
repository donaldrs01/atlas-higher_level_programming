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
        self.assertIsInstance(s, Square, "s is not an instance of Square")
