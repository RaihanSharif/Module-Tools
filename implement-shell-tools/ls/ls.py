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
    elif (len(entries) > 0):
        for i in range(len(entries)-1):
            print(f"{entries[i]}\t", end="")
        print(f"{entries[-1]}")


def main():
    # file and directory paths are processed separately
    # file_args = [arg for arg in args.paths if os.path.isfile(arg)]
    # dir_args = [arg for arg in args.paths if os.path.isdir(arg)]

    file_args = []
    dir_args = []
    invalid_args = []

    # this is a simplication, it groups all errors under "invalid file"
    # real ls would have different messages things like permission denied
    # also bad because it makes two syscalls
    for arg in args.paths:
        if (os.path.isfile(arg)):
            file_args.append(arg)
        elif (os.path.isdir(arg)):
            dir_args.append(arg)
        else:
            invalid_args.append(arg)

    for arg in invalid_args:
        print(f"ls: {arg}: No such file or directory", file=sys.stderr)

    if (len(file_args) > 0):
        print_entries(file_args)

    for index, path in enumerate(dir_args, start=0):
        if (len(args.paths) > 1):
            if (index > 0 or len(file_args) > 0):
                print("")
            print(f"{path}:")
        print_entries(get_dir_entries(path))


if __name__ == "__main__":
    main()