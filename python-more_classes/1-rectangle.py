#!/usr/bin/python3
"""
    This module contain an empty Rectangle class with
    width and height attributes and also a proprety and
    proprety setter
"""


class Rectangle:
    """ An rectangle class with width and height properties """

    def __init__(self, width=0, height=0):
        """ Initialize a new instance """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ get the width proprety """

        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width proprety """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ get the height proprety """

        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height property """

        if type(value) is not int:
            raise TypeError("heigth must be an integer")
        if size < 0:
            raise ValueError("heigth must be >= 0")
        else:
            self.__height = value