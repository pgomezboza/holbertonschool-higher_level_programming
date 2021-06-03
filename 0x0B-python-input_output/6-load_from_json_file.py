#!/usr/bin/python3
"""
Module: 6-load_from_json_file.py
create an object from JSON file.
"""
import json


def load_from_json_file(filename):
    """
    args:
        filename: name of JSON file
    return: object
    """
    with open(filename) as file:
        return (json.load(file))
    """ with open(filename, 'r', encoding='utf-8') as file: """
