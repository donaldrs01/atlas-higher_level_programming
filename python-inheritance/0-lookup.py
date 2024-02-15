#!/usr/bin/python3
"""
Module allowing us to lookup a list of all attributes
and methods of object passed through function
"""


def lookup(obj):
    """
    Takes object as argument and returns a list of all
    attributes and methods associated with that object

    Args:
        obj: the object whose methods will be retrieved
    """
    return dir(obj)
