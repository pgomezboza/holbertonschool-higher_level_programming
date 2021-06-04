#!/usr/bin/python3
"""
Module: 100-my_int
"""


class MyInt(int):
    """
    Class inheriting from int
    """

    def __ne__(self, other):
        """
        Inequality change into equality (reverse !=)
        """
        return super().__eq__(other)

    def __eq__(self, other):
        """
        Equality change into inequality (reverse ==)
        """
        return super().__ne__(other)
