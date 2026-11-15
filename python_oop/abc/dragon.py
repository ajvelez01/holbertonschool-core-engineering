#!/usr/bin/env python3
"""Defines SwimMixin, FlyMixin and a Dragon class combining them."""


class SwimMixin:
    """Mixin that gives a creature the ability to swim."""

    def swim(self):
        """Prints the swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that gives a creature the ability to fly."""

    def fly(self):
        """Prints the flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a dragon that can swim, fly and roar."""

    def roar(self):
        """Prints the roaring message."""
        print("The dragon roars!")
