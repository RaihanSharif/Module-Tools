import fs from "node:fs";
import process from "node:process";

const args = process.argv.slice(2);

const flags = new Set();
let paths = [];

let isFlag = true;
for (const arg of args) {
    if (isFlag && arg === "--") {
        isFlag = false;
    } else if (isFlag && arg.startsWith("-") && arg !== "-") {
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
    entries = [".", "..", entries];

    if (!aFlag) {
        entries = entries.filter((e) => !e.startsWith("."));
    }
    return entries;
}

// formatter: if -1 flag, print entry per line
// else all in one line with
function printEntries(entries, onePerLineFlag = flags.has("1")) {
    if (onePerLineFlag) {
        entries.forEach((e) => console.log(e));
    } else {
        // if join on empty entries arr, add extra blank line
        if (entries.length !== 0) {
            console.log(entries.join("\t"));
        }
    }
}

// this is needed to group files at the top and folers at the bottom when giving mutiple path arguements
// to argv e.g. node ls.js sample-files/*
const fileArgs = paths.filter((p) => !fs.statSync(p).isDirectory());
const dirArgs = paths.filter((p) => fs.statSync(p).isDirectory());

// First print all plain file arguments together, as one group
if (fileArgs.length > 0) {
    printEntries(fileArgs);
}

// Then print each directory's listing, with headers if needed
dirArgs.forEach((path, index) => {
    if (paths.length > 1) {
        if (index > 0 || fileArgs.length > 0) console.log("");
        console.log(`${path}:`);
    }
    printEntries(getPathEntries(path));
});
