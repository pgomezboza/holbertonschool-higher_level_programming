#!/usr/bin/python3
"""
Module: base
"""
import json


class Base:
    """
    Base Class
    nb: number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialize attributes
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns JSON string representation of list_dictionaries.
        """
        if list_dictionaries and len(list_dictionaries) is not 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
