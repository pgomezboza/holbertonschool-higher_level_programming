#!/usr/bin/python3
"""
Module: 0-read_file
Description: reads from a file and print.
"""


def read_file(filename=""):
    """
    Reads a text file(UTF8) and prints it to stdout
    args: name of the file
    """

    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
