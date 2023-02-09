#!/usr/bin/python3
""" Rectangle that inherits from module with class BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ An rectangle class with width and height properties """

    def __init__(self, width, height):
        """ Initialize a new instance """

        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)