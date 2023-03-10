#!/usr/bin/python3
""" First Rectangle """
from models.base import Base


class Rectangle(Base):
    """ inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ public method that returns the area
         value of the Rectangle instance """

        area = self.__height * self.__width
        return (area)

    def display(self):
        """ print the rectangle with the character # """

        for i in range(self.__y):
            print("")
        if (self.__height) == 0 or (self.__width) == 0:
            return ("")
        string = ""
        for i in range(self.__height):
            for j in range(self.__x):
                string += ' '
            for j in range(self.__width):
                string += '#'
            string += '\n'
        print(string[:-1])

    def __str__(self):
        """ Returns the [Rectangle] [<id>] - <width>/<height> """

        identifier = self.id
        h = self.__height
        w = self.__width
        x = self.__x
        y = self.__y

        return f"[Rectangle] ({identifier}) {x}/{y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """ Method that assigns an argument to each attribute"""
        if args:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[arg]
                if arg == 1:
                    self.width = args[arg]
                if arg == 2:
                    self.height = args[arg]
                if arg == 3:
                    self.x = args[arg]
                if arg == 4:
                    self.y = args[arg]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Method that returns the dictionary
        representation of a Rectangle """
        dictionary = {
            'id': self.id,
            'height': self.height,
            'width': self.width,
            'x': self.x,
            'y': self.y}
        return (dictionary)
