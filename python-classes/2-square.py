#!/usr/bin/python3

"""
Creation of square class with size attribute
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0):
        """
        Method for square class that defines size

        Args:
        size(int) : size of Square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
