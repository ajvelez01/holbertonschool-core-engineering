#!/usr/bin/env python3
"""Defines the BaseGeometry class with shared shape behavior."""


class BaseGeometry:
    """Represents the foundational behavior for geometric shapes."""

    def area(self):
        """Raises an exception, since area is not defined here.

        Raises:
            Exception: always, because subclasses must implement area.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a value is a positive integer.

        Args:
            name (str): the name of the parameter, used in messages.
            value (int): the value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
