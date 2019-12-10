#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            new_str += chr(ord(str[i]) - 32)
            continue
        new_str += str[i]

    print('{0}'.format(new_str))
