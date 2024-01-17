#!/usr/bin/python3
"""
Module for function that searches for characters and prints new lines
"""


def text_indentation(text):
    """
    Function that searches for special characters and prints 2 new lines

    Args:
        text (str) : the inputted text

    Errors:
        TypeError : if text is not a proper string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    break_chars = [".", "?", ":"]
    new_line = ""
    for char in text:
        if char in break_chars:
            new_line += char + "\n\n"
        else:
            new_line += char
    print("{}".format(new_line), end="")
