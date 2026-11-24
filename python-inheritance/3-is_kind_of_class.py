#!/usr/bin/python3
"""This module defines is_kind_of_class for instance checks."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or of a subclass."""
    return isinstance(obj, a_class)
