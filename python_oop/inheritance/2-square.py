#!/usr/bin/env python3
"""Defines a Square class with its own string representation."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square as a rectangle with equal sides."""

    def __init__(self, size):
        """Initializes the square with a single validated size.

        Args:
            size (int): the side length of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Returns the description [Square] side/side."""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
