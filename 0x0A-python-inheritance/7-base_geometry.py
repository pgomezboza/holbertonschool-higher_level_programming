#!/usr/bin/python3
"""
Module: 7-base_geometry
"""


class BaseGeometry:
    """
    Base class with public instance method.
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates that value is an integer greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
