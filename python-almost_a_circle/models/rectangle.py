#!/usr/bin/python3
"""
Module for Rectangle sub-class definition
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class definition - inherits from Base

    Attributes:
        __width (int) : private attribute representing width
        __height (int) : private attribute representing height
        __x (int) : private attribute representing x coordinate
        __Y (int) : private attribute representing y coordinate
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes new instance of Rectangle class

        Args:
            width : width of rectangle
            height : height of rectangle
            x : x coordinate of rectangle (default 0)
            y : y coordinate of rectangle (default 0)
            id : if provided, assigns ID attribute to given value
                if not provided, automatically creates ID
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute

        Args:
            value (int) : value of rectangle's width
        """
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
        Setter for height attribute

        Args:
            value (int) : value of rectangle's height
        """
        self.__height = value

    @property
    def x(self):
        """
        Getter for x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x attribute

        Args:
            value (int) : value of rectangle's x coordinate position
        """
        self.__x = value

    @property
    def y(self):
        """
        Getter for y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y attribute

        Args:
            value (int) : value of rectangle's y coordinate position
        """
        self.__y = value
