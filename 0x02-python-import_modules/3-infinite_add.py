#!/usr/bin/python3
import sys

if __name__ == '__main__':
    av = sys.argv
    l_av = len(av)
    sum = 0

    if l_av > 1:
        for i in range(1, l_av):
            sum += int(av[i])

    print(sum)
