#!/usr/bin/python3
"""This module defines load_from_json_file."""
import json


def load_from_json_file(filename):
    """Create and return a Python object read from a JSON file."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
