#!/usr/bin/env python3
"""Defines a Rectangle class with area and string representation."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle with validated width and height."""

    def __init__(self, width, height):
        """Initializes the rectangle, validating both dimensions.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the description [Rectangle] width/height."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
