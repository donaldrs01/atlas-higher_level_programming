import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Tests Rectangle class
    """

    def setUp(self):
        """
        Imports base model and instantiates Rectangle class
        """
        Base._Basei__nb_objects = 0

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
        self.assertIsInstance(Rectangle(), Rectangle)  # instance is type Rectangle

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

