#!/usr/bin/python3
"""
Module that declares a Rectangle class
"""


class Rectangle:
    """
    Definition of Rectangle class with attributes width and height
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle

        Args:
            width (int) : the width of the rectangle
            height (int) : the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute of rectangle

        Args:
            value (int) : the value of new rectangle's width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter for height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height

        Args:
            value (int) : the value of the new rectangle's height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
