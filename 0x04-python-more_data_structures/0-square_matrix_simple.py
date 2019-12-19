#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    if len(matrix) > 0:
        for elems in matrix[:]:
            new_matrix.append(list(map(lambda x: x ** 2, elems)))

    return new_matrix
