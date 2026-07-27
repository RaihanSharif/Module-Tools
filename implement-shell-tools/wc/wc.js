import { program } from "commander";
import fs, { chownSync } from "node:fs";
import process from "node:process";

program
    .name("wc")
    .description("Mimics the wc command line tool")
    .option("-w")
    .option("-c")
    .option("-l")
    .argument("<files...>", "file to process");

program.parse();

const options = program.opts();
const paths = program.args;

console.log(options);
console.log(paths);

// if no -lwc flags are supplied, wc prints
// lines, words, bytes of each file
// whereas if any flags are supplied only those
// values are printed
if (Object.keys(options).length === 0) {
    options.l = options.w = options.c = true;
}

/*
for each path:
    if path is not a directory, show error message
    else:
        create a temporary array
        if l in options:
            push line count to temp arr
        if w in options:
            push word count into temp arr
        if c in options:
           push byte count into data 
    
    join the array with path and print
*/

for (const path of paths) {
    if (fs.statSync(path).isDirectory()) {
        console.log(`wc: ${path}: read: Is a directory`);
    } else {
        console.log(`${path} is a file`);
    }
}
