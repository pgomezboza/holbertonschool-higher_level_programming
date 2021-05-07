#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    n = 0
    dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for x, y in zip(roman_string, roman_string[1:]):
        if x not in dictionary.keys():
            return 0
        elif dictionary[x] >= dictionary[y]:
            n += dictionary[x]
        else:
            n -= dictionary[x]
    n += dictionary[roman_string[-1]]
    return (n)
