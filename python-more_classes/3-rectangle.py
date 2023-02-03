#!/usr/bin/python3
"""
    This module contain an empty Rectangle class with
    width and height attributes and also a proprety and
    proprety setter
    It contain also area and perimeter
"""


class Rectangle:
    """ An rectangle class with width and height properties """

    def __init__(self, width=0, height=0):
        """ Initialize a new instance """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ get the width proprety """

        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width proprety """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ get the height proprety """

        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height property """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ returns area of the rectangle """

        area = self.__height * self.__width
        return (area)

    def perimeter(self):
        """ returns perimeter of the rectangle """

        if (self.__width) == 0 or (self.__height) == 0:
            return 0

        return (((self.__width) + (self.__height)) * 2)

    def __str__(self):
        """ print the rectangle with the character # """

        if (self.__height) == 0 or (self.__width) == 0:
            return ("")
        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += '#'
            string += '\n'
        return string[:-1]
