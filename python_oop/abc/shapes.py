#!/usr/bin/env python3
"""Defines Shape, Circle and Rectangle, and shape_info."""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Returns the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Returns the perimeter of the shape."""
        pass


class Circle(Shape):
    """Represents a circle defined by its radius."""

    def __init__(self, radius):
        """Initializes the circle with its radius.

        Args:
            radius (float): the radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Returns the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Returns the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Represents a rectangle defined by its width and height."""

    def __init__(self, width, height):
        """Initializes the rectangle with its dimensions.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a shape.

    Args:
        shape: any object providing area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
