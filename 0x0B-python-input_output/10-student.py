#!/usr/bin/python3
"""
Module: 10-student
"""


class Student:
    """
    Representation of a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes the student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        self: retrieve a dictionary representation
        of a student instance.
        attrs: list of attributes.
        """
        if (attrs) and type(attrs) is list:
            for n in attrs:
                if type(n) is not str:
                    return (self.__dict__)
                else:
                    new_dict = {}
                    for m in attrs:
                        if m in self.__dict__:
                            new_dict.update({m: self.__dict__[m]})
                    return new_dict
        else:
            return (self.__dict__)
