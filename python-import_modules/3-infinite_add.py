#!/usr/bin/python3
import sys

if __name__ == "__main__":
    print(sum(int(number) for number in sys.argv[1:]))
