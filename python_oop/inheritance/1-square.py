#!/usr/bin/env python3
"""Defines a Square class that inherits from Rectangle."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square as a rectangle with equal sides."""

    def __init__(self, size):
        """Initializes the square with a single validated size.

        Args:
            size (int): the side length of the square.
        """
        super().__init__(size, size)
