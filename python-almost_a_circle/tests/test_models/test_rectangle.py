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

