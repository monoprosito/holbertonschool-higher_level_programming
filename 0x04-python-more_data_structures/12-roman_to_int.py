#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    if len(roman_string) == 0:
        return 0

    roman_letters = [
        ['M', 1000], ['D', 500],
        ['C', 100], ['L', 50],
        ['X', 10], ['V', 5], ['I', 1]
    ]
    num = 0
    last = 0
    rep = 1

    for letter in roman_string:
        for elem in roman_letters:
            if letter == elem[0]:
                if last == 0 or last >= elem[1]:
                    num += elem[1]
                    rep += last

                    if last != elem[1]:
                        rep = 1
                elif last < elem[1]:
                    if rep > 1:
                        num = (num - rep) + (elem[1] - rep)
                    else:
                        num = elem[1] - last

                last = elem[1]

    return num
