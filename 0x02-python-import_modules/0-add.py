#!/usr/bin/python3
from add_0 import add

# The code only is executed when isn't imported by __import__
if __name__ == "__main__":
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
