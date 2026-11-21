#!/usr/bin/env python3
"""Defines write_file, which writes text to a UTF-8 file."""


def write_file(filename="", text=""):
    """Writes text to a file, overwriting it, and returns the character count.

    Args:
        filename (str): path of the file to write.
        text (str): text to write.

    Returns:
        int: number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
