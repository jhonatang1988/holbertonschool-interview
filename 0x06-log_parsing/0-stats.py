#!/usr/bin/python3
"""
reads from stdin and compute metrics
the input format
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""
# import signal
import sys
from collections import OrderedDict

consolidated_file_size = 0

output_format = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

times = 0
buff = ''

# def keyboard_exit_message(signal, frame):
#     print("File size: {}".format(consolidated_file_size))
#     for keys, values in output_format.items():
#         if values != 0:
#             print("{}: {}".format(keys, values))
#     exit(0)


# signal.signal(signal.SIGINT, keyboard_exit_message)

while True:
    try:
        buff += sys.stdin.read(1)
        if buff.endswith('\n'):
            separated_terms = buff[:-1].split(' ')
            file_size = separated_terms[-1]
            consolidated_file_size += int(file_size)
            status_code = separated_terms[-2]
            output_format[status_code] += 1
            buff = ''
            times += 1
            if times % 10 == 0:
                ordered_dict = sorted(output_format.items(),
                                      key=lambda k: k[0])
                print("File size: {}".format(consolidated_file_size))
                for status_code in ordered_dict:
                    if status_code[1] != 0:
                        print("{}: {}".format(status_code[0], status_code[1]))

    except KeyboardInterrupt:
        ordered_dict = sorted(output_format.items(),
                              key=lambda k: k[1])
        print("File size: {}".format(consolidated_file_size))
        for status_code in ordered_dict:
            if status_code[1] != 0:
                print("{}: {}".format(status_code[0], status_code[1]))
