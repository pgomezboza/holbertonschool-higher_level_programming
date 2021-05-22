#!/usr/bin/python3
"""
Module: add_integer
Description: This module supplies one method "add_integer".
Parameters: a, b with int or float type.
"""


def add_integer(a, b=98):
    """
    Return addition of two numbes
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
