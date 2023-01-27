#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for x in range(x):
        try:
            print("{:d}".format(my_list[x]), end="")
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            j += 1
    print()
    return(j)
