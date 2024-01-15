#!/usr/bin/python3
"""
Module that performs basic integer additiojn
"""


def add_integer(a, b=98):
    """
    Function that performs basic addition between two integers

    Args:
        a: the first integer
        b: the second integer
    Return:
        the sum of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)  # ensures a and b are treated as integers if originally floats
