#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return(None)
    length = len(my_list)
    maxi = my_list[0]
    for i in range(0, length):
        if my_list[i] > maxi:
            maxi = my_list[i]
        i += 1
    return(maxi)
