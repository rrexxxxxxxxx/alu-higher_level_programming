#!/usr/bin/python3
"""Unittests for models/base.py."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove files created by the tests."""
        for name in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_auto_ids(self):
        """Ids are assigned automatically in order."""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

    def test_given_id(self):
        """A given id is used as is and doesn't count."""
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 1)

    def test_none_id(self):
        """None gets an automatic id."""
        self.assertEqual(Base(None).id, 1)

    def test_other_id_types(self):
        """Any non-None id is kept."""
        self.assertEqual(Base("a").id, "a")
        self.assertEqual(Base(-5).id, -5)

    def test_to_json_string(self):
        """Dictionaries become a JSON string."""
        d = [{"id": 1, "width": 2}]
        self.assertEqual(json.loads(Base.to_json_string(d)), d)
        self.assertEqual(type(Base.to_json_string(d)), str)

    def test_to_json_string_empty(self):
        """None and an empty list give []."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string(self):
        """A JSON string becomes a list."""
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{"id": 89}])

    def test_from_json_string_empty(self):
        """None and an empty string give []."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_save_to_file_rectangle(self):
        """Rectangles are saved to Rectangle.json."""
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8, 1)])
        with open("Rectangle.json") as f:
            self.assertEqual(json.loads(f.read()), [
                {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}])

    def test_save_to_file_square(self):
        """Squares are saved to Square.json."""
        Square.save_to_file([Square(1, 0, 0, 5)])
        with open("Square.json") as f:
            self.assertEqual(json.loads(f.read()),
                             [{"id": 5, "size": 1, "x": 0, "y": 0}])

    def test_save_to_file_none_and_empty(self):
        """None and [] save an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_create(self):
        """create builds an equal but separate instance."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        s = Square.create(**{"id": 89, "size": 3, "x": 1, "y": 2})
        self.assertEqual(str(s), "[Square] (89) 1/2 - 3")

    def test_load_from_file(self):
        """Saved instances are loaded back."""
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8, 1),
                                Rectangle(2, 4, 0, 0, 2)])
        loaded = Rectangle.load_from_file()
        self.assertEqual([str(r) for r in loaded],
                         ["[Rectangle] (1) 2/8 - 10/7",
                          "[Rectangle] (2) 0/0 - 2/4"])

    def test_load_from_missing_file(self):
        """A missing file gives []."""
        self.assertEqual(Square.load_from_file(), [])


if __name__ == "__main__":
    unittest.main()
