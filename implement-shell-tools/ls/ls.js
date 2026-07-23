import fs from "node:fs";
import process from "node:process";

const args = process.argv.slice(2);

const flags = new Set();
const path = "";

for (const arg of args) {
    if (arg.startsWith("-") && arg !== "-") {
        // capture the flags without the -
        for (const ch of arg.slice(1)) {
            flags.add(ch);
        }
    }
}

console.log(flags);

// console.log(
//     fs.readdir("./", (err, files) => {
//         if (err) throw err;

//         console.log(files);
//     }),
// );
