#!/usr/bin/python3
"""
Module for reading a file and printing content to stdout
"""


def read_file(filename=""):
    """
    Reads file and prints it out to stdout

    Args:
        filename (str) : the name of the text file
    """

    with open(filename, encoding="utf-8") as file:
        read_data = file.read().rstrip('\n')
        if read_data:
            print(read_data)
