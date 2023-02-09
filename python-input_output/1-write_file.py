#!/usr/bin/python3
""" 1. Write to a file """


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8)
     and returns the number of characters written """

    with open(filename, 'w') as f:
        f = f.write(text)
        return (f)
