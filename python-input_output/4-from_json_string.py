#!/usr/bin/python3
"""
Module that returns an object represented by JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by JSON string

    Args:
        my_str (str) : JSON string

    Returns:
        object : Python data struct represented by JSON string
    """
    return json.loads(my_str)  # deserializes JSON string into object
