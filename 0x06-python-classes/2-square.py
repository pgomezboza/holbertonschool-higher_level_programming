#!/usr/bin/python3
"""A class Square"""


class Square:
    """ def of square """

    def __init__(self, size):
        """ create a square """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
