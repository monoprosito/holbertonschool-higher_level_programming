#!/usr/bin/env python3
import sys

sys.path.append('../')
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("4 is {}".format("lower" if islower("4") else "upper"))
print("5 is {}".format("lower" if islower("5") else "upper"))
print("z is {}".format("lower" if islower("z") else "upper"))
print("x is {}".format("lower" if islower("x") else "upper"))
print("X is {}".format("lower" if islower("X") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
