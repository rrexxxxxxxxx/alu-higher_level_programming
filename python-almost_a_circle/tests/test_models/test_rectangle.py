#!/usr/bin/python3
"""Unittests for models/rectangle.py."""
import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_is_base(self):
        """Rectangle inherits from Base."""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_attributes(self):
        """Attributes are set and ids increase."""
        r = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (10, 2, 3, 4, 12))
        self.assertEqual(Rectangle(1, 2).id, 1)
        self.assertEqual(Rectangle(1, 2).id, 2)

    def test_missing_args(self):
        """Width and height are required."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_type_errors(self):
        """Non-integers raise TypeError with the right message."""
        cases = [("width", ("1", 2)), ("height", (1, "2")),
                 ("x", (1, 2, "3")), ("y", (1, 2, 3, "4")),
                 ("width", (1.5, 2)), ("height", (1, None)),
                 ("width", (True, 2))]
        for name, args in cases:
            with self.assertRaisesRegex(TypeError,
                                        name + " must be an integer"):
                Rectangle(*args)

    def test_value_errors(self):
        """Out of range values raise ValueError with the right message."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -1)

    def test_setter_validation(self):
        """Setters validate too."""
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r.width = "5"
        with self.assertRaises(ValueError):
            r.x = -3

    def test_area(self):
        """area returns width * height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display(self):
        """display draws the rectangle."""
        f = io.StringIO()
        with redirect_stdout(f):
            Rectangle(2, 3).display()
        self.assertEqual(f.getvalue(), "##\n##\n##\n")

    def test_display_offset(self):
        """display uses x and y."""
        f = io.StringIO()
        with redirect_stdout(f):
            Rectangle(2, 3, 2, 2).display()
        self.assertEqual(f.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_str(self):
        """__str__ format."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """update with positional arguments."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """update with keyword arguments, ignored when args exist."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 10/1")
        r.update(7, width=3)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 10)

    def test_update_invalid(self):
        """update validates values."""
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.update(1, "2")

    def test_to_dictionary(self):
        """to_dictionary returns all attributes."""
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r.to_dictionary(),
                         {"x": 1, "y": 9, "id": 1, "height": 2, "width": 10})

    def test_save_and_create_roundtrip(self):
        """create rebuilds an instance from its dictionary."""
        r1 = Rectangle(3, 5, 1, 0, 4)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())


if __name__ == "__main__":
    unittest.main()
