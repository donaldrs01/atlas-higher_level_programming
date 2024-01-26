#!/usr/bin/python3
"""
Module for the Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class definition - inherits from Rectangle

    Attributes:
        size (int) : the size of one side of square
        x (int) : x coordinate
        y (int) : y coordinate
        ID (int) : ID # assigned to instance
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor that initializes attributes of Square
        """
        super().__init__(size, size, x, y, id)
        #  calls Rectangle constructor and passes through values
        #  'size' value is passed as both width and height

    @property
    def size(self):
        """
        Getter for size attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size attribute

        Args:
            value (int) : value of Square's side
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value  # width and height of square are same
            self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns attributes to specific arg order:
            [0] : ID attribute
            [1] : size attribute
            [2] : x attribute
            [3] : y attribute
        'Kwargs' pairs keyword arguments with key in specific order.
        Attribute is then assigned appropriate value.
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        for key, value in kwargs.items():  # access kwargs dict
            setattr(self, key, value)  # assign attributes

    def __str__(self):
        """
        Returns Square description in string form
        """
        return ('[{}] ({}) {}/{} - {}'
                .format(type(self).__name__, self.id,
                        self.x, self.y, self.height))

#  test_square = Square(1, 2, 3)
#  test_square.update(24, 3, 7)
#  print("String rep:", str(test_square))
