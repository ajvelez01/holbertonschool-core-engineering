#!/usr/bin/env python3
"""Demonstrates inheritance and polymorphism with animal classes."""


class Animal:
    """Represents a generic animal."""

    def speak(self):
        """Returns the sound of the animal."""
        return "Some sound"


class Dog(Animal):
    """Represents a dog."""

    def speak(self):
        """Returns the sound of a dog."""
        return "Woof"


class Cat(Animal):
    """Represents a cat."""

    def speak(self):
        """Returns the sound of a cat."""
        return "Meow"


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    print(dog.speak())
    print(cat.speak())

    animals = [Dog(), Cat(), Dog()]
    for animal in animals:
        print(animal.speak())

    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(issubclass(Dog, Animal))
