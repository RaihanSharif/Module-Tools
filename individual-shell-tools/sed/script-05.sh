#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt with one change:
# If a line starts with a number and a space, make the line instead end with a space and the number.
# So line 6 which currently reads "37 Alisha" should instead read "Alisha 37".
# The output should contain 11 lines.

# Use capture groups
# 1 is just numbers
# space after number is part of the pattern but not the group 
# 2 is everything else 
# then print out group 2, a space, and then group 1
sed -E 's/^([0-9]+) (.*)/\2 \1/' input.txt
