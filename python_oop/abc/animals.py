#!/usr/bin/env python3
"""Defines an abstract Animal class and its Dog and Cat subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Returns the sound the animal makes."""
        pass


class Dog(Animal):
    """Represents a dog."""

    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Represents a cat."""

    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"
