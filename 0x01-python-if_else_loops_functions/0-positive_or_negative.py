#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    print('{0} is zero'.format(number))
elif number < 0:
    print('{0} is negative'.format(number))
elif number > 0:
    print('{0} is positive'.format(number))
