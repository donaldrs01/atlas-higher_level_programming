#!/usr/bin/python3
"""
Module containing script to add args to a list
and then save them to a file
"""
from pathlib import Path
import json
import sys


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file using JSON representation

    Args:
        my_obj : object to be saved
        filename : name of the file
    """
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(json.dumps(my_obj))


def load_from_json_file(filename):
    """
    Loads an Object from a JSON file

    Args:
        filename : name of the JSON file

    Returns:
        obj : Object loaded from the file
    """
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    filename = "add_item.json"
    #  execute when run directly from command line

    my_list = load_from_json_file(filename)
    #  loads existing list from add_item

    my_list.extend(sys.argv[1:])
    # add command line arguments to list

    save_to_json_file(my_list, filename)
    #  saves updated list
