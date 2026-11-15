#!/usr/bin/env python3
"""Defines a Square class with a validated private size."""


class Square:
    """Represents a square with a validated private size."""

    def __init__(self, size=0):
        """Initializes the square and validates its size.

        Args:
            size (int): the side length of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
