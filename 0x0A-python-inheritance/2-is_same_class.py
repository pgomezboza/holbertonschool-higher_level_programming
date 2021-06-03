#!/usr/bin/python3
"""
Module: 2-is_same_class
"""


def is_same_class(obj, a_class):
    """
    Determine if obj is an instance of a_class.
        args:
            obj: object to look.
            a_class: class to verify the instance.
        return:
            true: if obj is an instance of a_class.
            false: otherwise.
    """
    if type(obj) is a_class:
        return True
        return False
    """ return (type(obj) == a_class) """
