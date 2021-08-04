#!/usr/bin/node

const { argv } = require('process');

let i;
const argument = parseInt(argv[2]);

if (isNaN(argument)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 1; i <= argument; i++) {
    console.log('C is fun');
  }
}
