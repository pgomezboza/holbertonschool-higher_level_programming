#!/usr/bin/node

const { argv } = require('process');
let rtn = 'Arguments found';

if (argv.lenght > 3) {
  rtn = 'Arguments found';
} else if (argv.lenght === 2) {
  rtn = 'No argument';
}

console.log(rtn);

/*
if (process.argv.length <= 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
*/
