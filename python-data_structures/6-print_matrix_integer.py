#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):  # enumerate gets index i and num
            if i != 0:
                print(" ", end="")
            print("{:d}".format(num), end="")  # prevents default \n print
        print()  # prints new line
