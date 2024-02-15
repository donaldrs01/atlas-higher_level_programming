#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_key = max(a_dictionary, key=a_dictionary.get)
    # get retreives value associated with given key
    # key parameter function - searches and grabs value from dict
    return best_key
