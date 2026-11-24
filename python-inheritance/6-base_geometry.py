#!/usr/bin/python3
"""This module defines BaseGeometry with an area method to override."""


class BaseGeometry:
    """A base class for geometry shapes."""

    def area(self):
        """Raise an Exception because subclasses must implement area."""
        raise Exception("area() is not implemented")
