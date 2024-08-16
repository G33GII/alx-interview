#!/usr/bin/python3
import sys
import signal
import re


def print_stats(total_size, status_counts):
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def handler(signum, frame):
    print_stats(total_size, status_counts)
    sys.exit(0)


# Set up the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, handler)

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0,
                 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Regular expression to match the log line format
log_pattern = re.compile(
    r'^'
    r'((\b\d{1,3}\.){3}\d{1,3}\b|\b\w+\b)'
    r' ?- ?'
    r'\[.*\]'
    r' "GET /projects/260 HTTP/1\.1"'
    r' (\d{3})'
    r' (\d+)$'
)


line_count = 0

try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            total_size += file_size

            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
        else:
            # status_code = int(match.group(3))
            # file_size = int(match.group(4))
            # print(file_size)
            # total_size += file_size
            found = re.search(r'\s(\d+)$', line)
            if found:
                file_size = int(found.group(1))
                total_size += file_size

    # Print stats if the loop exits naturally (e.g., EOF)
    print_stats(total_size, status_counts)

except KeyboardInterrupt:
    # Handle keyboard interruption
    print_stats(total_size, status_counts)
    sys.exit(0)
