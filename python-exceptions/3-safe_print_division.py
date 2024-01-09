#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Can't divide by 0, bozo.")
        result = None
        return None
    except Exception as error:  # flags other unexpected errors
        print("Unexpected error: {}".format(error))
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
