#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # check to see if list is empty
        return None

    max_num = my_list[0]  # iterate through list to find max and assign

    for num in my_list:
        if num > max_num:
            max_num = num

    return max_num
