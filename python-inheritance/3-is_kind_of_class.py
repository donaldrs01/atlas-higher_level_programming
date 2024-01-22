#!/usr/bin/python3
"""
Module evaluates for whether object is instance or sub-instance
of specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Function that checks if object is instance of / inherited from
    the specified class

    Args:
        obj : object to evaluate
        a_class: specified class

    Returns:
        True is obj is instance of a_class or its subclass
        False otherwise
    """
    return isinstance(obj, a_class)
