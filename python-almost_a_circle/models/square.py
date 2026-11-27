#!/usr/bin/python3
"""This module defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square: a rectangle with equal width and height."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square.

        Args:
            size (int): the length of a side, greater than 0.
            x (int): the horizontal offset, 0 or more.
            y (int): the vertical offset, 0 or more.
            id (int): the id of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size, applied to both width and height."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attributes by position (id, size, x, y) or by name."""
        names = ["id", "size", "x", "y"]
        if args:
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in names:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
