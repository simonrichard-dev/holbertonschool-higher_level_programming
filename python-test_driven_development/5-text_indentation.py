#!/usr/bin/python3
""" function that prints a text with 2 new lines after each of these\
    characters: ., ? and : """


def text_indentation(text):
    """ text must be a string, otherwise raise a TypeError exception\
        with the message text must be a string.
        There should be no space at the beginning or at the end of\
        each printed line.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        i = 0
        for k in text:
            if i == 0:
                if k == " ":
                    continue
                else:
                    i = 1
            if i == 1:
                if k == '.' or k == '?' or k == ':':
                    print(k + '\n')
                    i = 0
                else:
                    print(k, end="")
