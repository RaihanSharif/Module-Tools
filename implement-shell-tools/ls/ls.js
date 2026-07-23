import { dir } from "node:console";
import fs from "node:fs";
import path from "node:path";
import process from "node:process";

const args = process.argv.slice(2);

const flags = new Set();
let paths = [];

if (args.length === 0) {
    args.push(".");
}

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

const files = [];
const directories = [];

if (paths.length > 1) {
    paths.forEach((path) => {
        if (fs.statSync(path).isDirectory()) {
            directories.push(path);
        } else {
            files.push(path);
        }
    });
} else {
    fs.readdir(paths[0], (err, files) => console.log(files.join("\t")));
}

if (files.length > 0) {
    console.log(files.join("\t"));
}

if (directories.length > 0) {
    directories.forEach((dir) => {
        console.log(`\n${dir}:`);
        fs.readdir(dir, (err, files) => {
            console.log(files.join("\t"));
        });
    });
}
