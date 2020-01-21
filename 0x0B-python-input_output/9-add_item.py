#!/usr/bin/python3
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if len(argv) == 1:
    save_to_json_file([], 'add_item.json')
else:
    obj_json_file = load_from_json_file('add_item.json')

    for i in range(1, len(argv)):
        obj_json_file.append(argv[i])

    save_to_json_file(obj_json_file, 'add_item.json')
