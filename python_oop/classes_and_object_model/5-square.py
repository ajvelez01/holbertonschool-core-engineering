#!/usr/bin/env python3
"""Defines a Square class with validation, area and printing."""


class Square:
    """Represents a square with a validated private size."""

    def __init__(self, size=0):
        """Initializes the square through the size setter.

        Args:
            size (int): the side length of the square.
        """
        self.size = size

    @property
    def size(self):
        """int: the side length of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the side length after validating it.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
