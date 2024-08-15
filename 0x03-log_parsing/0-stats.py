#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
It processes log lines of a specific format and prints statistics
every 10 lines or upon keyboard interruption.
"""

import sys
import re
from collections import defaultdict


def print_stats(total_size, status_codes):
    """
    Print the computed statistics.

    Args:
    total_size (int): The total file size processed so far.
    status_codes (dict): A dictionary containing counts of each status code.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """
    Parse a single line of log input.

    Args:
    line (str): A line from the log file.

    Returns:
    tuple: A tuple containing the status code and file size as integers,
           or (None, None) if the line doesn't match the expected format.
    """
    pattern1 = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    pattern2 = r' - \[(.+)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
    pattern = pattern1 + pattern2
    match = re.match(pattern, line)
    if match:
        ip, date, status, file_size = match.groups()
        return int(status), int(file_size)
    return None, None


def main():
    """
    Main function to process input and compute statistics.
    Reads from stdin, processes each line, and prints statistics
    every 10 valid lines or upon keyboard interruption.
    """
    total_size = 0
    line_count = 0
    status_codes = defaultdict(int)

    try:
        for line in sys.stdin:
            status, file_size = parse_line(line.strip())
            if status is not None and file_size is not None:
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
