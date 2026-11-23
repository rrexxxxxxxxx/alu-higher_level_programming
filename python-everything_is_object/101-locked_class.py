#!/usr/bin/python3
"""This module defines LockedClass, which only allows first_name."""


class LockedClass:
    """A class that only lets you create the first_name attribute."""

    __slots__ = ["first_name"]
