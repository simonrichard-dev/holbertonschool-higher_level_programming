#!/usr/bin/python3
""" To JSON string """
import json


def from_json_string(my_string):
    """ function that returns an object (Python data
     structure) represented by a JSON string """

    return (json.loads(my_string))
