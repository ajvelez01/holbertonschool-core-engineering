#!/usr/bin/env python3
"""Defines a Square class with size, position, area and printing."""


class Square:
    """Represents a square with a validated size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square through the setters.

        Args:
            size (int): the side length of the square.
            position (tuple): two non-negative integers (x, y).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """tuple: the (x, y) position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position after validating it.

        Raises:
            TypeError: if value is not a tuple of 2 non-negative integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(v, int) and v >= 0 for v in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character # using its position."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns the printed representation of the square."""
        if self.__size == 0:
            return ""
        rows = [" " * self.__position[0] + "#" * self.__size] * self.__size
        return "\n" * self.__position[1] + "\n".join(rows)
