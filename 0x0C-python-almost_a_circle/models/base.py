#!/usr/bin/python3
"""
Module: base
"""


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
