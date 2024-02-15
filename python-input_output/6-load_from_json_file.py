#!/usr/bin/python3
"""
Module that creates an object from a JSON file
"""

import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a JSON file

    Args:
        filename : the name of the JSON file

    Returns:
        obj : the Object created from the file
    """

    with open(filename, 'r', encoding="utf-8") as file:
        #  reads file and converts JSON data into Object
        return json.load(file)
