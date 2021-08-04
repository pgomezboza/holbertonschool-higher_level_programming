#!/usr/bin/node

const { argv } = require('process');
const arg = parseInt(argv[2]);

let rtn = 'Not a number';

if (!isNaN(arg)) {
  rtn = `My number: ${arg}`;
}

console.log(rtn);
