#!/usr/bin/python3
"""
Module: Rectangle
"""


class Rectangle:
    """ Rectangle class """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Return width value
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Sets the width of a Rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Return height value
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Sets the height of a Rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return area of Rectangle
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__height * self.__width)

    def perimeter(self):
        """
        Return perimeter of Rectangle
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return ((self.__width + self.__height) * 2)
