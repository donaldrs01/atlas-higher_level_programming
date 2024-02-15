#!/usr/bin/python3
"""
Module that contains function that writes string
to text file and returns # of characters written
"""


def write_file(filename="", text=""):
    """
    Writes inputted text into given file

    Arguments:
        filename (str) : name of file being added to
        text (str) : text to be written into file

    Return:
        The number of characters written
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        chars_written = file.write(text)

    return chars_written
