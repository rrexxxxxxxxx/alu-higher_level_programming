#!/usr/bin/python3
"""This module defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """A rectangle with a width, a height and an x/y position."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle.

        Args:
            width (int): the width, greater than 0.
            height (int): the height, greater than 0.
            x (int): the horizontal offset, 0 or more.
            y (int): the vertical offset, 0 or more.
            id (int): the id of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def _check(name, value, positive):
        """Validate that value is an integer within its allowed range."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if positive and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if not positive and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width after validating it."""
        self._check("width", value, True)
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height after validating it."""
        self._check("height", value, True)
        self.__height = value

    @property
    def x(self):
        """Get the horizontal offset."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the horizontal offset after validating it."""
        self._check("x", value, False)
        self.__x = value

    @property
    def y(self):
        """Get the vertical offset."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the vertical offset after validating it."""
        self._check("y", value, False)
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with #, shifted by x and y."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update attributes by position (id, width, height, x, y) or name."""
        names = ["id", "width", "height", "x", "y"]
        if args:
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in names:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
