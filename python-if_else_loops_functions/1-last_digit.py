#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
original_number = number
if number < 0:
    last_digit = (-1) * number % 10
    last_digit = (-1) * last_digit
else:
    last_digit = number % 10
if last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not \
0")
