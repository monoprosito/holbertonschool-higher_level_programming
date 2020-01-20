#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        if issubclass(MyList, list):
            print(sorted(self))
