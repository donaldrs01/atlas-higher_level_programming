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

    def __str__(self):
        """
        Returns Square description in string form
        """
        return ('[{}] ({}) {}/{} - {}'
                .format(type(self).__name__, self.id,
                        self.x, self.y, self.height))
