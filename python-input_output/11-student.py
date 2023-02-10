#!/usr/bin/python3
""" Student to JSON """


class Student ():
    """ class Student that defines a student by:
        Public instance attributes:
         - first_name
         - last_name
         - age """

    def __init__(self, first_name, last_name, age):
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        if attrs is None:
            return vars(self)
        else:
            return {k: v for k, v in vars(self).items() if k in attrs}

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
