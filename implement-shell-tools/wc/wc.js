import { program } from "commander";
import fs from "node:fs";
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
const files = program.args;

console.log(options);
console.log(files);

// if no -lwc flags are supplied, wc prints
// lines, words, bytes of each file
// whereas if any flags are supplied only those
// values are printed
if (Object.keys(options).length === 0) {
    options.l = options.w = options.c = true;
}

/*
array of objects with data [{l: 2, w: 12: c: 123, file: 'sample-files/1.txt}, ...]
For each item, create a temp string
If options.l, append to temp string the w value
*/
