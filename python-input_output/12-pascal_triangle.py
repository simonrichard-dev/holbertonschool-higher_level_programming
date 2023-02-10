#!/usr/bin/python3
"""
    Module that creates a function: pascal_triangle
"""


def pascal_triangle(n):
    """ Returns a list of lists of integers
        representing the Pascal's triangle of n
    """
    pas_tri = []
    if n <= 0:
        return pas_tri

    for i in range(n):
        row = []
        for j in range(i + 1):
            if (j == 0) or (j == i):
                r = 1
            else:
                r = pas_tri[i - 1][j - 1] + pas_tri[i - 1][j]
            row.append(r)
        pas_tri.append(row)
    return pas_tri
