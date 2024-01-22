#!/usr/bin/python3
"""
Module for function that converts string object into JSON representation
"""
import json


def to_json_string(my_obj):
    """
    Returns JSON representation of an object (str)

    Args:
        my_obj (str) : objected to be converted

    Returns:
        str : JSON representation of object
    """
    return json.dumps(my_obj)

