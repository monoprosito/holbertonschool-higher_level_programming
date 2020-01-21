#!/usr/bin/python3
from math import sqrt
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    def __str__(self):
        sqroot = int(sqrt(self.area()))
        return '[Square] ' + str(sqroot) + '/' + str(sqroot)
