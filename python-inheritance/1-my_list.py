#!/usr/bin/python3
"""
Module for a sub-class 'MyList' that inherits from class 'list'
"""


class MyList(list):
    """
    Sub-class of 'list'

    """

    def print_sorted(self):
        """
        Method that prints list in ascending order
        """
        print(sorted(self))
