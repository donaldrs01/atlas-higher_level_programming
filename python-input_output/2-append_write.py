#!/usr/bin/python3
"""
Module for function that appends string at end of file
"""


def append_write(filename="", text=""):
    """
    Appends inputted text at end of given file

    Arguments:
        filename (str) : name of file being appended to
        text (str) : text to be appended at end of file

    Returns:
        The number of characters added
    """

    with open(filename, 'a', encoding="utf-8") as file:
        chars_added = file.write(text)

        return chars_added
