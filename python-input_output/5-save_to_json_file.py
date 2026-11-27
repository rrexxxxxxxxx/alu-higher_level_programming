#!/usr/bin/python3
"""This module defines save_to_json_file."""
import json


def save_to_json_file(my_obj, filename):
    """Write the JSON representation of my_obj to a text file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
