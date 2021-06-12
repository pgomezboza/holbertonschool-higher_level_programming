#!/usr/bin/python3
"""
Module: Rectangle.
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle object from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        id = super().__init__(id)

    @property
    def width(self):
        """
        Gets width of rectangle instance.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets width of rectangle.
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets height of rectangle instance.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets height of rectangle instance.
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Gets "x" value.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets "x" value.
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Gets "y" value.
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets "y" value.
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate area of rectangle
        """

        return self.__width * self.__height

    def display(self):
        """
        Prints the rectangle using '#'
        """

        for y in range(0, self.__y):
                print()
        for m in range(0, self.__height):
            for x in range(0, self.__x):
                print(' ', end='')
            for n in range(0, self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """
        Create string representation.
        """

        return ('[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        Updates attributeis values
        args:id, width, height,x and y.
        """

        if args:
            new_arg = len(args)

        if args and new_arg != 0:
            if new_arg > 0:
                self.id = args[0]
            if new_arg > 1:
                self.width = args[1]
            if new_arg > 2:
                self.height = args[2]
            if new_arg > 3:
                self.x = args[3]
            if new_arg > 4:
                self.y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs.get('id')
            if 'width' in kwargs:
                self.width = kwargs.get('width')
            if 'height' in kwargs:
                self.height = kwargs.get('height')
            if 'x' in kwargs:
                self.x = kwargs.get('x')
            if 'y' in kwargs:
                self.y = kwargs.get('y')
