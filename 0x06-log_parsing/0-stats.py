#!/usr/bin/python3
"""
reads from stdin and compute metrics
the input format
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""
import signal
import sys

consolidated_file_size = 0

output_format = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

times = 0
buff = ''


def keyboard_exit_message():
    print("File size: {}".format(consolidated_file_size))
    for keys, values in output_format.items():
        if values != 0:
            print("{}:{}".format(keys, values))
    exit(0)


signal.signal(signal.SIGINT, keyboard_exit_message)

while True:
    buff += sys.stdin.read(1)
    if buff.endswith('\n'):
        separated_terms = buff[:-1].split(' ')
        file_size = separated_terms[-1]
        consolidated_file_size += int(file_size)
        status_code = int(separated_terms[-2])
        output_format[status_code] += 1
        buff = ''
        times += 1
        if times % 10 == 0:
            print("File size: {}".format(consolidated_file_size))
            for key, value in output_format.items():
                if value != 0:
                    print("{}:{}".format(key, value))
