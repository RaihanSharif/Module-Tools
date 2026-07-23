import { dir } from "node:console";
import fs from "node:fs";
import process from "node:process";

const args = process.argv.slice(2);

const flags = new Set();
let paths = [];

for (const arg of args) {
    if (arg.startsWith("-") && arg !== "-") {
        // capture the flags without the -
        // supports combined flags like -1a
        for (const ch of arg.slice(1)) {
            flags.add(ch);
        }
    } else {
        paths.push(arg);
    }
}

if (paths.length === 0) {
    paths.push(".");
}

function printFiles(path) {
    if (fs.statSync(path).isDirectory()) {
        if (flags.has("a")) {
            if (flags.has("1")) {
                fs.readdirSync(path).forEach((e) => console.log(e));
            } else {
                console.log(fs.readdirSync(path).join("\t"));
            }
        } else {
            if (flags.has("1")) {
                fs.readdirSync(path)
                    .filter((e) => !e.startsWith("."))
                    .forEach((e) => console.log(e));
            } else {
                console.log(
                    fs
                        .readdirSync(path)
                        .filter((e) => !e.startsWith("."))
                        .join("\t"),
                );
            }
        }
    } else {
        console.log(path);
    }
}

if (paths.length === 1) {
    printFiles(paths[0]);
} else {
    paths.forEach((path) => {
        if (fs.statSync(path).isDirectory()) {
            console.log(`\n${path}:`);
        }
        printFiles(path);
    });
}
