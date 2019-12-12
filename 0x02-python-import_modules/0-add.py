#!/usr/bin/python3
import add_0 as add_op

# The code only is executed when isn't imported by __import__
if __name__ == "__main__":
    """

    Prints the result of the addition between two numbers

    """
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add_op.add(a, b)))
