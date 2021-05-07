#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        for n in a_dictionary:
            if n == key:
                a_dictionary[n] = value
    else:
        a_dictionary[key] = value
    return (a_dictionary)
