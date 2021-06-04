#!/usr/bin/python3
"""
Module: 4-inherits_from
"""


def inherits_from(obj, a_class):
    """
    Evaluate if the object is an instance of a class
    that inherited from the specified class.
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
