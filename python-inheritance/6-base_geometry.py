#!/usr/bin/python3
""" Geometry module with class BaseGeometry """


class BaseGeometry():
    """ raise an Exception with the message
    'area() is not implemented'
    """

    def area(self):
        raise Exception("area() is not implemented")
