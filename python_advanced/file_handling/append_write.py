#!/usr/bin/env python3
"""Defines append_write, which appends text to a UTF-8 text file."""


def append_write(filename="", text=""):
    """Appends text at the end of a file and returns the characters added.

    Args:
        filename (str): path of the file to append to.
        text (str): text to append.

    Returns:
        int: number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
