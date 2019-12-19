#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) is dict:
        if len(a_dictionary) == 0:
            return None

        return max(a_dictionary)

    return None
