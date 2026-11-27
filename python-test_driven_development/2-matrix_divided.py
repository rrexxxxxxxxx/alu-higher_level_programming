#!/usr/bin/python3
"""This module defines matrix_divided, which divides a matrix by a number."""


def matrix_divided(matrix, div):
    """Return a new matrix with every element divided by div.

    Results are rounded to 2 decimal places.

    Args:
        matrix (list): a list of lists of integers or floats.
        div (int or float): the divisor.

    Raises:
        TypeError: if matrix is not a list of lists of numbers, if rows
            have different sizes, or if div is not a number.
        ZeroDivisionError: if div is 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) and len(row) > 0
                    for row in matrix)):
        raise TypeError(msg)
    for row in matrix:
        for x in row:
            if type(x) not in (int, float):
                raise TypeError(msg)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]
