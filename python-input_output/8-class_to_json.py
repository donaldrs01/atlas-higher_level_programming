#!/usr/bin/python3
"""
Module for JSON serialization
"""


def class_to_json(obj):
    """
    Converts instance of a class into a format
    that can easily be turned into JSON text

    Arguments:
        obj : object to convert

    Returns:
        dict : object's attributes (dict description)
    """
    return obj.__dict__
