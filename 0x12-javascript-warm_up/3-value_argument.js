#!/usr/bin/node

const { argv } = require('process');
let rtn = 'No argument';

if (argv[2] !== undefined) {
  rtn = argv[2];
}

console.log(rtn);
