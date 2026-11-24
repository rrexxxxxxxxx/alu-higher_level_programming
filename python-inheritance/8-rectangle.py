#!/usr/bin/python3
"""This module defines Rectangle, built on BaseGeometry."""
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
