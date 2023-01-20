#!/usr/bin/python3
import sys

if __name__ == "__main__":
    for nb_argument in range(0, len(sys.argv)):
        nb_argument += 1

    nb_argument = nb_argument - 1

    if nb_argument == 0:
        print("{} arguments.".format(nb_argument))
    elif nb_argument == 1:
        print("{} argument.".format(nb_argument))
    else:
        print("{} arguments:".format(nb_argument))

    for letter in range(0, len(sys.argv)):
        if letter != 0:
            print("{}: {}".format(letter, sys.argv[letter]))
