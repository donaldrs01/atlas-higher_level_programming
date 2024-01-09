#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisonError:
        print("Can't divide by 0, bozo.")
        result = None
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
