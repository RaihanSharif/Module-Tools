import { program } from "commander";

program
    .name("wc")
    .description("Mimics the wc command line tool")
    .option("-w")
    .option("-c")
    .option("-l");

program.parse();

const options = program.opts();

console.log(options);
