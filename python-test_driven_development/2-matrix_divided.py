#!/usr/bin/python3
""" function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ matrix must be a list of lists of integers or floats
    each row of the matrix must be of the same size
    div must be a number (integer or float)
    div can’t be equal to 0 """
    if type(div) is not int or type(div):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if div == None:
        raise TypeError('div must be a number')

    if div == NaN:
        raise TypeError('div must be a number')

    new_matrix = list(map(lambda row: list(map(lambda x: round(x / div, 2), row)), matrix))
    return new_matrix
