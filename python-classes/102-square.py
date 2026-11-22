#!/usr/bin/python3
"""This module defines a Square class that can be compared by area."""


class Square:
    """A class that represents a square compared by its area."""

    def __init__(self, size=0):
        """Initialize the square with the given size.

        Args:
            size (int): the length of one side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after checking it.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Return True if both squares have the same area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if the squares have different areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Return True if this square has a smaller area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if this square's area is smaller or equal."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Return True if this square has a bigger area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if this square's area is bigger or equal."""
        return self.area() >= other.area()
