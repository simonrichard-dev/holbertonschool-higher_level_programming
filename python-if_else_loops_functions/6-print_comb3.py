#!/usr/bin/python3
i = 0
j = 1
while i < 8:
    print("{}{}".format(i, j), end=", ")
    if j == 9:
        i += 1
        j = i + 1
    else:
        j = j + 1
print("89")
