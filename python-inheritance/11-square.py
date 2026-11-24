#!/usr/bin/python3
"""This module defines Square with its own string form."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square with a validated size."""

    def __init__(self, size):
        """Initialize the square after validating its size.

        Args:
            size (int): the length of a side, a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the square as [Square] <size>/<size>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
