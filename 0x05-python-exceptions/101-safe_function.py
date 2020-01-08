#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except ZeroDivisionError:
        result = None
        sys.stderr.write("Exception: division by zero\n")
    except IndexError:
        result = None
        sys.stderr.write("Exception: list index out of range\n")

    return result
