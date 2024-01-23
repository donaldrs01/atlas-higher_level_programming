#!/usr/bin/python3
"""
Module that writes object to a text file using JSON rep
"""
import json

def save_to_json(my_obj, filename):
    """
    Writes an Object to a text file using JSON representation

    Args:
        my_obj : object to be saved
        filename : the name of the file
    """
    with open(filename, 'w', encoding="utf-8") as file:
        f.write(json.dumps(my_obj))

