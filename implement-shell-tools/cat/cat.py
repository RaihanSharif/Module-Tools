import argparse
import sys

parser = argparse.ArgumentParser(
    prog="a simple cat implementation",
    description="cat command line tool with the -n and -b flags"
)

parser.add_argument("-n", action="store_true", help="number all output lines")
parser.add_argument("-b", action="store_true", help="number non-empty output lines")
parser.add_argument("paths", nargs="+", help="file path or paths", )

args = parser.parse_args()

# cat returns different error messages depending on the reason the path could be read
def read_file(path):
    """Returns (content, error_message). error_message is None on success"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read(), None
    except FileNotFoundError:
        return None, f"cat: {path}: No such file or directory"
    except IsADirectoryError:
        return None, f"cat: {path}: Is a directory"
    except PermissionError:
        return None, f"cat: {path}: Permission denied"


# -b (number the non-empty lines) takes priority over -n (number all lines)
# if both are present
def format_lines(lines, number_all=False, number_nonempty=False):
    """Returns a list of formatted output lines"""
    output = []
    
    if number_nonempty:
        line_num = 0
        for line in lines:
            if line == "":
                output.append("")
            else:
                line_num += 1
                # {line_num:6} right justied number, length of at least 6
                # {some_str:6} left justifed string, length fo at least 6
                output.append(f"{line_num:6}\t{line}")
    elif number_all:
        for i, line in enumerate(lines, start=1):
            output.append(f"{i:6}\t{line}")
    else:
        output = lines

    return output


# TODO: runner function to call read_file, and feed it into formatLines, then print
def cat_file(path, number_all=False, number_nonempty=False):
    """
    Calls read_file -> format_lines -> prints formatted line. 
    Returns True if file read successfully, else returns False

    If failed to read file, prints error to stderr
    """
    content, error = read_file(path)
    if (error):
        print(error, file=sys.stderr)
        return False

    # splitlines automatically trims trailing empty lines
    lines = content.splitlines()
    for line in format_lines(lines, number_all, number_nonempty):
        print(line)

    return True


def main():
    # cat exits with error code 1 if any file read fails
    file_error = False

    for path in args.paths:
        line_num = 1
        is_success = cat_file(path, args.n, args.b)

        if not is_success:
            file_error = True

    # if at any point, file reading failed file error is set to True, 
    # and program exist with code 1 after all tasks completed
    sys.exit(1 if file_error else 0)

# ensures that main only runs when this file/module is directly executed
# not when it is imported, for example, for automated tests
if __name__ == "__main__":
    main()