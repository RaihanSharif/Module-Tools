import argparse
import sys
import os

# TODO: decompose into functions to make it more modular and reusable

parser = argparse.ArgumentParser(
    prog="a simple version of wc. Takes in one or more files.",
    description="ls command line tool which can accept -l -w -c cflags")

parser.add_argument("-l", action="store_true", help="show line count")
parser.add_argument("-w", action="store_true", help="show word count")
parser.add_argument("-c", action="store_true", help="show byte count")

parser.add_argument("paths", nargs="*", help="file(s) for which to show data")

args = parser.parse_args()

totals = {"l": 0, "w": 0, "c": 0}

# if no flags then set all flags to true, same as in real wc
if (not args.l and not args.w and not args.c):
    args.l = args.w = args.c = True

for path in args.paths:
    if (not os.path.exists(path)):
        print(f"wc: {path}: open: No such file or directory", file=sys.stderr)
    elif (os.path.isdir(path)):
        print(f"wc: {path}: read: Is a directory", file=sys.stderr) 
    elif (os.path.isfile(path)):
        output_str = ""
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()

            lines = content.split('\n')
            
            if (args.l):
                #if (len(lines)) > 0: 
                 #   lines[-1].strip()

                line_count = content.count('\n')
                totals["l"] += line_count
                output_str += f"{line_count:8}"

            if (args.w):
                word_count = len(content.split())
                totals["w"] += word_count
                output_str += f"{word_count:8}"

            if (args.c):
                bytes = os.path.getsize(path)
                totals["c"] += bytes
                output_str += f"{bytes:8}"

        output_str += f" {path}"
        print(output_str)

if (len(args.paths) > 1):
    res = {key : val for key, val in totals.items() 
           if val != 0}
    total_str = ""
    for v in res.values():
        total_str += f"{v:8}"

    total_str += " total"
    print(total_str)
            

                


