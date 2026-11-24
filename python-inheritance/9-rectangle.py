#!/usr/bin/python3
"""This module defines Rectangle with area and a string form."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with a validated width and height."""

    def __init__(self, width, height):
        """Initialize the rectangle after validating both sides.

        Args:
            width (int): the width, a positive integer.
            height (int): the height, a positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle as [Rectangle] <width>/<height>."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
