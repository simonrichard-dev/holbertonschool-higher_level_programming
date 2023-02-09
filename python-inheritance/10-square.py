#!/usr/bin/python3
""" Square that inherits from module with class Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ An square class with width and height properties """

    def __init__(self, size):
        """ Initialize a new instance """
        self.__size = size
        self.integer_validator('size', size)


    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)