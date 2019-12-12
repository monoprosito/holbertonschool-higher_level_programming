#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    def_names = dir(hidden_4)

    for i in range(len(def_names)):
        if def_names[i][:2] != '__':
            print(def_names[i])
