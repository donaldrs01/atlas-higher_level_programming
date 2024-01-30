"""
Module for Rectangle unit tests
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Tests Rectangle class
    """

    def setUp(self):
        """
        Imports base model, instantiates Rectangle, resets counter
        """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """
        Resets to setUp conditions
        """
        pass

    def test_class(self):
        """
        Tests Rectangle class type
        """
        r = Rectangle(1, 2)  # receives valid args
        self.assertIsInstance(r, Rectangle)  # instance is type Rectangle

    def test_inheritance(self):
        """
        Tests if Rectangle is sub-class of Base
        """
        self.assertTrue(issubclass(Rectangle, Base))
   
                    ### Constructor Tests ###

    def test_constructor_no_args(self):
        """
        Tests constructor when no arguments passed
        """
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        s = "Rectangle.__init__() missing 2 required positional arguments: 'width' and 'height'"
        self.assertEqual(str(e.exception), s)

    def test_constructor_too_many_args(self):
        """
        Tests constructor when too many args passed
        """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 5, 4, 2, 3, 12, 2)
        s = "Rectangle.__init__() takes from 3 to 6 positional arguments but 8 were given"
        self.assertEqual(str(e.exception), s)

    def test_constructor_one_arg(self):
        """
        Tests constructor when one argument is passed
        """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(7)
        s = "Rectangle.__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), s)

    def test_width_not_int(self):
        """
        Tests when width not valid integer
        """
        with self.assertRaises(TypeError) as e:
            r = Rectangle('test', 4)
        s = "width must be an integer"
        self.assertEqual(str(e.exception), s)

    def test_height_not_int(self):
        """
        Tests when height not valid integer
        """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(3, 'test')
        s = "height must be an integer"
        self.assertEqual(str(e.exception), s)

    def test_x_not_int(self):
        """
        Tests when X is not an integer
        """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(3, 4, "test")
        s = "x must be an integer"
        self.assertEqual(str(e.exception), s)

    def test_y_not_int(self):
        """
        Tests when Y is not an integer
        """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(3, 4, 1, "test")
        s = "y must be an integer"
        self.assertEqual(str(e.exception), s)

    def test_width_sub_zero(self):
        """
        Tests when width is less than zero
        """
        with self.assertRaises(ValueError) as e:
            r = Rectangle(-2, 4)
        s = "width must be > 0"
        self.assertEqual(str(e.exception), s)

    def test_height_sub_zero(self):
        """
        Tests when height is less than zero
        """
        with self.assertRaises(ValueError) as e:
            r = Rectangle(3, -2)
        s = "height must be > 0"
        self.assertEqual(str(e.exception), s)

    def test_x_sub_zero(self):
        """
        Tests when X is less than 0
        """
        with self.assertRaises(ValueError) as e:
            r = Rectangle(3, 1, -2)
        s = "x must be >= 0"
        self.assertEqual(str(e.exception), s)

    def test_y_sub_zero(self):
        """
        Tests when Y is less than 0
        """
        with self.assertRaises(ValueError) as e:
            r = Rectangle(3, 1, 2, -4)
        s = "y must be >= 0"
        self.assertEqual(str(e.exception), s)
