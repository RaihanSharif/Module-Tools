import cowsay
import sys
import argparse


#  parse the args
parser = argparse.ArgumentParser(
    prog="cowsay command line tool",
    description="Make animals say things")

parser.add_argument("--animal", choices=cowsay.char_names, help="The animal to be saying things.")
parser.add_argument("message", nargs='*', help="The message to say")

args = parser.parse_args()
# cowsay.cow(" ".join(sys.argv[1:]))