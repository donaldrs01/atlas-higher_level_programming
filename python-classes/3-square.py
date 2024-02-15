#!/usr/bin/python3

"""
Square class creation and size attribute
"""


class Square:
    """
    Square class
    """
    def __init__(self, size=0):
        """
        Method for square class

        Args:
        size (int) : size of Square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Method that calculates area of square

        Return:
        area of inputted square
        """
        return self.__size * self.__size
        # area = size * size
