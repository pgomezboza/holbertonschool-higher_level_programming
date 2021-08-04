#!/usr/bin/node

const { argv } = require('process');

const firstArgument = argv[2];
const secondArgument = argv[3];
const rtn = `${firstArgument} is ${secondArgument}`;
console.log(rtn);

/*
const arg1 = argv[2];
const arg2 = argv[3];

console.log(arg1 + ' is ' + arg2);
iconsole.log(`${arg1} is ${arg2}`);
console.log(argv[2], 'is', argv[3]);
*/

/*
const conc = argv[2] + ' is ' + argv[3];
console.log(conc);
*/

/*
const myArgs = process.argv.slice(2);
console.log(myArgs[0] + ' is ' + myArgs[1]);
*/
