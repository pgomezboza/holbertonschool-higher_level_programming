#!/usr/bin/python3
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
greater = "and is greater than 5"
less = "and is less than 6 and not 0"
zero = "and is 0"

if number > 0:
 ln = number % 10
else:
 ln = number % (-10)

if ln > 5:
 msg = greater
elif ln is 0:
 msg = zero
elif ln < 6 and not 0:
 msg = less
print("Last digit of", number, "is", ln, msg)
