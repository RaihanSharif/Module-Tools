import argparse
import sys
import os

parser = argparse.ArgumentParser(
    prog="a simple version of wc. Takes in one or more files.",
    description="ls command line tool which can accept -l -w -c cflags")

parser.add_argument("-l", action="store_true", help="show line count")
parser.add_argument("-w", action="store_true", help="show word count")
parser.add_argument("-c", action="store_true", help="show byte count")

parser.add_argument("paths", nargs="*", help="file(s) for which to show data")

args = parser.parse_args()