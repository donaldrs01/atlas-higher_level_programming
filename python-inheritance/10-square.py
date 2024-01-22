#!/usr/bin/python3
"""
Module containing BaseGeometry class and Rectangle and square subclasses
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class definition of square - subclass of rectangle
    """

    def __init__(self, size):
        """
        Method that initializes square instance

        Args:
            size : size of a side of the square
        """
        self.integer_validator("size", size)
        # validate and set size BEFORE instance is created 
        super().__init__(size, size)  # pass size as both width and height
        self.__size = size

    def area(self):
        """
        Finds area of square

        Returns:
            area of square
        """
        return self.__size ** 2

# test print
# print(issubclass(Square, Rectangle))
# print(Square)
# print(Rectangle)
