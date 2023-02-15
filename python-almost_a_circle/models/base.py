#!/usr/bin/python3
""" Base class """
import json


class Base:
    """ private class attribute nb_objects = 0 """
    __nb_object = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of
        list_dictionaries """
        if list_dictionaries:
            return (json.dumps(list_dictionaries))
        else:
            return ("[]")
