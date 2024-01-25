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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
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
        Setter for height attribute

        Args:
            value (int) : value of rectangle's height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Calculates area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Method that prints rectangle to stdout using '#' character

        Return:
            printed rectangle
        """
        if self.__width == 0 or self.__height == 0:
            print()
            return
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    print('#', end="")
                print()  # prints new line after finishing row

    def __str__(self):
        """
        Returns Rectangle description in string form
        """
        return '[{}]({}){}/{} - {}/{}'.format(type(self).__name__, self.id, self.x, self.y, self.width, self.height)
