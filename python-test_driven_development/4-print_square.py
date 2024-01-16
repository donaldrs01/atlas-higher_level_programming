#!/usr/bin/python3
"""
Module that defines function that prints square using '#' characters
"""
def print_square(size):
    """
    Function that prints square using '#' characters

    Args:
        size (int) : the size of 1 side of square

    Errors:
        TypeError : if 'size' is not an integer
        ValueError : if 'size' is less than 0
        TypeError : if 'size' is float and less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for jin range(size):
            print("#", end="")
        print()
