#!/usr/bin/python3
"""This module defines BaseGeometry with an integer validator."""


class BaseGeometry:
    """A base class for geometry shapes."""

    def area(self):
        """Raise an Exception because subclasses must implement area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check that value is an integer greater than 0.

        Args:
            name (str): the name used in error messages.
            value: the value to check.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
