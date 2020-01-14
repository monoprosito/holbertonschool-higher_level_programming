#!/usr/bin/python3
"""A module to divides all elements of a matrix.

This module is in charge of dividing all the values of a matrix
according to a divisor given by the user. For the program to work
properly, the following aspects must be taken into account:

    * The matrix must  must be a list of lists of integers or floats.
    * Each row of the matrix must be of the same size.
    * The divisor must be a number (integer or float) other than 0.
    * The division of all elements of the matrix is rounded off
    to 2 decimal places.
    * The result is delivered in a new matrix.

"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    This function takes the data sent by the user to verify
    that the matrix contains lists within it and that each
    list contains integer or floating type numbers.
    The result of the splitting operation is then added to a
    new list in a new matrix with the same matrix structure
    given by the user.

    In case the format of the matrix is incorrect
    or the divisor is not a number, this function
    will raise an error.

    Args:
        matrix (:obj:`list` of :obj:`list`): The matrix to be divided.
        div (int): The divisor number.

    Returns:
        list: A new matrix with all elements divided.

    Raises:
        TypeError: If `matrix` list of lists of integers or floats or
            if `div` is not a number.
        ZeroDivisionError: If `div` is equal to `0`.

    """

    check_for_list(matrix)
    check_for_divisor(div)

    elem_sizes = set()
    new_list = list()

    for elem in matrix:
        if check_for_list(elem) is False:
            raises_matrix_type_error()

        elem_sizes = check_row_size_inconsistency(elem_sizes, elem)
        values = []

        for value in elem:
            if check_for_number(value) is False:
                raises_matrix_type_error()

            values.append(round(value / div, 2))

        new_list.append(values)

    return new_list


def check_for_list(value):
    """

    Check if the value is of type list

    Args:
        value (any): The value to verify.

    Raises:
        TypeError: If `value` isn't a list.

    """

    if type(value) is not list or len(value) == 0:
        raises_matrix_type_error()


def check_for_divisor(div):
    """

    Check if the divisor is integer, float or zero

    Args:
        div (any): The divisor to verify.

    Raises:
        TypeError: If `value` isn't integer or float.
        ZeroDivisionError: If `div` is equal to `0`.

    """

    if check_for_number(div) is False:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')


def check_for_number(value):
    """Check if the value is integer or float

    Args:
        value (any): The value to verify.

    Returns:
        bool: True if successful, False otherwise.

    """

    if type(value) is not int and type(value) is not float:
        return False

    """ Check for a NaN value """
    if value != value:
        return False

    return True


def check_row_size_inconsistency(elem_sizes, row):
    """Checks the size consistency of rows in a matrix

    Check if all rows in the matrix are inconsistently sized

    Args:
        elem_sizes (:obj:`set` of :obj:`int`): Size of each row matrix.
        row (list): A row with elements to divide.

    Returns:
        set: A unique consistent size between all rows.

    Raises:
        TypeError: If `elem_sizes` has more than one size in its contents.

    """

    elem_sizes.add(len(row))

    if len(elem_sizes) > 1:
        raise TypeError('Each row of the matrix must have the same size')

    return elem_sizes


def raises_matrix_type_error():
    """Raises a Matrix TypeError

    Raises:
        TypeError: If `matrix` list of lists of integers or floats.

    """

    raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
