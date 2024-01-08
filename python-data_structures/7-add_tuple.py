#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)  # pads tuples w/ 0 if smaller than 2 elements
    tuple_b += (0, 0)

    return (sum(tuple_a[:2]), sum(tuple_b[:2]))
