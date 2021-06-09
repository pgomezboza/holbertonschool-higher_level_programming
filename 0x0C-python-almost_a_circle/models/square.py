#!/usr/bin/python3
"""
Module: Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherited from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
            super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Gets size of square
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        Sets size value
        """

        self.width = value
        self.height = value
