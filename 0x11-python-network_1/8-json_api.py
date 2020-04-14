#!/usr/bin/python3
"""Takes in a letter and sends a POST request
to `http://0.0.0.0:5000/search_user` with the
letter as a parameter and with `requests` module.
"""

from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''

    try:
        url = 'http://0.0.0.0:5000/search_user'
        payload = {'q': q}
        r = requests.post(url, payload).json()

        if {'id', 'name'} <= r.keys():
            print('[{id}] {name}'.format(id=r.get('id'), name=r.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
