#!/usr/bin/python3
"""Unittests for models/square.py."""
import io
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


if __name__ == "__main__":
    unittest.main()
