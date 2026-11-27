#!/usr/bin/python3
"""This module defines add_integer, which adds two numbers as integers."""


def add_integer(a, b=98):
    """Return the sum of a and b after casting them to integers.

    Args:
        a (int or float): the first number.
        b (int or float): the second number, 98 by default.

    Raises:
        TypeError: if a or b is not an integer or a float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
