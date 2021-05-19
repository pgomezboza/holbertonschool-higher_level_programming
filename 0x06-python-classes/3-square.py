#!/usr/bin/python3
""" A class Square """


class Square:
    """ def of square """

    def __init__(self, size=0):
        """ create square """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ return size squared """
        return (self.__size) ** 2
