#!/usr/bin/python3
"""
Module that lists integers representing the Pascal Triangle
"""


def pascal_triangle(n):
    """
    Pascal Triangle function that creates n row of triangle
    In Pascal's Triangle, the current element is the sum of the
    two elements directly above it. This function re-creates that logic.

    Args:
        n : the number of rows on triangle
    """
    if n <= 0:
        return []
    else:
        triangle = []
        for i in range(n):  # iterate through each row of triangle
            row = [1] * (i + 1)  # first element always 1 : prev_row + 1
            for j in range(1, i):  # iterates through each element in new row
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                #  [i - 1] = previous row in triangle
                #  [j - 1] = previous element on row
                #  gets sum of two elements directly above current
            triangle.append(row)

        return triangle

# Test
# n = 7
# result = pascal_triangle(n)
# print(result)
