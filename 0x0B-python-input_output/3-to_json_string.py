#!/usr/bin/python3
"""
Module: 3-to_json_string
"""
import json


def to_json_string(my_obj):
    """
    args:
        my_obj, string to represent.
        return: JSON representation of my_obj.
    """
    return (json.dumps(my_obj))
