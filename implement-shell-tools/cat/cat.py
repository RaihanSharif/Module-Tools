import argparse

parser = argparse.ArgumentParser(
    prog="a simple cat implementation",
    description="cat command line tool with the -n and -b flags"
)

parser.add_argument("-n", action="store_true", help="number all output lines")
parser.add_argument("-b", action="store_true", help="number non-empty output lines")
parser.add_argument("paths", nargs="+", help="file path or paths", )

args = parser.parse_args();

print(args)