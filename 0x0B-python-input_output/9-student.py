#!/usr/bin/python3
"""
Module: 9-student
create a Student class.
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

    def to_json(self):
        """
        self: retrieve a dictionary representation
        of a student instance.
        """
        return (vars(self))
        """ return self.__dict__ """
