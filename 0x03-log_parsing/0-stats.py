#!/usr/bin/python3
"""Pycode"""

import sys
import re
from collections import defaultdict


def print_stats(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line):
    pattern1 = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    pattern2 = r' - \[(.+)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
    pattern = pattern1 + pattern2
    match = re.match(pattern, line)
    if match:
        ip, date, status, file_size = match.groups()
        return int(status), int(file_size)
    return None, None


def main():
    total_size = 0
    line_count = 0
    status_codes = defaultdict(int)

    try:
        for line in sys.stdin:
            status, file_size = parse_line(line.strip())
            if status and file_size:
                total_size += file_size
                status_codes[status] += 1
                line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
