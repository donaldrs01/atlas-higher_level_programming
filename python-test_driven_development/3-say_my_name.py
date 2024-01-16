#!/usr/bin/python3
"""
Module that defines function that prints first and last name based on input
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints 'My name is <first name> <last name>'.

    Args:
        first_name (str) : The first name to be printed
        last_name (str) : The last name to be printed

    Errors:
        TypeError: If <first_name> or <last_name> are not proper strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
