#!/usr/bin/python3
""" 
Module: 1-my_list
"""


class MyList(list):
    """
    Class MyList inherits from list.
    """

    def print_sorted(self):
        """
        print_sorted: prints list in ascending sort
        """
        print(sorted(self))
