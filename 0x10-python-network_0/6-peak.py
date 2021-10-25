#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """ Finds a peak in a list of unsorted integers """
    lof = list_of_integers
    if not lof:
        return None

    left = 0
    right = len(lof) - 1

    while (left < right):
        mid = int((left + right) / 2)
        if lof[mid] < lof[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return (lof[left])
