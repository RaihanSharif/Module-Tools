import cowsay
import sys
import argparse


#  parse the args
parser = argparse.ArgumentParser(
    prog="cowsay command line tool",
    description="ASCII art of animals saying text supplied as argument")

parser.add_argument("--animal", choices=cowsay.char_names)

args = parser.parse_args()
# cowsay.cow(" ".join(sys.argv[1:]))