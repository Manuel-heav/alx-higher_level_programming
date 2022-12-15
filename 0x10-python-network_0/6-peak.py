#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    
    my_list = list_of_integers

    if my_list:
        my_list.sort()
        return my_list[-1]
    else:
        return None
