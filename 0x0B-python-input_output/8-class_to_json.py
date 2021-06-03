#!/usr/bin/python3
"""
Module: 8-class_to_json
Dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    args:
        obj: object to serialize
    return: dictionnary description of object
    """
    return (vars(obj))
    """ return obj.__dict__ """
