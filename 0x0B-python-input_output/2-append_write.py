#!/usr/bin/python3
"""
Module: 2-append_write
"""


def append_write(filename="", text=""):
    """
    args: name of file, text to append
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return(file.write(text))
