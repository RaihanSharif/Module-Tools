import argparse
import sys

parser = argparse.ArgumentParser(
    prog="a simple cat implementation",
    description="cat command line tool with the -n and -b flags"
)

parser.add_argument("-n", action="store_true", help="number all output lines")
parser.add_argument("-b", action="store_true", help="number non-empty output lines")
parser.add_argument("paths", nargs="+", help="file path or paths", )

args = parser.parse_args();

# cat returns different error messages depending on the reason the path could be read
def cat_file(path):
    try:
        with open(path, "r",) as f:
            content = f.read()
    except FileNotFoundError:
        print(f"cat: {path}: No such file or directory", file=sys.stderr)
        return
    except IsADirectoryError:
        print(f"cat: {path}: Is a directory", file=sys.stderr)
        return
    except PermissionError:
        print(f"cat: {path}: Permission denied", file=sys.stderr)
        return

    print(content)



for path in args.paths:
    line_num = 1
    cat_file(path)