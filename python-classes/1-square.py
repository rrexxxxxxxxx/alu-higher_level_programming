#!/usr/bin/python3
"""This module defines a Square class with a private size."""


class Square:
    """A class that represents a square by its size."""

    def __init__(self, size):
        """Initialize the square with the given size.

        Args:
            size: the length of one side of the square.
        """
        self.__size = size
