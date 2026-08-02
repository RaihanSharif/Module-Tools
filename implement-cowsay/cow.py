import cowsay
import sys
import argparse


#  set up options and argument parser
parser = argparse.ArgumentParser(
    prog="cowsay command line tool",
    description="Make animals say things")

# takes an --animal option, which takes a limited set of argument - names of characters in cowsay
parser.add_argument("--animal", choices=cowsay.char_names, help="The animal to be saying things.", default="cow")

# nargs takes a list of multiple (n) args to a list then perform one action. '*' means multiple 
# optional arguments, all collected into the message option since this is defined after the --animal option, 
# it will gather everything after the argument for the animal option
parser.add_argument("message", nargs="*", help="The message to say")

# parses the args into a Namepace class, e.g. Namespace(animal='fox', message=['hello,', 'starfox'])
args = parser.parse_args()

# list of positional arguments as space-separated string
message = " ".join(args.message)

# call cowsay with the animal and message
print(cowsay.get_output_string(args.animal, message))
