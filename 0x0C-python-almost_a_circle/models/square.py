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

    def __str__(self):
        return ('[Square] ({:d}) {:d}/{:d} - {:d}'.format(self.id, self.x,
                self.y, self.width))

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


def update(self, *args, **kwargs):
        if args:
            new_arg = len(args)

        if args and new_arg != 0:
            if new_arg > 0:
                self.id = args[0]
            if new_arg > 1:
                self.width = args[1]
            if new_arg > 2:
                self.x = args[2]
            if new_arg > 3:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs.get('id')
            if 'size' in kwargs:
                self.width = kwargs.get('size')
                self.height = kwargs.get('size')
            if 'x' in kwargs:
                self.x = kwargs.get('x')
            if 'y' in kwargs:
                self.y = kwargs.get('y')
