#!/usr/bin/python3
"""This module defines the Base class for all models."""
import json


class Base:
    """Base class that manages the id attribute of every model."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the id, or assign the next automatic id.

        Args:
            id (int): the id to use; None means assign automatically.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of list_objs to <Class>.json."""
        dicts = []
        if list_objs is not None:
            dicts = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dicts))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set from dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances read from <Class>.json."""
        try:
            with open(cls.__name__ + ".json", encoding="utf-8") as f:
                dicts = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in dicts]
