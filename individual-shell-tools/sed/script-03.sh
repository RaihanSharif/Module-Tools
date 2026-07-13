#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt removing any line which contains a number.
# The output should contain 6 lines.

# Should this not be done with grep?

# -n prevent default printing behaviour 
# ! negates regex match, i.e. gets lines that don't match
# p prints
sed -n '/[0-9]/!p' input.txt


