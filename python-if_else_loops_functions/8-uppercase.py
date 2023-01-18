#!/usr/bin/python3
def uppercase(str):
    for alpha in str:
        alpha = ord(alpha)
        if alpha in range(97, 123):
            alpha = alpha - 32
        print("{:c}".format(alpha), end="")
    print("")
