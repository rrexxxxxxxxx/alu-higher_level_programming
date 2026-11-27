#!/usr/bin/python3
"""This module defines text_indentation, which splits text into lines."""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'.

    There is no space at the start or end of each printed line.

    Args:
        text (str): the text to print.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for ch in text:
        line += ch
        if ch in ".?:":
            print(line.strip(), end="\n\n")
            line = ""
    print(line.strip(), end="")
