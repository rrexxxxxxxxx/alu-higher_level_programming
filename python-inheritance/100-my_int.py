#!/usr/bin/python3
"""This module defines MyInt, an int with == and != swapped."""


class MyInt(int):
    """An int subclass whose equality operators are inverted."""

    def __eq__(self, other):
        """Return True when the values are different."""
        return int(self) != other

    def __ne__(self, other):
        """Return True when the values are the same."""
        return int(self) == other
