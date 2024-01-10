#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    convert_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0
    prev_value = 0

    for char in roman_string:  # assigns chars (invalid) to 0
        current_value = convert_dict.get(char, 0)

        if current_value > prev_value:  # deals with cases like 'IX'
            result += current_value - prev_value
        else:
            result += current_value

        prev_value = current_value  # updates prev_value for next loop

    return result
