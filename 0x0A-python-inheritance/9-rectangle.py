#!/usr/bin/python3
"""
Module: 9-rectangle
Create a rectangle class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class represent a rectangle.
    private instance attrib: width, height.

    """

    def __init__(self, width, height):
        """
        initializes an instance.
        args: width, height.
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
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
        return ("[Retangle] {}/{}".format(self.__width, self.__height))
