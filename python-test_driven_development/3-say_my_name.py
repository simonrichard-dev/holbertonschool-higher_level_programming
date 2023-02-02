#!/usr/bin/python3


""" Write a function that prints My name is <first name> <last name> """
def say_my_name(first_name, last_name=""):
    """ first_name must be strings otherwise, raise a TypeError exception with\
        the message first_name must be a string.
        last_name must be strings otherwise, raise a TypeError exception with\
        the message first_name must be a string """

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    if first_name == None:
        raise TypeError('first_name must be a string')
    if last_name == None:
        raise TypeError('last_name must be a string')
    if first_name == None and last_name == None:
        raise TypeError("say_my_name() missing 2 required\
                positionnal arguments: 'first_name' and 'last_name'")
    print("My name is {} {}".format(first_name, last_name))
