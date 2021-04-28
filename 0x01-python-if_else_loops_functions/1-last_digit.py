#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
great = "and is greater than 5"
less = "and is less than 6 and not 0"
zero = "and is 0"

if n > 0:
    ln = num % 10
else:
    ln = num % (-10)

if ln > 5:
    msg = great
elif ln is 0:
    msg = zero
elif ln < 6 and not 0:
    msg = less
print("Last digit of", num, "is", ln, msg)
