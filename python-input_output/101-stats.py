#!/usr/bin/python3
"""This script reads log lines from stdin and prints metrics."""
import sys


def print_stats(size, codes):
    """Print the total file size and the count of each status code."""
    print("File size: {}".format(size))
    for code in sorted(codes):
        print("{}: {}".format(code, codes[code]))


if __name__ == "__main__":
    valid = ["200", "301", "400", "401", "403", "404", "405", "500"]
    size = 0
    codes = {}
    count = 0
    try:
        for line in sys.stdin:
            count += 1
            parts = line.split()
            try:
                size += int(parts[-1])
            except (IndexError, ValueError):
                pass
            try:
                if parts[-2] in valid:
                    codes[parts[-2]] = codes.get(parts[-2], 0) + 1
            except IndexError:
                pass
            if count % 10 == 0:
                print_stats(size, codes)
        print_stats(size, codes)
    except KeyboardInterrupt:
        print_stats(size, codes)
        raise
