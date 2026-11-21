#!/usr/bin/env python3
"""Defines read_file, which prints the content of a UTF-8 text file."""


def read_file(filename=""):
    """Prints the full content of a UTF-8 text file to stdout.

    Args:
        filename (str): path of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
