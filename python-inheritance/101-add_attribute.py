#!/usr/bin/python3
"""This module defines add_attribute."""


def add_attribute(obj, name, value):
    """Add a new attribute to obj if it can take new attributes.

    Raises:
        TypeError: if obj can't have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
