#!/usr/bin/python3
"""
Module that divides all elements in a matrix
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elemeents in a matrix by a specific number

    Args:
        matrix (list) : a list of numbers
        div (int) : the divisor

    Errors:
        TypeError: If 'div' is a non-number
        TypeError: If each row of matrix is not the same size
        TypeError: If 'matrix' is not fully made up of integers or floats
        ZeroDivisionError: If 'div' is equal to 0
    """

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
