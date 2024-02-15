#!/usr/bin/python3
"""
Square class definition
"""


class Square:
    """
    Class that defines our square
    """
    def __init__(self, size=0):
        """
        initializing method for Square class

        Args:
            size : size of the square
        """
        self.__size = size

    @property
    def size(self):
        #  decoration allows us to access 'size' using . (dot) notation
        """
        Getter for size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size attribute

        Args:
            value : the value of the square's size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        #  we can set value with setter using . notation

    def area(self):
        """
        Method of Square class that returns square's area
        Return:
            square's area
        """
        return self.__size * 2
