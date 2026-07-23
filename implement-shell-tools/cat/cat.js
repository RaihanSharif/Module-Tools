import { promises as fs } from "node:fs";
import process from "node:process";

/*
BASIC requirements:
single file with no flags:
    cat sample-files/1.txt
single file with a valid flag:
    cat -n sample-files/1.txt
    cat -b sample-files/1.txt
read mutliple files with the * wildcard
    cat -n sample/files/*.txt

Cat strips trailing new line in file

-n = number each line
-b = number each non-empty line

STRETCH GOALS
-b takes priority when -nb or -bn
must take in mutiple files:
  node cat file1.txt file2.txt file3.txt
  node cat -n file1.txt file2.txt file3.txt

must be able to take in multiple flags or combined flags
  node cat -bn file.txt
  node cat -b -n file.txt
*/

// capturing the user args
const args = process.argv.slice(2);

let flag;
const files = [];

// takes only one flag, and accepts whatever the last flag is
// can parse flag from any position in args

// the * (glob expansion is done automatically by the zsh, bash etc. on linux)
for (const arg of args) {
    if (arg === "-n" || arg === "-b") {
        flag = arg;
    } else {
        files.push(arg);
    }
}

// starting file number, if lines need to be prepended
let lineNum = 1;

// if no file is supplied
if (files.length === 0) {
    console.error("usage: cat [-n] <file...>");
    process.exit(1); // exit with error
}
