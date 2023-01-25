#!/usr/bin/python3
def search_replace(my_list, search, replace):
    length = len(my_list)
    new_list = []
    for i in range(0, length):
        if my_list[i] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])
        i += 1
    return(new_list)
