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

    def test_negative_size(self):
        """
        Tests constructor when receives negative value
        """
        with self.assertRaises(ValueError):
            s = Square(-5)

    def test_size_zero(self):
        """
        Tests constructor when it receives 0 as size value
        """
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_str_input(self):
        """
        Tests constructor when it receives a string as a size value
        """
        with self.assertRaises(TypeError):
            s = Square("test")

    def test_neg_x_value(self):
        """
        Tests constructor when 'x' value is negative
        """
        with self.assertRaises(ValueError):
            s = Square(10, -4)

    def test_neg_y_value(self):
        """
        Tests constructor when 'y' value is negative
        """
        with self.assertRaises(ValueError):
            s = Square(10, 4, -4)

    def test_square_to_dict(self):
        """
        Tests that to_dictionary method properly returns dict definition
        """
        s = Square(4, 1, 1, 15)
        dict_def = s.to_dictionary()
        expected_def = {"id": 15, "size": 4, "x": 1, "y": 1}
        self.assertEqual(expected_def, dict_def)

