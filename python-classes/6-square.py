#!/usr/bin/python3
"""
Square class with size and positional attributes
"""


class Square:
    """
    Definition of Square class
    Methods:
        area(): returns the area of a square
        my_print: prints out the square to stdout with '#' character
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square

        Args:
            size (int) : size of the side of a square
            position (tuple) : coordinate (x,y) position of the square
        """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter for position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Establishes coordinate (x,y) position of square

        Args:
            value (tuple) : the (x,y) position of new square
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if type(i) is not int or (type(i) is int and i < 0):
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
        if self.__size == 0:
            print("")
        for _ in range(self.__position[1]):
            print("")  # prints empty lines up to position of [1]
        for _ in range(self.__size):
            for x in range(self.position[0]):
                print(" ", end="")  # prints spaces based on horizontal position
            for j in range(self.size):
                print("#", end="")  # prints '#' based on size of square
            print("")  # finish with empty line after each row of '#' characters
