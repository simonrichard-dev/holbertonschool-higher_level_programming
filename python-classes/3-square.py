#!/usr/bin/python3
""" Area of a square - Python """


class Square:
    """ Area of a square - Python """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return(self.__size * self.__size)
