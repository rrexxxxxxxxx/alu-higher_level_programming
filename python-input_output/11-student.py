#!/usr/bin/python3
"""This module defines a Student class that can be saved and reloaded."""


class Student:
    """A student with a first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student.

        Args:
            first_name (str): the first name.
            last_name (str): the last name.
            age (int): the age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the student as a dictionary.

        Args:
            attrs (list): if a list of strings, only these attributes.
        """
        if (isinstance(attrs, list) and
                all(isinstance(a, str) for a in attrs)):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes with the values in a dictionary.

        Args:
            json (dict): attribute names and their new values.
        """
        for key, value in json.items():
            setattr(self, key, value)
