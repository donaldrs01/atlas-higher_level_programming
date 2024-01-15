#!/usr/bin/python3
"""
Module that continues with our Square class
"""


class Square:
    """
    Definition of Square class

    Methods:
        area(): returns the area of a square
        my_print: prints out the square to stdout with '#' character
    """
    def __init__(self, size=0):
        """
            Initializes the square

            Args:
                size (int) : size of the side of a square
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter for size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size attribute of square's side

        Args:
            value (int) : the value of the new square's side
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Method that calculates area of square

        Returns:
            the area of the square
        """
        return self.size ** 2

    def my_print(self):
        """
        Method that prints the square using the '#' character
        """
        if self.__size < 1:
            print("")
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")  # no \n
                print("")  # prints empty line after each row
