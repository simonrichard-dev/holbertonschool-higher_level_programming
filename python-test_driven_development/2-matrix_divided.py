#!/usr/bin/python3
""" function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ matrix must be a list of lists of integers or floats
    each row of the matrix must be of the same size
    div must be a number (integer or float)
    div can’t be equal to 0 """

    for row in matrix:
        for data in row:
            if type(data) is not int and type(data) is not float:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of "
                                "integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
                raise TypeError("Each row of the matrix "
                                "must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(a / div, 2) for a in row] for row in matrix]
    return new_matrix
