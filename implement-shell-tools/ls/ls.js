import { dir } from "node:console";
import fs from "node:fs";
import path from "node:path";
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

// returns all entries for a given path
// if -a flag, then include dotfiles, else exclude dotfiles
function getPathEntries(path, aFlag = flags.has("a")) {
    let entries = fs.readdirSync(path);

    if (!aFlag) {
        entries = entries.filter((e) => !e.startsWith("."));
    }
    return entries;
}

console.log(getPathEntries(paths[0]));
