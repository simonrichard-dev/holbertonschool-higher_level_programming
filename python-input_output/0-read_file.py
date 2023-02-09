#!/usr/bin/python3
""" 0. Read file """


def read_file(filename=""):
    """ function that reads a text file (UTF8)
     and prints it to stdout """

    with open(filename, 'r') as f:
        file = f.read()
        print(file, end="")
