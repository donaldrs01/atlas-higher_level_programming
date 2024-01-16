#!/usr/bin/python3
"""
Module for function that searches for characters and prints new lines
"""


def text_indentation(text):
    """
    Function that searches for special characters and follows them with 2 new lines

    Args:
        text (str) : the inputted text

    Errors:
        TypeError : if text is not a proper string
    """

    if type(text) is not string:
        raise TypeError("text must be a string")

