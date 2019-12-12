#!/usr/bin/python3
import sys

if __name__ == '__main__':
    """Prints the argument list passed to the program

    The program takes all the arguments starting from the second
    and prints the number of arguments and their value

    """
    av = sys.argv
    l_av = len(av)

    if l_av > 1:
        print(l_av - 1, 'arguments:')
        for i in range(1, l_av):
            print('{:d}: {}'.format(i, av[i]))
    else:
        print(l_av - 1, 'arguments.')
