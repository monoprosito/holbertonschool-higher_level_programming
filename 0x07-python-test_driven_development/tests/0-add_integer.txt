===============================
0. Integer addition module
===============================

Import module:
==============
    >>> add_integer = __import__('0-add_integer').add_integer


Function:
=========
Write a function that adds 2 integers.


Operations:
===========
‘a’ and ‘b’ must be integers or floats, otherwise raise a TypeError exception
with the message 'a must be an integer' or 'b must be an integer'.


Section // Non-Parameters
=========================

Test case #0: A test case without parameters

    >>> add_integer()
    Traceback (most recent call last):
    TypeError: add_integer() missing 1 required positional argument: 'a'

Test case #1: A test case for an argument with no assigned value

    >>> add_integer(a, 123)
    Traceback (most recent call last):
    NameError: name 'a' is not defined

Test case #2: A test case for using the default value of parameter 'b'

    >>> add_integer(5)
    103

Test case #3: A test case for using the default value of parameter 'b'
with the float parameter 'a'

    >>> add_integer(1.0, )
    99


Section // Numbers
==================

Test case #4: A test case between two integers

    >>> add_integer(1, 2)
    3

Test case #5: A test case between two floats

    >>> add_integer(10.0, 15.0)
    25

Test case #6: A test case between integer and float

    >>> add_integer(6, 20.0)
    26

Test case #7: A test case between float and integer

    >>> add_integer(10.0, 8)
    18

Test case #8: A test case between two negatives floats

    >>> add_integer(-6.5, -5)
    -11

Test case #9: A test case between float and negative integer

    >>> add_integer(100.5, -10)
    90

Test case #10: A test case between integer and infinity float

    >>> add_integer(5, 1e400)
    Traceback (most recent call last):
    OverflowError: cannot convert float infinity to integer

Test case #11: A test case between infinity float and negative integer

    >>> add_integer(999e9999, -1)
    Traceback (most recent call last):
    OverflowError: cannot convert float infinity to integer


Section // Non-Numbers
======================

Test case #12: A test case with the first parameter of type 'None'

    >>> add_integer(None, 2)
    Traceback (most recent call last):
    TypeError: a must be an integer

Test case #13: A test case with the second parameter of type 'None'

    >>> add_integer(5, None)
    Traceback (most recent call last):
    TypeError: b must be an integer

Test case #14: A test case with the first parameter of type 'list'

    >>> add_integer([1, 2], 15)
    Traceback (most recent call last):
    TypeError: a must be an integer

Test case #15: A test case with the second parameter of type 'str'

    >>> add_integer(1, "Monty Python")
    Traceback (most recent call last):
    TypeError: b must be an integer


Section // Types
======================

Test case #16: A test case to check the returned integer type

    >>> type(add_integer(5, 5))
    <class 'int'>
