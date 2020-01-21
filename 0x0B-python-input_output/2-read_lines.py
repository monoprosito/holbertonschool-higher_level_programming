#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as f:
        tot_lines = len(f.readlines())

        if nb_lines <= 0 or nb_lines >= tot_lines:
            f.seek(0)
            print(f.read())
        else:
            f.seek(0)
            for i in range(nb_lines):
                print(f.readline(), end='')
