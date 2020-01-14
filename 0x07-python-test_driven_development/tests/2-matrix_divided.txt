===============================
2. Division of matrix module
===============================

Import module:
==============
    >>> matrix_divided = __import__('2-matrix_divided').matrix_divided


Function:
=========
Write a function that divides all elements of a matrix.


Operations:
===========
 * matrix must be a list of lists of integers or floats,
   otherwise raise a TypeError exception with the message
   'matrix must be a matrix (list of lists) of integers/floats'.

 * Each row of the matrix must be of the same size, 
   otherwise raise a TypeError exception with the message
   'Each row of the matrix must have the same size'.

 * div must be a number (integer or float), 
   otherwise raise a TypeError exception with the message
   'div must be a number'.

 * div can’t be equal to 0, otherwise raise a ZeroDivisionError
   exception with the message 'division by zero'.

 * All elements of the matrix should be divided by div, 
   rounded to 2 decimal places.


Section // Non-Parameters
=========================

Test case #0: A test case without parameters

    >>> matrix_divided()
    Traceback (most recent call last):
    TypeError: matrix_divided() missing 2 required positional arguments: 'matrix' and 'div'


Section // Correct Matrix
=========================

Test case #1: A test case with integer elements and integer divider

    >>> matrix = [[1, 2, 3],[4, 5, 6]]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

Test case #2: A test case with integer and float elements and float divider

    >>> matrix = [[1.0, -2.0, -3.0],[-4.0, 5.0, -6.0]]
    >>> matrix_divided(matrix, 3.0)
    [[0.33, -0.67, -1.0], [-1.33, 1.67, -2.0]]

Test case #3: A test case with infinity elements to divide

    >>> matrix = [[1e400, 1e500, 1e600],[1e900, 1e800, 1e700]]
    >>> matrix_divided(matrix, 3)
    [[inf, inf, inf], [inf, inf, inf]]


Section // Incorrect Matrix
===========================

Test case #4: A test case with a matrix as a string

    >>> matrix = 'Monty Python'
    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Test case #5: A test case with the rows of an inconsistent size matrix

    >>> matrix = [[1, 2, 3], 4, 5, 6]
    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Test case #6: A test case with lists of integers and floats within
the rows of the matrix

    >>> matrix = [[[10.0], [65], [37.0]],[[40], [15.0], [66]]]
    >>> matrix_divided(matrix, 2)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Test case #7: A test case with strings within the rows of the matrix

    >>> matrix = [['1', '2', '3'], ['4', '5', '6']]
    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Test case #8: A test case with integers instead of lists in the matrix

    >>> matrix = [1, 2, 3, 4, 5, 6]
    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Test case #9: A test case with a string acting as a row

    >>> matrix = [[1, 2, 3], [4, 5, 6], 'Monty Python']
    >>> matrix_divided('matrix', 2)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Test case #10: A test case with a matrix of empty lists
    >>> matrix = []
    >>> type(matrix_divided(matrix, 3))
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Test case #11: A test case with a matrix of empty lists
    >>> matrix = [[], []]
    >>> type(matrix_divided(matrix, 3))
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats


Section // Bad Divisor
======================

Test case #12: A test case with a 'None' divider

    >>> matrix = [[1, 2, 54.0], [24, 35.5, 6]]
    >>> matrix_divided(matrix, None)
    Traceback (most recent call last):
    TypeError: div must be a number

Test case #13: A test case with a string divider

    >>> matrix = [[1, 2, 54.0], [24, 35.5, 6]]
    >>> matrix_divided(matrix, 'Monty Python')
    Traceback (most recent call last):
    TypeError: div must be a number

Test case #14: A test case with a NaN divider

    >>> matrix = [[1, 2, 54.0], [24, 35.5, 6]]
    >>> matrix_divided(matrix, float('nan'))
    Traceback (most recent call last):
    TypeError: div must be a number

Test case #15: A test case with a zero as a divisor

    >>> matrix = [[10.0, 65, 37.0],[40, 15.0, 66]]
    >>> matrix_divided(matrix, 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero


Section // Inconsistent rows
======================

Test case #16: A test case with inconsistent rows

    >>> matrix = [[1, 2, 3], [4, 5]]
    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    TypeError: Each row of the matrix must have the same size


Section // Types
======================

Test case #17: A test case with the type of value returned

    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> type(matrix_divided(matrix, 3))
    <class 'list'>
