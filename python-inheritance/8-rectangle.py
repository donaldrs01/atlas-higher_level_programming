#!/usr/bin/python3
"""
Module containing:
    BaseGeometry : parent class
    Rectangle : sub class
"""


from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class definition of rectable - subclass
    """
    def __init__(self, width, height):
        """
        Method that initializes Rectangle instance

        Args:
            width : width of rectangle
            height : height of rectangle
        """
        super().__init__()
        # validate and set width and height #
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
