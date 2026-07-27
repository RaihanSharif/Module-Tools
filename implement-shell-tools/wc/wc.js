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

console.log(files);
