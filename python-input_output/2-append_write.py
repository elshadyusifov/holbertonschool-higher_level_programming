#!/usr/bin/python3
"""This module contains a function to append string a
UTF-8 text file."""


def append_write(filename="", text=""):
    """append a UTF-8 text file."""
    with open(filename, "a", encoding="utf-8"):
        return filename(text)
