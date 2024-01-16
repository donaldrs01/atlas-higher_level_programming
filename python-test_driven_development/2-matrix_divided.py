#!/usr/bin/python3
"""
Module that divides all elements in a matrix
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elemeents in a matrix by a specific number
    
    Args:
        matrix (set) : a set of numbers
        div (int) : the divisor

    Errors:
        TypeError: If 'div' is a non-number
        TypeError: If each row of matrix is not the same size
        TypeError: If 'matrix' is not fully made up of integers or floats
        ZeroDivisionError: If 'div' is equal to 0
    """

