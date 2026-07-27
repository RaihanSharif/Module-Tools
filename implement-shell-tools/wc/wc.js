import { program } from "commander";
import fs, { chownSync } from "node:fs";
import process from "node:process";

program
    .name("wc")
    .description("Mimics the wc command line tool")
    .option("-w")
    .option("-c")
    .option("-l")
    .argument("<files...>", "files to process");

program.parse();

const options = program.opts();
const paths = program.args;

// if no -lwc flags are supplied, wc prints
// lines, words, bytes of each file
// whereas if any flags are supplied only those
// values are printed
if (Object.keys(options).length === 0) {
    options.l = options.w = options.c = true;
}

// keeps track of total values for each of the data
// incrementally updated in the loop below
const totals = { l: 0, w: 0, c: 0 };

let fileCount = 0;
for (const path of paths) {
    if (fs.statSync(path).isDirectory()) {
        console.log(`wc: ${path}: read: Is a directory`);
    } else {
        fileCount++;
        let outputStr = "";
        const file = fs.readFileSync(path, "utf-8");
        if (options.l) {
            const lines = file.split("\n");
            // exclude trailing empty line from count
            if (lines.at(-1) === "") {
                lines.pop();
            }
            const lineCount = lines.length;
            totals.l += lineCount;
            outputStr += `\t${lineCount}`;
        }

        if (options.w) {
            // real wc splits not just on " ", but on white spaces more generally
            const words = file.split(/\s+/).filter(Boolean);
            const wordCount = words.length;
            totals.w += wordCount;
            outputStr += `\t${wordCount}`;
        }

        if (options.c) {
            file.size;
            const byteCount = fs.statSync(path).size;
            totals.c += byteCount;
            outputStr += `\t${byteCount}`;
        }

        outputStr += ` ${path}`;
        console.log(outputStr);
    }
}

if (fileCount > 1) {
    console.log(`\t${totals.l}\t${totals.w}\t${totals.c} total`);
}
