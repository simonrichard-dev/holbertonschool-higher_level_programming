#!/usr/bin/python3
""" Exact same object """


def is_kind_of_class(obj, a_class):
    """ returns True if the object is an instance of
    a class that inherited from the specifiec class ;
    otherwise False.
    Args:
        obj: object
        a_class: class type
    """

    return (isinstance(obj, a_class))
