#!/usr/bin/python3
"""
Module for same_class function that evaluates whether
passed object is exact instance of specified class
"""


def is_same_class(obj, a_class):
    """
    Method that evaluates whether passed object
    is instance of specified class

    Args:
        obj : the object to evaluate
        a_class : the type of class

    Returns:
        True is obj is exact instance of a_class.
        False otherwise
    """
    return type(obj) is a_class
