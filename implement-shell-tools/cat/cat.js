import { promises as fs } from "node:fs";
import process from "node:process";

const path = process.argv.slice(2)[0];
const numLines = process.argv.slice(3)[0];

// console.log(numLines);
// console.log(process.argv.slice(3)[0]);
const myFile = await fs.readFile(path, "utf-8");
let lines = myFile.split("\n");

if (!isNaN(numLines)) {
    lines = lines.slice(0, numLines);
}

lines.forEach((e) => console.log(e));
