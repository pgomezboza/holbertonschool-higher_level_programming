#!/usr/bin/node
const { argv } = require('process');

const n = parseInt(argv[2]);
if (isNaN(n)) {
  console.log('Missing size');
} else {
  const row = 'X'.repeat(n);

  for (let i = 0; i < n; i += 1) {
    console.log(row);
  }
}

/*
let row = ''

for (let i = 0; i < n; i += 1) {
  row += 'X'
}

for (let i = 0; i < n; i += 1) {
  console.log(row);
}

print('ss', end='');
*/
