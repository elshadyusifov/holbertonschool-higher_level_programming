#!/usr/bin/python3
"""This module contains a function to read a UTF-8 text file and print its content."""


def read_file(filename=""):
    with open("my_file_0.txt", "r", encoding="utf-8") as file:
        print(file.read())
