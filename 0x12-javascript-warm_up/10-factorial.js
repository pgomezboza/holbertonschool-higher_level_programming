#!/usr/bin/node

const { argv } = require('process');
const n = argv[2];

function factorial (n) {
  if (isNaN(n) || n === 1) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
console.log(factorial(Number(n)));

/*
const myArgs = parseInt(argv.slice(2));

function factorial (myArgs) {
  if (isNaN(myArgs[0]) || myArgs[0] === 0) {
    return (1);
  }
    return myArgs[0] * factorial(myArgs[0] - 1);
}
console.log(factorial(myArgs));
*/

/*
const n = parseInt(argv[2]);
function factorial(n) {
  if (isNaN(n)) {
    return (1);
  } else {
    if (n === 1) {
      return (1);
    }
    return (n * factorial(n - 1));
  }
}
console.log(factorial(n));
*/

/*
function factorial (n) {
  if (isNaN(n) || n < 2) return 1;
  else return n * factorial(n - 1);
}
console.log(factorial(process.argv[2]));
*/
