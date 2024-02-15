#!/usr/bin/python3
"""
Module for inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Function evaluates whether obj is instance of class
    that inherited from specified class

    Args:
        obj : the object to evaluate
        class : the specified class

    Returns:
        True if obj is instance of class inherited from a_class
        False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
    # type(obj) gets type of object and then checks
    # whether that type is subclass of 'a_class'
