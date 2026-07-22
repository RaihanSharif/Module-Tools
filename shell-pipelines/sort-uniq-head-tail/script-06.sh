#!/bin/bash

set -euo pipefail

# The input for this script is the events.txt file.
# TODO: Write a command to show how many times anyone has entered and exited.
# It should be clear from your script's output that there have been 5 Entry events and 4 Exit events.

# v1
#entryCount=$(grep -c '^Entry' events.txt)
#exitCount=$(grep -c '^Exit' events.txt)
#echo "There were $entryCount entries, $exitCount exits"

cut -d' ' -f1 ./events.txt | sort | uniq -c