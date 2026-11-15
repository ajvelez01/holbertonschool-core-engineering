#!/usr/bin/env python3
"""Defines a Rectangle class that inherits from BaseGeometry."""
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
