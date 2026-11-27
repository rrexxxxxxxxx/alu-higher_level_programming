#!/usr/bin/python3
"""This module defines append_after."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after each line of a file containing search_string.

    Args:
        filename (str): the file to update.
        search_string (str): the text to look for in each line.
        new_string (str): the line to insert after each match.
    """
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
    text = ""
    for line in lines:
        text += line
        if search_string in line:
            text += new_string
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
