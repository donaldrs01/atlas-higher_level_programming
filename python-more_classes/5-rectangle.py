#!/usr/bin/python3
"""
Module that continues with Rectangle class
"""


class Rectangle:
    """
    Rectangle class with width and height attributes
    """
    def __init__(self, width=0, height=0):
        """
        Init method for Rectangle

        Args:
            width (int) : width of rectangle
            height (int) : height of rectangle
        """
        self.width = width
        # defined attribute 'width' that is equal to width passed into method
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
        Setter for width attribute

        Args:
            value (int) : value of new rectangle's width
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
            value (int) : value of new rectangle's height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Method for area calculation of rectangle

        Return:
            area of the rectangle
        """
        return self.__width * self.__height
        # area = width * height for rectangle

    def perimeter(self):
        """
        Method for perimeter calculation of rectangle

        Return:
            perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def print(self):
        """
        Method that prints rectangle using '#' character

        Return:
            printed rectangle
        """
        if self.__width == 0 or self.__height == 0:
            print()
            return
        else:
            for i in range(self.height):
                for j in range(self.width):
                    print("#", end="")  # no \n

    def __str__(self):
        """
        Method for string representation of rectangle

        Return:
            string representation of rectangle using '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Representation of the rectangle

        Return:
            Representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes an instance of Rectangle
        """
        print("Bye rectangle...")
