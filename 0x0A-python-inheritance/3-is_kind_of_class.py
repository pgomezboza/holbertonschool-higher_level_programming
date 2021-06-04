#!/usr/bin/python3
"""
Module: 3-is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    finds if obj is an instance of a_class or a class
    inherited from a_class.
    args:
        obj: objecto to look
        a_class: class to be check
    return: true or false.
    """
    if issubclass(type(obj), a_class):
        return True
    return False
