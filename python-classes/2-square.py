#!/usr/bin/python3
"""This module defines a Square class that validates its size."""


class Square:
    """A class that represents a square with a validated size."""

    def __init__(self, size=0):
        """Initialize the square after checking the size.

        Args:
            size (int): the length of one side of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
