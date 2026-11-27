#!/usr/bin/python3
"""This module defines class_to_json."""


def class_to_json(obj):
    """Return the dictionary description of obj for JSON serialization."""
    return obj.__dict__
