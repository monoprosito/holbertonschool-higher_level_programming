#!/usr/bin/python3
import sys
import signal


def print_info():
    print('File size: {}'.format(file_size))

    for scode, code_times in sorted(status_codes.items()):
        if code_times > 0:
            print('{}: {}'.format(scode, code_times))


def signal_handler(sig, frame):
    print_info()


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

lc = 1
file_size = 0

for line in sys.stdin:
    pieces = line.split()
    status = int(pieces[7])

    if str(status) in status_codes.keys():
        status_codes[str(status)] += 1

    file_size += int(pieces[8])

    if lc % 10 == 0:
        print_info()

    signal.signal(signal.SIGINT, signal_handler)

    lc += 1
