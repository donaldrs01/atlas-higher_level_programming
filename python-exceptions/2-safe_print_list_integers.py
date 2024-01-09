#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    word_count = 0
    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end=" ")
                word_count += 1
    except IndexError:
        pass  # allows IndexError to pass without crash
    finally:
        print()
        return word_count
