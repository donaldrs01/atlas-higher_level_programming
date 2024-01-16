#!/usr/bin/python3

"""
Defining a class 'Square'
"""


clas Square:
    """
    'Square' class
    """
    def __init__(self, size):
        """
        Constructor method defines size of square

        Args:
            size(int) - size of square
        """
        self.__size = size
        # __ makes size private attribute
