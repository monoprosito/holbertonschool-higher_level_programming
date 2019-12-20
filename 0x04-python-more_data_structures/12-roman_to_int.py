#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_letters = [
        ['M', 1000], ['D', 500],
        ['C', 100], ['L', 50],
        ['X', 10], ['V', 5], ['I', 1]
    ]
    num = 0
    last = 0

    for letter in roman_string:
        for elem in roman_letters:
            if letter == elem[0]:
                if last == 0 or last >= elem[1]:
                    num += elem[1]
                    print('El ultimo anadido fue: {0} y acabe de anadir +{1}'.format(last, elem[1]))
                elif last <= elem[1]:
                    num += elem[1] - last
                    print('El ultimo anadido fue: {0} y acabe de quitar -{1}'.format(last, elem[1] - last))

                last = elem[1]

    return num