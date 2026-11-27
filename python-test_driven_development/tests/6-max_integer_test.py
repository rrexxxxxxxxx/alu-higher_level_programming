#!/usr/bin/python3
"""Unittests for max_integer([..])."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        """Max at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max in the middle."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max at the start."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """No argument returns None."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """A single element is the max."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """All negative numbers."""
        self.assertEqual(max_integer([-4, -2, -9]), -2)

    def test_mixed_signs(self):
        """Negative and positive numbers."""
        self.assertEqual(max_integer([-1, 0, 5, -10]), 5)

    def test_duplicates(self):
        """Repeated max values."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_floats(self):
        """Floats work too."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_ints_and_floats(self):
        """Mixed ints and floats."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_string(self):
        """A string returns its largest character."""
        self.assertEqual(max_integer("hello"), "o")

    def test_list_of_strings(self):
        """A list of strings returns the largest string."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_none(self):
        """None raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_mixed_types(self):
        """Comparing ints and strings raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "a", 2])


if __name__ == "__main__":
    unittest.main()
