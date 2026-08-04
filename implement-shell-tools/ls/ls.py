import argparse
import sys
import os

parser = argparse.ArgumentParser(
    prog="a simple version of ls",
    description="ls command line tool which can accept 0 or more arguements" \
    "and take -a and -1 flags")

parser.add_argument("-a", action="store_true", help="show all files, including dot files")

# can't store as an attribute of Namespace object, because 1 is not a valid python identifier
# but can store under the name given in the dest argument. When working with this
# parser, look for "opt_one", not "1".
parser.add_argument("-1", dest="opt_one", action="store_true", help="show one file/directory name per line")

# takes 0 more arguments, if none are given, sets "." as default value
parser.add_argument("paths", nargs="*", help="file/directory path(s) to display", default=".")

args = parser.parse_args()


def get_dir_entries(path, aFlag=args.a):
    # warning: listdir() prints current directory by default
    entries = os.listdir(path)
    entries = [".", ".."] + entries
    entries.sort()

    if (not args.a):
        entries = [entry for entry in entries if not entry.startswith(".")]

    return entries

def print_entries(entries, onePerLineFlag = args.opt_one):
    if (onePerLineFlag):
        for entry in entries:
            print(entry)
    else:
        for i in range(len(entries)-1):
            print(f"{entries[i]}\t", end="")
        print(entries[-1])


# for path in args.paths:
#     printEntries(getDirectoryEntries(path))
