#!/usr/bin/python3
"""
A module to prints a list in ascending order
"""


class MyList(list):
    """
    A class to customize the list class
    """

    def print_sorted(self):
        """
        Prints a list in ascending order

        Sort a list and then prints on the output
        """

        if issubclass(MyList, list):
            print(sorted(self))
