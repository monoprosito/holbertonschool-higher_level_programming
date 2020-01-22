#!/usr/bin/python3
import sys


def print_info(file_size, status_codes):
    print('File size: {:d}'.format(file_size))

    for scode, code_times in sorted(status_codes.items()):
        if code_times > 0:
            print('{}: {:d}'.format(scode, code_times))


status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

lc = 0
file_size = 0

try:
    for line in sys.stdin:
        pieces = line.split()
        status = int(pieces[7])

        if str(status) in status_codes.keys():
            status_codes[str(status)] += 1

        file_size += int(pieces[8])

        if lc != 0 and lc % 10 == 0:
            print_info(file_size, status_codes)

        lc += 1
except KeyboardInterrupt:
    print_info(file_size, status_codes)
    raise
