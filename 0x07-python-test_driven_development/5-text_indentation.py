#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError('text must be a string')

    text_length = len(text)
    idx = 0
    new_string = ''

    while idx < text_length:
        if text[idx] in '.?:':
            new_string += text[idx]
            new_string += '\n'
            new_string += '\n'
            idx += 1

            if idx < text_length:
                while text[idx] == ' ':
                    idx += 1

        new_string += text[idx]
        idx += 1

    print(new_string, end='')
