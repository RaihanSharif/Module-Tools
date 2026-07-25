import { readFileSync } from "node:fs";
import process from "node:process";

// Note: takes only one flag, -n or -b, and accepts whatever the last flag is
// can parse flag from any position in args

// capturing the user args
const args = process.argv.slice(2);

let flag;
const paths = [];

// the * (glob expansion is done automatically by zsh, bash etc. on linux)
for (const arg of args) {
    if (arg === "-n" || arg === "-b") {
        flag = arg;
    } else {
        paths.push(arg);
    }
}

// if no file is supplied exit with error
if (paths.length === 0) {
    console.error("usage: cat [-n] <file...>");
    process.exit(1);
}

// starting file number, if lines need to be prepended

for (const path of paths) {
    let lineNum = 1;
    let file;
    try {
        // using sync as it's a simple short program
        file = readFileSync(path, "utf-8");
    } catch (err) {
        console.error(`cat: ${path}: ${err.message}`);
        continue; // Real cat continues to next file if current file not found
    }

    const lines = file.split("\n");

    // remove trailing empty line as this how real cat works
    if (lines[lines.length - 1] === "") lines.pop();

    if (flag === "-n") {
        for (const line of lines) {
            console.log(`${lineNum} ${line}`);
            lineNum++;
        }
    } else if (flag === "-b") {
        for (const line of lines) {
            if (line === "") {
                console.log(line);
            } else {
                console.log(`${lineNum} ${line}`);
                lineNum++;
            }
        }
    } else {
        for (const line of lines) {
            console.log(line);
        }
    }
}
