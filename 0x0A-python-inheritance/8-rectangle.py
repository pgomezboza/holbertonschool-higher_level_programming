#!/usr/bin/python3
"""
Module: 8-rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class represent a rectangle
    """

    def __init__(self, width, height):
        """
        Initializes an instance.
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
