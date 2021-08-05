#!/usr/bin/node

const { argv } = require('process');
let rtn = '';

if (argv.length <= 2) {
  rtn = 'No argument';
  console.log(rtn);
} else if (process.argv.length === 3) {
  rtn = 'Argument found';
  console.log(rtn);
} else {
  rtn = 'Arguments found';
  console.log(rtn);
}

/*
if (process.argv.length <= 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
*/
