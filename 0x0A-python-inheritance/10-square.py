#!/usr/bin/python3
"""
Module: 10-square
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


class Square(Rectangle):
    """
    represent a square.
    """

    def __init__(self, size):
        """
        initialize a square.
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        return area of squared
        """
        return (self.__size ** 2)
