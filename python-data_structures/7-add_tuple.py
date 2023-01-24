#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = []
    for i in range(0, 2):
        if len(tuple_a) < 2:
            tuple_a += (0, 0)
        if len(tuple_b) < 2:
            tuple_b += (0, 0)
        res.append(tuple_a[i]+tuple_b[i])
        i += 1
    res = tuple(res)
    return(res)
