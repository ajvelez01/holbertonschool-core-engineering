#!/usr/bin/env python3
"""Defines VerboseList, a list that prints notifications on changes."""


class VerboseList(list):
    """A list that notifies when items are added or removed."""

    def append(self, item):
        """Appends an item and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extends the list and prints how many items were added."""
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Removes an item and prints a notification before removing."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item and prints a notification before popping."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
