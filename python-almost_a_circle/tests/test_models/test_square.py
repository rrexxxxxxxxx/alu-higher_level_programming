#!/usr/bin/python3
"""Unittests for models/square.py."""
import io
import json
import os
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_is_rectangle(self):
        """Square inherits from Rectangle."""
        self.assertIsInstance(Square(1), Rectangle)

    def test_attributes(self):
        """Size sets width and height."""
        s = Square(5, 2, 3, 7)
        self.assertEqual((s.size, s.width, s.height, s.x, s.y, s.id),
                         (5, 5, 5, 2, 3, 7))

    def test_size_setter(self):
        """Changing size updates width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))

    def test_validation(self):
        """Size uses the width messages."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("9")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)
        s = Square(2)
        with self.assertRaises(TypeError):
            s.size = "9"

    def test_missing_size(self):
        """Size is required."""
        with self.assertRaises(TypeError):
            Square()

    def test_area_and_display(self):
        """area and display work."""
        s = Square(2, 1, 1)
        self.assertEqual(s.area(), 4)
        f = io.StringIO()
        with redirect_stdout(f):
            s.display()
        self.assertEqual(f.getvalue(), "\n ##\n ##\n")

    def test_str(self):
        """__str__ format."""
        self.assertEqual(str(Square(3, 1, 3, 4)), "[Square] (4) 1/3 - 3")

    def test_update(self):
        """update by position and by name."""
        s = Square(5, 0, 0, 1)
        s.update(10, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (10) 3/4 - 2")
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (10) 3/1 - 7")

    def test_to_dictionary(self):
        """to_dictionary returns id, size, x and y."""
        self.assertEqual(Square(10, 2, 1, 1).to_dictionary(),
                         {"id": 1, "x": 2, "size": 10, "y": 1})

    def test_y_not_int(self):
        """Square(1, 2, "3") raises TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_negative_size(self):
        """Square(-1) raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_negative_x(self):
        """Square(1, -2) raises ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_negative_y(self):
        """Square(1, 2, -3) raises ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_save_to_file_none(self):
        """Square.save_to_file(None) writes []."""
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_empty(self):
        """Square.save_to_file([]) writes []."""
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_one(self):
        """Square.save_to_file([Square(1)]) writes the dictionary."""
        Square.save_to_file([Square(1)])
        with open("Square.json") as f:
            self.assertEqual(json.loads(f.read()),
                             [{"id": 1, "size": 1, "x": 0, "y": 0}])
        os.remove("Square.json")

    def test_load_from_file(self):
        """Square.load_from_file returns saved squares, or []."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])
        Square.save_to_file([Square(4, 1, 2, 9)])
        self.assertEqual([str(x) for x in Square.load_from_file()],
                         ["[Square] (9) 1/2 - 4"])
        os.remove("Square.json")

    def test_create(self):
        """Square.create builds a square from a dictionary."""
        self.assertEqual(str(Square.create(**{"id": 89, "size": 1})),
                         "[Square] (89) 0/0 - 1")


if __name__ == "__main__":
    unittest.main()
