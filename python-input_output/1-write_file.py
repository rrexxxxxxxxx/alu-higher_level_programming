#!/usr/bin/python3
"""This module defines write_file, which writes text to a file."""


def write_file(filename="", text=""):
    """Write text to a UTF8 file and return the number of characters."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
