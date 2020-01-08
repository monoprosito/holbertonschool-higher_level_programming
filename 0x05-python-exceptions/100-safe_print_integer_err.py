#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
        return True
    except ValueError as ve:
        sys.stderr.write("Exception: " + str(ve) + "\n")
        return False
    except TypeError as ve:
        sys.stderr.write("Exception: " + str(ve) + "\n")
        return False
