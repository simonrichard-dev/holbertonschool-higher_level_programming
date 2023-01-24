#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if idx < 0 or idx > len(my_list):
        return(my_list)
    for number in range(0, length):
        if number == idx:
            del(my_list[idx])
    return (my_list)
