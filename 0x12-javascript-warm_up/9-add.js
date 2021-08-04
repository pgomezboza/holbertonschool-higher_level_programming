#!/usr/bin/node

const { argv } = require('process');
const myArgs = argv.slice(2);
const a = myArgs[0];
const b = myArgs[1];

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return (NaN);
  }
  return (parseInt(a) + parseInt(b));
}
console.log(add(a, b));

/*
const n1 = parseInt(argv[2]);
const n2 = parseInt(argv[3]);

function add (a, b) {
  return (a + b);
}

console.log(add(n1, n2));

function add (a, b) {
  console.log(a + b);
}

add(n1, n2);
*/
