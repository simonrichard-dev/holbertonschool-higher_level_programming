#!/usr/bin/python3
""" First Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns the [Rectangle] [<id>] - <size> """

        identifier = self.id
        size = self.width
        x = self.x
        y = self.y

        return f"[Square] ({identifier}) {x}/{y} - {size}"

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.__size = value
