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
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns Square description in string form
        """
        return ('[{}] ({}) {}/{} - {}'
                .format(type(self).__name__, self.id,
                        self.x, self.y, self.height))
