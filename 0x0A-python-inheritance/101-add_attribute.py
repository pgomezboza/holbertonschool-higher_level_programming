#!/usr/bin/python3
"""
Module: 101-add_attribute
"""


def add_attribute(objeto, new_attrib, value):
    """
    add attribute to object
    """

    if hasattr(objeto, "__dict__") is True:
        setattr(objeto, new_attrib, value)
    else:
        raise TypeError("can't add new attribute")
