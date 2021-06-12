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
        """
        Updates attributes of instance.
        args: id, size, x, y.
        """
        if args:
            n_arg = len(args)

        if args and n_arg != 0:
            if n_arg > 0:
                self.id = args[0]
            if n_arg > 1:
                self.size = args[1]
            if n_arg > 2:
                self.x = args[2]
            if n_arg > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Return dictionary representation.
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}