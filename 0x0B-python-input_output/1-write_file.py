#!/usr/bin/python3
"""
Module: 1-write_file
return the number of characters written
"""


def write_file(filename="", text=""):
    """
    args: name of file, text to write.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return (file.write(text))
