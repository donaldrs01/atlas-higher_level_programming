#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    new_list = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:  # checks for divisibility
            new_list[i] = True  # prints true in new list
        else:
            new_list[i] = False  # prints false if not % by 2
    return new_list
