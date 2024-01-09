#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
    # lambda allows us to create our own function
    # map applies it to all elements of my_list
