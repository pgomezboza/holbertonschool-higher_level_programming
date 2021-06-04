#!/usr/bin/python3
"""
Module: 9-rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class represent a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes an instance.
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """
        return area of rectangle.
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        return a formatted string.
        """
        return ("[Retangle] {:d}/{:d}".format(self.__width, self.__height))
