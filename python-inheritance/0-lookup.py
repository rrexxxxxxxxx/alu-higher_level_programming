#!/usr/bin/python3
"""This module defines lookup, which lists an object's attributes."""


def lookup(obj):
    """Return the list of attributes and methods available on obj."""
    return dir(obj)
