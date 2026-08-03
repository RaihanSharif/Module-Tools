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
        return False
    except IsADirectoryError:
        print(f"cat: {path}: Is a directory", file=sys.stderr)
        return False
    except PermissionError:
        print(f"cat: {path}: Permission denied", file=sys.stderr)
        return False

    print(content)



# cat exits with error code 1 if any file read fails
file_error = False

for path in args.paths:
    line_num = 1
    is_success = cat_file(path)

    if not is_success:
        file_error = True

# if at any point, file reading failed file error is set to True, 
# and program exist with code 1 after all tasks completed
sys.exit(1 if file_error else 0)