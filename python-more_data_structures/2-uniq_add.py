#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for i in my_list:
        if i not in new_list:  # only adds unique values to new list
            new_list.append(i)
    return sum(new_list)

my_list = [1, 2, 2, 3, 4, 5, 5]
result = uniq_add(my_list)
print(result)
