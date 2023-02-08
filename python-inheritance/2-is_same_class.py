#!/usr/bin/python3
""" Exact same object """


def is_same_class(obj, a_class):
    """ returns True if the object is exctly
     an instance of the specified class;
      otherwise False.
    Args:
        obj: object
        a_class: class type
    """
    if type(obj) is a_class:
        return True
    else:
        return False
