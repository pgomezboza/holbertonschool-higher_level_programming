#!/usr/bin/python3
"""
Module: 5-save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    args:
        my_obj: object to be saved
        filename: name of file to be saved
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
        """return (file.write(json.dumps(my_obj)))"""
