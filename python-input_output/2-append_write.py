#!/usr/bin/python3
""" 2. Append to a file """


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text file
     (UTF8) and returns the number of characters added: """

    with open(filename, 'a') as f:
        string = f.write(text)
        return (string)
