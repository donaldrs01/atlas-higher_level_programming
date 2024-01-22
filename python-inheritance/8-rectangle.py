#!/usr/bin/python3
"""
Module containing:
    BaseGeometry : parent class
    Rectangle : sub class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class definition of rectangle - subclass
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


# test function #

# print(issubclass(Rectangle, BaseGeometry)) #
