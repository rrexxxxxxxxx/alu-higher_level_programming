#!/usr/bin/python3
"""This module defines to_json_string."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of my_obj as a string."""
    return json.dumps(my_obj)
